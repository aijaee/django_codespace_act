
def theme(request):
    theme = ''
    try:
        theme = request.session['theme']
    except KeyError:
        if request.user.is_anonymous:
            return {'theme': ''}
        try:
            theme = request.user.theme.mode
        except:
            return {'theme': ''}
    return {'theme': theme}
