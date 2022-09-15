from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk

class criminal:
    def __init__(self, win):
        self.win=win

        self.win.geometry("1655x1355+0+0")
        self.win.title('CRIME CONTROL SYSTEM')

        self.var_case_id=StringVar()
        self.var_case_no = StringVar()
        self.var_case_crimetype = StringVar()
        self.var_case_name = StringVar()
        self.var_case_crimedate = StringVar()
        self.var_case_cfb = StringVar()
        self.var_case_gender = StringVar()
        self.var_case_birthmark = StringVar()
        self.var_case_age = StringVar()
        self.var_case_occup = StringVar()
        self.var_case_wanted = StringVar()

        Label_title=Label(self.win,text="CRIME MANAGEMENT SYSTEM",font=('Nanum Gothic',40,'bold'),bg='black',fg='yellow')
        Label_title.place(x=0,y=0,width=1300,height=70)

        image_logo=Image.open('Delhi_Police_Logo.png')
        image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
        self.Photo_icon=ImageTk.PhotoImage(image_logo)

        self.logo=Label(self.win,image=self.Photo_icon)
        self.logo.place(x=200,y=5,width=50,height=50)

        image_frame=Frame(self.win,border=4,relief=RIDGE,bg='white')
        image_frame.place(x=0,y=70,width=1300,height=120)

        image1=Image.open('police.png')
        image1=image1.resize((450,160),Image.ANTIALIAS)
        self.police1=ImageTk.PhotoImage(image1)

        self.img1=Label(image_frame,image=self.police1)
        self.img1.place(x=0,y=0,width=450,height=160)
        image2 = Image.open('police2.png')
        image2 = image2.resize((450, 160), Image.ANTIALIAS)
        self.police2 = ImageTk.PhotoImage(image2)
        self.img2 = Label(image_frame, image=self.police2)
        self.img2.place(x=450, y=0, width=450, height=160)
        image3 = Image.open('police3.png')
        image3 = image3.resize((450, 160), Image.ANTIALIAS)
        self.police3 = ImageTk.PhotoImage(image3)
        self.img3 = Label(image_frame, image=self.police3)
        self.img3.place(x=900, y=0, width=450, height=160)
        Frame3=Frame(self.win,bg='snow',relief=RIDGE,border=2)
        Frame3.place(x=10,y=200,width=1300,height=560)
        Frame4 = LabelFrame(Frame3, bg='snow', relief=RIDGE ,text="Criminal Details",font=('Nanum Gothic',18,'bold'),fg='maroon')
        Frame4.place(x=5, y=10, width=1240, height=240)

#CaseID
        Case_Id=Label(Frame4,text="Case Id:",font=('arial',12,'bold'),bg='white')
        Case_Id.grid(row=0,column=0,padx=2,sticky=W)

        Case_Id = ttk.Entry(Frame4,textvariable=self.var_case_id,width=22,font=('arial',10,'bold'))
        Case_Id.grid(row=0,column=1,padx=2,pady=2,sticky=W)

#CriminalNo
        Criminal_No=Label(Frame4,font=('arial',12,'bold'),text="Criminal Number:",bg='white')
        Criminal_No.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        Criminal_No = ttk.Entry(Frame4,textvariable=self.var_case_no,width=22,font=('arial',10,'bold'))
        Criminal_No.grid(row=0,column=3,padx=2,pady=7,sticky=W)

# CriminalArrest
        Criminal_CrimeType = Label(Frame4, font=('arial', 12, 'bold'), text="Crime Type:", bg='white')
        Criminal_CrimeType.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        Criminal_CrimeType = ttk.Entry(Frame4,textvariable=self.var_case_crimetype, width=22, font=('arial', 10, 'bold'))
        Criminal_CrimeType.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        Criminal_Name = Label(Frame4, font=('arial', 12, 'bold'), text="Criminal Name:", bg='white')
        Criminal_Name.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        Criminal_Name = ttk.Entry(Frame4,textvariable=self.var_case_name, width=22, font=('arial', 10, 'bold'))
        Criminal_Name.grid(row=0, column=5, padx=2, pady=7, sticky=W)

