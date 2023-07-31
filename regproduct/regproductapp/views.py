from django.shortcuts import render,redirect

# Create your views here.

from . models import regview

from . models import regproduct
 
def index(request):
    return render(request,"index.html")


def view(request):
    data=regview.objects.all()
    return render(request,"regview.html",{'data':data}) 



def productview(request):
    data=regproduct.objects.all()
    return render(request,"productview.html",{'data':data})     


def product(request):
    return render(request,"product.html")

def saveregdata(request):
    if request.method=="POST":

        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
      
        print(name,username,email,contact,password)
        add=regview(name=name,username=username,email=email,contact=contact,password=password)
        add.save()
        return redirect('view')
    return render(request,"index.html",)



def saveproduct(request):
    if request.method=="POST":

        ppname=request.POST['ppname']
        pid=request.POST['pid']
        pcat=request.POST['pcat']
        pprice=request.POST['pprice']
        
      
        print(ppname,pid,pcat,pprice)
        add=regproduct(ppname=ppname,pid=pid,pcat=pcat,pprice=pprice)
        add.save()
        return redirect('productview')
    return render(request,"index.html",)


    # --------------edit fir -----------------
   
def editr(request,id):
    Data=regview.objects.get(id=id)
    return render(request,"regedit.html",{'Data':Data}) 

def editrdata(request,id):
    if request.method=='POST':
        add=regview.objects.get(id=id)
        add.name=request.POST["name"]
        add.username=request.POST["username"]
        add.email=request.POST["email"]
        add.contact=request.POST["contact"]
        add.password=request.POST["password"]
        
        add.save()
        return redirect("view")





# ----------------------delete------------
def deleter(request,id):
    add=regview.objects.get(id=id)     
    add.delete()
    return redirect('view')

def deletep(request,id):
    add=regproduct.objects.get(id=id)     
    add.delete()
    return redirect('productview')    



    # ---------------------edit p----------

def editp(request,id):
    Data=regproduct.objects.get(id=id)
    return render(request,"productedit.html",{'Data':Data}) 

def editpdata(request,id):
    if request.method=='POST':
        add=regproduct.objects.get(id=id)
        add.ppname=request.POST["ppname"]
        add.pid=request.POST["pid"]
        add.pcat=request.POST["pcat"]
        add.pprice=request.POST["pprice"]
        add.save()
        return redirect("productview")