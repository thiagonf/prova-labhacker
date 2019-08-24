from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.shortcuts import redirect, render


class HomeView(TemplateView):
    '''
    Login of User
    '''
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, self.template_name)
