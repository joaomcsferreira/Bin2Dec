from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversion_list, name='conversion-list'),
    path('delete/<int:id>', views.conversion_delete, name='conversion_delete')
]
