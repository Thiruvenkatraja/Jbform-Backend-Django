from django.db import models

class Jdform(models.Model):
    _id=models.AutoField(primary_key=True)
    candidatename=models.CharField(max_length=50,blank=True)
    mobile=models.IntegerField()
    technology= models.CharField(max_length=50,blank=True)
    startdate= models.CharField(max_length=50,blank=True)
    followupdate=models.CharField(max_length=50,blank=True)
    resource= models.CharField(max_length=50,blank=True)
    status= models.CharField(max_length=50,blank=True)
    feedback= models.CharField(max_length=100,blank=True)

    def __str__(self):
     return self.candidatename