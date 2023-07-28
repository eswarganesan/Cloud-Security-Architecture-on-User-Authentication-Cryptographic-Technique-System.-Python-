from django.shortcuts import render,redirect
from .forms import it_sales_form
from .models import Employee,Company,Products,Transactions,TCP,Temp
from django.core.files.storage import FileSystemStorage
import random
from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
from .models import  Transactions
from .models import Transcations111
from sklearn import tree

pass_phrase = "7GoodLuck7"

loginUser = ""
loginFlag = False
forgotEmpID = ""

ques1List = ["--","What was your childhood nickname?","In what city did you meet your spouse/significant other?","What is the name of your favorite childhood friend?",
"What is your oldest sibling’s birthday month and year?","What is the middle name of your oldest child?"]

ques2List = ["--","What school did you attend for sixth grade?","What was the name of your first stuffed animal?","In what city does your nearest sibling live?",
"In what city or town was your first job?","Which is the first company you ever worked for?"]

def index(request):
    name = "INDEX:"
    var = random.randint(1,1000)
    context = {'var':var,'name':name}
    return render(request,'app1/index.html',context)

def createFeatureVector(x):
    featureDict = {
            "/":0,
            "int":0,
            "new":0,
            "[":0,
            "File":0,
            "FileInputStream":0,
            "BufferedReder":0,
            "mysql":0,
            "charAt":0,
            "parseInt":0,
            "null":0,
            "FileReader":0,
            "main":0
        }
    for word in featureDict:
        if word in x:
            featureDict[word] = 1
    featureVector = []
    for val in featureDict:
        featureVector.append(featureDict[val])
    return featureVector, pd.Series(featureDict)





def check(request):
    name = "CHECK:"
    var = random.randint(1,1000)
    context = {'var':var,'name':name}
    return render(request,'app1/check.html',context)




def uploadfile(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage(location='Original/')
        filename = fs.save(uploaded_file.name, uploaded_file)
        print(filename)
        #Alw6YoYAHTtO3nqvaNeExz
        from filestack import Client
        client = Client("Alw6YoYAHTtO3nqvaNeExz")
        params = {'mimetype': 'text/py'}
        new_filelink = client.upload(
            filepath="G:/ESWAR/INTERN/Edge Computing/Original/{0}".format(filename))
        print(new_filelink.url)
        link=new_filelink.url
        request.session['location_we_got'] = link
        filelink = client.upload(filepath="G:/ESWAR/INTERN/Edge Computing/Original/{0}".format(filename), store_params=params)
        link=filelink.url
        request.session['location_we_got'] = link
        from .models import FileCDN
        FileCDN(userid=loginUser,filename=filename,cdn=link).save()


        data=uploaded_file.read()
        for i in data.decode("utf-8") :
            print(i)

        cov = str(data)
        print(type(cov))
        print(cov)
        import pyAesCrypt
        from os import stat, remove
        # encryption/decryption buffer size
        bufferSize = 64 * 1024
        password = "pwd"  # encryption of file data.txt
        with open("G:/ESWAR/INTERN/Edge Computing/Original/{0}".format(filename), "rb") as fIn:
            with open("G:/ESWAR/INTERN/Edge Computing/Original/Encryption/{0}.{1}".format(filename,"aes"), "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        # get encrypted file size
        encFileSize = stat("G:/ESWAR/INTERN/Edge Computing/Original/Encryption/{0}.{1}".format(filename,"aes")).st_size
        print(encFileSize)
        # prints file size# decryption of file data.aes
        from time import timezone
        print("username",loginFlag,loginUser,filename)

        Transcations111(userid=loginUser,filename=filename,otp="dbd",access1="1").save()
        request.session['filename'] = filename

        return render(request,'app1/output.html')
    return render(request, 'app1/upload.html')


import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request):
    path="G:/ESWAR/INTERN/Edge Computing/Original/"
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists("G:/ESWAR/INTERN/Edge Computing/Original/dd.txt"):
        with open("G:/ESWAR/INTERN/Edge Computing/Original/dd.txt", 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename("G:/ESWAR/INTERN/Edge Computing/Original/dd.txt")
            return response
    raise Http404



def access1(request):
    if request.method == 'POST':
        access1 = request.POST['code']
        filename = request.session['filename']
        print("adafe",filename)
        Transcations111.objects.filter(userid=loginUser,filename=filename).update( access1=access1)
        loc = request.session['location_we_got']

        return render(request,'app1/FileSuccess.html',{'loc':loc})
    return render(request, 'app1/output.html')



def register(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        
        emp_id = request.POST['emp_id']
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        dept = request.POST['dept']
        ques_1_id = request.POST['ques_1_id']
        ans_1 = request.POST['ans_1']
        ques_2_id = request.POST['ques_2_id']
        ans_2 = request.POST['ans_2']
        gender = request.POST['gender']
        phone = request.POST['phone']
        repeat_password = request.POST['repeat_password']
        print(emp_id,name,password,email,dept,ques_1_id,ans_1,ques_2_id,ans_2,gender,phone,repeat_password)
        count = 0
        message = ""
        searchObject = Employee.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0],emp_id)
            if lst[0] == emp_id:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1    
        
        if password == repeat_password:
            if len(password)>6:
                flag1,flag2,flag3 = 0,0,0
                for i in range(len(password)):
                    ele = ord(password[i])
                    if ele>96 and ele<123:
                        flag1 = 1
                    elif ele>47 and ele<58:
                        flag2 = 1
                    elif ele>64 and ele<91:
                        flag3 = 1
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    count = count + 1
                else:
                    message = message +"Re-enter the Password.\n"
        else:
            message = message + "Passwords does not match.\n"
        
        print(count)
        if count == 2:
            raw_text = password
            encrypt_text = raw_text
            Employee(emp_id = emp_id,
            name = name,
            password = encrypt_text,
            email = email,
            dept = dept,
            ques_1_id = ques_1_id,
            ans_1 = ans_1,
            ques_2_id = ques_2_id,
            ans_2 = ans_2,
            gender = gender,
            phone = phone).save()
            
            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}  
        return render(request,'app1/register.html',context)

    else:
        message = "Welcome To Registration Page"
        context = {"message":message}
        return render(request,'app1/register.html',context)



