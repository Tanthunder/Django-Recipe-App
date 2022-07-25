from socket import fromfd
from django.shortcuts import render , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import ListView , DetailView , CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from . import models




def home(request):
    recipes = models.Recipe.objects.all()
    return render (request,'home.html',{'recipes':recipes})

def about(request):
    return render (request,'about.html')

class RecipeDetailView(DetailView):
    model=models.Recipe

class RecipeCreateView(LoginRequiredMixin , CreateView):
    model = models.Recipe
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title','description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    