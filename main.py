from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()

options.add_experimental_option('prefs', {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
URL = 'https://jeemain.nta.ac.in/'
driver.get(URL)

driver.maximize_window()
driver.implicitly_wait(5)

first_pdf = driver.find_element(By.XPATH, "//div[@class='news-eve-scroll pr-2']/ul/li/a")
first_pdf.click()

sleep(5)