def login(request):
    global loginFlag,loginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username,password)
        message = ""

        if len(Employee.objects.filter(emp_id=username)) == 0:
            message = message + "No Matching Accounts Found"
        else:
            pass_hash = str(Employee.objects.filter(emp_id=username)[0]).split(";")[4] 
            decrypt_text = pass_hash
            if password == decrypt_text:
                message = message + "Welcome to the Home Page"
                loginFlag = True
                loginUser = username
                print(loginUser)
                return redirect('home')
            else:
                message = message + "Wrong Password Entered"

        print(message)
        context = {"message":message}
        return render(request,'app1/login.html',context)

    else:
        return render(request,'app1/login.html')
    
def home(request):
    global loginFlag,loginUser,loginName
    if loginFlag == False:
        return redirect('login')

    loginObj = str(Employee.objects.filter(emp_id=loginUser)[0]).split(";")
    name = loginObj[1]
    loginName = name
    print("Name:",name)

    context = {"name":name}
    return render(request,'app1/home.html',context)

def logout(request):
    global loginFlag,loginUser
    loginFlag = False
    loginUser = ""
    print("After Logout:",loginFlag,loginUser)
    return redirect('login')

def accountUpdate(request):
    global loginUser,loginName
    message = ""
    print("Login Flag:",loginFlag)
    if loginFlag == False:
        return redirect('login')

    loginObj = str(Employee.objects.filter(emp_id=loginUser)[0]).split(";")

    if request.method == 'POST':
        dept = request.POST['dept']
        contact = request.POST['contact']
        ans1ID = request.POST['ans1ID']
        ans1 = request.POST['ans1']
        ans2ID = request.POST['ans2ID']
        ans2 = request.POST['ans2']
        email = request.POST['email']
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        confnewpass = request.POST['confnewpass']

        if oldpass == "" or newpass == "" or confnewpass == "":
            Employee(emp_id=loginUser,name=loginObj[1],password=loginObj[4],dept=dept,phone=contact,
            ques_1_id=ans1ID,ans_1=ans1,ques_2_id=ans2ID,ans_2=ans2,email=email,gender=loginObj[2]).save()
            message = message + "Account Updated Successfully.\n"
        else:
            oldpassDB = loginObj[4]
            if oldpass == oldpassDB:
                if newpass == confnewpass:
                    if len(newpass)>6:
                        flag1,flag2,flag3 = 0,0,0
                        for i in range(len(newpass)):
                            ele = ord(newpass[i])
                            if ele>96 and ele<123:
                                flag1 = 1
                            elif ele>47 and ele<58:
                                flag2 = 1
                            elif ele>64 and ele<91:
                                flag3 = 1
                        if flag1 == 1 and flag2 == 1 and flag3 == 1:
                            encrpytPass = newpass
                            Employee(emp_id=loginUser,name=loginObj[1],password=encrpytPass,dept=dept,phone=contact,
                            ques_1_id=ans1ID,ans_1=ans1,ques_2_id=ans2ID,ans_2=ans2,email=email,gender=loginObj[2]).save()
                            message = message + "Account Updated Successfully.\n"
                        else:
                            message = message +"Re-enter The Password. Does'nt Follow Password Constraints.\n"
                    else:
                        message = message + "Password Length is less than 7 Characters."
                else:
                    message = message + "New Passwords Does Not Match."
            else:
                message = message + "Old Password Does Not Match."

        loginObj = str(Employee.objects.filter(emp_id=loginUser)[0]).split(";")

        context = {"empID":loginObj[0],"name":loginObj[1],"dept":loginObj[5],"contact":loginObj[6],"gender":loginObj[2],"ans1":loginObj[8],
        "ans1ID":ques1List[int(loginObj[7])],"ans2":loginObj[10],"ans2ID":ques2List[int(loginObj[9])],"email":loginObj[3],"message":message}    
        return render(request,'app1/account-update.html',context)
    else:
        # GET METHOD
        context = {"empID":loginObj[0],"name":loginObj[1],"dept":loginObj[5],"contact":loginObj[6],"gender":loginObj[2],"ans1":loginObj[8],
        "ans1ID":ques1List[int(loginObj[7])],"ans2":loginObj[10],"ans2ID":ques2List[int(loginObj[9])],"email":loginObj[3]}    
        return render(request,'app1/account-update.html',context)

