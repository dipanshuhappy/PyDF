import time
def pikepdf(password:str,path:):
    start=time.process_time()
    import pikepdf
    pdf = pikepdf.Pdf.open("test//test.pdf")   
    pdf() 
    print(pdf)
    R=6
    pdf.save('test//test_output.pdf', encryption=pikepdf.Encryption(owner='password', user='password', R=R)) 
    pdf.close()
    print(f'time for pikepdf of 664 pages is {time.process_time()-start} with R {R} ')

