import enum
import time

from pikepdf import Pdf

def put_password(password:str,path:str):
    start=time.process_time()
    pdf = pikepdf.Pdf.open(path)  
    R=6
    pdf.save('test//test_output.pdf', encryption=pikepdf.Encryption(owner=password, user=password, R=R)) 
    pdf.close()
    print(f'time for pikepdf of {len(pdf.pages)} pages is {time.process_time()-start} with R {R} ')
def reverse_pdf(path:str,new_path:str):
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
# pdf= Pdf.new();
# with Pdf.open('test//test.pdf') as file:
#     # print(len(file.pages))
#     # print(file)
#     # print(file.pages[0])
#     # page1=file.pages[0]
#     # print(page1.Type)
#     # print(repr(file.Root.get("/AcroForm")))
#     # del file.pages[0:-30]
#     # file.save("test//test_output.pdf")
#     # for index,page in enumerate(file.pages):
#     #     single_pdf=Pdf.new()
#     #     single_pdf.pages.append(page)
#     #     single_pdf.save(f"test//{index}.pdf")
#     file.pages.reverse()
#     file.save("test//test_output.pdf")
# reverse_pdf('test//test.pdf','test//test_output.pdf')
merge_two_pdfs("test//test.pdf","test//test.pdf","test//test_output.pdf")