import pyttsx3
import os
import PyPDF2
from gtts import gTTS

book = open('emotionmachine.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Number of pages in this PDF file:", pages)

print("""Type one for pyttsx
Type two for gTTS""")
val=input("input:")




def my_pyttsx():
    speaker = pyttsx3.init()
    for num in range(8, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()

def my_gtts():
    textList = []
    for i in range(8, 9):
        try:
            page = pdfReader.getPage(i)
            textList.append(page.extractText())
        except:
            pass
    textString = " ".join(textList)
    print(textString)
    language = 'en'
    myAudio = gTTS(text=textString, lang=language, slow=False)
    myAudio.save("new.mp3")
    os.system("new.mp3")


if (val=='one'):
    print("This is Python Text to Speech")
    my_pyttsx()

elif (val=='two'):
    print("This is Google Text to Speech")
    my_gtts()

else:
    print("invalid input")



