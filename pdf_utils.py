import os
import time
from pikepdf import Encryption, Name, Object, Page, Pdf, Rectangle, Stream
import img2pdf


def get_saving_pdf_name(path: str, saving_path: str): return os.path.join(
    saving_path, os.path.basename(path)+".pdf")


def add_watermark(path: str, saving_path: str):
    pdf = Pdf.open(path)
    water_mark = make_pdf_from_string(
        "Hello this is water mark i want you too add ")
    print(repr(water_mark.trimbox))
    print(repr(water_mark.as_form_xobject(False)))
    print("--------------PDF--------------------------DocINfo---------------------------", repr(pdf.docinfo))
    x, y = (0, 0)
    destination_corrdinate = Rectangle(x, y, x+100, y+100)
    print("This is the Array ", repr(destination_corrdinate.as_array()))
    print(
        f"This is the height {destination_corrdinate.height} and width {destination_corrdinate.width} ")
    for page in pdf.pages:
        page.add_underlay(water_mark, destination_corrdinate)
    pdf.save(saving_path)
    pdf.close()


def add_watermaker_image(path: str, image_path: str, saving_path: str):
    pdf = Pdf.open(path)
    water_mark = make_pdf_from_image(image_path,"test//image.png")
    print(repr(water_mark.trimbox))
    print(repr(water_mark.as_form_xobject(False)))
    print("--------------PDF--------------------------DocINfo---------------------------", repr(pdf.docinfo))
    x, y = (0, 0)
    destination_corrdinate = Rectangle(x, y, x+100, y+100)
    print("This is the Array ", repr(destination_corrdinate.as_array()))
    print(
        f"This is the height {destination_corrdinate.height} and width {destination_corrdinate.width} ")
    for page in pdf.pages:
        page.add_underlay(water_mark, destination_corrdinate)
    pdf.save(saving_path)
    pdf.close()


def make_pdf_from_image(path: str, image_path: str) -> Page:

    with open(path, "wb") as f:
        f.write(
            img2pdf.convert(
                image_path
            )
        )
    temp_pdf=Pdf.open(path)
    return temp_pdf.pages[0]


def get_metadata(path): return repr(Pdf.open(path).docinfo)


def put_password(password: str, path: str, saving_path: str, return_time=False) -> str | None:
    start = time.process_time()
    pdf = Pdf.open(path)
    R = 6
    pdf.save(get_saving_pdf_name(path, saving_path),
             encryption=Encryption(owner=password, user=password, R=R))
    pdf.close()
    if return_time:
        return f'time taken for  {len(pdf.pages)} pages is {time.process_time()-start} with R {R} '
    print(
        f'time for pikepdf of {len(pdf.pages)} pages is {time.process_time()-start} with R {R} ')


def reverse_pdf(path: str, new_path: str):
    start = time.process_time()
    with Pdf.open(path) as pdf:
        pdf.pages.reverse()
        pdf.save(get_saving_pdf_name(path, new_path))
    print(
        f'time taken of {len(pdf.pages)} pages is {time.process_time()-start} when reversing ')


def make_pdf_from_string(string: str) -> Page:
    pdf = Pdf.new()
    rfont = {'/F1': pdf.make_indirect(
        Object.parse(
            """
            <<
                /Type /Font
                /Subtype /Type1
                /Name /F1
                /BaseFont /Helvetica
                /Encoding /UTF-8
            >>"""
        )
    )}
    encoded_string = string.encode()
    stream = b"""
        /F1 24 Tf 72 720 Td ("""+encoded_string+b""") Tj ET
        q 144 0 0 144 234 324 cm
        """
    contents = Stream(pdf, stream)
    page_dict = {
        '/Type': Name('/Page'),
        '/MediaBox': [0, 0, 612, 792],
        '/Contents': contents,
        '/Resources': {'/Font': rfont},
    }
    page = pdf.make_indirect(page_dict)
    pdf.pages.append(page)
    pdf.save("test//123.pdf")
    pdf.close()
    P = Pdf.open("test//123.pdf")
    return P.pages[0]

 
def merge_two_pdfs(first_pdf_path: str, second_pdf_path: str, saving_path: str):
    start = time.process_time()
    first_pdf = Pdf.open(first_pdf_path)
    second_pdf = Pdf.open(second_pdf_path)
    with Pdf.new() as pdf:
        pdf.pages.extend(first_pdf.pages)
        pdf.pages.extend(second_pdf.pages)
        pdf.save(saving_path)
    first_pdf.close()
    second_pdf.close()
    print(
        f'time taken of merging {len(first_pdf.pages)} pages  and {len(second_pdf.pages)} page is {time.process_time()-start} when merging'
    )


if __name__ == "__main__":
    # add_watermark("test//test.pdf", "test//new_test.pdf")
    add_watermaker_image("test//test.pdf","test//simple_page.pdf","test//test2.pdf")
