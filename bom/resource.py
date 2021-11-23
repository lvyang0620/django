import datetime
from random import randint

from import_export import resources
from import_export.fields import Field
from .models import *

class BomlistResource(resources.ModelResource):
    sn = Field(column_name='序号')
    material_code = Field(attribute='material__code', column_name='物料编码')
    material_description = Field(attribute='material__description', column_name='物料描述')
    material_partnumber = Field(attribute='material__partnumber', column_name='物料型号')
    material_supplier_name = Field(attribute='material__supplier__name', column_name='物料编码')
    num = Field(attribute='num', column_name='数量')
    references = Field(attribute='references', column_name='位号')

    count = 0
    @staticmethod
    def dehydrate_sn(instance: Bomlist):
        BomlistResource.count +=1
        return BomlistResource.count

    def after_export(queryset, data, *args, **kwargs):
        BomlistResource.count = 0

    class Meta:
        model = Bomlist
        fields = ('sn', 'material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')
        export_order = ('sn','material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')