from django.urls import path

from . import views  # from the current directory import views

app_name = 'polls'
urlpatterns = [
    # path( the path , the view used to handle the logic at that route which is located in views.py)
    path('', views.IndexView.as_view(), name='index'),  # '' resembles an empty path, used for the home page
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # .as_view() is used because django expected a function call not a class call, so as view makes it appear as a function
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),


    path('thoughts/', views.thoughtsSubmit, name='thoughts submission'),
    path('thoughts/list/', views.ThoughtsView.as_view(), name='thoughts'),
    #   path('thoughts/', 'views.thoughtseditor()', name='thinking'),
]


