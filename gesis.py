import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import copy
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

############# functions#######################3
def is_file_downloaded(filename, timeout=60):
    end_time = time.time() + timeout
    while not os.path.exists(filename):
        time.sleep(1)
        if time.time() > end_time:
            print("File not found within time")
            return False

    if os.path.exists(filename):
        print("File found")
        return True
#==================================

#!!!!!!   ÖNEMLİ NOT = google chrome versiyonu ile chromedriver versiyonu aynı olmalı !!!!!!!!!!!!!!!!!

###################  Önemli Not => eğer selenium düzgün çalışmıyorsa aşağıdaki paketleri yükleyin.

# pip install selenium==3.141.0
# pip install --upgrade urllib3==1.26.16
# pip install --upgrade requests

#########******* Değiştirilecek ve doldurulacak kısımlar  *******###############
# chromedriver_path="/home/bilgi/Desktop/chromedriver" # chromedriver in bulunduğu pathi kendinize göre değiştirin.
chromedriver_path="./chromedriver"
user_login=['asuerdem@bilgi.edu.tr','Deneme1234!'] #kullanıcı kendi hesap bilgilerini gircek.
d_path='/home/bilgi/Downloads/'  #download pathini düzeltip giriniz.
search_list=['ZA7691','ZA7782']  # Not buraya istenildiği kadar arama terimi girilebilir. örnek olsun diye 2 tane yaptım.

#***************************************************#

########################################### dokunulmayacak kısım #######################3
for search in search_list:
    url="https://login.gesis.org/realms/gesis/protocol/openid-connect/auth?client_id=gesis-gws-client&redirect_uri=https%3A%2F%2Fsearch.gesis.org%2Fresearch_data%2F{}%3Flang%3Den&state=71378aec-528d-45cd-836d-fcc3d36d1ec3&response_mode=fragment&response_type=code&scope=openid&nonce=bcba6094-c4e2-4e3d-80f0-515c1f3affe6&ui_locales=en".format(search)
    email='//*[@id="username"]'
    password='//*[@id="password"]'
    login_button='//*[@id="kc-login"]'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    el = wait.until(EC.visibility_of_element_located((By.XPATH, email)))
    el.send_keys(user_login[0])
    el.send_keys(Keys.ENTER)
    time.sleep(1)
    el = wait.until(EC.visibility_of_element_located((By.XPATH, password)))
    el.send_keys(user_login[1])
    el.send_keys(Keys.ENTER)
    time.sleep(4)
    print("sssssssssssss")
    try:
            db_path='//*[@id="sidebar"]/div/div[1]/a'
            chs='//*[@id="{}_dataset_popup"]/span[2]/select/option[5]'.format(search)
            sav_path='//*[@id="{}_dataset_popup"]/a'.format(search)
            sav_path1='//*[@id="{}_dataset_popup"]/a[1]'.format(search)
            el = wait.until(EC.visibility_of_element_located((By.XPATH, db_path)))
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            print("database clicked")
            el=wait.until(EC.visibility_of_element_located((By.XPATH,sav_path1)))
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            print("database clicked on screen")
            dropdownbox=driver.find_elements(by=By.TAG_NAME,value="Option")
            sc=0
            while sc<len(dropdownbox):
                print(dropdownbox[sc].text)
                if dropdownbox[sc].text.strip()=="for scientific research (incl. doctorate)":
                    dropdownbox[sc].click()
                sc+=1
            time.sleep(1)
            print("dropbox")
            sav_link=""
            download_name=""
            for i in range(4):
                try:
                    np="{}[{}]".format(sav_path,i+1)
                    print(np)
                    txt=wait.until(EC.visibility_of_element_located((By.XPATH,np)))
                    print(txt.text)
                    text=txt.text.split('.')
                    if str(text[1]).startswith("s"):
                        sav_link=np
                        download_name=txt.text.strip().split(' ')[0]
                    else:
                        pass
                except:
                    pass

            el = wait.until(EC.visibility_of_element_located((By.XPATH, sav_link)))
            el.send_keys(Keys.ENTER)
#######################################################################
            # driver.find_element(By.XPATH, '//button[text()="Download"]').click()
            print(sav_link)
            print("=====")
            print("sav")
            print(download_name)
            counter=0
            while True:
                if counter>120:
                    break
                print("döngüde devam ediyor.")
                file_path = '{}{}'.format(d_path,download_name)
                if is_file_downloaded(file_path, 3):
                    print("{} completed".format(search))
                    break
                else:
                    pass
                counter+=1

###########============================================================
            # time.sleep(download_bekleme_suresi)
            print("{} completed".format(search))
    except:
        print("handle error")
    print("completed succesfully")
    driver.quit()
