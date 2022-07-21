from cProfile import label
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class QR_Generator:
    def _init_(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")  #600=width, 300=height,
        self.root.title("QR CODE GENERATOR")
        title=Label(self.root,text="QR CODE GENERATOR",font=("times new roman",20),bg='#550A35',fg='white').place(x=0,y=0,relwidth=1)

        #variables
        self.var_data=StringVar()
        self.var_title=StringVar()

        # input data
        data_Frame=Frame(self.root,bd=2,relief=RIDGE)
        data_Frame.place(x=50,y=80,width=400,height=380)
        data_title=Label(data_Frame,text="Input",font=("times new roman",20),bg='#7D0541',fg='white').place(x=0,y=0,relwidth=1)

        lbl_data=Label(data_Frame,text="Text or Link:",font=("times new roman",15,"bold"),bg='white').place(x=20,y=70)
        lbl_data=Label(data_Frame,text="Title:",font=("times new roman",15,"bold"),bg='white').place(x=20,y=160)

        entry_data=Entry(data_Frame,font=("times new roman",15),textvariable=self.var_data,bg='#FFF8DC').place(x=20,y=110)
        entry_data=Entry(data_Frame,font=("times new roman",15),textvariable=self.var_title,bg='#FFF8DC').place(x=20,y=200)

        btn_generate=Button(data_Frame,text="Generate",command=self.generate,font=("times new roman",18,'bold'),bg="#7E354D",fg="white").place(x=70,y=260,width=100,height=30)
        btn_generate=Button(data_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg="#7E354D",fg="white").place(x=210,y=260,width=100,height=30)

        self.msg=''
        self.lbl_msg=Label(data_Frame,text=self.msg,font=("times new roman",15),fg='green')
        self.lbl_msg.place(x=60,y=310)

        # QR code
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE)
        qr_Frame.place(x=480,y=80,width=380,height=380)
        qr_title=Label(qr_Frame,text="QR Code",font=("times new roman",20),bg='#7D0541',fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="No QR \nAvailable",font=("times new roman",18,'bold'),bg="#7E354D",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=95,y=100,width=180,height=180)

    def clear(self):
        self.var_data.set('')
        self.var_title.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_data.get()=='' or self.var_title.get()=='':
            self.msg='All Fields are required!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"link or text: {self.var_data.get()}\nTitle:{self.var_title.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR_"+str(self.var_title.get())+'.png')
            #qr image update
            self.im=ImageTk.PhotoImage(file="QR_"+str(self.var_title.get())+'.png')
            self.qr_code.config(image=self.im)
            #messege update
            self.msg='QR Generated successfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')

    
root=Tk()
obj=QR_Generator(root)
root.mainloop()
