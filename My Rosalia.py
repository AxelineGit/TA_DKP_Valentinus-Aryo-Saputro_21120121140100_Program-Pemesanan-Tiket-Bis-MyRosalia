from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as msg
from tkinter import ttk
import datetime as dt

from setuptools import Command

#Membuat sebuah class yang berisi method
class Loginregisteruser:
    def main_screen(self):
        Button(text='Login',bg= "White",fg='Black',height= '2',width= '30',command = self.login).place(x=400, y=639/2)
    #inisialisasi OOP
    def __init__(self,gui,header):
        self.gui = gui
        self.gui.geometry('960x639')
        self.gui.title(header)
        self.gui.resizable(0,0)
        self.main_screen()
    #Menu untuk login
    def login(self):
        screen1 = Toplevel(app)
        screen1.title("Login My Rosalia")
        screen1.geometry('350x160')
        screen1.resizable(0,0)
        Label(screen1, text= "Email").pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text = "Password").pack()
        self.entryPass = Entry(screen1,show='*',width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text = "Show Password", variable=self.check,command=self.view_password).pack(expand=False,fill=BOTH,padx=10,pady=5)
        self.showPass
        self.btnlogin = Button(screen1, text="Login", bg= 'white',fg='black',command=self.do_login).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)
    #Untuk mengecek input yang dimasukan, apakah sudah sesuai dengan file data.txt
    def do_login(self):
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open('data.txt','r')
        
        for i in file :
            name,email,password = i.split(",")
            password = password.strip()
            if get_username == email and get_password == password:
                sukses = True
                break
        if (sukses):
            msg.showinfo("Login Success","Login Berhasil %s"%(name),parent=self.gui)
            self.sec_screen()
            return 
        elif get_username == '' or get_password == '':
            msg.showwarning("Login Gagal","Email atau Password Tidak Boleh Kosong",parent=self.gui)
            self.entryUser.focus_set()
        else :
            msg.showerror('Login Gagal','Email atau Password Salah',parent=self.gui)
            self.delete_data()

    #Method untuk membuat password bisa dilihat isinya atau dalam bentuk bintang
    def view_password(self):
        Show = self.check.get()      
        if Show == 1:
            self.entryPass['show']=''
        else :
            self.entryPass['show']='*'

    #Menampilkan menu untuk pesan tiket bis
    def sec_screen(self):
        global screen2
        screen2 = Toplevel(app)
        screen2.title("My Rosalia")
        screen2.geometry('430x450')
        screen2.resizable(0,0)
        #Header untuk menu pesan tiket
        Label(screen2,text="BOOKING TIKET" ,bg='Yellow',width='300',height='2',font= ('English111',13, "bold"),fg='Red').pack()
        Label(screen2,text='').pack()
        Label(screen2,text= "Nama\t\t:",).place(x=30, y=53)
        self.entryID = Entry(screen2, font = ("times new roman", 10))
        self.entryID.place(x=140, y=57)
        #Tombol untuk Pemesanan Nomor Kursi
        self.kursi = StringVar('')
        Label(screen2, text = "Nomor Kursi\t:").place(x=30, y=80)
        self.combobox1 = ttk.Combobox(screen2,width = 18,font = ("times new roman", 10), textvariable = self.kursi, state ="readonly")
        self.combobox1.place(x=140, y=80)
        self.combobox1['values'] = ('1','2','3','4','5','6','7','8','9')
        self.posisi = IntVar()
        Label(screen2, text = "Posisi\t\t:").place(x=30, y=105)
        self.entryposisi1 = Radiobutton(screen2, text = 'A', variable=self.posisi,value =1,command=self.posisi)
        self.entryposisi1.place(x = 140, y = 105)
        self.entryposisi2 = Radiobutton(screen2, text = 'B', variable=self.posisi,value =2,command=self.posisi)
        self.entryposisi2.place(x = 140, y = 125)
        self.entryposisi3 = Radiobutton(screen2, text = 'C', variable=self.posisi,value =3,command=self.posisi)
        self.entryposisi3.place(x = 140, y = 145)
        self.entryposisi4 = Radiobutton(screen2, text = 'D', variable=self.posisi,value =4,command=self.posisi)
        self.entryposisi4.place(x = 140, y = 165)
        #Tombol untuk memilih rute perjalanan
        self.rute = StringVar(value="...")
        Label(screen2, text = "Rute\t\t:").place(x=30, y=185)
        self.combobox1 = ttk.Combobox(screen2,width = 17,font = ("times new roman", 10), textvariable = self.rute, state ="readonly")
        self.combobox1.place(x=140, y=185)
        self.combobox1['values'] = ('Tangerang-Solo','Jakarta-Surabaya','Jakarta-Jogja','Jakarta-Madiun','Tangerang-Klaten')
        #Tombol untuk mengecek rute dan menentukan kelas serta harga bis
        self.btncek=Button(screen2,text="Cek",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.kelastiket,state = ACTIVE)
        self.btncek.place(x = 270, y = 175)
        #Tombol untuk memilih metode pembayaran
        Label(screen2, text = "Pembayaran\t\t:").place(x=30, y=280)
        self.payment = StringVar(value='...')
        self.combobox2 = ttk.Combobox(screen2,width = 18,font = ("times new roman",10),textvariable=self.payment,state="readonly")
        self.combobox2.place(x=140,y=280)
        self.combobox2['values']=('Mandiri','BCA','BNI','ShopeePay')
        #Tombol untuk bayar agar bisa memasukan nomor rekening atau Virtual Account(ShopeePay)
        self.btncek2=Button(screen2,text="Bayar",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.bayar,state = ACTIVE)
        self.btncek2.place(x = 280, y = 270)
        #Tombol untuk melakukan booking tiket
        self.btnsub = Button(screen2, text="Checkout",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.btn_sub,state = ACTIVE)
        self.btnsub.place(x = 320, y = 380)

    #Method untuk Menentukan Kelas dari Bis dah Harganya
    def kelastiket(self):
        pilih = self.rute.get()
        if pilih == 'Tangerang-Solo' :
            self.kelas = IntVar()
            Label(screen2, text = "Kelas\t\t:").place(x=30, y=215)
            self.entrykelas1 = Radiobutton(screen2, text = "Super TOP (Rp 320.000,-)", variable=self.kelas,value =320000,command=self.kelas1)
            self.entrykelas1.place(x = 140, y = 215)
            self.entrykelas2 = Radiobutton(screen2, text = "Executive (Rp 275.000,-)", variable=self.kelas,value =275000,command=self.kelas2)
            self.entrykelas2.place(x = 140, y = 235)
            self.entrykelas3 = Radiobutton(screen2, text = "Patas (Rp 230.000,-)", variable=self.kelas,value =230000,command=self.kelas3)
            self.entrykelas3.place(x = 140, y = 255)
        elif pilih == 'Jakarta-Surabaya' :
            self.kelas = IntVar()
            Label(screen2, text = "Kelas\t\t:").place(x=30, y=215)
            self.entrykelas1 = Radiobutton(screen2, text = "Super TOP (Rp 525.000,-)", variable=self.kelas,value =525000,command=self.kelas1)
            self.entrykelas1.place(x = 140, y = 215)
            self.entrykelas2 = Radiobutton(screen2, text = "Executive (Rp 440.000,-)", variable=self.kelas,value =440000,command=self.kelas2)
            self.entrykelas2.place(x = 140, y = 235)
            self.entrykelas3 = Radiobutton(screen2, text = "Patas (Rp 395.000,-)", variable=self.kelas,value =395000,command=self.kelas3)
            self.entrykelas3.place(x = 140, y = 255)
        elif pilih == 'Jakarta-Jogja' :
            self.kelas = IntVar()
            Label(screen2, text = "Kelas\t\t:").place(x=30, y=215)
            self.entrykelas1 = Radiobutton(screen2, text = "Super TOP (Rp 325.000,-)", variable=self.kelas,value =325000,command=self.kelas1)
            self.entrykelas1.place(x = 140, y = 215)
            self.entrykelas2 = Radiobutton(screen2, text = "Executive (Rp 230.000,-)", variable=self.kelas,value =230000,command=self.kelas2)
            self.entrykelas2.place(x = 140, y = 235)
            self.entrykelas3 = Radiobutton(screen2, text = "Patas (Rp 210.000,-)", variable=self.kelas,value =210000,command=self.kelas3)
            self.entrykelas3.place(x = 140, y = 255)
        elif pilih == 'Jakarta-Madiun' :
            self.kelas = IntVar()
            Label(screen2, text = "Kelas\t\t:").place(x=30, y=215)
            self.entrykelas1 = Radiobutton(screen2, text = "Super TOP (Rp 355.000,-)", variable=self.kelas,value =355000,command=self.kelas1)
            self.entrykelas1.place(x = 140, y = 215)
            self.entrykelas2 = Radiobutton(screen2, text = "Executive (Rp 310.000,-)", variable=self.kelas,value =310000,command=self.kelas2)
            self.entrykelas2.place(x = 140, y = 235)
            self.entrykelas3 = Radiobutton(screen2, text = "Patas (Rp 250.000,-)", variable=self.kelas,value =250000,command=self.kelas3)
            self.entrykelas3.place(x = 140, y = 255)
        elif pilih == 'Jakarta-Klaten' :
            self.kelas = IntVar()
            Label(screen2, text = "Kelas\t\t:").place(x=30, y=215)
            self.entrykelas1 = Radiobutton(screen2, text = "Super TOP (Rp 280.000,-)", variable=self.kelas,value =280000,command=self.kelas1)
            self.entrykelas1.place(x = 140, y = 215)
            self.entrykelas2 = Radiobutton(screen2, text = "Executive (Rp 230.000,-)", variable=self.kelas,value =230000,command=self.kelas2)
            self.entrykelas2.place(x = 140, y = 235)
            self.entrykelas3 = Radiobutton(screen2, text = "Patas (Rp 200.000,-)", variable=self.kelas,value =200000,command=self.kelas3)
            self.entrykelas3.place(x = 140, y = 255)

    #Method untuk pemilihan metode pembayaran
    def bayar(self):
        byr=self.payment.get()
        if byr == 'Mandiri':
            Label(screen2, text='No Rekening\t\t:').place(x=30,y=300)
            self.masukan = Entry(screen2, font = ("times new roman", 10))
            self.masukan.place(x=140, y= 310)
        elif byr == 'BCA':
            Label(screen2, text='No Rekening\t\t:').place(x=30,y=310)
            self.masukan = Entry(screen2, font = ("times new roman", 10))
            self.masukan.place(x=140, y= 310)
        elif byr == 'BRI':
            Label(screen2, text='No Rekening\t\t:').place(x=30,y=310)
            self.masukan = Entry(screen2, font = ("times new roman", 10))
            self.masukan.place(x=140, y= 310)
        elif byr == 'BNI':
            Label(screen2, text='No Rekening\t\t:').place(x=30,y=310)
            self.masukan = Entry(screen2, font = ("times new roman", 10))
            self.masukan.place(x=140, y= 310)
        elif byr == 'ShopeePay':
            Label(screen2, text='Virtual Accoutn\t:').place(x=30,y=310)
            self.masukan = Entry(screen2, font = ("times new roman", 10))
            self.masukan.place(x=140, y= 310)

    #Method untuk mengambil data inputan dari user , dan menampilkannya berupa pop up Info Booking Tiket
    def btn_sub(self):
        name = self.entryID.get()
        kursi = self.kursi.get()
        posisi = self.posisi.get()
        payment=self.payment.get()
        if posisi==1: #Pengkondisian untuk mengubah nilai posisi dari integer 1-4 menjadi string A-D
            posisi='A'
        elif posisi==2:
            posisi='B'
        elif posisi==3:
            posisi='C'
        elif posisi==4:
            posisi='D'
        rute = self.rute.get()
        date = dt.datetime.now()
        if name == "" :
            msg.showwarning("Peringatan","Nama Tidak Boleh Kosong!",parent=self.gui)
            return
        if kursi == '':
            msg.showwarning("Peringatan","Harap Pilih Kursi!",parent=self.gui)
            return
        if rute == '...':
            msg.showwarning("Peringatan","Harap Pilih Rute!",parent=self.gui)
            return
        if payment == '...':
            msg.showwarning("Peringatan","Harap Pilih Metode Pembayaran!",parent=self.gui)
            return
        else :
            msg.showinfo("Info Booking Tiket",f"Nama\t\t\t: {self.entryID.get()} \nKursi\t\t\t: {kursi}-{posisi} \nRute\t\t\t: {rute}\nKelas\t\t\t: {self.tingkat} \nTotal Harga\t\t: Rp.{self.kelas.get()},-\nMetode Pembayaran\t: {self.payment.get()}\nTanggal Pemesanan\t: {date:%A, %B %d, %Y} \nStatus Pemesanan\t\t: Sukses!" )
            self.close_gui()

    def kelas1(self):
        self.tingkat="Super TOP"

    def kelas2(self):
        self.tingkat="Executive"
    
    def kelas3(self):
        self.tingkat="Patas"

    def delete_data(self):
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryUser.focus_set()
    
    def delete_uname(self): 
        self.entryPass.focus_set()
        self.entryUser.focus_set()
        self.entryUserName.delete(0,END)
        self.entryUserName.focus_set()
    
    def delete_email(self):
        self.entryUser.delete(0,END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryUser.focus_set()

    def delete_pass(self):
        self.entryPass.delete(0,END)
        self.entryUserName.focus_set()
        self.entryUser.focus_set()
        self.entryPass.focus_set()
        
    def close_gui(self):
        self.gui.destroy()

#Main menu agar GUI dapat berjalan
if __name__ == '__main__':
    global app
    app = Tk()
    logo = PhotoImage(file="logo.png")
    app.iconphoto(True,logo)
    label = Label(app)
    bg = PhotoImage(file="ros1.png")
    a_label = Label(app, image=bg)
    a_label.place(x=0, y=0, relheight=1, relwidth=1)
    start = Loginregisteruser(app,"Rosalia Indah")
    app.mainloop()