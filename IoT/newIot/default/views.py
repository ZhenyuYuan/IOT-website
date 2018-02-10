
# Create your views here.
# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from default.models import Device,history,Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import json
import random
import datetime


# Create your views here.

logger = logging.getLogger('django')
Biguser = None
#Person.objects.all().delete()
@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        key = request.POST['keybit']
        if(key=="1"):
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            #user = Person.objects.filter(username=username)
            if True==Person.objects.filter(username=username).exists():
                user = Person.objects.get(username=username)
                if password==user.password :
                    global Biguser
                    Biguser = user
                    return HttpResponseRedirect("/index")
            return HttpResponseRedirect("/")
        else:
            print("7845623")
            username = request.POST['username']
            password = request.POST['password']
            if False==Person.objects.filter(username=username).exists():
                user = Person(username=username,password=password)
                user.save()
            return HttpResponseRedirect("/")


@csrf_exempt
def my_logout(request):
    Biguser=None
    # print request.session.keys()
    return HttpResponseRedirect("/")

def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr



def showList(request):
    global Biguser
    infolist = Device.objects.filter(user=Biguser)
    info = []
    for item in infolist:
        temp = {"id": item.id, "Name": item.Name, "SN": item.SN, "Temperature": item.Temperature, "Temrange": item.Temrange, "Updatetime": item.Updatetime, "Alarm": item.Alarm, "Operation": item.Operation}
        info.append(temp)
    res = {"info": info}
    print(info)
    return JsonResponse(res)

def table(request):
    return render(request, "table.html")

def add1(request):
    if request.method=='POST':
        alllist = Device.objects.filter(user=Biguser)
        for item in alllist:
            if item.Operation == 'ON':
                a = int(item.Temperature) + random.randint(-3, 3)
                if a < 0:
                    a = 0
                elif a > 100:
                    a = 100
                item.Temperature = str(a)
                if int(item.Temperature)>=int(item.Temrange):
                    item.Alarm=True
                else:
                    item.Alarm=False
                item.save()
                sn = item.SN
                tem = item.Temperature
                ut =  item.Updatetime
                ran = item.Temrange
                if(int(tem)>int(ran)):
                    alr="ON"
                else:
                    alr="OFF"
                todo = history(user=Biguser, SN=sn,Temperature=tem,Updatetime=ut,Temrange=ran,Alarm=alr)
                todo.save()
        print('qqqqqqqq')
        return HttpResponse(json.dumps({'name':'hxq','check':1}))

#@login_required()
def addlist(request):
    name = request.POST['Name']
    sn = request.POST['SN']
    temrange = request.POST['Temrange']
    if temrange == '':
        temrange = '60'
    tem = random.randint(0,int(temrange))
    alarm = 0
    #uptime = datetime.datetime.now()
    op = 'ON'
    if name != '' and sn != '':
        global Biguser
        Device.objects.create(user=Biguser,Name=name, SN=sn, Temperature=tem, Temrange=temrange,
                          Alarm=alarm,  Operation=op)
        res = {"success": "true"}
    return JsonResponse(res)

#@login_required()
def editlist(request):
    id = request.POST['id']
    name = request.POST['Name']
    sn = request.POST['SN']
    temrange = request.POST['Temrange']
    if temrange == '':
        temrange = '60'
    device = Device.objects.filter(user=Biguser).get(id=id)
    if name != '' and sn != '':
        device.Name = name
        device.SN = sn
        device.Temrange = temrange
        if int(device.Temperature) >= int(device.Temrange):
            device.Alarm = True
        else:
            device.Alarm = False
        device.save()
        res = {"success": "true"}
    return JsonResponse(res)

#@login_required()
def dellist(request):
    id = request.GET['id']
    Device.objects.filter(user=Biguser).get(id=id).delete()
    res = {"success": "true"}
    return JsonResponse(res)

#@login_required()
def switchdevice(request):
    id = request.GET['id']
    device = Device.objects.filter(user=Biguser).get(id=id)
    if device.Operation == 'ON':
        device.Operation = 'OFF'
        device.Temperature = str(int(device.Temrange)-random.randint(5,15))
        device.Alarm = False
    elif device.Operation == 'OFF':
        device.Operation = 'ON'
    device.save()
    res = {"success": "true"}
    return JsonResponse(res)

def showhistory(request):
    sn=request.GET['SN']
    his = history.objects.filter(user=Biguser).get(SN=sn)
    res = {"his":his}
    return JsonResponse(res)

def getlog(request):
    if request.method == 'GET':
        return render(request, 'table.html')
    elif request.method == 'POST':
        getSN = request.POST['postSN']
        info=history.objects.filter(user=Biguser).filter(SN=getSN);
        info = info.order_by('-Updatetime')
        return render(request,"log.html",{'info':info})

def indexlog(request):
    infolist = history.objects.filter(user=Biguser)
    info = []
    for item in infolist:
        temp = {"SN": item.SN, "Temperature": item.Temperature, "Updatetime":item.Updatetime}
        info.append(temp)
    res = {"info": info}
    return JsonResponse(res)

def showDevNum(request):
    info = Device.objects.filter(user=Biguser).count()
    res = {"info": info}
    return JsonResponse(res)

def showLogNum(request):
    info= history.objects.filter(user=Biguser).count()
    res={"info":info}
    return JsonResponse(res)

def showNorDevNum(request):#在主页显示正常设备数量
    info=0
    count = Device.objects.filter(user=Biguser)
    for temp in count:
        if(int(temp.Temrange)>int(temp.Temperature)):
            info=info+1
    res = {"info": info}
    return JsonResponse(res)

def showAlrDevNum(request):
    info=0
    count = Device.objects.filter(user=Biguser)
    for temp in count:
        if(int(temp.Temrange)<int(temp.Temperature)):
            info=info+1
    res = {"info": info}
    return JsonResponse(res)

def getDevTemNum(request):
    temp1 = Device.objects.filter(user=Biguser)
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    for tem in temp1:
        if (int(tem.Temperature) > 0 and int(tem.Temperature) <= 20):
            count1=count1+1
        elif (int(tem.Temperature)  >20 and int(tem.Temperature) <= 40):
            count2=count2+1
        elif (int(tem.Temperature) > 40 and int(tem.Temperature) <= 60):
            count3=count3+1
        elif (int(tem.Temperature) > 60 and int(tem.Temperature) <= 80):
            count4=count4+1
        else:
            count5=count5+1
    print('试一下')
    dict = {"catagories": ["0-20℃","20-40℃","40-60℃","60-80℃","80-100℃"],"data":[count1, count2, count3, count4, count5]}
    return JsonResponse(dict)


def alertlog(request):
    info = history.objects.filter(user=Biguser).filter(Alarm="ON");
    info = info.order_by('-Updatetime')
    return render(request, "alertlog.html", {'info': info})










