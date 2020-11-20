import pyttsx3
import PyPDF2
book = open('test.pdf', 'rb') ##binary reading
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
speaker.setProperty('rate',70)  ##to set the frequency
voices=speaker.getProperty('voices')
speaker.setProperty('voices',voices[0].id)

for num in range(27, pages):   ## manually insert the page no. of pdf to start reading from the desired page
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
~                             
