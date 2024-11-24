# middleware.py
class SessionDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # قبل از پردازش درخواست
        print("Session before request:", request.session.items())
        
        response = self.get_response(request)
        
        # بعد از پردازش درخواست
        print("Session after request:", request.session.items())
        
        return response
