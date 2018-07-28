from django.shortcuts import render , redirect , get_object_or_404
from .models import Information,About,Classes,Instructors_Row,Email,Post
# Create your views here.
def home(request):
    site_infos = Information.objects.first()
    data = {'site_infos':site_infos}
    return render(request, 'yoga/home.html' , context=data)

def about(request):  
    site_infos = Information.objects.first()
    about = About.objects.first()
    data = {'site_infos':site_infos,
            'about':about,
    }
    return render(request, 'yoga/about.html' , context=data)

def classes(request):
    site_infos = Information.objects.first()
    classes = Classes.objects.first()
    data = {'site_infos':site_infos,
            'classes':classes,
    }
    return render(request, 'yoga/classes.html' , context=data)

def instructors(request):
    site_infos = Information.objects.first()
    instructors = Instructors_Row.objects.all()
    data = {'site_infos':site_infos,
            'instructors':instructors,
    }
    return render(request, 'yoga/instructors.html' , context=data)

def contact(request):
    site_infos = Information.objects.first()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_contact = Email.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect('home')
    data = {'site_infos':site_infos}
    return render(request, 'yoga/contact.html' , context=data)

def blog(request):
    site_infos = Information.objects.first()
    posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    data = {'site_infos':site_infos,
            'posts':posts,
    }
    return render(request, 'yoga/blog.html' , context=data)

def post(request, id):
    site_infos = Information.objects.first()
    latest_posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    post = get_object_or_404(Post,pk=id)
    data = {'site_infos':site_infos,
            'post':post,
            'latest_posts':latest_posts,
    }
    return render(request, 'yoga/post.html' , context=data)