def forgotpass(request):
    global forgotEmpID
    if request.method == "POST":
        forgotEmpID = request.POST['eid']
        if len(Employee.objects.filter(emp_id=forgotEmpID)) == 0:
            message = "No Matching Employee ID Found."
            context = {"message":message}
            return render(request,"app1/forgotpass.html",context)
        
        return redirect("forgotpass2")
    else:
        return render(request,"app1/forgotpass.html")

def forgotpass2(request):
    global forgotEmpID
    message = ""
    if forgotEmpID == "":
        return redirect('forgotpass')

    forgotLst = str(Employee.objects.filter(emp_id=forgotEmpID)[0]).split(";")
    if request.method == "POST":
        email = request.POST['email']
        quesID = request.POST['quesID']
        ans = request.POST['ans']
        psw = request.POST['psw']
        pswRep = request.POST['pswRep']

        if email == forgotLst[3]:
            if (quesID == "1" and ans == forgotLst[8]) or (quesID == "2" and ans == forgotLst[10]):
                if psw == pswRep:
                    if len(psw)>6:
                        flag1,flag2,flag3 = 0,0,0
                        for i in range(len(psw)):
                            ele = ord(psw[i])
                            if ele>96 and ele<123:
                                flag1 = 1
                            elif ele>47 and ele<58:
                                flag2 = 1
                            elif ele>64 and ele<91:
                                flag3 = 1
                        if flag1 == 1 and flag2 == 1 and flag3 == 1:
                            encrpytPass = psw
                            Employee(emp_id=forgotEmpID,name=forgotLst[1],password=encrpytPass,dept=forgotLst[5],phone=forgotLst[6],
                            ques_1_id=forgotLst[7],ans_1=forgotLst[8],ques_2_id=forgotLst[9],ans_2=forgotLst[10],email=forgotLst[3],gender=forgotLst[2]).save()
                            message =  "Password Updated Successfully."
                        else:
                            message = "Re-enter The Password. Does'nt Follow Password Constraints."
                    else:
                        message = "Password Length is less than 7 Characters."
                else:
                    message = "New Passwords Does Not Match."
            else:
                message = "Question and Answer Does Not Match."
        else:
            message = "Email ID Does Not Match."

        context = {"message":message,"ques1":ques1List[int(forgotLst[7])],"ques2":ques2List[int(forgotLst[9])],"empID":forgotEmpID,"name":forgotLst[1]}
        return render(request,"app1/forgotpass2.html",context)
    else:
        context = {"ques1":ques1List[int(forgotLst[7])],"ques2":ques2List[int(forgotLst[9])],"empID":forgotEmpID,"name":forgotLst[1]}
        return render(request,"app1/forgotpass2.html",context)


