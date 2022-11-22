from django.contrib.admin import AdminSite


class CustomeSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'

custom_site = CustomeSite(name='cus_admin')