# CriminalCrimeDate
        Criminal_CrimeDate = Label(Frame4, font=('arial', 12, 'bold'), text="Arrest Date", bg='white')
        Criminal_CrimeDate.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        Criminal_CrimeDate= ttk.Entry(Frame4, textvariable=self.var_case_crimedate, width=22, font=('arial', 10, 'bold'))
        Criminal_CrimeDate.grid(row=1, column=1, padx=2, pady=7, sticky=W)

# CriminalCrimalCFB
        Criminal_CFB = Label(Frame4, font=('arial', 12, 'bold'), text="Cases filed before:", bg='white')
        Criminal_CFB.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        Criminal_CFB = ttk.Entry(Frame4,textvariable=self.var_case_cfb, width=22, font=('arial', 10, 'bold'))
        Criminal_CFB.grid(row=2, column=1, padx=2, pady=7, sticky=W)

# CriminalAge
        Criminal_Gender= Label(Frame4, font=('arial', 12, 'bold'), text="Gender", bg='white')
        Criminal_Gender.grid(row=2, column=2, padx=2, pady=7, sticky=W)

# CriminalBirth
        Criminal_BirthMark = Label(Frame4, font=('arial', 12, 'bold'), text="Birth Mark:", bg='white')
        Criminal_BirthMark.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        Criminal_BirthMark= ttk.Entry(Frame4, textvariable=self.var_case_birthmark, width=22, font=('arial', 10, 'bold'))
        Criminal_BirthMark.grid(row=3, column=1, padx=2, pady=7, sticky=W)

# CriminalAge
        Criminal_age = Label(Frame4, font=('arial', 12, 'bold'), text="Age:", bg='white')
        Criminal_age.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        Criminal_age = ttk.Entry(Frame4,textvariable=self.var_case_age, width=22, font=('arial', 10, 'bold'))
        Criminal_age.grid(row=3, column=3, padx=2, pady=7, sticky=W)

# CrimeBirth
        Criminal_Occup = Label(Frame4, font=('arial', 12, 'bold'), text="Occupation:", bg='white')
        Criminal_Occup.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        Criminal_Occup = ttk.Entry(Frame4, textvariable=self.var_case_occup, width=22, font=('arial', 10, 'bold'))
        Criminal_Occup.grid(row=4, column=1, padx=3, pady=7, sticky=W)

        # CriminalName
        Criminal_Wanted = Label(Frame4, font=('arial', 12, 'bold'), text="Wanted:", bg='white')
        Criminal_Wanted.grid(row=4, column=2, padx=12, pady=8, sticky=W)

