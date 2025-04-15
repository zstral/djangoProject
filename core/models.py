from django.db import models

class Forumusers(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Forumuser'
        verbose_name_plural = 'Forumusers'