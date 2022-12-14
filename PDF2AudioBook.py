import PyPDF2
import pyttsx3
from pyttsx3 import engine
pdfReader = PyPDF2.PdfFileReader(open('PDF_file.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
