from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)


def project_dev(request):
    return render(request, 'project_dev.html', {})

def project_menu(request):
    return render(request, 'project_menu.html', {})

def project_config(request):
    return render(request, 'project_config.html', {})

def project_prov_os(request):
    return render(request, 'project_provision_os.html', {})

def project_prov_vmw(request):
    return render(request, 'project_provision_vmw.html', {})

def project_fa(request):
    return render(request, 'project_fa.html', {})
