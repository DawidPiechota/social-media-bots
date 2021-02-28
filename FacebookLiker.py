from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class FacebookBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.bot = webdriver.Firefox(firefox_profile=_browser_profile)

    def login(self):
        bot = self.bot
        bot.get('https://www.facebook.com/')
        time.sleep(5)
        email = bot.find_element_by_name('email')
        password = bot.find_element_by_name('pass')
        email.clear()
        time.sleep(1)
        password.clear()
        time.sleep(1)
        email.send_keys(self.email)
        time.sleep(1)
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(50)
    
    def likeAll(self, who, pages):
        bot = self.bot
        time.sleep(3)
        bot.get("https://www.facebook.com/"+ who)
        time.sleep(4)
        for i in range(1,pages):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3+random.randint(0,1))
        likes = bot.find_elements_by_xpath("//div[@class='_666k']//a[contains(@aria-pressed, 'false')]")
        for like in likes:
            try:
                like.click()
                time.sleep(7+random.randint(0, 3))
            except Exception:
                time.sleep(7+random.randint(0, 3))
            
    
    def randomComment(self, who): # Not used
        bot = self.bot
        time.sleep(3)
        bot.get("https://www.facebook.com/"+ who)
        time.sleep(4)

        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

        commentFields = bot.find_elements_by_class_name('______________TODO______________')
        for commentField in commentFields:
            commentField.send_keys("______________TODO______________")
            time.sleep(3)
            commentField.send_keys(Keys.RETURN)
            #______________TODO______________

    def closeDriver(self):
        self.bot.close()

    def testOpen(self):
        bot = self.bot
        bot.get('https://www.facebook.com/')


#______________________________________________#
botInstance = FacebookBot('<Your_email>','<Your_password>')

botInstance.login()
botInstance.likeAll('Target, ex: jan.kowalski.71', 30)
time.sleep(5)
botInstance.closeDriver()
