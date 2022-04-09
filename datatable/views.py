from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import *
from .forms import *

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "datatable/category.html"

class CategoryAddView(View):
    template_name = 'datatable/category_add.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name)


class CategoryUpdateView(View):
    template_name = 'datatable/category_update.html'

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        return render(request, self.template_name, {'category': category})
    
    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'category': category})


class CategoryDeleteView(View):
    def delete(self, request, pk):
        arr = list()
        Category.objects.get(pk=pk).delete()
        categories = Category.objects.all()
        for item in categories:
            data = dict()
            data["id"] = item.id
            data["name"] = item.name
            arr.append(data)
        return JsonResponse({"categories": arr})
        

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "datatable/post.html"


class PostAddView(View):
    template_name = 'datatable/post_add.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = dict()
        req_data = dict()
        if(request.FILES['upload']):
            upload = request.FILES['upload']
            req_data["title"] = request.POST["title"][0]
            req_data["description"]= request.POST["description"][0]
            req_data["image"] = "/media/"+upload.name
            req_data["category"] = request.POST["category"][0]
        form = PostForm(req_data)
        if form.is_valid():
            form.save()
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            data = {}
        else:
            data = {"errors": form.errors}
        return render(request, self.template_name, data)


class PostUpdateView(View):
    template_name = 'datatable/post_update.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, self.template_name, {'post': post})
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        data = dict()
        req_data = dict()
        if(request.FILES):
            upload = request.FILES['upload']
            req_data["title"] = request.POST["title"][0]
            req_data["description"]= request.POST["description"][0]
            req_data["image"] = "/media/"+upload.name
            req_data["category"] = request.POST["category"][0]
        else:
            req_data["title"] = request.POST["title"]
            req_data["description"] = request.POST["description"]
            req_data["image"] = post.image
            req_data["category"] = request.POST["category"]
        
        form = PostForm(req_data, instance=post)
        
        if form.is_valid():
            form.save()
            if(request.FILES):
                upload = request.FILES['upload']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
            data = {"post": post}
        else:
            data = {"post": post, "errors": form.errors}
        return render(request, self.template_name, data)


class PostDeleteView(View):
    def delete(self, request, pk):
        arr = list()
        Post.objects.get(pk=pk).delete()
        posts = Post.objects.all()
        for item in posts:
            data = dict()
            data["id"] = item.id
            data["title"] = item.title
            data["description"] = item.description
            data["category_name"] = item.category.name
            data["image"] = item.image
            arr.append(data)
        return JsonResponse({"posts": arr})

class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/home.html"


class BlogGetListView(View):
    template_name = "blog/home.html"

    def get(self, request, pk):
        post = Post.objects.filter(category_id=pk)
        return render(request, self.template_name, {"post": post})