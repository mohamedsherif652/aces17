from django.http import HttpResponse

def mainPage(request):
    return HttpResponse("<p1><center>Welcone To Django<center/><p1/>")
