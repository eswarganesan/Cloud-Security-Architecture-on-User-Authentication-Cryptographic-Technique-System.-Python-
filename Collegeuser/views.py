from django.shortcuts import render,redirect
from random import random
from app1.models import College
# Create your views here.
from app1.models import Transcations111
bufferSize = 64 * 1024
password = "pwd"#
import pyAesCrypt
from os import stat, remove
loginUser = ""
loginFlag = False
forgotEmpID = ""
def index1(request):

    return render(request,'Collegeuser/register.html')


def register1(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        emp_id = request.POST['emp_id']
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        college = request.POST['code']
        ques_1_id = request.POST['ques_1_id']
        ans_1 = request.POST['ans_1']
        ques_2_id = request.POST['ques_2_id']
        ans_2 = request.POST['ans_2']
        gender = request.POST['gender']
        phone = request.POST['phone']
        repeat_password = request.POST['repeat_password']
        print(emp_id, name, password, email, college, ques_1_id, ans_1, ques_2_id, ans_2, gender, phone, repeat_password)
        count = 0
        message = ""
        searchObject = College.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0], emp_id)
            if lst[0] == emp_id:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1

        if password == repeat_password:
            if len(password) > 6:
                flag1, flag2, flag3 = 0, 0, 0
                for i in range(len(password)):
                    ele = ord(password[i])
                    if ele > 96 and ele < 123:
                        flag1 = 1
                    elif ele > 47 and ele < 58:
                        flag2 = 1
                    elif ele > 64 and ele < 91:
                        flag3 = 1
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    count = count + 1
                else:
                    message = message + "Re-enter the Password.\n"
        else:
            message = message + "Passwords does not match.\n"

        print(count)
        if count == 2:
            raw_text = password
            encrypt_text = raw_text
            College(emp_id=emp_id,
                     name=name,
                     password=encrypt_text,
                     email=email,
                     college=college,
                     ques_1_id=ques_1_id,
                     ans_1=ans_1,
                     ques_2_id=ques_2_id,
                     ans_2=ans_2,
                     gender=gender,
                     phone=phone).save()

            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}
        return render(request, 'Collegeuser/register.html', context)

    else:
        message = "Welcome To Registration Page"
        context = {"message": message}
        return render(request, 'Collegeuser/register.html', context)


def login1(request):
    global loginFlag, loginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)
        message = ""

        if len(College.objects.filter(emp_id=username)) == 0:
            message = message + "No Matching Accounts Found"
        else:
            pass_hash = str(College.objects.filter(emp_id=username)[0]).split(";")[4]
            decrypt_text = pass_hash
            if password == decrypt_text:
                message = message + "Welcome to the Home Page"
                loginFlag = True
                loginUser = username
                print(loginUser)
                return redirect('home1')
            else:
                message = message + "Wrong Password Entered"

        print(message)
        context = {"message": message}
        return render(request, 'Collegeuser/login.html', context)

    else:
        return render(request, 'Collegeuser/login.html')


def home1(request):
    global loginFlag, loginUser, loginName
    if loginFlag == False:
        return redirect('login')

    loginObj = str(College.objects.filter(emp_id=loginUser)[0]).split(";")
    name = loginObj[1]
    loginName = name
    print("Name:", name)

    context = {"name": name}
    return render(request, 'Collegeuser/home.html', context)


def logout1(request):
    global loginFlag, loginUser
    loginFlag = False
    loginUser = ""
    print("After Logout:", loginFlag, loginUser)
    return redirect('login')

import os
from django.conf import settings
from django.http import HttpResponse, Http404

def request(request):
    global loginFlag, loginUser
    if request.method == 'POST':
        filename = request.POST['filename']

        print("Downloadable file name",filename)
        message = ""

        with open("G:/ESWAR/INTERN/Edge Computing/Encryption/{0}.{1}".format(filename,"aes"), "rb") as fIn:
            with open("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename),"wb") as fOut:
                encFileSize = stat("G:/ESWAR/INTERN/Edge Computing/Encryption/{0}.{1}".format(filename,"aes")).st_size
                try:
        # decrypt file stream

                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                except ValueError:
                    # remove output file on error
                    remove("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename))


    else:
        downdata=Transcations111.objects.all()
        context={'downdata':downdata}
        return render(request, 'Collegeuser/request.html',context)








def down(request):

    global loginFlag, loginUser
    message=''
    if request.method == 'POST':
        filename = request.POST['filename']
        otp_from_user = request.POST['otp']
    print("Downloadable file name", filename)
    print("acces", loginUser)
    Wholedata = College.objects.get(emp_id=loginUser)
    axes_by_user = Wholedata.college
    Wholedata1 = Transcations111.objects.get(filename=filename)
    axes_by_file = Wholedata1.access1

    print('axis', axes_by_user, axes_by_file)
    print(otp_from_user)
    Otpdata = RequestFile.objects.get(otp=otp_from_user)
    the_otp = Otpdata.otp

    print(the_otp)
    print(otp_from_user)
    print(the_otp==otp_from_user)
   # import hashlib
   # hash_string1 = the_otp
   # sha_signature1 = hashlib.sha256(hash_string1.encode()).hexdigest()
   # print(sha_signature1)

   # hash_string2 = otp_from_user
   # sha_signature2 = hashlib.sha256(hash_string2.encode()).hexdigest()
   # print(sha_signature2)
    
    file_state = Otpdata.status
    print('file status', file_state)
    
    if (file_state == True) :
        print('Its status loop')

        #if axes_by_file == axes_by_user:
            #print('Its Axis loop')

        if otp_from_user==the_otp:
                with open(
                        "G:/ESWAR/INTERN/Edge Computing/Encryption/{0}.{1}".format(filename, "aes"),
                        "rb") as fIn:
                    with open("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename),
                              "wb") as fOut:
                        encFileSize = stat(
                            "G:/ESWAR/INTERN/Edge Computing/Encryption/{0}.{1}".format(filename,
                                                                                                      "aes")).st_size
                        try:
                            # decrypt file stream

                            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)

                        except ValueError:
                            # remove output file on error
                            remove("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename))
                if os.path.exists(
                        "G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename)):
                    with open("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename),
                              'rb') as fh:
                        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(
                            ("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename)))
                        return response
                raise Http404

        message = message + "OTP Does't match.\n"
        context = {'message': message}
        return render(request, 'Collegeuser/request.html', context)

        message = message + "axis Does't match.\n"
        context = {'message': message}
        return render(request, 'Collegeuser/request.html', context)

    message = message + "Status Does't match.\n"
    context = {'message': message}
    return render(request, 'Collegeuser/request.html', context)

    message = message + "Loading Failure.\n"
    context = {'message': message}
    return render(request, 'Collegeuser/request.html', context)


from random import randint


from app1.models import RequestFile

def reqkey(request):


    global loginFlag, loginUser
    if request.method == 'POST':
        filename = request.POST['filename']

        print(filename)
        message = ""
        print("its in req key page")
        userid=loginUser
        otp="000"
        state=False
        RequestFile(userid=userid,filename=filename,otp=otp,status=state).save()
        print(RequestFile)
        return render(request, 'Collegeuser/done.html')



    else:
        downdata=Transcations111.objects.all()
        context={'downdata':downdata}
        return render(request, 'Collegeuser/keyreq.html',context)



