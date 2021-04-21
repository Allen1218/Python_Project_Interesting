import pyttsx3
import PyPDF4

filename = 'api.pdf'
ratePatial = -60
startPage = 0

def parsePdf():
    pdfreader = PyPDF4.pdf.PdfFileReader(filename)
    print(pdfreader.isEncrypted)

    pages = pdfreader.numPages
    print(pages)

    for num in range(startPage, pages -1 ):
        page = pdfreader.getPage(num)
        text = page.extractText()
        voice(text)

def voice(msg):
    teacher = pyttsx3.init()
    # 1. 说话速度
    rate = teacher.getProperty('rate')
    teacher.setProperty('rate', rate + ratePatial)

    # 2. 声音种类
    voices = teacher.getProperty('voices')
    print(voices)
    # 0：英语男声；1：英语女声
    voices = teacher.setProperty('voice', voices[1].id)

    teacher.say(msg)
    teacher.runAndWait()

if __name__ == '__main__':
    parsePdf()