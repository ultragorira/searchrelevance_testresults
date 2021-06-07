from django.db import models
from django.contrib.auth.models import User

class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    search_query =  models.CharField(max_length=200)
    link_query = models.URLField(max_length=400)
    user_answer = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)
    verdict = models.CharField(max_length=50)

    def __str__(self):
        return self.search_query

    
    class Meta:
        #Ordering first by wrong
        ordering = ['-verdict']


