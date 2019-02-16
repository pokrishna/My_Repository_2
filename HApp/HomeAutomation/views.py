from django.shortcuts import render
from .models import logintable,homeDevices
from django.http import HttpResponse
import sqlite3
from sqlite3 import Error

# Create your views here.
idno=1
def login(request):
    uname=request.POST.get('username')
    pword=request.POST.get('password')
    tuser=request.POST.get('useradmin')
    logdata=logintable.objects.all()
    for ld in logdata :
        if tuser=='user':
            if tuser== ld.usertype:
                if uname==ld.username:
                    if pword==ld.password:
                        ifname={ 'usname':ld.username}
                        return render(request,'UserPortal.html',ifname)
        if tuser=='admin':
            if tuser== ld.usertype :
                if uname==ld.username:
                    if pword==ld.password:
                        ifname={ 'usname':ld.username}
                        return render(request,'AdminPortal.html',ifname)
    return render(request,'loginerror.html')
def logs(request):
    return render(request,'LoginPage.html')

def register(request):
    uname = request.POST.get('username')
    pword = request.POST.get('password')
    tuser = request.POST.get('useradmin')
    login_table=logintable(username=uname,password=pword,usertype=tuser)
    login_table.save()
    info={'usernames':uname}
    return render(request,"successful.html",info)
def createuser(request):
    return render(request,'CreateUser.html')
def addDevice1(request):
    return render(request,'AddDevices.html')
def addDevice2(request):
    divname=request.POST.get('dname')
    didesc=request.POST.get('ddesc')
    distatus=request.POST.get('dstatus')
    dt=homeDevices(device_name=divname,device_desc=didesc,device_status=distatus)
    dt.save()
    info = {'usernames': divname}
    return render(request, "successful.html", info)
def updateDevice1(request):
    id=request.POST.get('id')
    return render(request,'UpdateDevices.html',id)
def edits(request):
    device = homeDevices.objects.all()
    id=int(request.POST.get('id'))
    if id=="":
        info={'fyi':'please enter the valid id 1,2,3,4,.....'}
        return render(request,'UpdateDevices.html',info)
    for i in device:
        if i.id==id:
            idno=i.id
            info={'fyi':['Device Found',i.device_name,i.device_desc,i.device_status,id]}
            return render(request,'UpdateDevices.html',info)
    info={'fyi':'Device id not found'}
    return render(request,'UpdateDevices.html',info)

def updateDevices2(request):
    divname = request.POST.get('dname')
    didesc = request.POST.get('ddesc')
    distatus=request.POST.get('dstatus')
    try:
        homeDevices.objects.filter(device_name=divname).update(device_desc=didesc , device_status=distatus)
        list_data = homeDevices.objects.all()
    except Exception as ex:
        print(ex)
        return HttpResponse('Not able to update DEVICE')
    else:
        return HttpResponse('Device has been updated')
    return HttpResponse("Device  has been updated")

def deviceCon1(request):
    divname1 = request.POST.get('dname')
    distatus = request.POST.get('ac')
    desc=request.POST.get('desc')
    divname1=divname1.rstrip('/')
    print("divce name = ",divname1)
    print("divce status = ",distatus)
    print("device description = ",desc  )
    try:
        homeDevices.objects.filter(device_name=divname1).update(device_status=distatus)
        list_data = homeDevices.objects.all()
        info={'list_data':list_data}
    except Exception as ex:
        print(ex)
        return HttpResponse('Not able to update DEVICE')
    else:
        return render(request,'DeviceControler.html',info)

    return render(request,'DeviceControler.html',info)
def deviceCon(request):
    list_data= homeDevices.objects.all()
    info={'list_data':list_data}
    return render(request,'DeviceControler.html',info)

def UserList(request):
    list_user=logintable.objects.all()
    info_user={'list_user':list_user}
    return render(request,'UserList.html',info_user)

def devicesList(request):
     list_data = homeDevices.objects.all()
     info = {'list_data': list_data}
     return render(request,'DevicesList.html',info)


def delete_data1(request):
    divname1 = request.POST.get('dname')
    distatus = request.POST.get('ac')
    desc = request.POST.get('desc')
    divname1 = divname1.rstrip('/')
    print("divce name = ", divname1)
    print("divce status = ", distatus)
    print("device description = ", desc)
    try:
        homeDevices.objects.filter(device_name=divname1).delete()
        list_data = homeDevices.objects.all()
        info = {'list_data': list_data}
    except Exception as ex:
        print(ex)
        return HttpResponse('Not able to DELETE DEVICE')
    else:
        return render(request, 'DeleteDevices.html', info)

    return render(request, 'DeleteDevices.html', info)
def delete_data(request):
    try:
        list_data = homeDevices.objects.all()
        info = {'list_data': list_data}
    except Exception as ex:
        print(ex)
        return HttpResponse('Not able to DELETE DEVICE')
    else:
        return render(request, 'DeleteDevices.html', info)

    return render(request, 'DeleteDevices.html', info)


def ActiveDevicesList(request):
     list_data1 = homeDevices.objects.filter(device_status="ON").all()
     info = {'list_data':list_data1}

     return render(request,'DevicesList.html',info)


def InActiveDevicesList(request):
    list_data1 = homeDevices.objects.filter(device_status="OFF").all()
    info = {'list_data': list_data1}

    return render(request,'DevicesList.html', info)
