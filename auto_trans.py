from selenium import webdriver
from time import sleep
import sys

def data_load():
    data = []
    filename = sys.argv[1]
    f = open(filename,'r')
    for rows in f:
        data.append(rows)

    return data

def data_join(datum,driver):
    element = driver.find_element_by_id('source')
    element.send_keys(datum)

def textarea_reset(driver):
    element = driver.find_element_by_id('source')
    element.clear()
    
def result_get_draw(driver,f):
    element2 = driver.find_element_by_xpath('//*[@id="result_box"]/span')
    print(element2.text)
    f.write(element2.text)
    f.write('\n')
    
    
    

def main():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://translate.google.co.jp/?hl=ja')
    data = data_load()
    f = open('result.txt','w')
    for datum in data:
        print(datum)
        data_join(datum,driver)
        sleep(5)
        result_get_draw(driver,f)
        sleep(1)
        textarea_reset(driver)
    f.close()
        

if __name__ == '__main__':
    main()
