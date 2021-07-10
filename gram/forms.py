from django.forms import ModelForm
from .models import *
class MyCommentForm(ModelForm):
    class Meta:
        model = CommentForm
        fields = ['comment']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields=['image','image_name','image_caption']