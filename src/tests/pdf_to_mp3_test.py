from src.pdf_to_mp3 import read_pdf, convert_text_to_mp3
import os


def test_read_pdf():
    test_pdf = 'src/tests/test_resources/Sample_test.pdf'
    text = read_pdf(test_pdf)
    assert text == "This is a sample file  "

def test_convert_text_to_mp3():
    test_output_file = "src/tests/test_resources/output_test.mp3"
    text = "Hello, world!"
    convert_text_to_mp3(text,test_output_file)
    assert os.path.exists(test_output_file)
