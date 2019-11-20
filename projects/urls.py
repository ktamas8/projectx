from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("dev/", views.project_dev, name="project_dev"),
    path("menu/", views.project_menu, name="project_menu"),
    path("menu/configuration", views.project_config, name="project_config"),
    path("menu/provision-os", views.project_prov_os, name="project_prov_os"),
    path("menu/provision-vmw", views.project_prov_vmw, name="project_prov_vmw"),
    path("fa/", views.project_fa, name="project_fa"),
]
