import PyPDF2


def create_pdf_with_js(output_filename):
    # Create a PDF writer object
    output = PyPDF2.PdfWriter()

    output.add_blank_page(612.0, 792.0)

    # Add JavaScript to the PDF
    output.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

    # Write the PDF content to a file
    with open(output_filename, "wb") as f:
        output.write(f)
