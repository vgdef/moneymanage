
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