def test(request):
    if request.method == 'POST':
        form = it_sales_form(request.POST)
        #context = {'form':form}
        print(form.is_valid())
        if form.is_valid():

            Temp(temp_id = request.POST.get('temp_id',False),
                name = request.POST.get('name',False)).save()

            #data = request.POST['var']
            #print("DATA",data)
            print("FORM:",form)
            #context = {'form':form}
            return render(request,'app1/test.html')
    
    else:
       
        form = it_sales_form()
    
        return render(request,'app1/test.html')
# Create your views here.
# REDIRECT = redirects to the URL.
# RENDER = renders to the file where there is an HTML page inside a directory.

from .forms import  UploadFileForm
def EH(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        if form.is_valid():

            data6 = request.POST['details']
            data2 = data6.splitlines()
            # for h in data2:
            #   print(h)
            #################################################################################################################################################
            results = []
            cnt = 1
            data3 = [[]]
            for line1 in data2:
                results = []
                results.append(line1.strip().translate({ord(c): " " for c in "!@#$%^&*()[]{};:,.<>?\|`~-=_+"}).split())
                # print(results)

                # print("Line No","\t","Exception")

                results = sum(results, [])
                print(results)
                for line in results:
                    l = []
                    for word in line:
                        l.append(word.split('='))
                    x = []
                    for i in l:
                        for j in i:
                            x.append(j)
                    x = set(x)
                    print(x)

                    featureVector, featureDict = createFeatureVector(x)
                    print(featureDict)
                    data = pd.read_csv("app1/data.csv")
                    x = data.iloc[:, 0:-1].values
                    y = data.iloc[:, -1].values
                    clf = tree.DecisionTreeClassifier()
                    clf = clf.fit(x, y)
                    pqx = str(clf.predict([featureDict])[0])
                    if pqx != "None":
                        data3.append([cnt, pqx])
                        # print(cnt,"\t",str(clf.predict([featureDict])[0]))
                    cnt = cnt + 1

            ##########################################################################################################################################################################################
            # data3.pop(0)
            return render(request, 'app1/eh.html', {'data2': data3, 'form': form})
    else:
        form1 = UploadFileForm(request.POST)
        return render(request, 'app1/eh.html', {'form': form1})


from .models import RequestFile
from .models import College


def ViewReq(request):
    global loginFlag, loginUser

    if request.method == 'POST':
        filename = request.POST['filename']
        print(filename)
        college = request.POST['college']
        message = ""
        print("its in provide permisiion section")
        print(college)
        userid = loginUser
        data = College.objects.get(emp_id=college)
        print(data.email)
        email = data.email
        digits = "0123456789"
        otp = ""
        import math, random
        # length of password can be chaged
        # by changing value in range
        for i in range(4):
            otp += digits[math.floor(random.random() * 10)]

        print(otp)
        state = 'True'
        req_approve = RequestFile.objects.filter(filename=filename)[0]
        print('req_approve.state', req_approve.status)
        print("req_approve.otp", req_approve.otp)
        req_approve.status = state
        req_approve.otp = otp
        print(req_approve)
        req_approve.save()
        print(req_approve.otp)
        print(req_approve.status)
        from redmail import outlook

        outlook.user_name = "sunilhari496@gmail.com"
        outlook.password = "sunilhari9986336399"

        outlook.send(
            receivers=email,
            subject="Secret Key Code",
            #text="Hi, this is an example."
        
        
        text = """\
                Hi,
         
                                    
                     File Name :{0}   
                OTP : {1}  


                   
                """.format(filename, otp))

       
        return render(request, 'app1/approved.html')

    reqkey = RequestFile.objects.filter(status=0)
    print(reqkey)
    context = {'reqkey': reqkey}
    return render(request, 'app1/give_acsess.html', context)


def cdn(request):
    print("Its comming")
    from .models import FileCDN
    dis=FileCDN.objects.filter(userid=loginUser)
    print(dis.filename)
    context={'dis':dis}
    return render(request, 'app1/cdn.html', context)
