from django.db import models

# Create your models here.



class Receipe(models.Model):
    receipe_name= models.CharField( max_length=100)
    receipe_discription=models.TextField()
    receipe_image=models.ImageField((""), upload_to="receipe", height_field=None, width_field=None, max_length=None)

