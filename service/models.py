from django.db import models

# Create your models here.

class Service(models.Model):
    title= models.CharField(max_length=25)
    icon= models.CharField(max_length=20 ,null=True)
    description = models.TextField(max_length=110) # 110 to not destroy responsive

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'
        ordering=['-id']  #-id to show last one first

    def __str__(self):
        return self.title


class Facts(models.Model):
    Projects_Completed=models.IntegerField(default=0)
    clients=models.IntegerField(default=0)
    Coffee=models.IntegerField(default=0)
    Professionals=models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


