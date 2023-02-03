from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse('This is HomePage')
    return render(request,'index.html')
def grocery(request):
    return render(request,'grocery.html')
    #return HttpResponse('This is Grocery Page')
def mobiles(request):
    return render(request,'mobiles.html')
    #return HttpResponse('This is Mobile Page')
def fashion(request):
    return render(request,'fashion.html')
    #return HttpResponse('This is Fashion Page')
def electronics(request):
    return render(request,'electronics.html')
    #return HttpResponse('This is Electronics Page')
def appliances(request):
    return render(request,'appliances.html')
    #return HttpResponse('This is Appliances Page')
def travel(request):
    return render(request,'travel.html')
    #return HttpResponse('This is Travel Page')
def topoffer(request):
    return render(request,'topoffer.html')
    #return HttpResponse('This is TopOffer Page')
def beauty(request):
    return render(request,'beauty.html')
    #return HttpResponse('This is Beauty Page')