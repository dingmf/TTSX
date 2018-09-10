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

from goods.models import Goods

# all_categorys = GoodsCategory.objects.all()

from db_tools.data.product_data import row_data

for goods_dateil in row_data:
    goods = Goods()
    goods.name = goods_dateil["name"]