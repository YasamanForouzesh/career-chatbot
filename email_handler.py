import os
from mailjet_rest import Client

data = {'Messages': [{
            "From": {"Email": ""},
            "To": [{"Email": ""}],
            "Subject": "",
            "TextPart": "",
            "HTMLPart": ""
        }]}
class EmailHandler:
    def __init__(self):
        self.sender_email = os.getenv("FROM_EMAIL")  
        api_key = os.getenv('MJ_APIKEY_PUBLIC')
        api_secret = os.getenv('MJ_APIKEY_PRIVATE')
        self.mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    def send_email(self, sessiondata, reply=None):

        data["Messages"][0]["From"]["Email"] = self.sender_email
        data["Messages"][0]["To"][0]["Email"] = sessiondata["email"] if reply else os.getenv("TO_EMAIL")
        if not reply:
            data["Messages"][0]["Subject"] = "Follow up"
            body = (
                f"{sessiondata.get('name','(no name)')} reached out and had these questions: "
                f"user had these questions {sessiondata.get('questions','(no questions)')} \n\nChat history:\n{" ".join([msg["content"] for msg in sessiondata["history"]])}\n\n"
                f"Contact: {sessiondata['email']}"
            )
            data["Messages"][0]["TextPart"] = body
        else:
            data["Messages"][0]["TextPart"] = reply.text_body
            data["Messages"][0]["HTMLPart"] = reply.html_body
            data["Messages"][0]["Subject"] = reply.subject

        result = self.mailjet.send.create(data=data)
        print (result.status_code)
        print (result.json())




