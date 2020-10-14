from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey('Category',related_name='project_category',on_delete=models.CASCADE) # (on_delete=models.CASCADE) to delete category project had deleted
    image= models.ImageField(upload_to='projects/')

        


    def __str__(self):
        return str(self.title)




class Category(models.Model):
    name = models.CharField(max_length=25)


    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return str(self.name)