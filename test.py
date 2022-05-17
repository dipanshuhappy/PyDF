from pikepdf import Pdf,Object,Stream,Name
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
        /F1 24 Tf 72 720 Td (lsdjflsldfsldfjsldflsdfsdljslll) Tj ET
        q 
        """
    # stream = b"""
    #     (Hi there ghhjhgjhgh) 
    #     """
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
test_create_pdf("test")
p=Pdf.open("test//hi.pdf")
print(p.pages[0])