from django.shortcuts import render

def get_page(request):
    return render(request, 'vue_app/finalpage.html')
