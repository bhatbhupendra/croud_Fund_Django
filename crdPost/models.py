from django.db import models
from django.utils.text import slugify
# Create your models here.
class Posts(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    category = models.ForeignKey('postCategory' , on_delete=models.SET_NULL , null=True)
    date=models.DateTimeField()
    image=models.ImageField(upload_to='posts/')
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Posts,self).save(*args,**kwargs)    
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"


class postCategory(models.Model):
    name = models.CharField(max_length=30)


    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.name




