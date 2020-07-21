from django.shortcuts import render
from django.http import HttpResponse
from .models import todo
# Create your views here.

def index(request):
    kaam=todo.objects.all()
    return render(request,'index.html',{'kaam':kaam})

def delete(request,n):
    todo.objects.filter(work_id=n).delete()

    kaam = todo.objects.all()
    return HttpResponse("<script>window.location = '/todo/' ;</script>")

    #return render(request, 'index.html',{'kaam':kaam})

def add(request):
    if request.method == "POST":
        work = request.POST.get('work', '')
        desc = request.POST.get('desc', '')
        date = request.POST.get('date', '')
        newest = todo(work=work, due_date=date, desc=desc)
        newest.save()
        kaam = todo.objects.all()
        return HttpResponse("<script>window.location = '/todo/' ;</script>")
    else:
        kaam = todo.objects.all()
        return render(request, 'index.html', {'kaam':kaam})
