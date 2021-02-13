""" Post forms """

# Django
from django.forms import ModelForm

# Models
from posts.models import Post


class PostForm(ModelForm):
    """ Post model form """

    class Meta:
        """ Form settings """

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
