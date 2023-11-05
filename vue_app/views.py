from django.shortcuts import render

def main_page_vue(request):
    return render(request, 'vue_app/main_page.html')
