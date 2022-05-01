from django.db import models

#WORKS(person-name,Company-name,Salary) 
#LIVES(Person_name, Street, City)


class works(models.Model):
    person_name = models.TextField()
    company_name = models.CharField(max_length=30)
    salary = models.IntegerField(default=0)

class lives(models.Model):
    p_name = models.TextField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    

  