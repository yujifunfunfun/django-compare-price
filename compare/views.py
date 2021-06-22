from django.http import request
from django.shortcuts import render,redirect
from .models import Apparel
from django.views.generic import View
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic import TemplateView


class SearchView(TemplateView):
    template_name = "compare/search.html"


class ApparelList(ListView):

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

    def get_queryset(self):
        n_word  = self.request.GET.get('name')

        if n_word:
            object_list = Apparel.objects.filter(
                Q(name__icontains=n_word) 
            )
        else:
            object_list = Apparel.objects.all()

        return object_list


    