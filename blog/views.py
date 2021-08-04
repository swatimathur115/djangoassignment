from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Category, Comment, Post, Tag,CustomUser
from .forms import PostForm,NewUserForm,ProfileUserForm,CommentForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# # Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')    
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	form = CommentForm(request.POST) 	
	comment=Comment.objects.filter(post=post,parent__id=None)		
	return render(request, 'blog/post_detail.html', {'post': post,'form':form,'comment':comment})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			form.save_m2m()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES,instance=post)
		print(form)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			form.save_m2m()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def registerPage(request):
	form = NewUserForm()
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Successfully created account for '+username)
			return redirect('loginPage')
	context = {'form': form}
	return render(request, 'blog/register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('post_list')		
		else:
			messages.info(request, "Username or Password is incorrect!")
	return render(request, 'blog/loginPage.html')

def logoutUSer(request):
	logout(request)
	return redirect('loginPage')

def CategoryView(request,slug):
	category = Category.objects.filter(slug=slug).last()
	category_posts = Post.objects.filter(category=category)	
	return render(request, 'blog/category_detail.html', {'slug':slug, 'category_posts':category_posts,'category':category})

def TagView(request,slug):
	tag= Tag.objects.filter(slug=slug).last()
	tag_posts = Post.objects.filter(tag=tag)
	return render(request, 'blog/tag_detail.html', {'slug':slug, 'tag_posts':tag_posts,'tag':tag})

def profile_edit(request):
	form =  ProfileUserForm(instance=request.user)
	profile=CustomUser.objects.filter(id=request.user.id)
	if request.method == 'POST':
		form =  ProfileUserForm(request.POST,request.FILES,instance= request.user)
		if form.is_valid():
			form=form.save()
			messages.success(request,"Profile details updated successfully")
			return redirect('profile_edit')
	context = {'form':form,'profile':profile}			
	return render(request, 'blog/profile_edit.html',context)

def add_comment(request, pk):
	form = CommentForm(request.POST)
	post = get_object_or_404(Post, pk=pk)		
	if request.method == "POST":
		form = CommentForm(request.POST)		
		if form.is_valid():		
			parent_obj = None		
			try:			
				parent_id = request.POST.get('parent_id')
			except:
				parent_id = None			
			if parent_id:
				parent_obj =  Comment.objects.get(id=parent_id)		
				print(parent_obj,'111')		
				if parent_obj:				
					replay_comment = form.save(commit=False)					
					replay_comment.parent = parent_obj		
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	return render(request, 'blog/post_detail.html', {'form': form,'post':post})