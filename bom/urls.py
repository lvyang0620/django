from django.urls import path
from . import views
from . import bominfo_to_bomlist_views

app_name = 'bom'

urlpatterns = [
    path('test02/', views.test02),
    path('test/<int:id>/', views.test,name='test'),
    path('test_reverse/<int:id>/', views.test_reverse,name='test_reverse'),
    #path('index/<int:id>/', views.index,name='index'),
    path('', views.index,name='index'),
    path('supplierlist/',views.SupplierListView.as_view(),name='supplierlist'),
    path('categorylist/',views.CategoryListView.as_view(),name='categorylist'),
    path('projectlist/',views.ProjectListView.as_view(),name='projectlist'),
    path('specific_bom_detail/<str:bomname>/', bominfo_to_bomlist_views.specific_bom_detail,name='specific_bom_detail'),

]
