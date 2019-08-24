from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect


class LogoutView(View):
    '''
    Logout of User.
    '''

    def get(self, request):
        logout(request)
        return redirect('/')
