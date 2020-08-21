from time import sleep

from celery.task import task
from django.contrib.auth import get_user_model
from kavenegar import KavenegarAPI, HTTPException, APIException

from blog.local_settings import KAVENEGAR_API

User = get_user_model()


@task(name='send welcoming message')
def send_welcoming_message(username):
    try:
        user = User.objects.get(username=username)
        try:
            api = KavenegarAPI(KAVENEGAR_API)
            params = {'sender': '1000596446', 'receptor': user.phone_number,
                      'message': 'خوش امدید\nپروفایل شما با موفقیت ساخته شد'}
            response = api.sms_send(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
    except User.DoesNotExist:
        return None
