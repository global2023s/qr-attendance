from functools import wraps
from django.http import JsonResponse

def login_required_or_pin_check(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        elif request.method == "POST" and request.POST.get("pin") == "1234":
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

    return _wrapped_view
