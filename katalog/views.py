from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    catalog_items = CatalogItem.objects.all()
    context = {
        'name': "Adjie Djaka Permana",
        'student_id': "2106702485",
        'catalog_items': catalog_items,
    }


    return render(request, "katalog.html", context)