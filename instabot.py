from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request
import urllib3
import urllib3.request
import os
import csv



class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.login()

    def login(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
        sleep(2)
        login_field = self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        login_field = self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
    
    def user_action(self):
        while True:
            action = input("type what you would like to do follow, search, download, stop: ")
            if action == "stop":
                break
            elif action == "download":
                # new_action = input("Videos or Images?: ")
                # if new_action == "videos":
                #     self.download_videos()
                # else:
                self.donwload_images()
            elif action == "follow":
                self.follow()
            elif action == "search":
                self.search_user()


    def search_user(self):
            user = input("Enter an Instagram id type 'stop' to stop searching: ")
            self.driver.get(f"https://www.instagram.com/{user}/")



    def follow(self):
        user = input("Instagram id of user that you want to follow: ")
        self.driver.get(f"https://www.instagram.com/{user}")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
    
    def infinite_scroll(self):

        self.last_height = self.driver.execute_script("return document.body.scrollHeight")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(2)

        self.new_height = self.driver.execute_script("return document.body.scrollHeight")


        if self.new_height == self.last_height:
            return True

        self.last_height = self.new_height
        return False

    # def download_videos(self):
    #     self.search_user()
    #     video_src = []
    #     name = input("Type folder name: ")
    #     folder_name = f"D:\{name}"
    #     if not os.path.exists(folder_name):
    #         os.makedirs(folder_name)
    #         print("True")

    #     while True:
    #         result = self.infinite_scroll()

    #         # images.append(self.driver.find_elements_by_class_name('_9AhH0'))
    #         videos = self.driver.find_elements_by_tag_name('video')
    #         for video in videos:
    #             if video.get_attribute("src") in video_src:
    #                 continue
    #             else:
    #                 video_src.append(video.get_attribute("src"))
    #             # print(image.get_attribute("src"))
            
    #         if result == True:
    #             break

    #     for i, src in enumerate(video_src):
    #         vid_filename = f"video_{i}.jpg"
    #         print(f"{vid_filename} saved")
    #         # urllib.request.urlretrieve(src, img_filename)
    #         urllib.request.urlretrieve(src, f"{folder_name}/{vid_filename}")

    def donwload_images(self):
        self.search_user()
        images_src = []
        video_src = []
        name = input("Type folder path: ")
        folder_name = name
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print("True")

        while True:
            result = self.infinite_scroll()
            print("scrolling...")

            # images.append(self.driver.find_elements_by_class_name('_9AhH0'))
            images = self.driver.find_elements_by_tag_name('img')
            for image in images:
                if image.get_attribute("src") in images_src:
                    continue
                else:
                    images_src.append(image.get_attribute("src"))
                # print(image.get_attribute("src"))
            
            if result == True:
                break

        for i, src in enumerate(images_src):
            img_filename = f"image_{i}.jpg"
            print(f"{img_filename} saved")
            # urllib.request.urlretrieve(src, img_filename)
            urllib.request.urlretrieve(src, f"{folder_name}/{img_filename}")
            


        

username = input("Username: ")
password = input("Password: ")
mybot = InstaBot(username, password)
mybot.user_action()
print("Goodbye")
exit()