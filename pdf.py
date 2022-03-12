from importlib.resources import path
from pikepdf import Pdf
class PDF:
    def __init__(self,path:str,has_password=False,password="")->None:
        self.path:str=path
        self.has_password=has_password
        self.pdf:Pdf=self.__get_pdf()
    def __get_pdf(self)->Pdf:
        return Pdf.open(self.path,self.password)  if (self.has_password) else Pdf.open(self.path)