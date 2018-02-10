from django.conf.urls import url
from django.contrib import admin

from . import views

from django.conf.urls import include, url
from tastypie.api import Api
from default.api.resource import DeviceResource

v1_api = Api(api_name='v1')
v1_api.register(DeviceResource())

urlpatterns = [
     url(r'^add1/$', views.add1),
     url(r'^$', views.my_login), #登陆
     url(r'^logout/$', views.my_logout),#注销
     url(r'^index$', views.index),
     #url(r'^table$', views.showList),
     url(r'^tablePage$', views.table),
     url(r'^getlog$',views.getlog),


     url(r'^api/table/$', views.showList),
     url(r'^alertlog$',views.alertlog),
     url(r'^api/del/$', views.dellist),          #删除设备
     url(r'^api/add/$', views.addlist),          #添加设备
     url(r'^api/edit/$', views.editlist),        #编辑设备
     url(r'^api/switch/$', views.switchdevice),  #设备开关操作
     url(r'^api/getlog$',views.getlog),
     url(r'^api/indexlog$',views.indexlog),
     url(r'^api/showDevNum$',views.showDevNum),
     url(r'^api/showAlrDevNum$',views.showAlrDevNum),
     url(r'^api/showLogNum$',views.showLogNum),
     url(r'^api/showNorDevNum$',views.showNorDevNum),
     url(r'^getDevTemNum$',views.getDevTemNum),

     url(r'api/', include(v1_api.urls))
]
