from django.db.models import Q
from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from posts.constants import PAGINATION_LIMIT


def main_page_view(request):
    if request.method == 'GET':
        context = {
            'user': request.user
        }
        return render(request, 'layouts/index.html', context=context)


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        if search:
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search))

        # if search:
        #     posts = posts.filter(title__icontains=search) | posts.filter(description__icontains=search)
        #     # posts = posts.filter(title__icontains=search)# поиск по всему тайтлу
        #     # posts = posts.filter(title__endswith=search)# поиск на права слева
        #     # posts = posts.filter(title__startswith=search)#поиск слева на права

        """ starts_with ends_with icontains contains """

        context = {
            'posts': posts,
            'user': request.user,
            'pages': range(1, max_page+1)
        }


        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        # comments = Comment.objects.filter(post_id=id)

        context = {
            'post': post,
            'form': CommentCreateForm,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post=post
            )
            return redirect(f'/posts/{id}/')
        context = {
            'post': post,
            'form': form,
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



