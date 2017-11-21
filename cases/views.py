from django.shortcuts import render, get_object_or_404

from .models import *

def homepage(request):
    district_list = District.objects.all()
    binder_list = Binder.objects.all()
    case_list = Case.objects.all()
    event_list = Event.objects.all()
    person_list = Person.objects.all()

    print(case_list)

    return render(request, 'homepage.html', {
        'district_list': district_list,
        'binder_list': binder_list,
        'case_list': case_list,
        'person_list': person_list
    })

def add_entry(request):
    return render(request, 'add-entry.html', {})

def advanced_search(request):
    return render(request, 'advanced-search.html', {})

def district_detail(request, district_id):
    office = get_object_or_404(District, id=district_id)
    return render(request, 'district/detail.html', {'district': district})
