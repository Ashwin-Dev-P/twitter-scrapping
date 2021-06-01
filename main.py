  
from selenium import webdriver
import pyautogui,time
from MYGLOBALVARIABLES import *

import operator

CHROME_WEBDRIVER_PATH = "D:\chromedriver.exe"
USERNAME = "zaynmalik"



class TwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        
        #To prevent unknown warning or error in command line
        options.add_experimental_option('excludeSwitches', ['enable-logging'])


        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH,options=options)
        print("Bot created.")
        
        
        LINK = "https://twitter.com/"+ USERNAME
        self.driver.get(LINK)
        time.sleep(AVERAGE_WAITING_TIME)

    
    
    def scroll(self):
        content_list = []
        cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for card in cards:
            try:
                handle = card.find_element_by_xpath('.//span[contains(text(),"@")]').text
                print(handle)
                if(handle[1:] != USERNAME):
                    continue
            except:
                pass
            
            
            try:
                content = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
            except:
                content = ""
            if(content not in content_list):
                content_list.append(content)
        
        
        
        
        lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            
            
            cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for card in cards:
                try:
                    handle = card.find_element_by_xpath('.//span[contains(text(),"@")]').text
                    #print(handle)
                    if(handle[1:] != USERNAME):
                        continue
                except:
                    pass
                
                
                try:
                    content = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
                except:
                    content = ""
                if(content not in content_list):
                    content_list.append(content)
                
            
            
            lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            
            if lastCount==lenOfPage:
                match=True

            
            
        for content in content_list:
            print(content)
        return content_list     
    
    def dictionary(self,tweet_list):
        my_dict = {}
        for tweet in tweet_list: 
            words = tweet.split(" ")
            for word in words:
                if(word not in my_dict):
                    my_dict[word] = 1
                else:
                    my_dict[word] += 1
        
        sorted_d = dict( sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True))
        
        for word in sorted_d:  
            print(word,sorted_d[word])              

        
    def close_tab(self):
        pyautogui.hotkey('ctrl','w')
        print("Tab closed.")

bot = TwitterBot()
tweet_list = bot.scroll()
bot.dictionary(tweet_list)
bot.close_tab()
print("Python program exited.")
exit()