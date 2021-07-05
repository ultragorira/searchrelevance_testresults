from django.db import models
from django.contrib.auth.models import User

class Results(models.Model):
    id_result = models.AutoField(primary_key=True)
    account = models.CharField(max_length=50)
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


class CSV(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)