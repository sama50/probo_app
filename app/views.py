from django.shortcuts import render ,redirect
from app.models import Myuser , Context , User_context
# Create your views here.


def index(request):
    if request.method=='POST':
        mobile_number = request.POST.get('mobile_number')
        request.session['number'] = mobile_number 
        return redirect('otp')
    return render(request,'index.html')

def otp(request):
    return render(request,'otp_page.html')
def home(request):
    number = request.session.get('number',None)
    user_details = Myuser.objects.get(number=number)
    all_context = Context.objects.filter(done='start')
    return render(request,'home.html',{'all_context':all_context,'user_details':user_details})


def money_panel(request):
    return render(request,'money_panel.html')


def win(request,choine,id):
    print(request.session.get('number',None))
    print(choine)
    print(id)
    contex_get = Context.objects.get(id=id)
    user = Myuser.objects.get(number=request.session.get('number'))
    User_context(user=user,context=contex_get,option=choine).save()
    return redirect('/')

def panel(request):
    number = request.session.get('number',None)
    user_details = Myuser.objects.get(number=number)
    user_context = User_context.objects.filter(user=user_details)
    return render(request,'panel.html',{'user_details':user_details,'user_context':user_context})