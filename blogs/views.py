from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from forms import BlogEntry
from models import blog
from datetime import datetime



# Create your views here.
def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../login')

    temp = loader.get_template('blog/index.html')
    blogs_all = list(blog.objects.all())

    context = dict()
    context['username'] = request.session['username']
    context['objects'] = blogs_all

    return HttpResponse(temp.render(context, request))

def create_blog(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../login')
    if request.method == 'POST':
        form = BlogEntry(request.POST, request.FILES)

        if form.is_valid():
            ent = blog()
            ent.user = request.session['username']
            ent.title = form.cleaned_data['blogTitle']
            ent.body = form.cleaned_data['blogContent']
            ent.image = form.cleaned_data['blogPic']

            ent.save()
            return HttpResponseRedirect('../blog')
    form = BlogEntry()
    context = dict()
    context['form'] = form
    temp = loader.get_template('blog/register.html')

    return HttpResponse(temp.render(context, request))