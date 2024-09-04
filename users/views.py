from django.shortcuts import render,redirect
from .models import Profile,Skill,Message
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import customusercreationform,usereditform,skillmodel,MessageForm
from .utils import searchprofile,paginateprofile
from django.core.paginator import Paginator


# Create your views here.

def registeruser(request):
    page='register'
    form=customusercreationform
    if request.method=='POST':
        form=customusercreationform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,'user account was created')
            login(request,user)
            return redirect('profile-edit')
            
        else:
            messages.success(request,'an error has been occurred')

    context={
        'page':page,
        'form':form
    }
    return render(request,'users/login_register.html',context)





def loginpage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=='POST':
        # print(request.method)
        username=request.POST['username'].lower()
        password=request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist ')        

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,'username or password is invalid')


    return render(request,'users/login_register.html')

def logoutpage(request):
    logout(request)
    messages.info(request,'user logout successfully')
    return redirect('login')


def profiles(request):
    profiles,search_query=searchprofile(request)
    custom_range,profiles=paginateprofile(request,profiles,3)
    context={
        'profile':profiles,
        'search_query':search_query,
        'custom_range':custom_range
    }
    return render(request,'users/profiles.html',context)

def userprofile(request,pk):
    profile=Profile.objects.get(id=pk)
    topskills=profile.skill_set.exclude(description__exact="")
    otherskills=profile.skill_set.filter(description="")

    context={
        'profile':profile,
        'topskills': topskills,
         'otherkills': otherskills
    }
    return render(request,'users/user_profile.html',context)

@login_required(login_url='login')
def accounts(request):
    profile=request.user.profile
    skills=profile.skill_set.all()
    project=profile.project_set.all()
    context={
    'profile':profile,
    'skills':skills,
    'projects':project
    }
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def useredit(request):
    profile=request.user.profile
    form=usereditform(instance=profile)
    if request.method=='POST':
        form=usereditform(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={
        'form':form
    }
    return render(request,'users/profile_edit.html',context)

@login_required(login_url='login')
def addskill(request):
    profile=request.user.profile
    form=skillmodel()
    if request.method=='POST':
        form=skillmodel(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            return redirect('account')
            
    context={
        'form':form
    }

    return render(request,'users/skill_form.html',context)



@login_required(login_url='login')
def updateskill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=skillmodel(instance=skill)
    if request.method=='POST':
        form=skillmodel(request.POST,instance=skill)
        if form.is_valid():
          
            form.save()
            return redirect('account')
            
    context={
        'form':form
    }

    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def deleteskill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    if request.method=="POST":
        skill.delete()
        return redirect('account')
    context={
    'object':skill
    }
    return render(request,'delete_template.html',context)


@login_required(login_url='login')
def inbox(request):
    profile=request.user.profile
    messageRequestes=profile.messages.all()
    unreadCount=messageRequestes.filter(is_read=False).count()
    context={
    'messageRequestes':messageRequestes,
    'unreadCount':unreadCount

    }

    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile=request.user.profile
    message=profile.messages.get(id=pk)
    if message.is_read==False:
    
        message.is_read=True
        message.save()
    context={
    'message':message
    }
    return render(request,'users/message.html',context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('user-profiles', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)

