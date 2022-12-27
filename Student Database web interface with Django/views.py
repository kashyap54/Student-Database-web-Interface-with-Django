from django.shortcuts import render
from assignment4.models import StuModel
from assignment4.models import CorModel
from assignment4.forms import Stuforms
from assignment4.forms import Corforms
from curses import savetty
from statistics import mean
from django.contrib import messages
from django.forms.models import model_to_dict


def showstu(request):
    showall = StuModel.objects.all()
    showall1 = CorModel.objects.all()
    return render(request, 'index.html', {"data": showall,"data1":showall1})

def Insertemp(request):
    if request.method == "POST":
        if request.POST.get('sname') and request.POST.get('age') and request.POST.get('dob') and request.POST.get('grade') and request.POST.get('cid'):
            saverecord = StuModel()
            saverecord.sname = request.POST.get('sname')
            saverecord.age = request.POST.get('age')
            saverecord.dob = request.POST.get('dob')
            saverecord.grade = request.POST.get('grade')
            saverecord.cid = request.POST.get('cid')
            saverecord.save()
            messages.success(request,'Student '+saverecord.sname+' is saved successfully')
            return render(request, 'Insert.html')
    else:
        return render(request, 'Insert.html')

def Insertcor(request):
    if request.method == "POST":
        if request.POST.get('cid') and request.POST.get('course_title') and request.POST.get('course_hours'):
            saverecord1 = CorModel()
            saverecord1.cid = request.POST.get('cid')
            saverecord1.course_title = request.POST.get('course_title')
            saverecord1.course_hours = request.POST.get('course_hours')
            saverecord1.save()
            messages.success(request,'Course '+saverecord1.course_title+' is saved successfully')
            return render(request, 'Insert2.html')
    else:
        return render(request, 'Insert2.html')

def Editstu(request, id):
    editstuobj = StuModel.objects.get(id = id)
    return render(request,'Stuedit.html',{"StuModel":editstuobj})

def Updatestu(request, id):
    updatestuobj = StuModel.objects.get(id = id)
    form = Stuforms(request.POST, instance=Updatestu)
    if form.is_valid():
        print("Form is valid")
        form.save()
        return render(request, 'Stuedit.html',{"StuModel": updatestuobj})

def Editcor(request, id):
    editcorobj = CorModel.objects.get(cid = id)
    return render(request, 'Coredit.html', {"CorModel":editcorobj})

def Updatecor(request, id):
    updatecorobj = CorModel.objects.get(cid = id)
    form = Corforms(request.POST, instance = Updatecor)
    if form.is_valid():
        print("Form is valid")
        form.save()
        return render(request, 'Coredit.html',{"CorModel": updatecorobj})

def Deletestu(request, id):
    deletestuobj = StuModel.objects.get(id = id)
    deletestuobj.delete()
    showdata = StuModel.objects.all()
    return render(request, "index.html", {"data":showdata})

def Deletecor(request, id):
    deletecorobj = CorModel.objects.get(cid = id)
    deletecorobj.delete()
    showdata2 = CorModel.objects.all()
    return render(request, "index.html", {"data":showdata2})