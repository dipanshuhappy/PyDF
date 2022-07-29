
from tkinter import Button, Entry, Label
from pages.Page import Page
from utils import Utils
from pdf_utils import  add_text_watermark
class AddWaterMarkPage(Page):
    def __init__(self,app)->None:
        super().__init__(app)
    def show_page(self)->None:
        self.make_widgets()
        self.pack(expand=True)
    def make_widgets(self)->None:
        Label(self, text="Enter A Text Watermark").pack()
        self.watermark_text_entry: Entry = Entry(self, width=10)
        self.watermark_text_entry.pack()
        Button(self, text="Open PDf", command=self.get_PDF).pack(anchor='center')
        Button(self, text="Get saving file path",command=self.get_saving_file_path).pack()
        Button(self, text="Add WaterMark", command=self.add_watermark).pack(anchor='center')
    def add_watermark(self)->None:
        print(self.watermark_text_entry.get())
        add_text_watermark(
            self.pdf_filename,
            self.saving_file_path,
            self.watermark_text_entry.get()
        )
    def get_saving_file_path(self)->None:
        self.saving_file_path = Utils.get_saving_file_path();

    def get_PDF(self)->None:
        self.pdf_filename=Utils.getPDf();
        
