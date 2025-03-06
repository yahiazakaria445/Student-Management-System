from tkinter import *
from tkinter import ttk
import pymysql
#---------------------------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('Student Management System')
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title =Label(self.root,text='Student Management System',bg='#306EFF',font=('monospace',14),fg='white')
        title.pack(fill=X)
        #----------------------Variables---------------------
        self.id_var =StringVar()
        self.name_var =StringVar()
        self.email_var =StringVar()
        self.phone_var =StringVar()
        self.moahel_var =StringVar()
        self.gender_var =StringVar()
        self.address_var =StringVar()
        self.dell_var =StringVar()
        self.se_var =StringVar()
        self.se_by =StringVar()
        #--------------------------------------Control Tools----------------------------------------
        manage_frame = Frame(self.root,bg='white')
        manage_frame.place(x=1137,y=30,width=210,height=400)

        lbl_id = Label(manage_frame,text='Student ID',bg='white')
        lbl_id.pack()
        ID_Entry = Entry(manage_frame,textvariable=self.id_var,bd=2)
        ID_Entry.pack()

        lbl_name =Label(manage_frame,bg='white',text='Student Name')
        lbl_name.pack()
        Name_Entry =Entry(manage_frame,textvariable=self.name_var,bd=2)
        Name_Entry.pack()
        
        lbl_email = Label(manage_frame,text='Student Email',bg='white')
        lbl_email.pack()
        email_Entry = Entry(manage_frame,textvariable=self.email_var,bd=2)
        email_Entry.pack()

        lbl_phone = Label(manage_frame,text='Student Phone',bg='white')
        lbl_phone.pack()
        phone_Entry = Entry(manage_frame,textvariable=self.phone_var,bd=2)
        phone_Entry.pack()

        lbl_certi = Label(manage_frame,text='Educational Level',bg='white')
        lbl_certi.pack()
        combo_gender =ttk.Combobox(manage_frame,textvariable=self.moahel_var)
        combo_gender['value'] =('Elementary','Preparatory','Secondary')
        combo_gender.pack()

        lbl_gender = Label(manage_frame,text='Student Gender',bg='white')
        lbl_gender.pack()
        combo_gender =ttk.Combobox(manage_frame,textvariable=self.gender_var)
        combo_gender['value'] =('male','female')
        combo_gender.pack()

        lbl_address = Label(manage_frame,text='Student Address',bg='white')
        lbl_address.pack()
        address_Entry = Entry(manage_frame,textvariable=self.address_var,bd=2)
        address_Entry.pack()

        lbl_delete = Label(manage_frame,text='Delete By Name',fg='red',bg='white')
        lbl_delete.pack()
        delete_Entry = Entry(manage_frame,textvariable=self.dell_var,bd=2)
        delete_Entry.pack()
        #------------------------Control buttons---------------------------
        btn_frame = Frame(self.root,bg='white')
        btn_frame.place(x=1137,y=435,width=210,height=253)
        title1 =Label(btn_frame,text='Control Buttons',font=('Deco',14),fg='white',bg='#306EFF')
        title1.pack(fill=X)

        add_btn =Button(btn_frame,text='Add',bg='#CFD8DC',command=self.add_student)
        add_btn.place(x=33,y=45,width=150,height=30)

        del_btn =Button(btn_frame,text='Delete',bg='#CFD8DC',command=self.delete)
        del_btn.place(x=33,y=80,width=150,height=30)

        update_btn =Button(btn_frame,text='Updata',bg='#CFD8DC',command=self.update)
        update_btn.place(x=33,y=115,width=150,height=30)

        clear_btn =Button(btn_frame,text='Clear',bg='#CFD8DC',command=self.clear)
        clear_btn.place(x=33,y=150,width=150,height=30)

        exit_btn =Button(btn_frame,text='Exit',bg='#CFD8DC',command=root.quit)
        exit_btn.place(x=33,y=185,width=150,height=30)
        #------------------------search managing--------------------------
        search_Frame =Frame(self.root,bg='white')
        search_Frame.place(x=1,y=30,width=1134,height=50)

        lbl_search =Label(search_Frame,text='Searching Bar',bg='white')
        lbl_search.place(x=1034,y=12)

        combo_search = ttk.Combobox(search_Frame,textvariable=self.se_by)
        combo_search['value']=('id','name','email','phone')
        combo_search.place(x=880,y=12)

        search_Entry = Entry(search_Frame,textvariable=self.se_var,bd='2')
        search_Entry.place(x=750,y=12)

        se_Dutton =Button(search_Frame,text='search',bg='white',command=self.search)
        se_Dutton.place(x=630,y=12,width=100,height=25)
        #---------------Dietals-----------------------------------------
        Dietals_Frame = Frame(self.root,bg='white')
        Dietals_Frame.place(x=1,y=82,width=1134,height=605)
        #---------------Scrolls-----------------------------------------
        scroll_x =Scrollbar(Dietals_Frame,orient= HORIZONTAL)
        scroll_y =Scrollbar(Dietals_Frame,orient= VERTICAL)
        #---------------treeveiw-----------------------------------------
        self.student_table = ttk.Treeview(Dietals_Frame,columns=('address','gender','certi','email','phone','name','id'),
       
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'
        self.student_table.heading('address',text='Student Address')
        self.student_table.heading('gender',text='Student Gender')
        self.student_table.heading('certi',text='Educational Level')
        self.student_table.heading('phone',text='Student Phone')
        self.student_table.heading('email',text='Student Email')
        self.student_table.heading('name',text='Student Name')
        self.student_table.heading('id',text='Student ID')

        self.student_table.column('address',width=125)
        self.student_table.column('gender',width=30)
        self.student_table.column('certi',width=65)
        self.student_table.column('phone',width=65)
        self.student_table.column('email',width=70)
        self.student_table.column('name',width=100)
        self.student_table.column('id',width=17)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

    #----------conection with database----------------------
        self.fetch_all()
    def add_student(self):
            con = pymysql.connect(host ='localhost', user='root', password='1234',database='stud1')
            cur = con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.address_var.get(),self.gender_var.get(),self.moahel_var.get(),self.email_var.get(),self.phone_var.get(),self.name_var.get(),self.id_var.get()))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()

    def fetch_all(self):
            con = pymysql.connect(host ='localhost', user='root', password='1234',database='stud1')
            cur = con.cursor()
            cur.execute('select * from student')
            rows = cur.fetchall()
            if len(rows) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)
                    con.commit()
                con.close()
        
    def delete(self):
            con = pymysql.connect(host ='localhost', user='root', password='1234',database='stud1')
            cur = con.cursor()
            cur.execute('delete from student where name=%s',self.dell_var.get())
            con.commit()
            self.fetch_all()
            con.close()
            
    def clear(self):
            self.id_var.set('')
            self.name_var.set('')
            self.email_var.set('')
            self.phone_var.set('')
            self.address_var.set('')
            self.moahel_var.set('')
            self.gender_var.set('')
            
    def get_cursor(self,ev):
            Cursor_row =self.student_table.focus()
            contents =self.student_table.item(Cursor_row)
            row = contents['values']
            self.id_var.set(row[6])
            self.name_var.set(row[5])
            self.phone_var.set(row[4])
            self.email_var.set(row[3])
            self.moahel_var.set(row[2])
            self.gender_var.set(row[1])
            self.address_var.set(row[0])
    def update(self):
            con = pymysql.connect(host ='localhost', user='root', password='1234',database='stud1')
            cur = con.cursor()
            cur.execute("update student set address=%s, gender=%s, moahel=%s, email=%s, phone=%s, name=%s where id=%s ",
            (self.address_var.get(),
            self.gender_var.get(),
            self.moahel_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.name_var.get(),
            self.id_var.get()))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
            
    def search(self):
            con = pymysql.connect(host ='localhost', user='root', password='1234',database='stud1')
            cur = con.cursor()
            cur.execute("select * from student where " + str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
            rows = cur.fetchall()
            if len(rows) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)
                    con.commit()
                con.close()



root = Tk()
ob = Student(root)
root.mainloop()

