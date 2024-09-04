from .models import Profile,Skill
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def paginateprofile(request,profile,result):
    page=request.GET.get('page')
    
    paginator=Paginator(profile,result)

    try:
        profile=paginator.page(page)
    except PageNotAnInteger:
        page=1
        profile=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        profile=paginator.page(page)

    leftindex=(int(page)-4)
    if leftindex<1:
        leftindex=1
    rightindex=(int(page)+5)
    if rightindex>paginator.num_pages:
        rightindex=paginator.num_pages+1

    custom_range=range(leftindex,rightindex)
    return custom_range,profile




def searchprofile(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    skills=Skill.objects.filter(name__iexact=search_query)

    profiles=Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills)

    )
    return profiles,search_query