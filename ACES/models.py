from django.db import models

# Create your models here.

class applicant(models.Model):
    mobileNumber = models.IntegerField()
    intrvwSlt = models.DateField()

class interviewSlot(models.Model):
	numberOfApplicants = 10
	interviewDate = models.DateField


	def chckNmbrOfAplcnts():
		if numberOfApplicants > 0:
			numberOfApplicants-1
			return self


