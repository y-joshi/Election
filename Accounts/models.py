from django.db import models

# Create your models here.
class Alliance(models.Model):
    name = models.CharField(max_length=100)

class Party(models.Model):
    name = models.CharField(max_length=100)
    alliance = models.ForeignKey(Alliance,on_delete=models.CASCADE)

class State(models.Model):
    name = models.CharField(max_length=100)

class Constituency(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Candidate_photos')
    gender = models.IntegerField()  # 1 for male, 2 for female, 3 for transgender
    dob = models.DateField()
    mobileno = models.IntegerField()
    age = models.IntegerField()
    address = models.TextField()
    constituency = models.ForeignKey(Constituency,on_delete=models.CASCADE)
    party = models.ForeignKey(Party,on_delete=models.CASCADE)

class Party_Result(models.Model):
    party = models.ForeignKey(Party,on_delete=models.CASCADE)
    seats = models.IntegerField()

class Alliance_Result(models.Model):
    alliance = models.ForeignKey(Alliance,on_delete=models.CASCADE)

class Constituency_Result(models.Model):
    constituency = models.ForeignKey(Constituency,on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)

class Constituency_Votes(models.Model):
    constituency = models.ForeignKey(Constituency,on_delete=models.CASCADE)
    votes = models.IntegerField()
    party = models.ForeignKey(Party,on_delete=models.CASCADE)

class Voter(models.Model):
    vid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Voters_photos')
    gender =  models.IntegerField() # 1 for male, 2 for female, 3 for transgender
    dob = models.DateField()
    mobileno = models.IntegerField()
    age = models.IntegerField()
    voted = models.BooleanField(default=False)
    constituency = models.ForeignKey(Constituency,on_delete=models.CASCADE)