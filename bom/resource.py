import datetime
from random import randint

from import_export import resources
from import_export.fields import Field
from .models import *

class BomlistResource(resources.ModelResource):
    id = Field(attribute='id', column_name='编号')
    sn = Field(column_name='序号')
    material_code = Field(attribute='material__code', column_name='物料编码')
    material_description = Field(attribute='material__description', column_name='物料描述')
    material_partnumber = Field(attribute='material__partnumber', column_name='物料型号')
    material_supplier_name = Field(attribute='material__supplier__name', column_name='物料编码')
    num = Field(attribute='num', column_name='数量')
    references = Field(attribute='references', column_name='位号')

    @staticmethod
    def dehydrate_sn(instance: Bomlist):
        return str(randint(0, 100))

    class Meta:
        model = Bomlist
        fields = ('id','sn', 'material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')
        export_order = ('id', 'sn','material_code', 'material_description', 'material_partnumber','material_supplier_name','num','references')