from django.shortcuts import render
from django.utils import timezone
from blog_app.models import Post
from django.shortcuts import render, get_object_or_404
#import pudb

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'post_list.html', {
		'posts': posts,
		})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post})