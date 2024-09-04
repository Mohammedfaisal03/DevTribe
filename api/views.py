from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import project,Review

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/project'},
        {'GET':'/api/project/id'},
        {'POST':'/api/project/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},


    ]
    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(routes):
    projects=project.objects.all()
    serializer=ProjectSerializer(projects,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getProject(routes,pk):
    projects=project.objects.get(id=pk)
    serializer=ProjectSerializer(projects,many=False)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectvote(request,pk):
    projects=project.objects.get(id=pk)
    user=request.user.profile
    data=request.data

    review,created=Review.objects.get_or_create(
        owner=user,
        project=projects,


    )
    review.value=data['value']
    review.save()
    projects.getvotecount
    
    serializer=ProjectSerializer(projects,many=False)
    return Response(serializer.data)