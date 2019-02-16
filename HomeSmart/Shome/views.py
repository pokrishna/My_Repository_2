from django.shortcuts import render
from .models import logintable,homeDevices
from django.http import HttpResponse
# Create your views here.
duname=''
def Login(request):
   return render(request,'LoginForm.html')

def loginPro(request):
    uname=request.POST.get('uname')
    pword=request.POST.get('password')
    tuser=request.POST.get('useradmin')
    logdata=logintable.objects.all()
    for ld in logdata :
        if tuser=='user':
            if tuser== ld.usertype:
                if uname==ld.username:
                    if pword==ld.password:
                        ifname={ 'usname':ld.username   }
                        return render(request,'UserPortal.html',ifname)
        if tuser=='admin':
            if tuser== ld.usertype :
                if uname==ld.username:
                    if pword==ld.password:
                        ifname={ 'usname':ld.username}
                        return render(request,'adminDashboard.html',ifname)

    return render(request,'loginerror.html')


def adminPanel(request):
    return render(request,'adminDashboard.html')
def AddUser1(request):
    return render(request,'AddUser.html')

def AddUser(request):
    uname = request.POST.get('uname')
    pword = request.POST.get('password')
    tuser = request.POST.get('useradmin')
    login_table=logintable(username=uname,password=pword,usertype=tuser)
    login_table.save()
    info={'username':uname+" has added successfully !!!"}
    return render(request,"adminDashboard.html",info)

def AddDevice1(request):
    list_user = logintable.objects.all()
    info_user = {'list_user': list_user}
    return render(request,'AddDevices.html',info_user)
def AddDevice2(request):
    divname=request.POST.get('device')
    duser=request.POST.get('uname')
    distatus=request.POST.get('status')
    dt=homeDevices(device_name=divname,device_operator=duser,device_status=distatus)
    dt.save()
    info = {'devicename': divname+" has added successfully !!!"}
    return render(request, "adminDashboard.html", info)


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
        return render('Not able to update DEVICE')
    else:
        return render(request,'DeviceControler.html',info)

    return render(request,'DeviceControler.html',info)
def deviceCon(request):
    list_data= homeDevices.objects.all()
    info={'list_data':list_data}
    return render(request,'DeviceControler.html',info)

def UserDeviceCon1(request):
    divname1 = request.POST.get('dname')
    distatus = request.POST.get('ac')
    desc=request.POST.get('desc')
    doperator=request.POST.get('doperator')
    divname1=divname1.rstrip('/')
    print("divce name = ",divname1)
    print("divce status = ",distatus)
    print("device description = ",desc  )
    doperator=doperator.rstrip('/')
    print("device operator",doperator)

    try:
        homeDevices.objects.filter(device_name=divname1).update(device_status=distatus)
        list_data = homeDevices.objects.filter(device_operator=doperator).all()
        info={'list_data':list_data}

    except Exception as ex:
        print(ex)
        return render('Not able to update DEVICE')
    else:
        return render(request,'UserDevicesControler.html',info)

    return render(request,'UserDevicesControler.html',info)
def UserDeviceCon(request):
    uname=request.POST.get('uname')
    list_data= homeDevices.objects.filter(device_operator=uname).all()
    info={'list_data':list_data}
    return render(request,'UserDevicesControler.html',info)
def UsersList(request):
    list_user = logintable.objects.all()
    info_user = {'list_user': list_user}
    return render(request, 'UsersList.html', info_user)



