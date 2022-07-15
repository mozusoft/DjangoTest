from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lasttname = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lasttname}"


class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(Region)

    def __str__(self):
        # {self.members.count()}
        # {self.members.all()}
        return f"{self.name}"


class Place(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    # city = models.CharField(max_length=2, choices=CITY, blank=True, default='M')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.CharField(max_length=2, choices=city.get_choices(), blank=True)
    street = models.CharField(max_length=50)
    home = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
