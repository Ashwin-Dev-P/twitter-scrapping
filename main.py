  
from selenium import webdriver
import pyautogui,time
from MYGLOBALVARIABLES import *

CHROME_WEBDRIVER_PATH = "D:\chromedriver.exe"
USERNAME = "evienevillee"
#USERNAME = "zaynmalik"

span_class = "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"
span_class = "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"
div_class = "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"


span_class = "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"

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

    def tweets(self):
        
        
        #Select the tweets section
        tweet_tab = self.driver.find_element_by_xpath(TWEET_TAB_XPATH)
        tweet_tab.click()
        print(tweet_tab)
        
        """
        #Find the tweet content
        time.sleep(4)
        tweet_content = self.driver.find_elements_by_class_name(CONTENT_CLASS_NAME)
        #print(tweet_content)
        """
        
        articles = self.driver.find_elements_by_tag_name('article')
        
        
        """
        span_elements = []
        
        time.sleep(10)
        for article in articles:
            
            span_element = article.find_elements_by_tag_name('span')[3]
            print(span_element)
            span_elements.append(span_element)
           
        
        for i in span_elements:  
            if(i.get_attribute('class').strip() == span_class ):
                print(i.text)
        """
                
                
        """
        my_span = span_elements.find_elements_by_class_name(span_class)
        print(my_span)
        """
        print("___________________________________________________________________________________________")
        
        time.sleep(10)
        """
        divs = self.driver.find_elements_by_class_name(div_class)
        for div in divs:
            print(div.text)
        print(divs)
        """
        #articles = self.driver.find_elements_by_tag_name('article')
        articles = self.driver.find_elements_by_xpath("//*[name()='article'][@role='article']")
        print(articles)
        for article in articles:  
            divs = article.find_element_by_xpath("//*[name()='div'][@dir='auto']")
            print(divs.text)
        print("___________________________________________________________________________________") 
        
    def tweets2(self):
        cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        
        for card in cards:
            #card = cards[0]
            content = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
            print(content)
            print("__________________________________________________________________________________________________")
            
    def scroll(self):
        while self.driver.find_element_by_tag_name('div'):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Divs=self.driver.find_element_by_tag_name('div').text
            if 'End of Results' in Divs:
                print('end')
                break
            else:
                continue
    
    def scroll2(self):
        content_list = []
        cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for card in cards:
            #card = cards[0]
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
            #lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            
            
            
            cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for card in cards:
                #card = cards[0]
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
                #print(content)
                #print("__________________________________________________________________________________________________")
            
            
            
            lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            
            if lastCount==lenOfPage:
                match=True

            
            
        for content in content_list:
            print(content)
            print("__________________________________________________________________________________________________")
                
            
        
    def close_tab(self):
        pyautogui.hotkey('ctrl','w')
        print("Tab closed.")

bot = TwitterBot()
#bot.tweets2()
bot.scroll2()
#bot.tweets2()
bot.close_tab()
print("Python program exited.")
exit()