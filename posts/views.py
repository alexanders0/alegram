""" Post views """

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """ Post detail view """
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Post.objects.all()
    context_object_name = 'post'


@login_required
def create_post(request):
    """ Create new post view """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
