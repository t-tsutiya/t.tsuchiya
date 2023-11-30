from django.urls import path
from . import views

app_name = 'koukaapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
    path('gpt/', views.GPTView.as_view(), name = 'gpttest'),

    path('Popular/', views.Index2View.as_view(), name = 'popular'),
    path('New/', views.Index3View.as_view(), name = 'new'),
   
]
