from tkinter import *              #importing this to create a GUI application 
import os                          #importing this to check  that the file is available that stores the login credentials to verify 
import csv                         #importing this to read the file of csv type  
from tkinter import filedialog     #importing this to attach the file to send the email 
import smtplib                     #importing this to allow python to send & receive emails 

#import the rest of the modules to allow the smtp server to send or receive the attachment with the email 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

count, c = 0,0

creds = 'tempfile.temp'  #path of the credentials that stores the username and password of different authorised users 

def login(): #creating a login function

    #creating the global variables so as to use globally
    global nameEL
    global pwordEL
    global rootA
    
    #creating a window manager 
    rootA = Tk()

    #giving a title to your window
    rootA.title('Login')

    #setting up the icon for your window 
    rootA.iconbitmap(r'20170115_144259.ico')

    #creating a label widget to set up the heading to your page
    instruction = Label(rootA,text = 'Please Login\n')
    instruction.grid(sticky=E)   #setting up the position of label


    #creating the labels to ask the user to enter the username and password;
    #also to setting up their positions using the grid 
    nameL = Label(rootA, text="Username: ")
    pwordL = Label(rootA, text="Password: ")
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    #creating the entries to let the user enter the username and password;
    #also to setting up their positions using the grid 
    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    #creating the buttons to login, signup and delete user,
    #also setup their properties with the labels on them
    loginB = Button(rootA, text="Login", relief=GROOVE, command= CheckLogin)
    loginB.grid(columnspan=2,sticky=W)
    signupB = Button(rootA, text="Signup", relief=GROOVE, command= Signup)
    signupB.grid(columnspan=2,sticky=W)
    rmuser = Button(rootA, text="Delete User", fg = 'red',relief=GROOVE, command= DelUser)
    rmuser.grid(column=2,sticky=W)

    #to close the window manually 
    rootA.mainloop()


def CheckLogin():  #creating a function to authenticate user 
    global ro      #creating a global variable 

    #opening the credentials in a read mode and
    #then checking each record to verify the authorised user 
    with open(creds) as f:
        data= csv.reader(f)  #reading credentials in csv format 
        for line in data:    #checking each line in the credential
            try:
                #storing the records from each line in variables uname
                #and pword respectively 
                uname = line[0]
                pword = line[1]
                
                #matching the uname and pword with the username and
                #password entered by the user respectively 
                if nameEL.get() == uname and pwordEL.get() == pword:

                    #destroy the current window &
                    #create a new window to display the message in case of correct credentials 
                    rootA.destroy()
                    r=Tk()
                    r.title(':D')
                    r.iconbitmap(r'20170115_144259.ico')
                    r.geometry('150x50')
                    rlbl = Label(r,text='\n[+] Logged In')
                    rlbl.pack()
                    r.mainloop()
                    send()     #calling the send() function to send an email 
            except IndexError: #in case of IndexError pass statement is passed to avoid raising the error 
                pass
        else:
            #In case the credentials didn’t match 
            r= Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r,text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
            login() #In case the credentials didn’t match login() function is called 

def send():   #creating a function to create new window to logout and
              #compose a new email and further sent it with or without attachment 
    global ro
    ro= Tk()
    ro.title('Send Message')
    ro.iconbitmap(r'20170115_144259.ico')
    ro.geometry('200x100')    #setting up the size of the window
    new = Button(ro,text='New Message', relief=GROOVE, command=mail)
    new.grid(row=1, column=0, sticky=N)
    new = Button(ro,text='Log Out', relief=GROOVE, command=logout)
    new.grid(row=1, column=2, sticky=N)
    ro.mainloop()
                
