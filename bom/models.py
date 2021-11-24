from django.db import models

#供应商表
class Supplier(models.Model):
    #供应商编码
    code = models.CharField(max_length=10,primary_key=True,verbose_name='供应商编码')
    #供应商名称
    name = models.CharField(max_length=50,db_index=True,verbose_name='供应商名称')
    #联系人姓名
    contacts_name = models.CharField(max_length=50,blank=True,null=True,verbose_name='联系人')
    # 联系人电话
    contacts_phone = models.CharField(max_length=20,blank=True,null=True,verbose_name='电话')
    # 联系人职位
    contacts_position = models.CharField(max_length=20,blank=True,null=True,verbose_name='职位')
    # 联系地址
    address = models.CharField(max_length=100,blank=True,null=True,verbose_name='地址')
    #是否有效
    isvalid_choices = [
        (0, '无效'),
        (1, '有效'),
    ]
    isvalid = models.IntegerField(choices=isvalid_choices,default=1)

    def __str__(self):
        return self.name

#物料类别表
class Category(models.Model):
    #物料类别码
    code = models.CharField(max_length=4, primary_key=True)
    #类别名称
    name = models.CharField(max_length=20)
    #是否有效
    isvalid_choices = [
        (0, '无效'),
        (1, '有效'),
    ]
    isvalid = models.IntegerField(choices=isvalid_choices,default=1)

    def __str__(self):
        return self.name

class Material(models.Model):
    #物料编码
    code = models.CharField(max_length=9, primary_key=True)
    #物料描述
    description = models.CharField(max_length=100,default='')
    #物料型号
    partnumber = models.CharField(max_length=50,default='',db_index=True)
    isvalid_choices = [
        (0, '无效'),
        (1, '有效'),
    ]
    isvalid = models.IntegerField(choices=isvalid_choices,default=1)
    #物料标记
    flag = models.CharField(max_length=10,blank=True,null=True)
    #供应商
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    #所属类别
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.code
        #return f'{self.code} {self.description} {self.partnumber} {self.supplier}'

class Project(models.Model):
    #项目名称
    name = models.CharField(max_length=20,unique=True)
    #项目配置描述
    description = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

#bom信息
class Bominfo(models.Model):
    #BOM列表的名称，存放BOM表的文件名称
    bomname = models.CharField(max_length=30,unique=True)
    #硬件版本号
    hw_version = models.CharField(max_length=5,null=True)
    #BOM配置描述
    description = models.CharField(max_length=100,default='')
    #该Bom文件隶属于某个项目
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #多对多器件列表 Material
    material = models.ManyToManyField(
        Material,
        through='bomlist',
        through_fields=('bominfo','material'),
    )
    def __str__(self):
        return self.bomname

class Bomlist(models.Model):
    #此条信息（包含物料、用量、位号等）所关联的bom名称
    bominfo = models.ForeignKey(Bominfo,on_delete=models.CASCADE)
    #器件列表
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    #用量
    num = models.IntegerField(max_length=5,default=1)
    #位号序列
    references = models.CharField(max_length=1000,default='')
    def __str__(self):
        return f'{self.bominfo}---{self.material}'

#ECN表
class Ecn(models.Model):
    #变更内容描述
    content = models.CharField(max_length=200)
    #状态
    state_choices = [
        (0, '未执行'),
        (1, '已执行'),
    ]
    state = models.IntegerField(choices=state_choices,default=0)
    #变更原因
    reason = models.CharField(max_length=100,null=True)
    #创建时间
    createtime = models.DateTimeField()
    #执行方式
    action_choices = [
        (0, '立即执行'),
        (1, '消化现有库存后执行'),
    ]
    action = models.IntegerField(choices=action_choices,default=0)
    #发起人
    createdby = models.CharField(max_length=20)
    #related bom
    bominfo = models.ForeignKey(Bominfo,on_delete=models.CASCADE)