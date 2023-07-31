from django.shortcuts import render,redirect

# Create your views here.

from . models import contactview

def index(request):
    return render(request,"home.html")
def view(request):
    data=contactview.objects.all()
    return render(request,"view.html",{'data':data})


def edit(request,id):
    Data=contactview.objects.get(id=id)
    return render(request,"edit.html",{'Data':Data})   


def savedata(request):
    if request.method=="POST":

        fname=request.POST['f_name']
        lname=request.POST['l_name']
        phone=request.POST['phone']
        print(fname,lname,phone)
        add=contactview(fname=fname,lname=lname,phone=phone)
        add.save()
        return redirect('view')
    return render(request,"home.html",)




def editdata(request,id):
    if request.method=='POST':
        add=contactview.objects.get(id=id)
        add.fname=request.POST["f_name"]
        add.lname=request.POST["l_name"]
        add.phone=request.POST["phone"]
        add.save()
        return redirect("view")



def delete(request,id):
    add=contactview.objects.get(id=id)     
    add.delete()
    return redirect('view')