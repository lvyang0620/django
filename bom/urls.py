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
    path('supplier_add/',views.supplier_add,name='supplier_add'),
    path('supplier_edit/<str:code>/',views.supplier_edit,name='supplier_edit'),
    path('supplier_del/<str:code>/',views.supplier_del,name='supplier_del'),
    path('supplier_handle/',views.supplier_handle,name='supplier_handle'),
    path('categorylist/',views.CategoryListView.as_view(),name='categorylist'),
    path('category/',views.category,name='category'),
    path('category_add/',views.category_add,name='category_add'),
    path('category_del/<str:code>/', views.category_del, name='category_del'),
    path('category_edit/<str:code>/',views.category_edit,name='category_edit'),
    path('category_handle/',views.category_handle,name='category_handle'),
    path('projectlist/',views.ProjectListView.as_view(),name='projectlist'),
    path('project/',views.project,name='project'),
    path('project_add/',views.project_add,name='project_add'),
    path('project_edit/<int:id>/',views.project_edit,name='project_edit'),
    path('project_del/<int:id>/',views.project_del,name='project_del'),
    path('project_handle',views.project_handle,name='project_handle'),
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
