
from django.http import HttpResponse
from django.template import loader
from .models import Income

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