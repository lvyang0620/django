from import_export.admin import ImportExportModelAdmin,ExportMixin,ImportMixin
from import_export import fields

from django.utils import timezone
from openpyxl import Workbook
from django.contrib import admin
from  .models import *
from  .resource import *
from django.utils.html import format_html
from django.http import HttpResponse
# Register your models here.
#注册Supplier模型
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['code','name','contacts_name','contacts_phone','contacts_position','address']
    list_display_links = ['name']
    search_fields = ('code', 'name','contacts_name')
    list_per_page = 10
admin.site.register(Supplier,SupplierAdmin)
#注册Category模型
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code','name']
    list_display_links = ['code','name']
    list_per_page = 10
admin.site.register(Category,CategoryAdmin)

class BomlistInline(admin.StackedInline):
    model = Bomlist
#注册Material模型
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['category','code','description','partnumber','supplier']
    list_display_links = ['code','description','partnumber']
    search_fields = ('code','description','partnumber')
    list_per_page = 5
    #inlines = [BomlistInline, ]
admin.site.register(Material,MaterialAdmin)
#注册Project模型
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    list_display_links = ['name','description']
    search_fields = ('name', 'description')
    list_per_page = 10
admin.site.register(Project,ProjectAdmin)
#注册Bominfo模型
class BominfoAdmin(admin.ModelAdmin):
    list_display = ['bomname','hw_version','description','project','detail']
    list_display_links = ['bomname']
    list_per_page = 10
    def detail(self,obj):
        return format_html('<a href="%s">%s</a>' % ("../bomlist/3/change/",'明细'))
    detail.allow_tags = True
    detail.short_description = 'BOM明细'
admin.site.register(Bominfo,BominfoAdmin)
#注册Bominfo模型
class EcnAdmin(admin.ModelAdmin):
    list_display = ['content','state','reason','createtime','action','createdby','bominfo']
    list_display_links = ['content']
    list_per_page = 10
admin.site.register(Ecn,EcnAdmin)

#注册Bomlist模型
class BomlistAdmin(ExportMixin, admin.ModelAdmin):
    #关联导出的类
    resource_class = BomlistResource
    #列表显示的字段，含自定义的外键关联字段信息'description','partnumber','supplier'
    list_display = ['bominfo','material','description','partnumber','supplier','num','references']
    list_display_links = ['material','description','partnumber']
    #可搜索的字段
    search_fields = ('bominfo__bomname', 'material__code',)
    list_per_page = 500
    #编辑页（详情页）显示的字段和顺序，不能显示外键的关联信息
    fields = ['bominfo','material','num','references']
    # 定义Bomlist的编辑页（详情页）中不可编辑的字段
    readonly_fields = ('bominfo','material')

    #显示外键的其他字段的函数
    def description(self,obj):
        return obj.material.description
    def partnumber(self,obj):
        return obj.material.partnumber
    def supplier(self,obj):
        return obj.material.supplier

admin.site.register(Bomlist,BomlistAdmin)