from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'ACf387894c0763a40c80be1910b72f3928'
auth_token = 'a6adfd4bba70e65ef838f06866b4db5c'

# Your Twilio phone number and the number you want to send the SMS to
from_number = '+12563686097'
to_number = '+91xxxxxxxxxx'

# Message you want to send
voltage = 11
current = 6
time = 2
wh = voltage*current*time
lt = 140
charge = 10
if(wh>=130 and wh<=lt):
    message_body = f" Watt-hour: {wh} Watt-hour \n Consumption reaching its limit. Extra Charge will be ₹15 per watt-hour above 140 Watt-hour. \n Current Bill: ₹{charge*wh}"

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body=message_body,
    from_=from_number,
    to=to_number
)

print(f"Message SID: {message.sid}")
