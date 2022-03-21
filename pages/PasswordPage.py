import os
from tkinter import Button, Entry, Label, filedialog, Text, END
from pages.Page import Page
from pdf_utils import  put_password
class PasswordPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False

    def show_page(self) -> None:
        self.make_widgets()
        self.pack(expand=True)
    def make_widgets(self) -> None:
        Label(self,text="Select A PDf and put password ").pack()
        Button(self,text="Open PDf",command=self.getPDf).pack(anchor='center')
        self.filename_label:Label=Label(self)
        self.password:Entry=Entry(self,width=10,show="*")
        self.password.pack()
        Label(self,text="Put password").pack()
        Button(self,text="Finish",command=self.encrypt).pack(anchor='center')
        self.time_text= Text(self,width = 20,height =2)
        self.time_text.pack()
    def encrypt(self):
        time=put_password(self.password.get(),self.filename,"test//test.pdf",return_time=True)
        self.time_text.insert(END,str(time))
    def getPDf(self):
        filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
        )
        self.filename=filedialog.askopenfilename(filetypes=filetypes)
        self.filename_label.config(text=os.path.basename(self.filename))
        self.filename_label.pack()
        print(self.filename)