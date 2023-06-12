from django.shortcuts import render
from main import models
from main import task

def mp(request):
    trener = models.Murabbiy.objects.all()
    muasasa = models.Arena.objects.all()
    context = {
        'muosasalar' : task.radom_objects(muasasa, 2),
        'trenerlar' : task.radom_objects(trener, 1),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'index.html', context)


def detail(request, id):
    context = {
        'muosasa':models.Arena.objects.get(id=id),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'single.html', context)


def arenalar(request):
    context = {
        'muasasalar':models.Arena.objects.all(),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'arenalar.html', context)


def viloyatlar(request, id):
    viloyat = models.Viloyat.objects.get(id=id)
    context = {
        'arenalar':models.Arena.objects.filter(tumon_sh__viloyat__nomi=viloyat),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'arenalar.html', context)