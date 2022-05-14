import os
import time
from pikepdf import Object, Page, Pdf, Rectangle
import pikepdf
def get_saving_pdf_name(path:str,saving_path:str):   return os.path.join(saving_path,os.path.basename(path)+".pdf")
def add_watermark(path:str,saving_path:str):
    pdf=Pdf.open(path)
    destination_page=Page(pdf.pages[1])
    c=Object.parse("kllkjlk")
    text=Page(c)
    destination_page.add_overlay(pdf.pages[0],Rectangle(100,100,200,200))
    pdf.save(saving_path)
    pdf.close()
def get_metadata(path):
    pdf=Pdf.open(path)
    a=pdf.docinfo
    return repr(a)
def put_password(password:str,path:str,saving_path:str,return_time=False)  -> str | None:
    start=time.process_time()
    pdf = pikepdf.Pdf.open(path)  
    R=6
    pdf.save(get_saving_pdf_name(path,saving_path), encryption=pikepdf.Encryption(owner=password, user=password, R=R)) 
    pdf.close()
    if return_time:  return f'time taken for  {len(pdf.pages)} pages is {time.process_time()-start} with R {R} '
    print(f'time for pikepdf of {len(pdf.pages)} pages is {time.process_time()-start} with R {R} ')
def reverse_pdf(path:str,new_path:str):
    start=time.process_time()
    with Pdf.open(path) as pdf:
        pdf.pages.reverse()
        pdf.save(get_saving_pdf_name(path,new_path))
    print(f'time taken of {len(pdf.pages)} pages is {time.process_time()-start} when reversing ')
def merge_two_pdfs(first_pdf_path:str,second_pdf_path:str,saving_path:str):
    start=time.process_time()
    first_pdf=Pdf.open(first_pdf_path)
    second_pdf=Pdf.open(second_pdf_path)
    with Pdf.new() as pdf:
        pdf.pages.extend(first_pdf.pages)
        pdf.pages.extend(second_pdf.pages)
        pdf.save(saving_path)
    first_pdf.close()
    second_pdf.close()
    print(f'time taken of merging {len(first_pdf.pages)} pages  and {len(second_pdf.pages)} page is {time.process_time()-start} when merging')
if __name__=="__main__":
    add_watermark("test//test.pdf","test//new_test.pdf")
