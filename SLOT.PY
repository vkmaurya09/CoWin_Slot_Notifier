
#function
def get_slot_data(pincode,check_date):
    import requests
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode='+pincode+'&date='+check_date
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
               'accept': 'text/html,application/xhtml+xml,application/xml'    }
    r = requests.get(url, headers=headers)
    sess = r.json()
    return sess['sessions']
def convert_into_table_data(data):  
    if (len(data)==0):   
        return ''
    table="<table border='1'><tr> <td>Date</td><td>Name</td><td>Pincode</td><td>Capacity</td><td>Vaccine</td>  </tr>"
    for center in data:
        table+="<tr>"
        table+="<td>"+center['date']+"</td>"
        table+="<td>"+center['name']+"</td>"
        table+="<td>"+str(center['pincode'])+"</td>"

        table+="<td>"+str(center['available_capacity'])+"</td>"
        table+="<td>"+center['vaccine']+"</td>"
        table+="</tr>"
    table+="</table>"
    return table
# if available_capacity != NA:
def send_notification(receiver_email,table_data,pincode):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "XYZ@GMAIL.COM"
#        
    password = "XYZ"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Slot Avaliable at pincode :"+pincode
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """Testing Text"""
    html = table_data

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

from datetime import datetime
from datetime import timedelta
receiver_mail ="XYZ@gmail.com"
pincode = '110001'
check_date = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")
slot_data= convert_into_table_data(get_slot_data(pincode,check_date))
print(slot_data)
if(slot_data!=''):
    send_notification(receiver_mail,slot_data,pincode)    
