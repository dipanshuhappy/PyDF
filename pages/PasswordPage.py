from tkinter import Button, Entry, Label, filedialog
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
        self.password=Entry(self,width=10)
        self.password.pack()
        Label(self,text="Put password").pack()
        Button(self,text="Finish",command=self.encrypt).pack(anchor='center')
    def encrypt(self):
        put_password(self.password.get(),self.filename)
    def getPDf(self):
        filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
        )
        self.filename=filedialog.askopenfilename(filetypes=filetypes)
        print(self.filename)