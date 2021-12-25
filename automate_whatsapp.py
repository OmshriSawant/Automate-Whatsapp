import pywhatkit as kt
import getpass as gp

print("Lets Automate WhatsApp!")

p_num = gp.getpass(prompt='Phonenumber: ', stream = None )

msg = 'hii tai'

kt.sendwhatmsg(p_num,msg,16,40)
