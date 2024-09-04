from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import project
from .forms import ProjectForm,reviewform
from django.contrib.auth.decorators import login_required
from .utils import searchproject,paginateproject

# Create your views here.



def projects(request):
    projects,search_query=searchproject(request)
    custom_range,projects=paginateproject(request,projects,3)
   



    
    context={
        'project':projects,
        'search_query':search_query,
        
        'custom_range':custom_range
    }
    return render(request,'projects/project.html',context)

def projectss(request,pk):
    projectobj=project.objects.get(id=pk)
    tags=projectobj.tags.all()
    form=reviewform()

    if request.method=='POST':
        form=reviewform(request.POST)
        review=form.save(commit=False)
        review.project=projectobj
        review.owner=request.user.profile
        review.save()

        projectobj.getvotecount


        return redirect('project',pk=projectobj.id)

       
        

    return render(request,"projects/single-project.html",{'project':projectobj,'tags':tags,'form':form})

@login_required(login_url='login')
def createproject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')

        
    
    context={'form':form}
    return render(request,"projects/project-form.html",context)



@login_required(login_url='login')
def updateproject(request,pk):
    profile=request.user.profile
    projects=profile.project_set.get(id=pk)
    form=ProjectForm(instance=projects)

    
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=projects)
        if form.is_valid():
            form.save()
            return redirect('account')

        
    
    context={'form':form}
    return render(request,"projects/project-form.html",context)


@login_required(login_url='login')
def deleteproject(request,pk):
    profile=request.user.profile
    projects=profile.project_set.get(id=pk)
    if request.method=='POST':
        projects.delete()
        return redirect('project')
    context={'object':projects}

    return render (request,'delete_template.html',context)
