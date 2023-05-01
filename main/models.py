from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm
from django import forms

# Create your models here.


class temp1(models.Model):
    layout1 = models.IntegerField(default=1,editable=False);
    para1=models.CharField(null=True,max_length=100)
    para2=models.CharField(null=True,max_length=100)
    

class temp2(models.Model):
    layout2 = models.IntegerField(default=2,editable=False);
    text=models.CharField(max_length=500,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    
class pages(models.Model):
    pagename = models.CharField(max_length=100,unique=True)
    # class Meta:
    #     ordering = ['pagename']
    def __str__(self):
        return "%s" % (self.pagename)

class l1(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE) 
    pagename = models.ForeignKey(pages,on_delete=models.CASCADE,null=True)  
    # page = models.CharField(max_length=200)
    layout1 = models.CharField(default=1,editable=False,max_length=1);
    changing_seconds =models.IntegerField(blank='True',default=5,help_text='enter the seconds to be displayed')
    priority = models.IntegerField(blank=False,default=0)

    cardTitle1=models.CharField(max_length=30,null=True)
    cardBody1=models.CharField(max_length=500,null=True)
    cardImage1=models.ImageField(null=True,blank=True,upload_to='static/images/')

    cardTitle2=models.CharField(max_length=30,null=True)
    cardBody2=models.CharField(max_length=500,null=True)
    cardImage2=models.ImageField(null=True,blank=True,upload_to='images/')
    
    cardTitle3=models.CharField(max_length=30,null=True)
    cardBody3=models.CharField(max_length=500,null=True)
    cardImage3=models.ImageField(null=True,blank=True,upload_to='images/')
   

    # def __str__(self):
    #     return self.layout1


class l2(models.Model):

    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pagename = models.ForeignKey(pages,on_delete=models.CASCADE,null=True)
    layout2 = models.CharField(default=2,editable=False,max_length=1);
    changing_seconds = models.IntegerField(blank='True',default=5)
    priority = models.IntegerField(blank=False,default=0)
    text = models.CharField(max_length=500,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    

    # def __str__(self):
    #     return self.layout2

class l3(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pagename = models.ForeignKey(pages,on_delete=models.CASCADE,null=True)
    layout3 = models.CharField(default=3,editable=False,max_length=1)
    changing_seconds =models.IntegerField(blank='True',default=5)
    priority = models.IntegerField(blank=False,default=0)
    text=models.CharField(max_length=500,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
   
    # def __str__(self):
    #     return self.layout3

class l4(models.Model):

    pagename = models.ForeignKey(pages,on_delete=models.CASCADE,null=True)
    layout4 = models.CharField(default=4,editable=False,max_length=1)
    priority = models.IntegerField(blank=False,default=0)
    changing_seconds =models.IntegerField(blank='True',default=5)
    video = models.FileField(upload_to='videos/%y',null=True,blank=True)
    caption = models.CharField(max_length=300,null=True)
    
    # def __str__(self):
    #     return self.layout4

class layout_name(models.Model):
    name = models.CharField(null=True,max_length=20)

    def __str__(self):
        return str(self.name)

class dynamic_forms(models.Model):

    choices = (('CharField','CharField'),('ImageField','ImageField'),('FileField','FileField'))
    layout_name = models.ForeignKey(layout_name,on_delete=models.CASCADE,null=True)
    content1 = models.CharField(null=True,max_length=100,choices=choices)
    content2 = models.CharField(null=True,max_length=100,choices=choices)
    content3 = models.CharField(null=True,max_length=100,choices=choices)
    content4 = models.CharField(null=True,max_length=100,choices=choices)

    def __str__(self):
        return str(self.layout_name)


class custom_layout_data(models.Model):

    page_name = models.ForeignKey(pages,on_delete=models.CASCADE,null=True)
    layout_name = models.ForeignKey(layout_name,on_delete=models.CASCADE,null=True)
    data = models.JSONField(default=dict)

class charfield(models.Model):

    content = models.CharField(max_length=20,null=True)

class Imagefield(models.Model):
    
    content = models.ImageField(null=True,blank=True,upload_to='images/')

    def returnUrl(self):
        return self.content.url

class videofield(models.Model):
    
    content = models.FileField(null=True,blank=True,upload_to='vidoes/%y')
    
    def returnUrl(self):
        return self.content.url
       
class dynamic_forms_data(models.Model):

    data = models.JSONField(default=dict)
    layout_name =  layout_name = models.ForeignKey(layout_name,on_delete=models.CASCADE,null=True)


class elements_data(models.Model):

    data = models.CharField(max_length=100000000,null=True,blank=True)
    layout_name = models.OneToOneField(layout_name,on_delete=models.CASCADE,null=True)
    




