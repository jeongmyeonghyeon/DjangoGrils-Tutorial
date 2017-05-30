from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

from blog.models import Post


def post_list(request):
    # posts변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)를 대입
    # post = Post.objects.all()
    # print(post)
    # posts변수에 ORM을 사용해서 전달할 쿼리셋이
    # Post의 published_date가 timezone.now()보다
    # 작은 값을 가질때만 해당하도록 필터를 사용한다
    # post = Post.objects.filter(published_date__lte=timezone.now())
    post = Post.objects.order_by('-created_date')
    context = {
        "title": "PostList from post_list view",
        "posts": post
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    # print('post_detail_pk: ',pk)
    post = Post.objects.get(id=pk)
    context = {
        "post": post
    }
    return render(request, 'blog/post_detail.html', context=context)


def post_create(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        # django.http.request.QueryDict 반환 (딕셔너리)
        data = request.POST
        print(data)
        title = data['post_title']
        text = data['post_text']
        user = User.objects.first()
        # post 객체 생성
        post = Post.objects.create(
            title=title,
            text=text,
            author=user
        )
        # return HttpResponse(post)
        return redirect('post_detail', pk=post.pk)
