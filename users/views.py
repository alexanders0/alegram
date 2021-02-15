""" User views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """ Sign up view """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save form data """
        form.save()
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Update profile view """
    model = Profile
    template_name = "users/update_profile.html"
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """ Return user's profile """
        return self.request.user.profile

    def get_success_url(self):
        """ Return to user's profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """ Login view """
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ Logout view """
    pass
