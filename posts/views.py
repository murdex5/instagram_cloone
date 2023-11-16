from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts.html", context)

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # if not request.user in post.likes:
    #     post.likes.add(request.user)
    #     post.likes_count += 1
    #     post.save()
    #     # If this view is intended for AJAX requests, return JSON
    #     return JsonResponse({'message': 'Liked successfully'})

    # # If not an AJAX request, render the template
    context = {
        "post": post,  # Pass the entire post object to the template
    }
    return render(request, 'post.html', context)
