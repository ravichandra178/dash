from django.shortcuts import render

def my_custom_error_view(request):
    return render(request,'500.html')
