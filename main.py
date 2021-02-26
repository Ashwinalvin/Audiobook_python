# importing the modules we have a file with name file ok add that to ur current project
#step1  for that is load two modules first pip install pyttsx3,pip install PyPDF2
#step 2 click file in taskbar then click (c drive) then click users then click pycharm_projects then wil get list of projects done under pycharm
#step3 now this project name is pdftospeech double click on this open it
#step4 copy paste the pdf file which we need to read
#step 5 now the file i pasted is present in my project (can be seen at left panel) there
import PyPDF2
import pyttsx3

# path of the PDF file
open_book = open('file.pdf', 'rb')

# creating a PdfFileReader object
Read = PyPDF2.PdfFileReader(open_book)

# the page with which you want to start
# this will read the page of 25th page.
from_page = Read.getPage(24)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
