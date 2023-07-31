from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('view',views.view,name='view'),
    # path('edit',views.edit,name='edit'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('editdata/<int:id>',views.editdata,name='editdata'),
    path('savedata',views.savedata,name='savedata'),
    path('delete/<int:id>',views.delete,name='delete'),
   
]