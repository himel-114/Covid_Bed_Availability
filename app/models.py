from django.db import models

# Create your models here.
class Division(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    def __str__(self):
        return self.name

class City(models.Model):
    name=models.CharField (max_length=50, null=False, blank=False)
    division=models.ForeignKey(Division, on_delete=models.CASCADE, related_name='cities')
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.CharField (max_length=50, null=False, blank=False)
    phone=models.CharField (max_length=11, null=False, blank=False)
    address=models.CharField (max_length=200, null=False, blank=False)
    city=models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')
    def __str__(self):
        return self.name
    
class Facility(models.Model):
#   // hospital=models.OneToOneField(Hospital, on_delete=models.CASCADE, primary_key=True)
#     oxygen_bed_total=models.IntegerField (default=0)
#     oxygen_bed_avilable=models.IntegerField (default=0)
#     oxygen_cylinder_total=models.IntegerField (default=0)
#     oxygen_cylinder_available=models.IntegerField (default=0)
#     ventilator_total=models.IntegerField (default=0)
#     ventilator_available=models.IntegerField (default=0)//
    title =models.CharField(max_length=60,null=False,blank=False, default="")
    def __str__(self):
        return self.title

class Availability(models.Model):
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='availabilies')
    facility =models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='availabilies')
    total=models.IntegerField (default=0)
    available=models.IntegerField (default=0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.hospital.name}-{self.facility.title}'
