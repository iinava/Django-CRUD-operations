from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('view',views.view,name='view'),
    path('product',views.product,name='product'),
    path('productview',views.productview,name='productview'),
    # # path('edit',views.edit,name='edit'),
    path('editr/<int:id>',views.editr,name='editr'),
    path('editrdata/<int:id>',views.editrdata,name='editrdata'),
    path('saveregdata',views.saveregdata,name='saveregdata'),
     path('saveproduct',views.saveproduct,name='saveproduct'),
    path('deleter/<int:id>',views.deleter,name='deleter'),
    path('deletep/<int:id>',views.deletep,name='deletep'),
    path('editp/<int:id>',views.editp,name='editp'),
    path('editpdata/<int:id>',views.editpdata,name='editpdata'),
   
]