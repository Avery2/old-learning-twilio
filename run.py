# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
step = 0

app = Flask(__name__)

username = 'error'

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    global step
    global username
    print(str(step))
    print(username)
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    if step==0:
        print("Step0")
        resp.message('Welcome to Hospital. What is your name?')
        step+=1
        return str(resp) #don't worry about it

    if step==1:
        print('Step1')
        username = message_body
        resp.message('Thank you for your confirmation ' + username  + '! Type \'wait\' to get your wait time.')
        step+=1
        return str(resp) #don't worry about it

    if ((step==2)&(message_body=='wait')):
        print('Step2')
        resp.message('Your wait time is forever. This is a fake hospital.')
        step=0
        return str(resp) #don't worry about it
    print("end")
    return str(resp) #don't worry about it

if __name__ == "__main__":
    app.run(debug=True)