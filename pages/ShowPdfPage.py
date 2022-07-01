import imp
from tkinter import Button
from pages.Page import Page
from tkPDFViewer import tkPDFViewer

class ShowPdfPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made = False
    # def show_page(self) -> None:
    #     self.make_widgets()
    #     self.pack(expand=True)
    # def make_widgets(self) -> None:
    #     Button(self,text="Enter",command=lambda:self.goto_mainPage()).pack(anchor='center')
    #     Button(self, text="info 💭", command=lambda:self.goto_inforpage()).pack()
    # def goto_mainPage(self):
    #     self.app.frame_manager.show_frame("MainPage")
    # def goto_inforpage(self):
    #     self.app.frame_manager.show_frame("InfoPage")


    def show_page(self) -> None:
        self.make_widgets()
        self.pack(expand=True)

    def make_widgets(self) -> None:
        pdf=tkPDFViewer.ShowPdf();
        pdf.pdf_view(
            self.app,
            pdf_location = "test//simple_page.pdf", 
            width = 50, height = 100
        ).pack()
