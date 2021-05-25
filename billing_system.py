from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_app:
    def __init__(self,root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.geometry("1390x740+0+0")
        self.root.title("BILLING SOFTWARE")
        bg_color = "#074463"
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill = X)
        #==========================variables=============================
        #==================cosmatics=========================
        # x=1
        self.soap=IntVar()
        # self.soap.set(x)
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        # ========================grocery================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #====================colddrink=====================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limka=IntVar()
        self.sprite=IntVar()
        #==============total product price & tax variables================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #==============customer========================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        
        self.bill_no=StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        # _____________________________customer detail frame___________________________________________________________
        F1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl = Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #_______________cosmatic frame___________________________________________________#

        F2 = LabelFrame(self.root,text="Cosmatic",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl = Label(F2,text="Body Deodorants",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2,text="Skin Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl = Label(F2,text="Facial Kit",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl = Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt = Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl = Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt = Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #_______________grocery frame___________________________________________________#

        F3 = LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335,y=180,width=325,height=380)

        g1_lbl = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3,text="Cooking Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3,text="Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3,text="Fruits",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #_______________cold drink frame___________________________________________________#

        F4 = LabelFrame(self.root,text="Soft Drink",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=665,y=180,width=325,height=380)

        c1_lbl = Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4,text="Thums Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F4,width=10,textvariable=self.limka,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #_BILL AREA____________________________________________________#

        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=995,y=180,width=365,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #ButtonFrame_______________________________________________________

        F6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl = Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl = Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt = Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl = Label(F6,text="Total Soft drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt = Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl = Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(F6,text="Soft drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        # btn
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=6,pady=2)
        GBill_btn=Button(btn_F,command=self.bill_area,text="Genrate Bill",bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=6,pady=2)
        Clear_btn=Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=1,column=0,padx=7,pady=2)
        Exit_btn=Button(btn_F,command=self.exit_app,text="Exit",bg="cadetblue",fg="white",width=21,height=1,bd=2,font="arial 15 bold").grid(row=1,column=1,padx=7,pady=2)

        self.welcome_bill()


    def total(self):
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.face_cream.get()*120
        self.c_fw_p = self.face_wash.get()*60
        self.c_hs_p = self.spray.get()*180
        self.c_hg_p = self.gell.get()*140
        self.c_bl_p = self.loshan.get()*180
        
        self.total_cosmetic_price=float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetic_price.set(str(self.total_cosmetic_price)+" Rs.")
        self.c_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set(str(self.c_tax)+" Rs.")

        self.g_r_p= (self.rice.get()*80)
        self.g_f_p= (self.food_oil.get()*180)
        self.g_d_p= (self.daal.get()*60)
        self.g_w_p= (self.wheat.get()*240)
        self.g_s_p= (self.sugar.get()*45)
        self.g_t_p= (self.tea.get()*150)
        
        self.total_grocery_price=float(
            self.g_r_p + self.g_f_p + self.g_d_p + self.g_w_p + self.g_s_p + self.g_t_p
            
        )
        self.grocery_price.set(str(self.total_grocery_price)+" Rs.")
        self.g_tax = round((self.total_grocery_price*0.01),2)
        self.grocery_tax.set(str(self.g_tax)+" Rs.")

        self.d_m_p= (self.maza.get()*60)
        self.d_c_p= (self.cock.get()*60)
        self.d_f_p= (self.frooti.get()*50)
        self.d_t_p= (self.thumbsup.get()*45)
        self.d_l_p= (self.limka.get()*40)
        self.d_s_p= (self.sprite.get()*60)
        
        self.total_drink_price=float(
            self.d_m_p + self.d_c_p + self.d_f_p + self.d_t_p + self.d_l_p + self.d_s_p
        )
        self.cold_drink_price.set(str(self.total_drink_price)+" Rs.")
        self.d_tax = round((self.total_drink_price*0.05),2)
        self.cold_drink_tax.set(str(self.d_tax)+" Rs.")

        self.Total_bill = float(self.total_cosmetic_price + self.total_grocery_price + self.total_drink_price
                            + self.c_tax + self.g_tax +self.d_tax)



    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Harsh\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n========================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif (self.c_phon.get().isdigit() != True) or (len(self.c_phon.get()) != 10) :
            messagebox.showerror("Error","Mobile Number must be integers and having 10 digits")
        elif (self.cosmetic_price.get() == "0.0 Rs.") and (self.grocery_price.get() == "0.0 Rs.") and (self.cold_drink_price.get() == "0.0 Rs." ):
            messagebox.showerror("Error","No Product Selected")


        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Body Deodorants\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Skin Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Facial Kit\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body lotion\t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Cooking Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Milk\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Fruits\t\t{self.tea.get()}\t\t{self.g_t_p}")

            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Coca Cola\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.cock.get()}\t\t{self.d_c_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thums Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limka.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limka.get()}\t\t{self.d_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")


            self.txtarea.insert(END,f"\n----------------------------------------")
            if self.cosmetic_tax.get()!="0.0 Rs.":
                self.txtarea.insert(END,f"\n Cosmatic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="0.0 Rs.":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="0.0 Rs.":
                self.txtarea.insert(END,f"\n Soft Drink Tax\t\t\t{self.cold_drink_tax.get()}")
            
            if self.cosmetic_price.get() !="0.0 Rs.":
                self.txtarea.insert(END,f"\n Cosmetic Price\t\t\t{self.cosmetic_price.get()}")
            if self.grocery_price.get() !="0.0 Rs.":
                self.txtarea.insert(END,f"\n Grocery Price\t\t\t{self.grocery_price.get()}")
            if self.cold_drink_price.get() !="0.0 Rs.":
                self.txtarea.insert(END,f"\n Soft Drink Price\t\t\t{self.cold_drink_price.get()}")
            
            self.txtarea.insert(END,f"\n----------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t{str(self.Total_bill)} Rs.")
            self.txtarea.insert(END,f"\n----------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0",END)
            f1 = open("customer_bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return
    def find_bill(self):
        present = "no"
        for i in os.listdir("customer_bills/"):
            if i.split(".")[0] == self.search_bill.get():
                present= "yes"
                f1 = open(f"customer_bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear the data?")
        if op>0:
            self.soap.set(0)
            # self.soap.set(x)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ========================grocery================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #====================colddrink=====================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limka.set(0)
            self.sprite.set(0)
            #==============total product price & tax variables================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #==============customer========================
            self.c_name.set("")
            self.c_phon.set("")
            
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_app(root)
root.mainloop()