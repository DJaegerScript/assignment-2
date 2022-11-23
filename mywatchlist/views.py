from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.core import serializers
from django.http import HttpResponse

# TODO: Create your views here.
def show_watchlist(request):
    watch_list_items = WatchListItem.objects.all()
    context = {
        'name': "Adjie Djaka Permana",
        'student_id': "2106702485",
        'watch_list_items': watch_list_items,
    }

    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchListItem.objects.all()
    
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_json(request):
    data = WatchListItem.objects.all()
    
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def update_json_by_id(request, id):
    data = WatchListItem.objects.get(pk=id)
    data.watched = not data.watched
    data.save()
    
    return HttpResponse(serializers.serialize('json', [data]), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml") 