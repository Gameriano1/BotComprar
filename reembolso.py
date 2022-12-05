from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

delay = 8

def bingantibug(xpath, driverz):
    try:
        myElem = WebDriverWait(driverz, delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException:
        raise Exception('A Pagina nao acrregou a tempo')

def xbox(conta, senha):
    global bixo
    global troxa
    global driver
    chrome_options = ChromeOptions()

    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get(
        'https://support.xbox.com/pt-BR/help/subscriptions-billing/buy-games-apps/refund-orders')
    bingantibug('//*[@id="RefundAuthCard_SignInButton"]', driver)
    driver.find_element('xpath','//*[@id="RefundAuthCard_SignInButton"]').click()
    bingantibug('//*[@id="i0116"]', driver)
    driver.find_element('xpath', '//*[@id="i0116"]').send_keys(conta)
    print('digitei a conta')

    bingantibug('//*[@id="idSIButton9"]', driver)
    driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
    print('cliquei em proximo')

    bingantibug('//*[@id="i0118"]', driver)
    driver.find_element('xpath', '//*[@id="i0118"]').send_keys(senha)
    print('digitei a senha')

    bingantibug('//*[@id="idSIButton9"]', driver)
    driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
    print('cliquei em entrar')

    bingantibug('//*[@id="idSIButton9"]', driver)
    driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
    print('cliquei em proximo')
    bingantibug('//*[@id="BodyContent"]/div/section/div[2]/div[1]/div/div[6]/section/div/div[2]/button', driver)
    driver.find_element(By.XPATH,'//*[@id="BodyContent"]/div/section/div[2]/div[1]/div/div[6]/section/div/div[2]/button').click()
    def idss(recarregar = False):
        global ids
        if recarregar:
            driver.refresh()
            bingantibug('//*[@id="BodyContent"]/div/section/div[2]/div[1]/div/div[6]/section/div/div[2]/button', driver)
            driver.find_element(By.XPATH,'//*[@id="BodyContent"]/div/section/div[2]/div[1]/div/div[6]/section/div/div[2]/button').click()
        l = driver.find_elements(By.XPATH,"//*[@class='undefined root-258']")
        ids = []
        for i in l:
            if len(i.text) >= 10 and not str(i.text).__contains__('/'):
                ids.append(i.text)
        print(ids)
        if not len(ids):
            idss(recarregar=True)
    idss()
    driver.get('https://support.xbox.com/pt-br/forms/request-a-refund')
    bingantibug('//*[@id="TextField0"]', driver)
    driver.find_element(By.XPATH, '//*[@id="TextField0"]').send_keys('Roblox 88 Subscribed')
    bingantibug('//*[@id="TextField5"]', driver)
    for i in ids:
        driver.find_element(By.XPATH, '//*[@id="TextField5"]').send_keys(i + ',')
    driver.find_element(By.XPATH, '//*[@id="TextField5"]').send_keys(Keys.BACKSPACE)
    bingantibug("//*[contains(text(), 'Selecione uma opção')]", driver)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Selecione uma opção')]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div/div/div[1]/div[7]/section/div/div[2]/ul/li[3]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div/div/div[1]/div[7]/section/div[2]/div/div/section/div/div[2]/button").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div/div/div[1]/div[7]/section/div[2]/div/div/section/div/div[2]/ul/li[1]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div[2]/div/div/div/div[3]/button").click()
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    xbox('qyyqdhsahdhsafd@outlook.com', 'S1splatina')