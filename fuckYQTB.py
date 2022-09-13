# -- coding: UTF-8
__author__ = 'ljj'

from asyncio.windows_events import NULL
import json
from time import sleep
from selenium import webdriver
import os
import shutil
from utils.bs64coder import strDecoder, strEncoder


class fuckYQTB(object):
   # 初始化
    def __init__(self, url):
        self.driver_path = r".\venv\Scripts\chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome_driver = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
        self.url = url

    def setUA(self, ua):
        self.chrome_driver.execute_cdp_cmd(
            'Network.setUserAgentOverride',
            {
                "userAgent": ua
            })

    # 获取登录URL

    def goToLogin(self):
        self.chrome_driver.get(self.url)

    # 输入用户名/密码
    def input_text(self, locator_type, value, text):
        self.chrome_driver.find_element(locator_type, value).send_keys(text)

    # 点击页面按钮
    def click_element(self, locator_type, value):
        self.chrome_driver.find_element(locator_type, value).click()

    def checkLogin(self, locator_type, value):
        if locator_type == 'title':
            return self.chrome_driver.title == value
        elif locator_type == 'url':
            return self.chrome_driver.current_url == value
        else:
            return self.chrome_driver.find_element(locator_type, value).text == value

    def fuckTb(self, js):
        # 执行js（懒得写，直接借用之前的js脚本）
        self.chrome_driver.execute_script(js)


if __name__ == '__main__':
    try:
        if not os.path.exists("./config/config.json"):
            if os.path.exists("./config/config_tmpl.json"):
                print('generating a new config.json file')
                shutil.copy("./config/config_tmpl.json", "./config/config.json")
            else:
                raise Exception("Could not find config.json file in folder config")
        f = open("./config/config.json","r",encoding="utf-8")
        config = json.load(f)
        f.close()

    except Exception as e:
        print(e)
        print("please check config.json ...")
        exit()

    
    okbrowser = fuckYQTB('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')

    okbrowser.setUA('superapp; app/Android')
    okbrowser.goToLogin()

    change = False

    if "username" in config.keys() and config["username"] != "":
        username = config["username"]
    else:
        username = input('Enter username:')  # 输入用户名
        config["username"] = username
        change = True

    if "password" in config.keys() and config["password"] != "":
        password = strDecoder(config["password"])
    else:
        password = input('Enter password:')  # 输入密码
        config["password"] = strEncoder(password)
        change = True

    if change:
        with open("./config/config.json", "w") as f:
            print(config)
            json.dump(config, f)

    okbrowser.input_text('id', 'username', username)
    okbrowser.input_text('id', 'password', password)
    okbrowser.click_element('name', 'submit')  # 点击“登录”按钮

    try:
        if not okbrowser.checkLogin('url', 'https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp'):
            raise Exception('Please check your username and password ...')
    except Exception as e:
        print("Login failed")
        print(e)
        exit()
    
    try:
        if config['fx']:
            bh_p = "fx"
        else:
            bh_p = ""
        
        if config["force"]:
            force = 'submit();'
        else:
            force = 'alert("alrady submited");'
        if config["location"] != "":
            loct = config["location"]
        else:
            loct = "您当前使用的终端设备不支持定位，请使用超级App或企业微信应用进行填报！"
    except Exception as e:
        print(e)
        print("please check config.json ...")
    
    set_location = """$("#havelocation").html("%s");"""%(loct)
    okbrowser.fuckTb(set_location)

    js = """
    function submit() { 
        go_sub%s();
        document.querySelector(".co3")
            .click();
        save%s();
    }
    if (document.querySelector(".co4") == null) {
        submit();
    } else {
        %s
    }
    """%(bh_p, bh_p, force)

    print(js)

    okbrowser.fuckTb(js)

    # print("sleeping ...")
    # sleep(60)
