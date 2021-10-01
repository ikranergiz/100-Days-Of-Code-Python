from twilio.rest import Client

TWILIO_SID = "AC6f27416fa93c67b62a8f3948834e83a6"
TWILIO_AUTH_TOKEN = "4323edcbda788b43e33d0377b3f8376c"
TWILIO_VIRTUAL_NUMBER = "+18638692878"
TWILIO_VERIFIED_NUMBER = "+905433320660"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)