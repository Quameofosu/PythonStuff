import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('PDF_file.pdf', 'rb'))
engine = pyttsx3.init()  # initialize the TTS engine

rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                         # printing current voice rate
engine.setProperty('rate', 210)     # setting up new voice rate
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)  # Changes voice to female


for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    engine.say(text)
    engine.runAndWait()
engine.stop()

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
