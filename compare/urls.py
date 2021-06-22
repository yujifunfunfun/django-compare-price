from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.SearchView.as_view(),name='search'),
    path('list/', views.ApparelList.as_view(),name='apparel'),
    path('compare',views.ComparePrice.as_view(),name='compare'),

]
