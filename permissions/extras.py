def clear_session(request):
    if 'old_search_b' in request.session:
        del request.session['old_search_b']
    if 'old_search_c' in request.session:
        del request.session['old_search_c']