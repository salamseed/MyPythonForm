from django.urls import path,include

from todoapp import views
app_name = 'todoapp'

urlpatterns = [
    path('',views.displayhome,name='displayhome'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('home1/',views.display.as_view(),name='home'),
    path('detail/<int:pk>/',views.detail.as_view(),name='detail'),
    path('updateview/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.deleteview.as_view(),name='deleteview'),

]