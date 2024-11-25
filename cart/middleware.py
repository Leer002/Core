
class SessionDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        print("Session before request:", request.session.items())
        
        response = self.get_response(request)
        
        
        print("Session after request:", request.session.items())
        
        return response
