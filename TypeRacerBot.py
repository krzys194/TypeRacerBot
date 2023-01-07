from PIL import Image
from pytesseract import pytesseract
import pydirectinput
import pyautogui

def botType():
    sayBool = True
    while sayBool:
        locate = pyautogui.locateCenterOnScreen("locateWhereType.png", confidence = 0.9)
        locateUp = pyautogui.locateOnScreen("locateUp.png", confidence = 0.9)
        if locate:
            if locateUp:
                x1, y1 = locate
                pyautogui.click(x1, y1+40 ) 
                x2, y2, xx2, yy2 = locateUp
                sayBool = False
                screenShot = pyautogui.screenshot(region = (x2-30, y2+20, xx2+10, 300))
                screenShot.save("zdjecieTekstu.png")

    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_image = 'images/sampletext1-ocr.png'
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open("zdjecieTekstu.png")

    text = pytesseract.image_to_string(img)
    text = text.replace("\n"," ")
    text = text.replace("[", "")

    for i in range(0, len(text)):
        pyautogui.typewrite(f"{text[i]}")
    sayBool = True


def antyBot():
    sayBool2 = True
    while sayBool2:
        locateAntyBotType = pyautogui.locateCenterOnScreen("antyBotType.png", confidence = 0.8)
        locateUpAntyBot = pyautogui.locateOnScreen("antyBotUp.png", confidence = 0.8)
        if locateAntyBotType:
            if locateUpAntyBot:
                x1, y1 = locateAntyBotType
                pyautogui.click(x1-20, y1) 
                x2, y2, xx2, yy2 = locateUpAntyBot
                sayBool2 = False
                screenShot = pyautogui.screenshot(region = (x2, y2+20, xx2, 300))
                screenShot.save("antyBotSs.png")

    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_image = 'images/sampletext1-ocr.png'
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open("antyBotSs.png")
    text = pytesseract.image_to_string(img)
    text = text.replace("\n"," ")
    text = text.replace("[", "")
    for i in range(0, len(text)):
        pyautogui.typewrite(f"{text[i]}")
    sub = pyautogui.locateCenterOnScreen("submit.png", confidence = 0.8)
    if sub:
        x3, y3 = sub
        pyautogui.click(x3, y3)

botType()
antyBot()