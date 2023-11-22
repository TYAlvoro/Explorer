from PyPDF2 import PdfFileReader
import pyttsx3


def read_page(num, name):
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices") 
    speaker.setProperty("voice", voices[2].id)
    speaker.setProperty("rate", 165) 

    with open(name, "rb") as filehandle:  
        pdf = PdfFileReader(filehandle)
        info = pdf.getDocumentInfo()
        pages = pdf.getNumPages()
        page = pdf.getPage(num)
        text = page.extractText()
        text = '  '.join(text.split())
        speaker.say(text)
        speaker.runAndWait()