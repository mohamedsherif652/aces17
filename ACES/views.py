from django.http import HttpResponse
from django.template import loader
from .models import interviewSlots


def submit(request):
    template = loader.get_template('ACES/submit.html')
    return HttpResponse(template.render("", request))

def mainPage(request):
    template = loader.get_template('ACES/form.html')
    all_slots = interviewSlots.objects.all()
    context = {
    	'all_slots': all_slots,
    }
    return HttpResponse(template.render(context, request))
