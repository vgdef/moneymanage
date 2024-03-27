
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Income
from .models import Need
from .models import Reference
from django.urls import reverse

# Create your views here
def income(request):
    myincome = Income.objects.all().values()
    template = loader.get_template('income.html')
    context = {
        'myincome': myincome,
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id):
    myincomes = Income.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myincomes': myincomes
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def income_entry(request):
    if request.method == 'POST':
        kategori = request.POST.get('kategori')
        jumlah = request.POST.get('jumlah')
        keterangan = request.POST.get('keterangan')

        income = Income(kategori=kategori, jumlah=jumlah, keterangan=keterangan)
        income.save()

        return HttpResponseRedirect (reverse ('income'))
    else:
        return HttpResponse|("Belum Tersimpan")
    
def delete(request, id):
    income = Income.objects.get(id=id)
    income.delete()
    return HttpResponseRedirect(reverse('income'))

def update(request, id):
    myincome = Income.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'myincome': myincome,
    }
    return HttpResponse(template.render(context, request))

def update_record(request,id):
    kategori = request.POST['kategori']
    jumlah = request.POST['jumlah']
    keterangan = request.POST['keterangan']
    income = Income.objects.get(id=id)
    income.kategori = kategori
    income.jumlah = jumlah
    income.keterangan = keterangan
    income.save()
    return HttpResponseRedirect (reverse ('income'))
 
def need(request):
    myneed = Need.objects.all().values()
    template = loader.get_template('need.html')
    context = {
        'myneed': myneed,
    }
    
    return HttpResponse(template.render(context, request))

def reference(request):
    myreference= Reference.objects.all().values()
    template = loader.get_template('reference.html')
    context = {
        'myreference': myreference,
    }
    
    return HttpResponse(template.render(context, request))