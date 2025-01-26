from django.shortcuts import render

# Create your views here.
def testapp_list(request):
    return render(request,'testapp/testapp_list.html')