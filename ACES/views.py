from django.http import HttpResponse
from django.template import loader
from .models import interviewSlots


def submit(request):
    template = loader.get_template('ACES/submit.html')
    return HttpResponse(template.render("", request))

def mainPage(request):
    template = loader.get_template('ACES/form.html')
    return HttpResponse(template.render("", request))
