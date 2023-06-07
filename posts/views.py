from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import PostCreateForm


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        # comments = Comment.objects.filter(post_id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }

        return render(request, 'posts/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = PostCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/posts')

        return render(request, 'posts/create.html', context={
            'form': form
        })



