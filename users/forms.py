from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill,Message

class customusercreationform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={
            'first_name':'name'
        }
    def __init__(self,*args,**kwargs):
        super(customusercreationform,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class usereditform(ModelForm):
    class Meta:
        model=Profile
        fields=['name','username','location','email','short_intro','bio','profile_image','socila_github','social_twitter','social_linkedin','social_youtube','social_website']
        labels={
            'socila_github':'github_link',
            'socila_twitter':'twitter',
            'socila_linkedin':'linkedin_profile',
            'socila_youtube':'youtube',
            'socila_website':'website'
        }

    def __init__(self,*args,**kwargs):
        super(usereditform,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class skillmodel(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']
    def __init__(self,*args,**kwargs):
        super(skillmodel,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['name','email','subject','body']

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})





