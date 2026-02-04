from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from .models import UserSubscription

class SubscriptionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if request.path.startswith('/api/orders/'):
                subscription = UserSubscription.objects.filter(user=request.user).first()
                if subscription is None or not subscription.status:
                    return HttpResponse('У вас нет активной подписки.', status=403)
        return None
