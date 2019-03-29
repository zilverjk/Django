"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse



class ProfileCompletionMiddleware:
    """Profile completion middleware
    
    Ensure every user thta is interacting wiht the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response


    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        
        # Nos aseguramos que el usuario este logeado
        if not request.user.is_anonymous:

            if not request.user.is_staff:
                profile = request.user.profile
                
                if not profile.picture or not profile.biography:

                    # Si estamos en otra pagina que no sea la del profile que nos redireccione a profile
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)
        return response