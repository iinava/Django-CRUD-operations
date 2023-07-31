from django.shortcuts import render,redirect

# Create your views here.

from . models import studentview

def index(request):
    return render(request,"index.html")

def view(request):
    data=studentview.objects.all()
    return render(request,"view.html",{'data':data}) 

def edit(request,id):
    Data=studentview.objects.get(id=id)
    return render(request,"edit.html",{'Data':Data})    


def savedata(request):
    if request.method=="POST":

        name=request.POST['name']
        parent=request.POST['parent']
        contact=request.POST['contact']
        pincode=request.POST['pincode']
        email=request.POST['email']
        adress=request.POST['adress']
        print(name,parent,contact,pincode,email,adress)
        add=studentview(name=name,parent=parent,contact=contact,pincode=pincode,email=email,adress=adress)
        add.save()
        return redirect('view')
    return render(request,"index.html",)






def editdata(request,id):
    if request.method=='POST':
        add=studentview.objects.get(id=id)
        add.name=request.POST["name"]
        add.parent=request.POST["parent"]
        add.contact=request.POST["contact"]
        add.pincode=request.POST["pincode"]
        add.email=request.POST["email"]
        add.adress=request.POST["adress"]
        add.save()
        return redirect("view")



def delete(request,id):
    add=studentview.objects.get(id=id)     
    add.delete()
    return redirect('view')