from django.shortcuts import render, redirect
from posts.models import Post, Comment


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
        return render(request, 'posts/create.html')

    if request.method == 'POST':
        data = request.POST
        errors = {}


    if data.get('title').__len__() < 8:
        errors['title_error'] = 'Min length 8 symbols'


    if data.get('description').__len__() < 6:
        errors['title_error'] = 'Min length 8 symbols'

    if errors.keys().__len__() == 0:
        Post.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            rate=data.get('rate')
        )

        return redirect('/posts/')
    return render(request, 'posts/create.html', context={'errors': errors})
