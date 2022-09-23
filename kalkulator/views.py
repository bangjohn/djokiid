from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import rankMobileLegends
#from .forms import hitungForm

# Create your views here.
def index(request):
    return render(request, 'kalkulator/index.html', {
        'rankml': rankMobileLegends.objects.all()
    })

def hitung(request):
    if request.method == 'POST':
        hitung = 0
        awal = request.POST['pilihrankawal']
        tujuan = request.POST['pilihranktujuan']
        print(awal)
        print(tujuan)
        # loop for awal and tujuan
        for i in range(int(awal), int(tujuan)):
            hitung += rankMobileLegends.objects.get(urutan=i).harga
        rankawal = rankMobileLegends.objects.get(urutan=awal).subrankml
        ranktujuan = rankMobileLegends.objects.get(urutan=tujuan).subrankml
        return render(request, 'kalkulator/index.html', {
            'rankml': rankMobileLegends.objects.all(),
            'success': True,
            'hitung': hitung,
            'tujuan': tujuan,
            'rankawal': rankawal,
            'ranktujuan': ranktujuan
        })