def mail():  #creating a function with multiple functions to compose an email
    def attach():     #creating a function to attach a file with email 
        global count  #setting up count as global variable 
        count +=1     #incrementing the counter

        #calling the dialog window to ask you to select a file to attach 
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes= (("jpeg files","*.jpg"),("all files","*.*")))

        #displaying path of selected file in a label widget in current window and
        #setting up the position of label
        file = Label(root, text=root.filename)
        file.grid(row=7, column=0,sticky=W)
        
    def Pass():  #creating a pass() function to do nothing 
        pass

    def Sendmail():   #creating Sendmail() function to send email with or without attachment 
        global count
        global c
        msg = MIMEMultipart()  #creating an object to send multiple stuff 

        msg['From']= 'abc123@gmail.com'   #sender’s mail id 
        msg['To']= Toe.get()               #send to multiple users 
        msg['Subject']= Subjecte.get()     #setup the subject to the email 

        body = texte.get("1.0","end-1c")   #fetching main message from the text widget from the compose window 
        msg.attach(MIMEText(body,'plain')) #combining the body of the email with rest of the message 

        if count>0:  #combining the attachment with rest of the message so that all the parts of the mail could be send as one 
            filename = root.filename
            attachment = open(filename,'rb')
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename="+filename)
            msg.attach(part)
        else:
            pass
        text= msg.as_string()  #converting the main message into string
        
        #setup the Gmail protocol to send or receive emails 
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login("abc123@gmail.com","hello456")
        try:
            mail.sendmail("abc123@gmail.com",msg['To'],text)
            c+=1    #incrementing the counter c 
            print('Email Sent')
        except:
            print('Error Sending Email')
        mail.quit()
        root.destroy()
        if c>=1:  #if mail was sent successfully the new window is opened and
                  #following message is displayed 
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r,text='\n[+] Email sent')
            rlbl.pack()
            r.mainloop()
        else:
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r,text='\n[!] Error Sending Email')
            rlbl.pack()
            r.mainloop()

    #The code below will display the following window to compose an email         
    root= Tk()
    root.title('New Message')
    root.iconbitmap(r'20170115_144259.ico')
    To= Label(root,text="To: ")
    Subject= Label(root,text="Subject: ")
    text= Label(root,text="Message: ")
    To.grid(row=1,column=0,sticky=W)
    Subject.grid(row=2,column=0,sticky=W)
    text.grid(row=3,column=0,sticky=NW)

    Toe= Entry(root,width=67)
    Subjecte= Entry(root,width=67)
    texte= Text(root,width=50,height=5)
    Toe.grid(row=1,column=1,sticky=W)
    Subjecte.grid(row=2,column=1,sticky=W)
    texte.grid(row=3,column=1,sticky=W)


    attach= Button(root,text="Attach",relief=GROOVE,command=attach)
    attach.grid(row=6, column=1,sticky=W)
    send= Button(root,text="Send",relief=GROOVE, command=Sendmail)
    send.grid(row=6, column=0,sticky=W)
    file=Label(root,text='')
    file.grid(row=7, column=0,sticky=W)
    root.geometry('500x170')
    root.mainloop()

def logout():    #creating a function to logout 
    ro.destroy()
    r=Tk()
    r.title(':D')
    r.iconbitmap(r'20170115_144259.ico')
    r.geometry('150x100')
    rlbl= Label(r,text='\n [+] Logged Out Successfully.')
    rlbl.pack()
    r.mainloop()
    login()

def Signup():      #creating a signup function to add new user 
    global pwordE  #creating a global variable 
    global nameE
    global roots

    rootA.destroy()
    roots= Tk()  #this creates the window just a blank one 
    roots.title("Signup")
    roots.iconbitmap(r'20170115_144259.ico')
    
    #this puts a label so just a piece of text saying 'please enter ...'
    instruction = Label(roots,text='Please Enter new Credentials\n')
    instruction.grid(row=0,column=0,sticky=E)
    nameL= Label(roots,text='New Username: ')
    pwordL= Label(roots,text='New Password: ')
    nameL.grid(row=1, column=0,sticky=W)
    pwordL.grid(row=2, column=0,sticky=W)

    nameE= Entry(roots)  #this now puts on text box waiting for input 
    pwordE= Entry(roots,show='*')   #same as above ,yet show ='*' what this does is just replace he text with the '*' like a password box :D 
  
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2, column=1)

    signupButton= Button(roots,text='Signup',relief=GROOVE,command=FSSignup)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()

def FSSignup():
    with open(creds,'a') as f:   #update the user name and password in the credentials for the new user 
        f.write(nameE.get())   #fetching the name from the name text 
        f.write(',')    #seperating username and password with comma
        f.write(pwordE.get())  #fetching the password 
        f.write('\n')  #creating a new line after each credentials 
        f.close()  #closes the file 
    roots.destroy()  #this will destroy the signup window 
    login()   #this will move us on to the login window to validate 

def DelUser():  #creating a function to delete credentials 
    os.remove(creds)  #removing the credentials file from the directory it is stored in 

    rootA.destroy()
    Signup()  #taking you to signup page so as to start creating new credentials 


if os.path.isfile(creds):  #checking whether credentials are there on the specified path or not ,
                           #if yes then login() window is called 
    login()
else:
    Signup()   #else signup window is called 
    
    
        
        
        





