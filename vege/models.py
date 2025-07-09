from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank =True)# models.cascade ka mtlb hai user deletion = user delete krna chahta  h toh krdo 
    receipe_name= models.CharField( max_length=100)
    receipe_discription=models.TextField(null=True, blank=True)
    receipe_image=models.ImageField((""), upload_to="receipe", height_field=None, width_field=None, max_length=None)
    receipe_view_count =models.IntegerField(default=1)
