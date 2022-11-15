from . import views
from django.urls import path
app_name='todoapp'
urlpatterns = [

    path('',views.Home,name='home'),
    # path('delete/<int:id>',views.delete,name='delete'),
    # path('update/<int:id>', views.update, name='update'),

    path('', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),

]