from django.db import models

# Create your models here.
class rankMobileLegends(models.Model):
    rankml = models.CharField(max_length=100)
    divisirankml = models.CharField(max_length=100)
    subrankml = models.CharField(max_length=100)
    harga = models.IntegerField()
    urutan = models.IntegerField()

    def __str__(self):
        return f"{self.subrankml}"