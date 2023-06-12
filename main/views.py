from django.shortcuts import render
from main import models
from main import task

def mp(request):
    trener = models.Murabbiy.objects.all()
    muasasa = models.Arena.objects.all()
    context = {
        'muosasalar' : task.radom_objects(muasasa, 2),
        'trenerlar' : task.radom_objects(trener, 2),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'index.html', context)


def detail(request, id):
    m = models.Arena.objects.get(id=id)
    sportd = models.Sport.objects.filter(arena=m)
    context = {
        'muosasa':m,
        'sportlar':sportd,
        'viloyatlar':models.Viloyat.objects.all(),
        'murabbiylar': models.Murabbiy.objects.all()
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
        'muasasalar':models.Arena.objects.filter(tumon_sh__viloyat__nomi=viloyat),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'viloyat.html', context)


def sport(request):
    context = {
        'viloyatlar':models.Viloyat.objects.all(),
        'sportlar':models.Sport.objects.all(),
        'murabbiylar': models.Murabbiy.objects.all()
    }
    return render(request, 'sport.html', context)

def sportdet(request, id):
    sportget = models.Sport.objects.get(id=id)
    context = {
        'sport' : sportget, 
        'trenerlar':models.Murabbiy.objects.filter(sport=sportget),
        'viloyatlar':models.Viloyat.objects.all()
    }
    return render(request, 'sportdet.html', context)