from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Theme


mode_options = {
    'light',
    'dark',
    'system',
}


def set_theme(request):
    next_url = None
    if request.method == 'POST':
        mode = request.POST.get('theme', None)
        next_url = request.GET.get('next', None)

        if mode is None:
            return HttpResponseBadRequest()

        if mode not in mode_options:
            if next_url:
                return redirect(next_url)
            else:
                return HttpResponseBadRequest()

        if request.user.is_authenticated:
            user = request.user
            theme = Theme.objects.update_or_create(
                user=user,
                defaults={
                    'mode': mode,
                    'user': user,
                }
            )
            request.session['theme'] = mode

        if next_url:
            return redirect(next_url)

        return HttpResponse(status=200)