#Buttonsgender
        radioframe_gender=Frame(Frame4,border=2,relief=RIDGE,bg='white')
        radioframe_gender.place(x=460,y=80,width=160,height=30)

        male=Radiobutton(radioframe_gender,variable=self.var_case_gender,text='Male',value='male',font=("times roman",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=4,sticky=W)

        Female = Radiobutton(radioframe_gender, variable=self.var_case_gender, text='Female', value='Female', font=("times roman", 9, "bold"), bg='white')
        Female.grid(row=0, column=2, pady=2, padx=4, sticky=W)

# Buttonswanted
        radioframe_wanted = Frame(Frame4, border=2, relief=RIDGE, bg='white')
        radioframe_wanted.place(x=460, y=160, width=160, height=30)

        Yes = Radiobutton(radioframe_wanted, variable=self.var_case_wanted, text='Yes',value='Yes',font=("times roman", 9, "bold"), bg='white')
        Yes.grid(row=4, column=2, pady=2, padx=4, sticky=W)

        No = Radiobutton(radioframe_wanted, variable=self.var_case_wanted, text='No',value='No', font=("times roman", 9, "bold"),
                             bg='white')
        No.grid(row=4, column=3, pady=2, padx=4, sticky=W)

        #BUTTONS

        button_frame = Frame(Frame4, border=2, relief=RIDGE, bg='white')
        button_frame.place(x=700, y=120, width=500, height=55)
        
        btn_add=Button(button_frame,command=self.add_Data,text="Save",font=("times roman", 9, "bold"),width=14,bg='maroon',fg='white')
        btn_add.grid(row=0,column=0,padx=6,pady=7)

        btn_Update = Button(button_frame, command=self.update_data, text="Update", font=("times roman", 9, "bold"), width=14, bg='maroon', fg='white')
        btn_Update.grid(row=0, column=1, padx=3, pady=7)

        btn_Delete = Button(button_frame,command=self.delete, text="Delete", font=("times roman", 9, "bold"), width=14, bg='maroon', fg='white')
        btn_Delete.grid(row=0, column=2, padx=3, pady=7)

        btn_Clear = Button(button_frame, command=self.clear_data, text="Clear", font=("times roman", 9, "bold"), width=14, bg='maroon', fg='white')
        btn_Clear.grid(row=0, column=3, padx=3, pady=7)

        Frame5 = LabelFrame(Frame3, bg='snow', relief=RIDGE, text="Criminal Details Table", font=('Nanum Gothic', 18, 'bold'),
                            fg='maroon')
        Frame5.place(x=5, y=250, width=1260, height=270)

        FrameSearch = LabelFrame(Frame5, bg='snow', relief=RIDGE, text="Search Criminal Record",
                            font=('Nanum Gothic', 10, 'bold'),
                            fg='maroon')
        FrameSearch.place(x=0, y=0, width=1465, height=70)

        search_by=Label(Frame5,font=("arial",10,"bold"),text="Search By:",bg="blue",fg="snow")
        search_by.grid(row=1,column=0,sticky=W,padx=6,pady=30)

        self.var_com_search=StringVar()

        combo_box=ttk.Combobox(FrameSearch, textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state='read')
        combo_box['value']=('Select Option','Case_Id','Criminal_No')
        combo_box.current(0)
        combo_box.grid(row=1,column=2,sticky=W,padx=90,pady=2)

        self.var_search = StringVar()

        search_Entry = ttk.Entry(FrameSearch,textvariable=self.var_search, width=18, font=('arial', 10, 'bold'))
        search_Entry.grid(row=1, column=3,sticky=W, padx=5, pady=2)

        btn_Search = Button(FrameSearch,command=self.Search, text="Search", font=("times roman", 9, "bold"), width=14, bg='maroon',
                            fg='white')
        btn_Search.grid(row=1, column=4,sticky=W, padx=5, pady=2)

        btn_all = Button(FrameSearch,command=self.fetch_data, text="Show all", font=("times roman", 9, "bold"), width=14, bg='maroon',
                           fg='white')
        btn_all.grid(row=1, column=5,sticky=W, padx=5, pady=2)

        CrimeDept= Label(FrameSearch, font=("arial", 15, "bold"), text="Sadrakṣaṇāya Khalanigrahaṇāya", bg="snow", fg="crimson")
        CrimeDept.grid(row=1, column=7, sticky=W, padx=200,pady=12)

        table_frame=Frame(Frame5,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1465,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview())
        scroll_y.config(command=self.criminal_table.yview())

        self.criminal_table.heading('1',text='Case_ID')
        self.criminal_table.heading('2', text='Criminal_No')
        self.criminal_table.heading('3', text= 'Criminal_CrimeType')
        self.criminal_table.heading('4', text='Criminal_Name')
        self.criminal_table.heading('5',text='Criminal_CrimeDate')
        self.criminal_table.heading('6', text='Criminal_CFB')
        self.criminal_table.heading('7', text='Criminal_Gender')
        self.criminal_table.heading('8', text='Criminal_BirthMark')
        self.criminal_table.heading('9',  text='Criminal_age')
        self.criminal_table.heading('10', text='Criminal_Occup')
        self.criminal_table.heading('11', text='Criminal_wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=90)
        self.criminal_table.column('2', width=90)
        self.criminal_table.column('3', width=90)
        self.criminal_table.column('4', width=90)
        self.criminal_table.column('5', width=90)
        self.criminal_table.column('6', width=90)
        self.criminal_table.column('7', width=90)
        self.criminal_table.column('8', width=90)
        self.criminal_table.column('9', width=90)
        self.criminal_table.column('10', width=90)
        self.criminal_table.column('11', width=90)

        self.criminal_table.pack(fill=BOTH,expand=1)
        scroll_x.config(command=self.criminal_table.xview())

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)


    def add_Data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required',parent=self.win)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Salonishah306@',port='3306',database='criminal1')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                    self.var_case_id.get(),
                                                                                                   self.var_case_no.get(),
                                                                                                   self.var_case_crimetype.get(),
                                                                                                   self.var_case_name.get(),
                                                                                                   self.var_case_crimedate.get(),
                                                                                                   self.var_case_cfb.get(),
                                                                                                   self.var_case_gender.get(),
                                                                                                   self.var_case_birthmark.get(),
                                                                                                   self.var_case_age.get(),
                                                                                                   self.var_case_occup.get(),
                                                                                                   self.var_case_wanted.get()
                                                                                                                        ))

                conn.commit()

                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Record has been added')

            except Exception as Exp:

                  messagebox.showerror('Error', f'Due to {str(Exp)}')


    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Salonishah306@', port='3306',
                                       database='criminal1')

        my_cursor = conn.cursor()

        my_cursor.execute("select * from criminal")

        data = my_cursor.fetchall()

        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("", END, values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_case_no.set(data[1])
        self.var_case_crimetype.set(data[2])
        self.var_case_name.set(data[3])
        self.var_case_crimedate.set(data[4])
        self.var_case_cfb.set(data[5])
        self.var_case_gender.set(data[6])
        self.var_case_birthmark.set(data[7])
        self.var_case_age.set(data[8])
        self.var_case_occup.set(data[9])
        self.var_case_wanted.set(data[10])

    def update_data(self):

        if self.var_case_id.get() == "":

            messagebox.showerror('Error', 'All fields are required', parent=self.win)

        else:

            try:

                update=messagebox.askyesno('Update','Do you want to Update this Criminal record?')

                if update>0:

                     conn = mysql.connector.connect(host='localhost', username='root', password='Salonishah306@', port='3306',
                                               database='criminal1')

                     my_cursor = conn.cursor()
                     my_cursor.execute('update criminal set Criminal_no=%s , Criminal_CrimeType=%s, Criminal_Name=%s , Criminal_CrimeDate=%s,Criminal_CFB=%s,Criminal_Gender=%s,Criminal_BirthMark=%s,Criminal_age=%s,Criminal_Occup=%s,Criminal_wanted=%s where Case_id=%s',(

                         self.var_case_no.get(),
                         self.var_case_crimetype.get(),
                         self.var_case_name.get(),
                         self.var_case_crimedate.get(),
                         self.var_case_cfb.get(),
                         self.var_case_gender.get(),
                         self.var_case_birthmark.get(),
                         self.var_case_age.get(),
                         self.var_case_occup.get(),
                         self.var_case_wanted.get(),
                         self.var_case_id.get()
                     ))

                else:
                    if not update:

                        return

                conn.commit()

                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Record has been successfully updated!!')

            except Exception as Exp:

                  messagebox.showerror('Error', f'Due to {str(Exp)}')

    def delete(self):

        if self.var_case_id.get() == "":

            messagebox.showerror('Error', 'All fields are required', parent=self.win)

        else:
            try:
                delete = messagebox.askyesno('delete', 'Do you want to Delete this Criminal record?')

                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Salonishah306@',
                                                   port='3306',
                                                   database='criminal1')

                    my_cursor = conn.cursor()
                    sql = 'delete from criminal where Case_Id=%s'
                    value = (self.var_case_id.get(),)
                    my_cursor.execute(sql, value)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo('Success','Criminal Record Deleted Successfully!!')
                conn.close()

            except Exception as Exp:

                  messagebox.showerror('Error', f'Due to {str(Exp)}')


    def clear_data(self):
        self.var_case_no.set("")
        self.var_case_crimetype.set("")
        self.var_case_name.set("")
        self.var_case_crimedate.set("")
        self.var_case_cfb.set("")
        self.var_case_gender.set("")
        self.var_case_birthmark.set("")
        self.var_case_age.set("")
        self.var_case_occup.set("")
        self.var_case_wanted.set("")
        self.var_case_id.set("")


    def Search(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required!!')

        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Salonishah306@',
                                               port='3306',
                                               database='criminal1')

                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows) != 0:

                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:

                         self.criminal_table.insert("", END, values=i)
                conn.commit()
                conn.close()

            except Exception as Exp:

                  messagebox.showerror('Error', f'Due to {str(Exp)}')

if __name__=="__main__":

    win = Tk()
    object1=criminal(win)
    win.mainloop()

