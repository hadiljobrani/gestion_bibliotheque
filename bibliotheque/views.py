from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre

def liste_livres(request):
    query = request.GET.get('q', '')
    if query:
        livres = Livre.objects.filter(titre__icontains=query) | Livre.objects.filter(auteur__icontains=query)
    else:
        livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste.html', {'livres': livres, 'query': query})

def ajouter_livre(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        auteur = request.POST['auteur']
        prix = request.POST['prix']
        disponible = 'disponible' in request.POST
        Livre.objects.create(titre=titre, auteur=auteur, prix=prix, disponible=disponible)
        return redirect('liste_livres')
    return render(request, 'bibliotheque/ajouter.html')

def supprimer_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    livre.delete()
    return redirect('liste_livres')

def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        livre.titre = request.POST['titre']
        livre.auteur = request.POST['auteur']
        livre.prix = request.POST['prix']
        livre.disponible = 'disponible' in request.POST
        livre.save()
        return redirect('liste_livres')
    return render(request, 'bibliotheque/modifier.html', {'livre': livre})