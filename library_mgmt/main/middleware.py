from django.shortcuts import redirect
from django.urls import reverse

class CheckLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/':
            
            if not request.user.is_authenticated:
                return redirect(reverse('login'))  

            print("working")
            if request.user.is_superuser:
                return redirect(reverse('admin_home'))  
            else:
                return redirect(reverse('user_home'))  

        response = self.get_response(request)
        return response