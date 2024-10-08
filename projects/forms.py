from django.forms import ModelForm
from .models import project,Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model=project
        fields=['title','featured_image','description','demo_link','source_link','tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple()
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class reviewform(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']

    labels={
        'vlaue':'Place your vote',
        'body':'Add a comment with your vote'
    }
    def __init__(self,*args,**kwargs):
        super(reviewform,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
