from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.StudentDetails.as_view()),
    path('list/', views.StudList.as_view(), name="stud"),
    path('update/<id>/', views.Stud.as_view(), name="my"),
]