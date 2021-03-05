import nexmo
import os
import json

from flask import Flask, request, flash

app = Flask(__name__)

NEXMO_API_KEY = '<INSERT NEXMO API KEY>' 
NEXMO_API_SECRET = '<INSERT NEXMO SECRET>'

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

def sendSMS(TO_NUMBER):
    responseData = client.send_message(
        {
            "from": "Get Chip",
            "to": TO_NUMBER,
            "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

@app.route('/', methods=['GET', 'POST'])
def landingPageSMS():
    print(request.method)
    if request.method == 'POST':
        print('request')
        print(request)
        TO_NUMBER = request.form['mobileInput']
        print('number ' + TO_NUMBER)
        sendSMS(TO_NUMBER)
        return None
        

if __name__ == "__main__":
    app.run(debug=True ,port=int(os.environ.get('PORT', 8080)))
