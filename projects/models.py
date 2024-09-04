from django.db import models
from users.models import Profile
# Create your models here.
import uuid
class project(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link=models.CharField(null=True,blank=True,max_length=2000)
    source_link=models.CharField(null=True,blank=True,max_length=2000)
    tags=models.ManyToManyField('Tag',blank=True)
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)

    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-vote_ratio','-vote_total','title']
    @property
    def reviewers(self):
        queryset=self.review_set.all().values_list('owner__id',flat=True)
        return queryset



     

    @property
    def getvotecount(self):
        reviews=self.review_set.all()
        upvotes=reviews.filter(value='up').count()
        totalvotes=reviews.count()

        ratio=(upvotes/totalvotes)*100
        self.vote_total=totalvotes
        self.vote_ratio=ratio
        self.save()


    


    
    
class Review(models.Model):
    Vote_Type=(
        ('up','up vote'),
        ('down','down vote')
    )
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project=models.ForeignKey(project, on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=Vote_Type)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together=[['owner','project']]

    def __str__(self):
        return self.value
    

    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name