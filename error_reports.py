from datetime import datetime

# pip install twilio
from twilio.rest import Client

# Your Twilio account SID and Token
SID = ""
TOKEN = ""

# List to hold results
failed_messages = list()

# Twilio client configuration
client = Client(SID, TOKEN)

# Getting all of your messages after the set date
messages = client.messages.list(
    date_sent_after=datetime(2020, 4, 1, 0, 0, 0)
)

# Create a dictionary from each message and add it to the results list
# You can customize the properties you want to include to fit your use case
for message in messages:
    if message.status == "undelivered" or message.status == "failed":
        failed_message = {
            "SID": message.sid,
            "Status": message.status,
            "Date": message.date_sent,
            "Error_code": message.error_code,
            "Error_message": message.error_message,
            "From": message.from_,
            "To": message.to,
            "Body": message.body
        }
        failed_messages.append(failed_message)

# Print the results list
for item in failed_messages:
    print("\n")
    for k, v in item.items():
        print(f"{k}: {v}")
