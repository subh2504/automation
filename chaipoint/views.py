from django.shortcuts import render
from .Cp import Cp
from .models import ChaipointAccount
# Create your views here.
def index(request):
    return render(request, 'chaipoint/index.html', {})
    
    
def get_cpa(request):
    print("fdjhdfhgkkf")
    cp = Cp()
    x=cp.fn1()
    print("**********")
    print(x)
    
    account=ChaipointAccount()
    account.email=x["email"]
    account.password=x["password"]
    account.mobile=x["mobile"]
    account.save();
    return render(request, 'chaipoint/index.html', {'account':account})