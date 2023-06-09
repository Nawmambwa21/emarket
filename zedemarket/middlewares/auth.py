from django.shortcuts import redirect

def auth_middleware(get_response):
    

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.meta['PATH_INFO']
        print(request.meta['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware