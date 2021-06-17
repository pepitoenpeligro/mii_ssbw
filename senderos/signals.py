import logging
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info("{} ha iniciado sesion {}".format(user.email, request))
    print("{} ha iniciado sesion {}".format(user.email, request))
    print('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
 
 
@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logger.info(user.email + ' ha intentado iniciar sesion de forma erronea')
    print('user {} logged in failed through page {}'.format(credentials.get('username'), request.META.get('HTTP_REFERER')))
 
 
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(user.email + ' ha finalizado la sesión')
    print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))