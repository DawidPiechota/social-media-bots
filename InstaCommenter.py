from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstaBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.bot = webdriver.Firefox(firefox_profile=_browser_profile)
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        time.sleep(1)
        password.clear()
        time.sleep(1)
        email.send_keys(self.email)
        time.sleep(1)
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def randomComments(self, who, list1, list2):
        bot = self.bot
        bot.get("https://www.instagram.com/" + who)
        time.sleep(5)
        for i in range(1,1):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2+random.randint(0,1))
        photos = bot.find_elements_by_xpath("//a[@href]")
        links = [photo.get_attribute("href") for photo in photos]
        for link in links:
            if(link.startswith("https://www.instagram.com/p/")):
                bot.get(link)
                time.sleep(60+random.randint(0,3))
                comment = bot.find_element_by_class_name("Ypffh") #RxpZH X7cDz
                comment.click()
                time.sleep(1)
                comment = bot.find_element_by_class_name("Ypffh")
                commentString = random.choice(list1) + " " + random.choice(list2)
                comment.send_keys(commentString)
                comment.send_keys(Keys.RETURN)
                print("Dodano komentarz: " + commentString.ljust(16) + "| Do zdjęcia: " + link.ljust(40) + "| Osobie: " + who)
                time.sleep(60+random.randint(0,5))
            
            

    def closeDriver(self):
        self.bot.close()


commentList1 =["Loff", "Mojaa", "SztosiQ", "Najss", "11/10", "Perfect", "Cudooo", "Mrr...","Aww", "No no", "Myszkaa", "Ideolo","Princess", "Skarb", "Kiss","Kocham","Najlepszaa","Cudeńko","Moja na zawsze","Profeszjonal", "Jest mocc", "Najładniejsza", "Mój świat","Słońce", "Śłodkoo", "Cukiereczek", "Boziuu", "O maj gasz!","Bff","Bejbii","Zamurowało mnie", "Boskie", "Muachh", "Cool", "KOCHAAAMM"]
commentList2 =["❤❤", "💞💞", "💕💕", "😏😏", "😍😍", "👌😂💓", "💞💞", "😂💓", "💕💕", "👌🔥", "🐭💗", "👌💓", "💞💞", "❤❤", "💋💋", "💖💖", "💓", "😂😍😍", "💪💪💞💞", "😍😍", "💓💓", "💫⭐☀", "🔥😍", "🌸🍬", "💓💓🔥", "💪💓", "😏😘😘", "😂❤🔥", "💗💗💗💗", "👌👌😏"]


botInstance = InstaBot('<Your_email>','<Your_password>')
botInstance.login()
botInstance.randomComments("<target_username>", commentList1, commentList2)
time.sleep(3)
botInstance.closeDriver()