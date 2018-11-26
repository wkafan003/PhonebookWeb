from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import phonebook, city_table, street_table


def index(request):
    if 'search' in request.GET:
        qs = phonebook.objects.all()
        tags = list()
        import json
        if 'schips' in request.GET:
            jtags = json.loads(request.GET['schips'])
            if len(jtags) > 0:
                for i in jtags:
                    for j in i['tag'].split():
                        tags.append(j)
                subqs = phonebook.objects.none()
                for i in tags:
                    subqs = subqs | phonebook.objects.filter(l_name__icontains=i)
                    subqs = subqs | phonebook.objects.filter(f_name__icontains=i)
                    subqs = subqs | phonebook.objects.filter(m_name__icontains=i)
                    subqs = subqs | phonebook.objects.filter(gender__iexact=i)
                    subqs = subqs | phonebook.objects.select_related('s_value').filter(street__s_value__icontains=i)
                    subqs = subqs | phonebook.objects.select_related('с_value').filter(city__c_value__icontains=i)
                    subqs = subqs | phonebook.objects.filter(tel__icontains=i)
                    subqs = subqs | phonebook.objects.filter(email__icontains=i)
                    subqs = subqs | phonebook.objects.filter(job__icontains=i)
                    subqs = subqs | phonebook.objects.filter(post__icontains=i)
                qs = subqs
        json = list()
        for i in qs:
            json.append(i.Json())
        resp = JsonResponse(json, safe=False)
        return resp
    else:
        return render(request, 'pb/base.html')


def contactAdd(request):
    if (request.method == 'POST'):
        pb = phonebook()
        pb.l_name = request.POST["l_name"]
        pb.f_name = request.POST["f_name"]
        pb.m_name = request.POST["m_name"]
        pb.gender = request.POST["gender"]
        pb.street = street_table.objects.get(id=request.POST["street"])
        pb.city = city_table.objects.get(id=request.POST["city"])
        pb.email = request.POST["email"]
        pb.b_num = request.POST["b_num"]
        pb.ap = request.POST["ap"]
        pb.tel = request.POST["tel"]
        pb.job = request.POST["job"]
        pb.post = request.POST["post"]
        pb.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        cities = city_table.objects.all()
        streets = street_table.objects.all()
        return render(request, 'pb/add.html', {'cities': cities, 'streets': streets})


def contactEdit(request, contact_id):
    if (request.method == 'POST'):
        pb = phonebook.objects.get(id=contact_id)
        pb.l_name = request.POST["l_name"]
        pb.f_name = request.POST["f_name"]
        pb.m_name = request.POST["m_name"]
        pb.gender = request.POST["gender"]
        pb.street = street_table.objects.get(id=request.POST["street"])
        pb.city = city_table.objects.get(id=request.POST["city"])
        pb.email = request.POST["email"]
        pb.b_num = request.POST["b_num"]
        pb.ap = request.POST["ap"]
        pb.tel = request.POST["tel"]
        pb.job = request.POST["job"]
        pb.post = request.POST["post"]
        pb.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        pb = phonebook.objects.get(id=contact_id)
        cities = city_table.objects.all()
        streets = street_table.objects.all()
        return render(request, 'pb/edit.html', {'cities': cities, 'streets': streets, 'phonebook': pb})


def contactDelete(request, contact_id):
    pb = phonebook.objects.get(id=contact_id)
    pb.delete()
    return HttpResponseRedirect(reverse('index'))


def city(request):
    if (request.method == 'POST'):
        city = city_table.objects.get(id=request.POST['id'])
        city.c_value = request.POST['city']
        city.save()
        return JsonResponse(["ok)"], safe=False)
    else:
        cities = city_table.objects.all()
        return render(request, 'pb/city.html', {'cities': cities})


def cityAdd(request):
    if (request.method == 'POST'):
        city = city_table()
        city.c_value = request.POST['city']
        city.save()
        return JsonResponse([city.id], safe=False)


def cityDelete(request):
    if (request.method == 'POST'):
        city = city_table.objects.get(id=request.POST["id"])
        city.delete()
        return JsonResponse(["ok)"], safe=False)


def street(request):
    if (request.method == 'POST'):
        street = street_table.objects.get(id=request.POST['id'])
        street.s_value = request.POST['street']
        street.save()
        return JsonResponse(["ok)"], safe=False)
    else:
        streets = street_table.objects.all()
        return render(request, 'pb/street.html', {'streets': streets})


def streetAdd(request):
    if (request.method == 'POST'):
        street = street_table()
        street.s_value= request.POST['city']
        street.save()
        return JsonResponse([street.id], safe=False)


def streetDelete(request):
    if (request.method == 'POST'):
        street = street_table.objects.get(id=request.POST["id"])
        street.delete()
        return JsonResponse(["ok)"], safe=False)