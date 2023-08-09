# middleware.py

from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class SessionIdleTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            current_time = timezone.now()
            session_key = request.session.session_key

            # Get the session associated with the current user
            try:
                session = Session.objects.get(session_key=session_key)
            except Session.DoesNotExist:
                pass
            else:
                last_activity = session.get_decoded().get('_session_last_activity')

                # If the session has expired, log out the user
                if last_activity and (current_time - last_activity).seconds > settings.SESSION_EXPIRE_SECONDS:
                    session.delete()
                    request.session.flush()
                    request.user = User()

                # Update the last activity timestamp
                session['_session_last_activity'] = str(current_time)
                session.save()

        response = self.get_response(request)

        return response
