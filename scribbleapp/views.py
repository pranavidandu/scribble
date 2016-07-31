from django.shortcuts import render
#views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from scribbleapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import *
from django.template import *
from django.template.loader import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import auth
from htmllib import *
from scribbleapp.forms import *
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
@csrf_protect
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/home')
    return render_to_response('blog/add_post.html',
                              {'form': form},
                              context_instance=RequestContext(request))
def about(request):
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))
class PostDelete(DeleteView):
    model = Post
    template_name = 'wildbloggerapp/post_confirm_delete.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('view_post')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'wildbloggerapp/post_form.html'
    context_object_name = 'form'
    def get_success_url(self):
        return reverse('view_post')
def view_all_posts(request):
    id = request.user
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('blog/view_all.html', locals(), context_instance=RequestContext(request))
def view_other_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/display_other_post.html', locals(), context_instance=RequestContext(request))


def all_posts(request):
    author_id = request.user
    post_list = Post.objects.filter(author=author_id)
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/all.html', locals(), context_instance=RequestContext(request))
def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/display_post.html', locals(), context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
# Create your views here.
