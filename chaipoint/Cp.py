#draedyn.trayveon@iku.us

import json
import random
import string
import datetime
import requests
import re
import time
from multiprocessing import Process
from .TempMail import TempMail


class Cp:

    FNAME = ['Abhay', 'Adesh', 'Adhik', 'Aditya', 'Agni', 'Ajay', 'Ajeet', 'Ajit', 'Ajith', 'Akash', 'Akhil', 'Amar',
             'Amit', 'Amrit', 'Anand', 'Ananden', 'Anandha', 'Anant', 'Ananta-Sesa', 'Ananth', 'Anil', 'Aniruddha', 'Anish',
             'Ankur', 'Anuj', 'Anupam', 'Aravind', 'Aravinda', 'Arjun', 'Arjuna', 'Arun', 'Aruna', 'Aseem', 'Ashok',
             'Ashoka', 'Avinash', 'Baladeva', 'Baldev', 'Bharat', 'Bharata', 'Bhaskar', 'Bhaskara', 'Bishen', 'Brahma',
             'Brijesh', 'Brijesha', 'Buddha', 'Carpanin', 'Chandan', 'Chander', 'Chandrakant', 'Chandraradj', 'Chanemouga',
             'Chanemougam', 'Chetan', 'Chiranjeevi', 'Chiranjivi', 'Cooldeepac', 'Damodar', 'Damodara', 'Darshan',
             'Dayanand', 'Dayaram', 'Deepak', 'Deo', 'Deodan', 'Dev', 'Deva', 'Devadas', 'Devaraja', 'Devayanne', 'Devdan',
             'Devdas', 'Devmani', 'Devraj', 'Dhananjay', 'Dharma', 'Dharmaradj', 'Dhaval', 'Dhruva', 'Dilip', 'Dilipa',
             'Dinesh', 'Dipak', 'Dipaka', 'Divyesh', 'Djagarajen', 'Djayssen', 'Djeyam', 'Drupada', 'Duleep', 'Ganapati',
             'Ganesh', 'Ganesha', 'Gautam', 'Gautama', 'Geevarghese', 'Girish', 'Girisha', 'Gobind', 'Gopal', 'Gopala',
             'Gopalkrishna', 'Gopinath', 'Gopinatha', 'Gotam', 'Gotama', 'Govind', 'Govinda', 'Govinden', 'Harendra',
             'Hari', 'Harinder', 'Harish', 'Harisha', 'Harishankar', 'Harsha', 'Harshad', 'Harshal', 'Hemacha dra',
             'Ilango', 'Inderpal', 'Indra', 'Indrajit', 'Isha', 'Ishvara', 'Ishwari', 'Itesh', 'Jagannath', 'Jagannatha',
             'Jagdish', 'Jagjit', 'Jai', 'Jaidev', 'Jayant', 'Jayanta', 'Jayendra', 'Jaywant', 'Jeetendra', 'Jitender',
             'Jitendra', 'Jitinder', 'Jiva', 'Jivan', 'Kadivel', 'Kadrivel', 'Kailash', 'Kalidas', 'Kalidasa', 'Kalyan',
             'Kalyana', 'Kama', 'Kamaradj', 'Kanda-Koumarane', 'Kapil', 'Kapila', 'Karan', 'Karna', 'Kartikeya', 'Kavi',
             'Kesavane', 'Kesaven', 'Keshavan', 'Kessavamohane', 'Kessavaperoumal', 'Keya', 'Kichenin', 'Kishan', 'Kishen',
             'Kishor', 'Kishore', 'Kistna', 'Komari', 'Krishna', 'Krishnaraja', 'Krishnin', 'Kshitij', 'Kumar', 'Kumara',
             'Kumaren', 'Kunal', 'Kunala', 'Lakshman', 'Lakshmana', 'Lal', 'Lalit', 'Laxman', 'Lekha', 'Lochan', 'Madhav',
             'Madhava', 'Madhukar', 'Mahavir', 'Mahavira', 'Mahendra', 'Mahesh', 'Mahesha', 'Mahinder', 'Mani', 'Manickam',
             'Maninder', 'Manish', 'Manu',  'Mayur', 'Mitul', 'Mogaya', 'Mohan', 'Mohandas', 'Mohinder',
             'Moryl', 'Mounoussamy', 'Mukesh', 'Mukesha', 'Mukul', 'Murali', 'Murugan', 'Nagendra', 'Nala', 'Nanda',
             'Narayan', 'Narayana', 'Narayanin', 'Narendra', 'Narinder', 'Nataraj', 'Naveen', 'Navin', 'Nikhil', 'Nil',
             'Ninad', 'Niraj', 'Nirav', 'Nirmal', 'Nishant', 'Nitin', 'Om', 'Outama', 'Pajani', 'Pajanivel', 'Pallab',
             'Pallav', 'Pankaj', 'Pankaja', 'Parth', 'Partha', 'Permal', 'Perumal', 'Poungodai', 'Pouranin', 'Pradip',
             'Pregassame', 'Pritam', 'Radjen', 'Radjiv', 'Radjou', 'Raghu', 'Rahul', 'Raj', 'Rajender', 'Rajendra',
             'Rajesh', 'Rajinder', 'Rajiv', 'Rajneesh', 'Rajnish', 'Rakesh', 'Rama', 'Ramachander', 'Ramachandra',
             'Ramakrishna', 'Ramesh', 'Ramesha', 'Rameshwar', 'Ranj', 'Ranjeet', 'Ranjit', 'Ratan', 'Ratnam', 'Ravi',
             'Ravindra', 'Rishi', 'Rohan', 'Rohit', 'Sachin', 'Saholy', 'Samourgom', 'Sandeep', 'Sandip', 'Sangaren',
             'Sanjay', 'Sanjaya', 'Sanjeet', 'Sanjeev', 'Sanjit', 'Sanjiv', 'Sankar', 'Sarad', 'Saral', 'Saravanan',
             'Satish', 'Satyakama', 'Savitr', 'Sejiyane', 'Sekar', 'Shankar', 'Shankara', 'Shanmouga', 'Shantanu', 'Sharma',
             'Shasty', 'Shekhar', 'Shiva', 'Shresth', 'Shrinivas', 'Shripati', 'Shrivatsa', 'Shyam', 'Shyamal', 'Sib',
             'Siddharta', 'Siddhartha', 'Singh', 'Sivacoumar', 'Skanda', 'Subhash', 'Sudarshan', 'Sudesh', 'Sudhir',
             'Sujay', 'Sukumar', 'Suman', 'Sumantra', 'Sundar', 'Sundara', 'Sundaram', 'Sunder', 'Sunil', 'Suraj',
             'Surendra', 'Suresh', 'Suresha', 'Surinder', 'Surya', 'Sushil', 'Swapan', 'Swapnil', 'Swaran', 'Tangavel',
             'Vadivel', 'Varghese', 'Variya', 'Vasant', 'Vasanta', 'Vassant', 'Vasu', 'Venkat', 'Venkata', 'Vidhyavathi',
             'Vignesh', 'Vijay', 'Vikram', 'Vikrama', 'Vikresen', 'Vimal', 'Vinay', 'Vipin', 'Vipul', 'Viraj', 'Vishal',
             'Vishnou', 'Vishnu', 'Vishvajit', 'Vivek', 'Vyasadeva', 'Yama', 'Yamaraja', 'Yash']
             
    LNAME = ['Banerjee', 'Bhatnagar', 'Bose', 'Chatterjee', 'Chauhan', 'Chavan', 'Chopra', 'Das', 'Dasgupta', 'Dutta',
             'Gavde', 'Gupta', 'Jaiteley', 'Jayaraman', 'Jhadav', 'Kadam', 'Kapoor', 'Khan', 'Malhotra', 'Malik', 'Mehra',
             'Mehta', 'Mistry', 'Mukopadhyay', 'Nair', 'Patel', 'Patil', 'Pawar', 'Pillai', 'Rangan', 'Rangarajan', 'Rao',
             'Sarin', 'Saxena', 'Sen', 'Sengupta', 'Shah', 'Sharma', 'Singh', 'Singh', 'Subramanium', 'Tambe', 'Venkatesan',
             'Verma', 'Yadav']
    
    
    
    
    def random_generator(self,size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    
    def __init__(self):
        self.email = ""
        self.mobile = ""
        self.otp=""
        self.lis=[]
        self.f_name=random.choice(self.FNAME)
    
    def reg(self):
        print("*****8regg************88")
        x = self.email.split(".")
    
        url = "https://api.urbanpiper.com/api/v2/card/?customer_phone=%2B91" + self.mobile + "&email=" + self.email + "&password="+self.mobile[2:-2]+"&customer_name="+self.f_name+"&channel=app_android"
        headers = {
            "Authorization": "apikey biz_adm_jgdLqvGhpBdjiBprHMFErW:1b5de5c716a4cd2088864fd40c5c2465d0f1f5fc",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.urbanpiper.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            
            "User-Agent": "okhttp/2.4.0",
        }
    
        #data = {"referral": {"channel": "WhatsApp", "code_link": "http://in.upipr.co/v2jh/N9OziMaCVC",
        #                     "linkGenTime": "May 6, 2017 7:13:12 PM", "referrer_card": "149131372a61a317f",
        #                     "linkGenTimeStr": "1494078192539", "platform": "android", "shared_on": 1494078192539}}
        data={}
        
        r = requests.post(verify=False, url=url, data=json.dumps(data), headers=headers)
        print(r.text)
    
    
    def enter_otp(self):
        print("*****otpppppppppppppp************88")
        pin =self.otp
        x = self.email.split(".")
        print(self.mobile,pin,self.f_name)
        url = "https://api.urbanpiper.com/api/v2/card/?nopinsend=true&customer_phone=%2B91" + self.mobile +"&pin="+pin+"&channel=app_android&customer_name="+self.f_name
        headers = {
            "Authorization": "apikey biz_adm_jgdLqvGhpBdjiBprHMFErW:1b5de5c716a4cd2088864fd40c5c2465d0f1f5fc",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.urbanpiper.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/2.4.0",
        }
        #data = {"customer_phone": "+91" + mobile, "pin": pin, "customer_name": random.choice(FNAME),"channel": "app_android"}
        r = requests.post(verify=False, url=url, headers=headers)
        
        print(r.text)
    
    
    
    
    
    def fn1(self):
        print("*****fn1************88")
        tm = TempMail()
        self.email = tm.get_email_address()
        d=self.random_generator(8,"1234567089")
        self.mobile = "71" + d
        print(self.email, self.mobile)
        self.reg()
    #if int(st) == 2:
        print(self.email)
        time.sleep(5)
        m=tm.get_mailbox(self.email)
        try:
            data=m[0]["mail_text_only"]
            otps = re.search(r'>(\d+)</span>', data)
            self.otp=otps.group(1)
            print(self.otp)
            self.enter_otp()
            # save_file()
        except:
            print(m)
            
        x={}
        x["email"]=self.email
        x["mobile"]=self.mobile
        x["password"]=self.mobile[2:-2]
        return x
