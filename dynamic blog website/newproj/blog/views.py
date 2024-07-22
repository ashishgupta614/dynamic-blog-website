from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages
from .templatetags import get_dict

def createblog(request):
    if request.method == "POST":
        category = request.POST.get('category', '')
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        slug = request.POST.get('slug', '')
        content = request.POST.get('content', '')
        create = Post(category=category, title=title, author=author, slug=slug, content=content)
        create.save()
        messages.success(request, "Success")
    return render(request, 'blog/createblog.html')

def bloghome(request):
    allposts=Post.objects.all().order_by('-timestamp')
    context={'allposts':allposts}
    return render(request, 'blog/bloghome.html', context)

def blogpost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post, parents=None)
    replies=BlogComment.objects.filter(post=post).exclude(parents=None)
    replyDict={}
    for reply in replies:
        if reply.parents.sno not in replyDict.keys():
            replyDict[reply.parents.sno]=[reply]
        else:
            replyDict[reply.parents.sno].append(reply)

    context={'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'blog/blogpost.html', context)
# Create your views here.

def postComment(request):
    if request.method=='POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment is added")
        else:
            parents = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parents=parents)
            comment.save()
            messages.success(request, "Your reply is added")
    return redirect(f"/blog/{post.slug}")


def search(request):
    query=request.GET['query']
    allpoststitle=Post.objects.filter(title__icontains=query)
    allpostscate=Post.objects.filter(category__icontains=query)
    allposts=allpoststitle.union(allpostscate)
    if allposts.count()==0:
        messages.warning(request, 'Please refine your search')
    param={'allposts' : allposts, 'query':query}
    return render(request, 'blog/search.html', param)
