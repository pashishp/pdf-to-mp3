import pypdf
import pyttsx3
import os

output_file = "output.mp3"
pdf_file = "Sample.pdf"


def read_pdf(pdf_file: str):
    pdf_file = open(pdf_file, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    pdf_file.close()
    return text


def convert_text_to_mp3(text, output_file):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')[3]
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate',120)
    engine.say(text)
    output_dir = "/home/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_file)
    print(output_path)
    engine.save_to_file(text, output_path)
    engine.runAndWait()

if __name__ == '__main__':
    try:
        text = read_pdf(pdf_file)
        convert_text_to_mp3(text, output_file)
    except Exception as error:
        print("Error occurred: ", str(error))
