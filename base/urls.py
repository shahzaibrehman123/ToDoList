from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.Weblogin.as_view(), name='login'),
    path('logout/', views.Weblogout.as_view(), name='logout'),
    path('signup/', views.Webregister.as_view(), name='signup'),
    path('', views.Tasklist.as_view(), name='home'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
    path('view/<int:pk>/', views.TaskDetail.as_view(), name='view'),
    path('note/', views.Notelist.as_view(), name='note_list'),
    path('note_create/', views.NoteCreate.as_view(), name='note_create'),
    path('note_delete/<int:pk>/', views.NoteDelete.as_view(), name='note_delete'),
    path('note_update/<int:pk>/', views.NoteUpdate.as_view(), name='note_update'),
    path('note_detail/<int:pk>/', views.NoteDetail.as_view(), name='note_detail')
]
