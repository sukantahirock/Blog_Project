from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm

def home(request):
    posts = Post.objects.all()  # ✅ সব পোস্ট দেখাবে
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # আপডেট হওয়ার পর হোমপেজে যাবে
    else:
        form = PostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == "POST":
        post.delete()
        return redirect('home')  # ✅ পোস্ট ডিলিট হলে হোমপেজে ফেরত যাবে
    
    return render(request, 'blog/delete_post.html', {'post': post})