from pikepdf import Pdf,Object,Stream,Name
import img2pdf
from pages.Page import Page
def test_create_pdf(outdir):
    pdf = Pdf.new()

    font = pdf.make_indirect(
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
    )

    width, height = 900, 900
    image_data = b"\xff\xff\x00" * (width * height)
    image = Stream(pdf, image_data)
    image.stream_dict = Object.parse(
        b"""
            <<
                /Type /XObject
                /Subtype /Image
                /ColorSpace /DeviceRGB
                /BitsPerComponent 8
                /Width 600
                /Height 600
            >>"""
    )

    rfont = {'/F1': font}

    xobj = {'/Im1': image}

    resources = {'/Font': rfont, '/XObject': xobj}

    mediabox = [0, 0, 612, 792]

    stream =b"""
        q 144 0 0 144 234 324 cm /Im1 Do Q
        """
    contents = Stream(pdf, stream)

    page_dict = {
        '/Type': Name('/Page'),
        '/MediaBox': mediabox,
        '/Contents': contents,
        '/Resources': resources,
    }
    qpdf_page_dict = page_dict
    page = pdf.make_indirect(qpdf_page_dict)
    pdf.pages.append(page)
    pdf.save(f"{outdir}//hi.pdf")
# def make_image_pdf(outdir):
#     pdf = Pdf.new()

#     font = pdf.make_indirect(
#         Object.parse(
#             """
#             <<
#                 /Type /Font
#                 /Subtype /Type1
#                 /Name /F1
#                 /BaseFont /Helvetica
#                 /Encoding /UTF-8
#             >>"""
#         )
#     )

#     width, height = 900, 900
#     with open("test//image.png", "rb") as image:
#         image_data = image.read1()
#     image = Stream(pdf, image_data)
#     print(image.read_bytes())
#     image.stream_dict = Object.parse(
#         b"""
#             <<
#                 /Type /XObject
#                 /Subtype /Image
#                 /ColorSpace /DeviceRGB
#                 /BitsPerComponent 8
#                 /Width 600
#                 /Height 600
#             >>"""
#     )

#     rfont = {'/F1': font}

#     xobj = {'/Im1': image}
    
#     resources = {'/Font': rfont, '/XObject': xobj}

#     mediabox = [0, 0, 612, 792]

#     stream =b"""
#         q 144 0 0 144 234 324 cm /Im1 Do Q
#         """
#     contents = Stream(pdf, stream)

#     page_dict = {
#         '/Type': Name('/Page'),
#         '/MediaBox': mediabox,
#         '/Contents': contents,
#         '/Resources': resources,
#     }
#     qpdf_page_dict = page_dict
#     page = pdf.make_indirect(qpdf_page_dict)

#     pdf.pages.append(page)
#     pdf.save(f"{outdir}//imagePDF.pdf")
def make_image_pdf(source_pdf:str):
    with open(source_pdf,"wb") as f :
	    f.write(
            img2pdf.convert(
                "test//image.png"
            )
        )
    
def make_an_empyt_pdf(name:str):
    # open("test//empty.pdf","w")
    dst=Pdf.new();
    dst.save(f"test//{name}.pdf")
# make_an_empyt_pdf("emp")
# make_image_pdf("test//simple_page.pdf")
import logging
 
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')