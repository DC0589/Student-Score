from django.shortcuts import render,redirect
from .models import section
from.forms import sectionform

# Create your views here.
def studentscore(request):
    students = section.objects.all().order_by('id')  # Replace 'id' with the appropriate field
    return render(request, "sApp/index.html", {'students': students})

def create(request):
    form = sectionform()
    if request.method == 'POST':
        form = sectionform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,"sApp/create.html",{'form':form})


def delete(request,id):
    student=section.objects.get(id = id)
    student.delete()
    return redirect('/')

def update(request,id):
    students = section.objects.get(id = id)
    form = sectionform(instance=students)
    if request.method == 'POST':
        form = sectionform(request.POST,instance=students)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "sApp/update.html", {'form': form})




