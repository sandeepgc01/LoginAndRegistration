from tkinter import*
from tkinter import messagebox 
from PIL import ImageTk



class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        
        
        #------bg image----

        self.bg=ImageTk.PhotoImage(file="D:\images\login.jpg.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       
        

       
        # ----- frame -----

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=300,y=150,height=340,width=500)

        # -----label----------

        title=Label(Frame_login, text="login",font=("impact",35,"bold"), fg="#d77337" ,bg="white" ).place(x=90,y=30)       
        desc=Label(Frame_login, text="business login area",font=("gaudy old style",15,"bold"), fg="#d25d17" ,bg="white" ).place(x=90,y=100) 
       
        
        lbl_user=Label(Frame_login, text="Username",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350,height=35)
      
        
        lbl_user=Label(Frame_login, text="Password",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times in roman",15),bg="lightgray")
        self.txt_pass.place(x=90, y=250, width=350,height=35)
        

        # ------button------
        
        forget_btm=Button(Frame_login,command=self.forget_function, text="forget password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=290)
        
        
        login_btn=Button(self.root,command=self.login_function, text="login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=500,y=470,width=180,height=40)

        
        CreateAccount_btm=Button(Frame_login,command=self.Create_function, text="Create account",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=250,y=290)
    
    

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fileds are required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="sandeep":
            messagebox.showerror("Error","Invalid Username or password",parent=self.root)
        else:
            window=Tk()
        window.title("bussiness page")
        window.geometry("1199x600+100+50")
        title=Label(window, text="wel-come",font=("impact",50,"bold"), fg="#d77337" ,bg="white" ).place(x=450,y=150) 
        
        window.resizable(False,False)

    
    
    #------forget function-----

    
    def forget_function(self):
        window=Tk()
        window.title("forget page ")
        window.geometry("800x400+80+40")
        window.resizable(False,False)


        #-----button-----
        Label_02=Label (window, text="phone no.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=80)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=125, width=350,height=35)


        confirm_btm=Button(window, text="confirm",bg="white",fg="#d77337",bd=0,font=("times new roman",25)).place(x=350,y=250)


       
             
    # ----- creating button function---

    def Create_function(self):
        window=Tk()
        window.title("Registration page")
        window.geometry("1199x600+100+50")
        window.resizable(False,False)
    
        
        Label_02=Label(window,text='registration form' , relief="solid",font=('arial',20,'bold')).place(x=450,y=70)
        
        
        Label_02=Label (window, text="first name.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=140)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=175, width=350,height=35)
        

        
        Label_03=Label (window, text="last name.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=210)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=250, width=350,height=35)

        
        Label_04=Label (window, text="email.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=290)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=330, width=350,height=35)


        
        Label_05=Label (window, text="phone no.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=90,y=370)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=410, width=350,height=35)

        
        Label_06=Label (window, text="date of birth.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=700,y=140)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=700, y=175, width=350,height=35)

        
        Label_07=Label (window, text="Address. ",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=700,y=210)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=700, y=250, width=350,height=35)

        
        Label_08=Label (window, text="country. ",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white").place(x=700,y=290)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=700, y=330, width=350,height=35)

        
        Label_09=Label (window, text="country code.",font=("gaudy old style",15,"bold"), fg="gray" ,bg="white" ).place(x=700,y=370)
        self.txt_user=Entry(window ,font=("times in roman",15),bg="lightgray")
        self.txt_user.place(x=700, y=410, width=350,height=35)

        
        #----button

        signup_btm=Button(window, text="signup",bg="white",fg="#d77337",bd=0,font=("times new roman",25)).place(x=400,y=470)

        cancel_btm=Button(window,text="cancle",command=window.quit,bg="white",fg="#d77337",bd=0,font=("times new roman",25)).place(x=600,y=470)

        #button_quit.pack

        
        #--term and condition----
        chk=Checkbutton(window, text="I Agree the term & condition",font=("gaudy old style",15,"bold"),fg="gray",bg="white").place(x=400,y=450)

        
        
    


    

        


     
     

root=Tk()
obj=login(root)
root.mainloop()