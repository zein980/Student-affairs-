from django.urls import path
from . import views
urlpatterns = [
    path('', views.newbage, name='newpage'),
    path('index', views.index, name='index'),
    path('add', views.add, name='add'),
    path('show/update/<int:id>', views.update, name='update'),
    path('show/update/updatestudent/<int:id>',views.updatestudent, name='updatestudent'),
    path('show/delete/<int:id>', views.delete, name='delete'),
    path('show', views.show, name='show'),
    path('search/department/<int:id>', views.department, name='department'),
    path('search', views.search, name='search'),
    path('ajex/validate_id/', views.validate_id, name='validate_id'),
]
