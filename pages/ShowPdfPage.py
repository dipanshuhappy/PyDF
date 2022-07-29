import imp
from tkinter import Button
from pages.Page import Page
from tkPDFViewer import tkPDFViewer

class ShowPdfPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made = False
    def show_page(self) -> None:
        self.make_widgets()
        self.pack(expand=True)

    def make_widgets(self) -> None:
        pdf=tkPDFViewer.ShowPdf();
        pdf.pdf_view(
            self,
            pdf_location = "test//test.pdf", 
            width = 50, height = 100,
            load="after"
        )
        pdf.frame.pack()
 