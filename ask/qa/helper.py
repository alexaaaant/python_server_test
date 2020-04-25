from . import models
from datetime import datetime, timedelta
import random
import string

def do_login(username, password):
    try:
        user = models.User.objects.get(username=username)
    except models.User.DoesNotExist:
        return None
    if password != user.password:
        return None
    session = models.Session()
    session.key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    session.user = user
    session.expires = datetime.now() + timedelta(5)
    session.save()
    return session.key