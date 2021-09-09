from django.views.generic import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "home.html", context)