from django.shortcuts import render

def home (request):
    return render(request,'home.html')
def calc(request):
    a=int(request.GET['Frist'])
    b=int(request.GET['Second'])
    c=request.GET['math']

    if c=='-':
        s=a-b
    elif c=='+':
        s=a+b
    elif c=='*':
        s=a*b
    else:
        s=a/b
    return render(request,'calc.html',{'sum':s})