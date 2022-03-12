
from tkinter import Label
from utils import Page
class FrontPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
        
    def show_page(self) -> None:
        self.place(x=200,y=200)
        self.tkraise()
    def make_widgets(self) -> None:
        self.label=Label(self.app,text="Hi this is a skdlfj jflksdjljd kdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk page")
        self.label.place(x=200,y=200)