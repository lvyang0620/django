import datetime
from random import randint

from django.apps import apps
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field
from .models import *


class SupplierResource(resources.ModelResource):
    ''' #此处不能设置中文别名，否则导入不成功
    code = Field(attribute='code', column_name='供应商编码')
    name = Field(attribute='name', column_name='供应商名称')
    contacts_name = Field(attribute='contacts_name', column_name='联系人姓名')
    contacts_phone = Field(attribute='contacts_phone', column_name='联系电话')
    contacts_position = Field(attribute='contacts_position', column_name='职位')
    address = Field(attribute='address', column_name='地址')
    '''
    def __init__(self):
        super(SupplierResource, self).__init__()
        field_list = apps.get_model('bom', 'Supplier')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name


    def get_export_fields(self):
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
                # 如果设置过verbose_name，则将column_name替换为verbose_name
                # 否则维持原有的字段名
        return fields

    class Meta:
        model = Supplier

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)
        # 导出字段
        fields = ('code', 'name', 'contacts_name', 'contacts_phone', 'contacts_position', 'address')
        # 导出字段的顺序
        #export_order = ('code', 'name', 'contacts_name', 'contacts_phone', 'contacts_position', 'address')


class MarerialResource(resources.ModelResource):
    '''
    code = Field(attribute='code', column_name='物料编码')
    description = Field(attribute='description', column_name='物料描述')
    partnumber = Field(attribute='partnumber', column_name='物料型号')
    '''
    Field(attribute='supplier_code', column_name='supplier_code',widget=ForeignKeyWidget(Supplier, 'code'))
    Field(attribute='supplier_name', column_name='supplier_name',widget=ForeignKeyWidget(Supplier, 'name'))
    Field(attribute='category_code', column_name='category_code',widget=ForeignKeyWidget(Category, 'code'))
    Field(attribute='category_name', column_name='category_name',widget=ForeignKeyWidget(Category, 'name'))
    '''
    def __init__(self):
        super(MarerialResource, self).__init__()
        field_list = apps.get_model('bom', 'Material')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
    
    def get_export_fields(self):
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
                # 如果设置过verbose_name，则将column_name替换为verbose_name
                # 否则维持原有的字段名
        return fields
    '''
    class Meta:
        model = Material
        #导出字段
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)
        #fields = ('code', 'description', 'partnumber','supplier__code','supplier__name','category__code','category__name')
        #导出字段的顺序
        #export_order = ('code', 'description', 'partnumber','supplier__code','supplier__name','category__code','category__name')

class BomlistResource(resources.ModelResource):
    sn = Field(column_name='序号')
    material_code = Field(attribute='material__code', column_name='物料编码')
    material_description = Field(attribute='material__description', column_name='物料描述')
    material_partnumber = Field(attribute='material__partnumber', column_name='物料型号')
    material_supplier_name = Field(attribute='material__supplier__name', column_name='供应商')
    num = Field(attribute='num', column_name='数量')
    references = Field(attribute='references', column_name='位号')

    #序号字段的生成器
    count = 0
    @staticmethod
    def dehydrate_sn(instance: Bomlist):
        BomlistResource.count +=1
        return BomlistResource.count
    #一次导出完成后序号生成器清0
    def after_export(queryset, data, *args, **kwargs):
        BomlistResource.count = 0

    class Meta:
        model = Bomlist
        #导出字段
        fields = ('sn', 'material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')
        #导出字段的顺序
        export_order = ('sn','material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')