from django.db import models

# Create your models here.

class applicant(models.Model):
    mobileNumber = models.IntegerField()
    interviewSlot = models.CharField(max_length=30)

class interviewSlots(models.Model):
    slot = models.CharField(max_length=30)
    numberOfApplicants = models.IntegerField()

