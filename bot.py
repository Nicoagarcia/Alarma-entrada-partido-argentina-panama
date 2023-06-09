from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright
from playsound import playsound
import time
from tkinter import messagebox

def get_link(page):
    eventoArgentina = page.locator('xpath=/html/body/div[4]/div/div[2]/div/div/div/div[1]/div/a')
    link = eventoArgentina.get_attribute('href')
    return link

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.deportick.com/")

    while True:
        link = get_link(page)
        if link:
            print("\nHora: {}\nFlaquito, activa, se publicaron! sos bueno esperando! ahora apurate.\n".format(datetime.fromtimestamp(time.time())))
            playsound('PvZ Victory Jingle.mp3')
            messagebox.showinfo(message="La imagen tiene un link asociado!", title="ATENCION")
            image = page.locator('xpath=/html/body/div[4]/div/div[2]/div/div/div/div[1]/div/a/img')
            image.click()
            print(link)
            break
        else:
            print("\nHora: {}\n SOS BUENOOOO. Nunca vi a nadie, que espere tan bien las entradas como vos. pero sigue sin publicarse\n".format(datetime.fromtimestamp(time.time())))
            time.sleep(60)
