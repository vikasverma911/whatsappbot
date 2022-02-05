from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .models import Message, User
from rest_framework import viewsets



account_sid = 'AC3a8ca162584725db278129c0425d56b7'
auth_token = '8f93843b87c099e467dff6bd5108a766'
client = Client(account_sid, auth_token)
# Create your views here.

@csrf_exempt
def bot(request):
    message = request.POST["Body"]
    sender_name = request.POST["ProfileName"]
    sender_number = request.POST["From"]

    entry = User.objects.filter(WaId=request.POST["WaId"]).all()
    if entry: Message.objects.create(user=entry[0], SmsStatus=request.POST["SmsStatus"], Body=request.POST["Body"])
    else:
        user = User.objects.create(ProfileName=request.POST["ProfileName"], WaId=request.POST["WaId"])
        Message.objects.create(user=user, SmsStatus=request.POST["SmsStatus"], Body=request.POST["Body"])

    if message == "Hi":
        message = client.messages.create(
            body="hey {}, Bot here. Please type a number".format(sender_name),
            from_='whatsapp:+14155238886',
            to=sender_number
        )

    if message =="1":
        message = client.messages.create(
            body="hey {}, This is a message".format(sender_name),
            from_='whatsapp:+14155238886',
            to=sender_number
        )

    if message == "2":
        message = client.messages.create(
            body="hey {}, This is a image".format(sender_name),
            from_='whatsapp:+14155238886',
            media_url=['https://demo.twilio.com/owl.png'],
            to=sender_number
        )

    if message == "3":
        message = client.messages.create(
            body="hey {}, This is an document".format(sender_name),
            from_='whatsapp:+14155238886',
            media_url=['https://www.gti.bh/Library/assets/djangobookwzy482.pdf'],
            to=sender_number
        )

    if message == "4":
        message = client.messages.create(
            body="hey {}, This is a image".format(sender_name),
            from_='whatsapp:+14155238886',
            media_url=['https://demo.twilio.com/owl.png'],
            to=sender_number
        )

        message = client.messages.create(
            body="hey {}, This is a list".format(sender_name),
            from_='whatsapp:+14155238886',
            media_url=['https://www.gti.bh/Library/assets/djangobookwzy482.pdf'],
            to=sender_number
        )

    return HttpResponse("Hello")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
