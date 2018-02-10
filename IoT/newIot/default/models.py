from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Device(models.Model):
    user = models.ForeignKey(Person)
    SN = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    Temperature = models.CharField(max_length=20)
    Temrange = models.CharField(max_length=20)
    Updatetime = models.DateTimeField(max_length=20,auto_now=True)
    Alarm = models.BooleanField(max_length=10)#OFF01，ON
    Operation = models.CharField(max_length=20)#OFF,ON

    def __unicode__(self):
        return '%s' % (self.catname)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
class history(models.Model):
    user = models.ForeignKey(Person)
    SN = models.CharField(max_length=20)
    Temperature = models.CharField(max_length=20)
    Updatetime = models.DateTimeField(max_length=20,auto_now=True)
    Temrange = models.CharField(max_length=20)
    Alarm= models.CharField(max_length=20)