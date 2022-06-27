import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests
import json
from datetime import datetime

def printpr(a):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print("[PRESTIGE][", current_time, "] ",a, sep='')

def inputpr(a):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[PRESTIGE][", current_time, "] ", a, sep='', end = '')
    inp = input()
    return inp

def inputproton(a):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[PRESTIGE][PROTONMAIL][", current_time, "] ", a, sep='', end = '')
    inp = input()
    return inp

def printproton(a):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[PRESTIGE][PROTONMAIL][", current_time, "] ", a, sep='', end = '')
    return inp

def clickpr():
    global nbchar
    global nbnb
    global noms
    global lienpt
    global prox
    global pro

    #PROXY
    prox += 1
    with open("http_proxies.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    PROXY = random.choice(content)  # IP:PORT or HOST:PORT
    chrome_options = webdriver.ChromeOptions()
    if pro == 'oui':
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
    #chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    mail = ''
    for i in range(nbchar):
        mail += chr(random.randint(97,122))
    for i in range(nbnb):
        mail += str(random.randint(0,10))
    nom = random.choice(noms)
    nnom = random.choice(nnoms)


    password = ''
    password += chr(random.randint(65, 90))
    for i in range(4):
        password += chr(random.randint(97,122))
    for i in range(4):
        password += str(random.randint(0,10))

    if len(content) == prox-1:
        return "ok"



    try:
        driver.get(lienpt)
    except:
        prox +=1
        driver.quit()
        printproton("Erreur, je reessaye...")
        clickpr()

    time.sleep(1)
    driver.switch_to.default_content()
    iframe = driver.find_element_by_xpath("//iframe[@sandbox='allow-scripts allow-same-origin allow-popups allow-top-navigation']")
    driver.switch_to.frame(iframe)

    inputElement_mail = driver.find_element_by_id('username')
    inputElement_mail.send_keys(mail)

    driver.switch_to.default_content()
    inputElement_pass = driver.find_element_by_name('password')
    inputElement_pass.send_keys(password)

    inputElement_conpass = driver.find_element_by_name('passwordc')
    inputElement_conpass.send_keys(password)

    iframe1 = driver.find_element_by_xpath("//iframe[@src='https://secure.protonmail.com/abuse.iframe.html?name=bottom']")
    driver.switch_to.frame(iframe1)
    Element_next = driver.find_element(By.XPATH, "//button[@name='submitBtn']")
    Element_next.click()


    time.sleep(1)
    driver.switch_to.default_content()
    Element_confirm = driver.find_element_by_id('confirmModalBtn')
    Element_confirm.click()

    time.sleep(1)

    #verify
    maildom = ''
    while maildom != 'wwjmp.com':
        mailver = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        print(mailver)
        mailver = mailver.text
        mailver = list(mailver)
        mailveri = ''
        for i in mailver:
            if i == '[' or i == ']' or i == '"':
                continue
            else:
                mailveri += i
        print(mailveri)
        maildeb, maildom = mailveri.split('@')

    inputElement_imail = driver.find_element(By.XPATH,
                                             "//input[@class='customRadio-input customMaskInput-input-radio ng-valid ng-not-empty ng-touched ng-dirty ng-valid-parse']")
    inputElement_imail.click()

    inputElement_mail = driver.find_element_by_id('emailVerification')
    inputElement_mail.send_keys(mailveri)

    Element_mail = driver.find_element(By.XPATH, "//button[@class='pm_button primary codeVerificator-btn-send']")
    Element_mail.click()


    lien ='https://www.1secmail.com/api/v1/?action=getMessages&login='
    lien += maildeb
    lien += '&domain='
    lien += maildom

    print(lien)
    time.sleep(20)
    mailver = requests.get(lien)
    print(mailver)
    mailver = mailver.json()
    print(mailver)
    id = mailver[0]['id']

    lien1 = 'https://www.1secmail.com/api/v1/?action=readMessage&login='
    lien1 += maildeb
    lien1 += '&domain='
    lien1 += maildom
    lien1 += '&id='
    lien1 += str(id)
    print(lien1)

    mailver1 = requests.get(lien1)
    print(mailver1)
    mailver1 = mailver1.json()
    print(mailver1)
    subject = mailver1['textBody']
    code = ''
    for i in subject:
        if  i.isdigit():
            code += str(i)

    inputproton("Code de vérification reçu!")

    try:
        inputElement_mail = driver.find_element_by_id('codeValue')
        inputElement_mail.send_keys(code)

        time.sleep(0.5)


        inputElement_mail = driver.find_element(By.XPATH, "//button[@class='pm_button primary large humanVerification-completeSetup-create']")
        inputElement_mail.click()
        inputproton("Vérification réussie!")

    except:
        driver.quit()
        inputproton("Vérification ratée. Je réessaye...")
        clickpr()

    time.sleep(10)



    try:
        file_object = open('passProton.txt', 'a+')
        file_object.write("\n")
        file_object.write(mail)
        file_object.write('@protonmail.com')
        file_object.write(':')
        file_object.write(password)
        file_object.close()
        inputproton("Réussi, identifiants enregistrés dans passProton.txt.")
    except:
        printproton("Erreur dans l'enregistrement dans passProton.txt.")


    driver.quit()
    return 0

def prog(a):
    if a == '1':
        nbco = inputpr("Nombre de comptes = ")
        for i in range(int(nbco)):
            print(a,"oui")
            clickpr()

#log
lienpt = 'https://mail.protonmail.com/create/new?language=fr'

#don't touch
prox = 0
pro = 'non'

#mail
nbchar = 8
nbnb = 5

#infos
noms = ['Arouf', 'Ahmed', 'Dylan', "Meddhi", "Shawnee", "Anne-Yvonne", "Siona", "Mackenson", "Anasthasia", "Nataly", "Mc", "Badria", "Pauline", "Hamelle", "Rehab", "Samentha", "Marie-Frede", "Diogou", "Adelphe", "Kaycie", "Annie-Christine", "Mirna", "Arlindo", "Bienvenida", "Mohamed-Bilal", "Yousseff", "Meera", "Djanina", "Nathanielle", "Oum", "Nathaelle", "Jorry", "Padrig"]
nnoms = ['Jackson','Smith','Schneider','Arouf','Hadad','Jager','Clavier','']



print(" _____  _____  ______  _____ _______ _____ _____ ______\n"
      "|  __ \|  __ \|  ____|/ ____|__   __|_   _/ ____|  ____|\n"
      "| |__) | |__) | |__  | (___    | |    | || |  __| |__\n"
      "|  ___/|  _  /|  __|  \___ \   | |    | || | |_ |  __|\n"
      "| |    | | \ \| |____ ____) |  | |   _| || |__| | |____\n"
      "|_|    |_|  \_\______|_____/   |_|  |_____\_____|______|\n")

printpr("Bienvenue sur PRESTIGE GEN!")
printpr("[1] ProtonMail")

prog(inputpr("Choisir le programme = "))
