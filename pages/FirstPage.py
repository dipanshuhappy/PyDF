
from tkinter import Label
import tkinter

from pyparsing import col
from utils import Page
class FrontPage(tkinter.Frame):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        self.grid(column=0,row=0,sticky='nsew')
        # self.tkraise()
    def make_widgets(self) -> None:
        self.label=Label(self,bg='red',text="Hi this is a skdlfj jflksdjljd kdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk page")
        self.label.pack()