from django.shortcuts import render,redirect
from django.views.generic import View, ListView

from myapp.forms import ContactForm
from myapp.models import Student

# Create your views here.
class StudentDetails(View):
    
    def get(self, request):
        form = ContactForm() 
        return render(request, "myapp/form.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST) 
        if form.is_valid():
            instance = form.save()
            return render(request, "myapp/home.html", {"data": instance})
        else:
            return render(request, "myapp/form.html", {"form": form})

class StudList(ListView):
    template_name = "myapp/list.html"
    context_object_name = "records"
    queryset = Student.objects.all()

class Stud(View):

    def get(self, request, id):
        form = ContactForm(instance=Student.objects.get(id=id))
        return render(request, "myapp/form.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, instance=Student.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("stud")
        else:
            return render(request, "myapp/form.html", {"form": form})