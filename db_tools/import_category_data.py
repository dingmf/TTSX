#独立使用django的models
import sys
import os

# 获取当前文件路径  __file__ 文件的完整路径和文件名
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append("../"+pwd)
# 和manage.py 中的环境变量保持一致
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TTSX.settings")
# c:\\xxx\\b.py
# Django 版本大于等于1.7的时候，需要加上下面两句
import django
# 否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
django.setup()

from goods.models import GoodsCategory

# all_categorys = GoodsCategory.objects.all()

from db_tools.data.category_data import row_data

# 一层一层的遍历data下面category_data的数据   goods.models 下的GoodsCategory
for lev1_cat in row_data:
    lev1_intance = GoodsCategory()
    lev1_intance.code = lev1_cat["code"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1
    lev1_intance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_intance = GoodsCategory()
        lev2_intance.code = lev2_cat["code"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.category_type = 2
        lev2_intance.parent_category = lev1_intance
        lev2_intance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_intance = GoodsCategory()
            lev3_intance.code = lev3_cat["code"]
            lev3_intance.name = lev3_cat["name"]
            lev3_intance.category_type = 3
            lev3_intance.parent_category = lev2_intance
            lev3_intance.save()
