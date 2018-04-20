from django.shortcuts import render, redirect

from posts.models import Post 

def index(request):
	post = Post.objects.all()
	context1 = {
		'post': post
	}
	return render(request, 'index.html', context)

def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	context2 = {
		'post': post
	}
	return render(request, 'post_detail.html', context2)

def post_add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		
		post = post(title = title, text = text)
		
		post.save()
		return redirect('/posts')
	else:
		return render(request, 'post_add.html')

def post_edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
    	title = request.POST['title']
		text = request.POST['text']
    	
    	post.title =title
    	post.text = text
    	post.save()
    	return redirect('index2') 
    else:
    	return render(request, 'post_edit.html', {"post": post})

def post_delete(request, post_id):
	post = post.objects.get(id = post_id)
	post.delete()
	return redirect('index2')



