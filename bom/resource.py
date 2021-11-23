import datetime
from random import randint

from import_export import resources
from import_export.fields import Field
from .models import *

class MarerialResource(resources.ModelResource):
    code = Field(attribute='code', column_name='物料编码')
    description = Field(attribute='description', column_name='物料描述')
    partnumber = Field(attribute='partnumber', column_name='物料型号')
    supplier_name = Field(attribute='supplier__name', column_name='供应商')
    category_name = Field(attribute='category__name', column_name='物料类别')

    class Meta:
        model = Material
        #导出字段
        fields = ('code', 'description', 'partnumber', 'supplier_name','category_name')
        #导出字段的顺序
        export_order = ('code', 'description', 'partnumber', 'supplier_name','category_name')

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