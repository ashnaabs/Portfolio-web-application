from django.urls import path
from . import views

urlpatterns=[
path('list/<int:profile_id>',views.list,name='list_id'),
path('list/',views.list,name='list'),
path('create/',views.Createbook,name='create'),
path('update/<int:profile_id>',views.UpdateProfile,name='update'),
path('update_port/<int:profile_id>',views.UpdatePortfolio,name='update_port'),
path('delete/<int:profile_id>',views.DeleteProfile,name='delete'),
path('portfolio/',views.CreatePortfolio,name='portfolio'),
path('index/',views.Index,name='index'),
path('index/<int:profile_id>',views.Index,name='index_id'),
path('', views.register, name='register'),
path('login/', views.login_user, name='login'),
path('logout/', views.logout_user, name='logout'),
path('indexi_id/<int:profile_id>',views.IndexI,name='indexi_id'),
path('indexi_id/',views.IndexI,name='indexi'),
path('project/',views.CreateProject,name='project'),
path('update_project/<int:profile_id>',views.UpdateProject,name='update_project'),
path('dlt/',views.dlt,name='dlt'),
path('add-id/', views.add_user_id, name='add_user_id')
]