from django.shortcuts import render

from core.models import Agency

# Create your views here.
def home(request):
  list_of_agencies = Agency.objects.all()
  return render(request, 'index.html', { 'agencies': list_of_agencies })

def agency(request, agency_name):
  list_of_agencies = Agency.objects.all()
  return render(request, 'agency.html', { 'agencies': list_of_agencies })