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
    path('supplier/',views.supplier,name='supplier'),
    path('categorylist/',views.CategoryListView.as_view(),name='categorylist'),
    path('category/',views.category,name='category'),
    path('projectlist/',views.ProjectListView.as_view(),name='projectlist'),
    path('project/',views.project,name='project'),
    path('materiallist/',views.MaterialtListView.as_view(),name='materiallist'),
    path('material/',views.material,name='material'),
    path('bominfolist/',views.BominfoListView.as_view(),name='bominfolist'),
    path('bominfo/',views.bominfo,name='bominfo'),
    path('bomlistlist/',views.BomlistListView.as_view(),name='bomlistlist'),
    path('ecnlist/',views.EcnListView.as_view(),name='ecnlist'),
    path('ecn/',views.ecn,name='ecn'),
    path('bominfotobomlistlist/', views.BominfoToBomlistListView.as_view(),name='bominfotobomlistlist'),
    path('bomdetail/<str:bomname>/', views.bomdetail,name='bomdetail'),
    path('specific_bom_detail/<str:bomname>/', bominfo_to_bomlist_views.specific_bom_detail,name='specific_bom_detail'),

]
