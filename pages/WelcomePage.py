
from tkinter import Button, Label
from components.ButtonGroup import ButtonGroup
from components.RoundButton import RoundButton
from pages.Page import Page
class WelcomePage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        # self.columnconfigure(0, weight=0)
        # self.rowconfigure(0, weight=0)
        self.pack(expand=True)
    def make_widgets(self) -> None:
        Button(self,text="Enter",command=lambda:self.goto_mainPage()).pack(anchor='center')
        RoundButton(self,200,30,'hi',lambda :print('kjld')).show_button()
    def goto_mainPage(self):
        self.app.frame_manager.show_frame("MainPage")
        