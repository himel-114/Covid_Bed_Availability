from django.contrib import admin
from app.models import Division,City,Hospital,Facility,Availability

# Register your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save , sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    facilities=Facility.objects.all()
    for facility in facilities:
        availibility=Availability(hospital=instance,facility=facility)
        availibility.save()

@receiver(post_save , sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
    hospitals=Hospital.objects.all()
    for hospital in hospitals:
        availibility=Availability(hospital=hospital,facility=instance)
        availibility.save()


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'division']

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name', 'phone', 'address', 'city']


class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['title']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital','facility','total','available','updated_at']
    list_editable= ['total','available']





admin.site.register(Division)
admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)