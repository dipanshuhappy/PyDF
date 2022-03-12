from tkinter import Button, Label
from pages.Page import Page
class MainPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        # self.columnconfigure(0, weight=0)
        # self.rowconfigure(0, weight=0)
        self.pack(expand=True)
    def make_widgets(self) -> None:
        Button(self,text="Main Page").pack(anchor='center')