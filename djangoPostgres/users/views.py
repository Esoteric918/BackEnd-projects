from django.shortcuts import render
from .models import User, Post

def index(request):
    users = User.objects.all()
    user_posts = Post.objects.all()
    print(users.all())
    print(user_posts.all())

    return render(request, 'users/index.html', {'users': users, 'user_posts': user_posts})
