from django.urls import path,include
from supply import  views

urlpatterns = [
    path('list/',views.supply_list),
    path('add/',views.supply_add),
    path('detail/', views.supply_detail),
    path('edit/',views.supply_edit),
    path('delete/',views.supply_delete),

    path('material/list/',views.material_list),
    path('material/add/',views.material_add),
    path('material/detail/',views.material_detail),
    path('material/edit/',views.material_edit),


    path('quote/list/',views.quote_list),
    path('quote/add/',views.quote_add),
    path('quote/detail/',views.quote_detail),
    path('quote/edit/',views.quote_edit),

    path('mm/list/', views.mm_list),
    path('mm/add/', views.mm_add),
    path('mm/detail/', views.mm_detail),
    path('mm/edit/', views.mm_edit),
    path('mm/delete/', views.mm_delete),

]
