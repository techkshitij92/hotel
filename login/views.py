from django.shortcuts import render
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="Hello@321.",database="hotel")
cursor=mycon.cursor()

def home(request):
        return render (request,"home.html")

def login(request):
        return render (request,"login.html")

def sign_up(request):
        return render(request,"sign_up.html")

def forgot(request):
        return render(request,"forgot.html")

def signup(request):
    d=request.POST
    email=d['email']
    st1="SELECT email from signup WHERE email LIKE '{}'".format(email)
    cursor.execute(st1)
    data=cursor.fetchall()
    for email in data:
        return render (request,'email_error.html')
    else:
        if d['psw']==d['psw-repeat']:
            st="INSERT INTO signup(firstname,lastname,email,phone,password)VALUES('{}','{}','{}','{}','{}')".format(d['fname'],d['lname'],d['email'],d['phn'],d['psw'])
            cursor.execute(st)
            mycon.commit()
            return render(request,'signup.html')
        else:
            return render(request,'error.html')

def logged_in(request):
        d=request.POST
        s="SELECT email,password, phone FROM signup WHERE email LIKE '{}' && password LIKE '{}'".format(d['uname1'],d['psw1'])
        cursor.execute(s)
        data=cursor.fetchall()
        for (a,b,phn) in data:
                break
        count=cursor.rowcount
        if count==1:
                st="INSERT INTO login_info VALUES('{0}', NOW(),'{1}')".format(d['uname1'],phn)
                cursor.execute(st)
                mycon.commit()
                return render(request,"logged_in.html")
        else:
                return render(request,"log_error.html")
                
def book(request):
	return render(request,"book.html")

def booked(request):
        d=request.POST
        cid=1
        s="INSERT INTO reservation_info VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d['fname'],d['lname'],d['add'],d['city'],d['zp'],d['state'],d['email'],d['phn'],cid)
        s1="INSERT INTO date_info VALUES('{}','{}','{}')".format(d['cind'],d['coud'],cid)
        s2="INSERT INTO booking_info VALUES('{}','{}','{}','{}')".format(d['nofa'],d['nofc'],d['rooms'],cid)
        cursor.execute(s)
        mycon.commit()
        cursor.execute(s1)
        mycon.commit()
        cursor.execute(s2)
        mycon.commit()
        return render(request,'booked.html')