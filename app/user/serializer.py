# import requests
# from rest_framework import serializers
#
# from .models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password2', 'telegram_chat_id']
#
#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username'],
#             telegram_chat_id=validated_data['telegram_chat_id'],
#         )
#         bot_message = f'Добро пожаловать в наш форум, {user.username}!'
#         bot_token = '6275876428:AAG0l9_8h4c5m_h-SsH0hdvq-7-YVRnt-nU'
#         bot_chat_id = user.telegram_chat_id
#         send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'
#         response = requests.get(send_text)
#         response.json()
#
#         if validated_data['password'] == validated_data['password2']:
#             user.set_password(validated_data['password'])
#             user.save()
#             return user
#         return ValueError('Wrong password')
#




import requests
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'telegram_chat_id', 'password','password2']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            telegram_chat_id=validated_data['telegram_chat_id'],
        )
        bot_message = f"Добро пожаловать в наш форум,{user.username}"
        bot_token = '6275876428:AAG0l9_8h4c5m_h-SsH0hdvq-7-YVRnt-nU'
        bot_chat_id = user.telegram_chat_id
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'
        response = requests.get(send_text)
        response.json()
        if validated_data['password'] == validated_data['password2']:
            user.set_password(validated_data['password2'])
            user.set_password(validated_data['password2'])
            user.save()
            return user
        return ValueError("не павильный пароль")
