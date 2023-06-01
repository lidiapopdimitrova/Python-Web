from django.contrib import admin
from django.urls import path, include

from departments_app.departments.views import show_not_found, redirect_to_first_department

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', include('departments_app.departments.urls')),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('not_found/', show_not_found, name='not found')
]

