import os
from tkinter import Button, Entry, Label
from components.ButtonGroup import ButtonGroup
from components.RoundButton import RoundButton
from pages.Page import Page
from pdf_utils import reverse_pdf
from utils import Utils
class ReversePage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        self.pack(expand=True)
    def make_widgets(self) -> None:
        Label(self,text="Select A PDf  ").pack()
        Button(self,text="Open PDf",command=self.getPDf).pack(anchor='center')
        self.filename_label:Label=Label(self)
        Button(self,text="Get saving file path",command=self.get_saving_file_path).pack()
        Button(self,text="Finish",command=self.reverse).pack(anchor='center')
        self.time_text= Label(self,width = 20,height =2)
        self.saving_path_text=Label(self)
        self.saving_path_text.pack()
        self.time_text.pack()
    def reverse(self):
        reverse_pdf(self.filename,self.save_file)
        self.time_text.config(text="Done!")
    def getPDf(self):
        self.filename=Utils.getPDf()
        self.filename_label.config(text=os.path.basename(self.filename))
        self.filename_label.pack()
        print(self.filename)
    def get_saving_file_path(self):
        self.save_file=Utils.get_saving_file_path()
        self.saving_path_text.config(text=os.path.basename(self.save_file))