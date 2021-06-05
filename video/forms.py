from .models import Video
from django import forms
from course.models import Course


class Video_form(forms.ModelForm):
    def __init__(self, user_id, *args, **kwargs):
        super(Video_form, self).__init__(*args, **kwargs)  # populates the post
        self.fields['Course'].queryset = Course.objects.filter(instructor= user_id)
        
    class Meta:
        model = Video
        fields = "__all__"
