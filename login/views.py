from django.shortcuts import render
em=''
pw=''


# Create your views here.
def loginaction(request):
    global em,pw
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",password="259811",database='Client')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value 
            if key=="password":
                pw=value         

        c="select * from users where email='{}'and password='{}'".format(em,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"Home.html")
        

        
    return render(request,'login_page.html')  
