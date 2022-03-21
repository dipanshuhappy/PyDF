import time
from pikepdf import Pdf
import pikepdf
def put_password(password:str,path:str,saving_path:str,return_time=False)  -> str | None:
    start=time.process_time()
    pdf = pikepdf.Pdf.open(path)  
    R=6
    pdf.save(saving_path, encryption=pikepdf.Encryption(owner=password, user=password, R=R)) 
    pdf.close()
    if return_time:  return f'time taken for  {len(pdf.pages)} pages is {time.process_time()-start} with R {R} '
    print(f'time for pikepdf of {len(pdf.pages)} pages is {time.process_time()-start} with R {R} ')
def reverse_pdf(path:str,new_path:str,path_to_be_saved:str):
    start=time.process_time()
    with Pdf.open(path) as pdf:
        pdf.pages.reverse()
        pdf.save(new_path)
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
