{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0d3d227c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border='1'><tr> <td>Date</td><td>Name</td><td>Pincode</td><td>Capacity</td><td>Vaccine</td>  </tr><tr><td>02-06-2021</td><td>DGHC Supreme Court</td><td>110001</td><td>0</td><td>COVISHIELD</td></tr><tr><td>02-06-2021</td><td>LHMC CVC 2</td><td>110001</td><td>0</td><td>COVAXIN</td></tr><tr><td>02-06-2021</td><td>RML Site 1</td><td>110001</td><td>0</td><td>COVAXIN</td></tr><tr><td>02-06-2021</td><td>G.B.Pant Hospital DH SITE 2</td><td>110001</td><td>100</td><td>COVISHIELD</td></tr><tr><td>02-06-2021</td><td>RML Site 2</td><td>110001</td><td>0</td><td>COVAXIN</td></tr><tr><td>02-06-2021</td><td>Rouse Avenue Court</td><td>110001</td><td>0</td><td>COVAXIN</td></tr><tr><td>02-06-2021</td><td>Atal Adarsh School Mandir Marg</td><td>110001</td><td>32</td><td>COVISHIELD</td></tr><tr><td>02-06-2021</td><td>LHMC CVC 1</td><td>110001</td><td>0</td><td>COVAXIN</td></tr><tr><td>02-06-2021</td><td>RML Site 3</td><td>110001</td><td>0</td><td>COVAXIN</td></tr></table>\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#function\n",
    "def get_slot_data(pincode,check_date):\n",
    "    import requests\n",
    "    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode='+pincode+'&date='+check_date\n",
    "    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',\n",
    "               'accept': 'text/html,application/xhtml+xml,application/xml'    }\n",
    "    r = requests.get(url, headers=headers)\n",
    "    sess = r.json()\n",
    "    return sess['sessions']\n",
    "def convert_into_table_data(data):  \n",
    "    if (len(data)==0):   \n",
    "        return ''\n",
    "    table=\"<table border='1'><tr> <td>Date</td><td>Name</td><td>Pincode</td><td>Capacity</td><td>Vaccine</td>  </tr>\"\n",
    "    for center in data:\n",
    "        table+=\"<tr>\"\n",
    "        table+=\"<td>\"+center['date']+\"</td>\"\n",
    "        table+=\"<td>\"+center['name']+\"</td>\"\n",
    "        table+=\"<td>\"+str(center['pincode'])+\"</td>\"\n",
    "\n",
    "        table+=\"<td>\"+str(center['available_capacity'])+\"</td>\"\n",
    "        table+=\"<td>\"+center['vaccine']+\"</td>\"\n",
    "        table+=\"</tr>\"\n",
    "    table+=\"</table>\"\n",
    "    return table\n",
    "# if available_capacity != NA:\n",
    "def send_notification(receiver_email,table_data,pincode):\n",
    "    import smtplib, ssl\n",
    "    from email.mime.text import MIMEText\n",
    "    from email.mime.multipart import MIMEMultipart\n",
    "\n",
    "    sender_email = \"igwolf.yt09@gmail.com\"\n",
    "#         receiver_email = \"itsvinay09@gmail.com\"\n",
    "    password = \"spxwolf@1999\"\n",
    "\n",
    "    message = MIMEMultipart(\"alternative\")\n",
    "    message[\"Subject\"] = \"Slot Avaliable at pincode :\"+pincode\n",
    "    message[\"From\"] = sender_email\n",
    "    message[\"To\"] = receiver_email\n",
    "\n",
    "    # Create the plain-text and HTML version of your message\n",
    "    text = \"\"\"Testing Text\"\"\"\n",
    "    html = table_data\n",
    "\n",
    "    # Turn these into plain/html MIMEText objects\n",
    "    part1 = MIMEText(text, \"plain\")\n",
    "    part2 = MIMEText(html, \"html\")\n",
    "\n",
    "    # Add HTML/plain-text parts to MIMEMultipart message\n",
    "    # The email client will try to render the last part first\n",
    "    message.attach(part1)\n",
    "    message.attach(part2)\n",
    "\n",
    "    # Create secure connection with server and send email\n",
    "    context = ssl.create_default_context()\n",
    "    with smtplib.SMTP_SSL(\"smtp.gmail.com\", 465, context=context) as server:\n",
    "        server.login(sender_email, password)\n",
    "        server.sendmail(\n",
    "            sender_email, receiver_email, message.as_string()\n",
    "        )\n",
    "\n",
    "from datetime import datetime\n",
    "from datetime import timedelta\n",
    "receiver_mail =\"itsvinay09@gmail.com\"\n",
    "pincode = '110001'\n",
    "check_date = (datetime.now() + timedelta(days=1)).strftime(\"%d-%m-%Y\")\n",
    "slot_data= convert_into_table_data(get_slot_data(pincode,check_date))\n",
    "print(slot_data)\n",
    "if(slot_data!=''):\n",
    "    send_notification(receiver_mail,slot_data,pincode)    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
