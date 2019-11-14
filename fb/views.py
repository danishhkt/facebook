from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_test(request):
    return render(request,'facebook.html')


def fn_register(req):
    firstname = req.POST['firstname']
    lname = req.POST['lastname']
    mobail = req.POST['mobail']
    passw=req.POST['password']
    dob = req.POST['dob']
    gender = req.POST['gender']
    check_exist=login.object.filter(email=mobail).exista()
    if not check_exist:
        login_obj=login(email=mobail,password=passw)
        logon_obj.save()
        if login_obj.id>0:
            register_obj=register(firstname=fname,surname=lname,birthday=dob,gender=gender,fk_login=login_obj)
            register_obj.save()
            if register_obj.id>0:
                return HttpResponse('success')
        return HttpResponse('success')
    return HttpResponse('alreadytaken....')            