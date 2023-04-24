from django.http import JsonResponse
from django.shortcuts import render
from django.forms import modelform_factory
from .models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

StudentForm = modelform_factory(Student, exclude=[])


def newbage(request):
    return render(request, 'pages/newpage.html')


def index(request):
    return render(request, 'pages/index.html')


def add(request):
    if request.method == "GET":
        return render(request, 'pages/add.html')
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'pages/add.html')


def delete(request, id):
    stu = Student.objects.get(id=id)
    stu.delete()
    return HttpResponseRedirect(reverse('show'))


def search(request):
    if request.method == "POST":
        namest = request.POST.get('name', None)
        if namest:
            results = Student.objects.all().filter(name__contains=namest)
            return render(request, 'pages/search.html', {"results": results, 'namest': namest})

    return render(request, 'pages/search.html')


def update(request, id):
    stu = Student.objects.get(id=id)
    template = loader.get_template('pages/update.html')
    context = {
        'stu': stu,
    }
    return HttpResponse(template.render(context, request))


def updatestudent(request, id):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    idst = request.POST['idst']
    level = request.POST['level']
    gpa = request.POST['gpa']
    #date = request.POST['date']
    gender = request.POST['gender']
    status = request.POST['status']

    stu = Student.objects.get(id=id)
    stu.name = name
    stu.email = email
    stu.phone = phone
    stu.idst = idst
    stu.level = level
    stu.gpa = gpa
    #stu.date = date
    stu.gender = gender
    stu.status = status
    stu.save()
    return HttpResponseRedirect(reverse('show'))


def show(request):
    x = Student.objects.all()
    data = {'sts': x.order_by('level')}
    return render(request, 'pages/show.html', data)


def department(request):
    return render(request, 'pages/department.html')
# Create your views here.


def validate_id(request):
    ID = request.GET.get('idst')
    is_taken = Student.objects.filter(idst__iexact = ID).exists()
    data = {'is_taken':is_taken}
    if data['is_taken']:
        data['errormsg'] = "The entered id alredy taken"
    return JsonResponse(data)
def add(request):
    if request.method == "GET":
        return render(request, 'pages/add.html')
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'pages/add.html')

def department(request, id):
    stu = Student.objects.get(id=id)
    template = loader.get_template('pages/department.html')
    context = {
        'stu': stu,
    }
    return HttpResponse(template.render(context, request))


# def addepartment(request, id):
#   department = request.POST['deparment']
#  stu = Student.objects.get(id=id)
# stu.department = department
# stu.save()
# return HttpResponseRedirect(reverse('search/department'))

# Create your views here.