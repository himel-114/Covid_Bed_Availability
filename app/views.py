from django.shortcuts import render
from django.http.response import HttpResponse
from app.models import Facility, Division, City,Hospital

# Create your views here.
def home(request):
    selected_division_id = request.GET.get('division')
    selected_city_id = request.GET.get('city') 
    facilities=Facility.objects.all().order_by('pk')
    if selected_division_id:
        cities=City.objects.filter(division=selected_division_id)
    else:
        cities=City.objects.all()
    divisions=Division.objects.all()
    hospitals=Hospital.objects.all()
    if selected_city_id:
        hospitals=hospitals.filter(city=City(pk=selected_city_id))
    
    context = {
     'facilities': facilities,
     'cities': cities,
     'divisions':divisions,
     'hospitals':hospitals,
     'selected_division_id':selected_division_id,
     'selected_city_id':selected_city_id
    }
    return render(request,template_name='index.html', context=context)