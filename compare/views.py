from django.http import request
from django.shortcuts import render,redirect
from .models import Apparel
from django.views.generic import View
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm
from django.shortcuts import redirect, get_object_or_404
from .models import Favorite

class SearchView(TemplateView):
    template_name = "compare/search.html"


class ApparelList(ListView):
    template_name = 'compare/apparel_list.html'
    paginate_by = 5

    def get_queryset(self):
        q_word  = self.request.GET.get('query')

        if q_word:
            object_list = Apparel.objects.filter(
                Q(name__icontains=q_word) 
            )
        else:
            object_list = Apparel.objects.all()

        return object_list

class ComparePrice(ListView):
    template_name = 'compare/compare_list.html'
    context_object_name = 'compare_list'
    def get_queryset(self):
        n_word  = self.request.GET.get('name')

        if n_word:
            compare_list = Apparel.objects.filter(
                Q(name__icontains=n_word) 
            )
        else:
            compare_list = Apparel.objects.all()

        return compare_list

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'compare/login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'compare/search.html'



class FollowApparel(View):
    def get(self,request,pk):

     apparel_list =  Apparel.objects.all()
     apparel_hit = apparel_list.pk == pk

     q = Favorite(
       user_id=request.user,
       item_id = pk,
       name = apparel_hit.name
     )
     q.save()
     return redirect('search:apparel')

