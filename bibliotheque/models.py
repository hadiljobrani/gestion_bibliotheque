from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    prix = models.FloatField(default=0.0)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
