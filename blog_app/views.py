from django.shortcuts import render
from django.utils import timezone
from blog_app.models import Post
#import pudb

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	#pudb.set_trace()
	return render(request, 'post_list.html', {
		'posts': posts
		})