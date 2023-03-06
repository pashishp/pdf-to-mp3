import sys

import pypdf
import pyttsx3  # type: ignore

pdf_file = "Sample.pdf"


def read_pdf(pdf_file: str):
    pdf_file_to_convert = open(pdf_file, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file_to_convert)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    pdf_file_to_convert.close()
    return text


def convert_text_to_mp3(text, output_file):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.save_to_file(text, output_file)
    engine.runAndWait()


try:
    text = read_pdf(sys.argv[1])
    convert_text_to_mp3(text, "sound_output.mp3")
except Exception as error:
    print("Error occurred: ", str(error))
