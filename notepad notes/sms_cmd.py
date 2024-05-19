def run():

account_sid = '****'
auth_token = '*****'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS
message = client.messages.create(
    body='Hey',
    from_='+******',
    to='+*****'
)

# Print the message SID
print(f"SMS sent successfully! SID: {message.sid}")