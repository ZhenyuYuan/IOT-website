from tastypie.resources import ModelResource
from default.models import Device


class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        allowed_methods = ['get']