from django.shortcuts import get_object_or_404, redirect, render
from .models import Application
from django.http import HttpResponseRedirect
from django.urls import reverse

def application(request):
    if request.method == "POST":
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        number = request.POST.get('number')
        email = request.POST.get('email')
        Application.objects.create(name=name, designation=designation, number=number, email=email)
        return HttpResponseRedirect(reverse('success'))
   
    applications = Application.objects.all()
    return render(request, 'submit.html', {'applications': applications})

def success(request):
    return render(request, 'success.html')

def view_users(request):
    applications = Application.objects.all()
   
    return render(request,'users_view.html',{'applications':applications})


from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'designation', 'number', 'email']

def edit_user(request, id):
    application = get_object_or_404(Application, pk=id)
    if request.method =='POST':
        form =ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = Application(isinstance=application)
    return render(request, 'edit_user.html', {'form':form})
def delete_user(request, id):
    application =get_object_or_404(Application, pk=id)
    application.delete()
    return redirect('view_users')

