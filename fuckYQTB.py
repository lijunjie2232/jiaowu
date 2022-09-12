# -- coding: UTF-8
__author__ = 'ljj'

from time import sleep
from selenium import webdriver


class fuckYQTB(object):
   # 初始化
    def __init__(self, url):
        self.driver_path = r".\venv\Scripts\chromedriver.exe"
        self.chrome_driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = url
        self.chrome_driver.execute_cdp_cmd(
            'Network.setUserAgentOverride',
            {
                "userAgent": "superapp; app/Android"
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

    def fuckTb(self, js):
        # 执行js（懒得写，直接借用之前的js脚本）
        self.chrome_driver.execute_script(js)


if __name__ == '__main__':
    okbrowser = fuckYQTB('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')

    okbrowser.goToLogin()
    username = input('Enter username')  # 输入用户名
    password = input('Enter password')  # 输入密码
    okbrowser.input_text('id', 'username', username)
    okbrowser.input_text('id', 'password', password)
    okbrowser.click_element('name', 'submit')  # 点击“登录”按钮
    
    js = """
    $("#havelocation").html("您当前使用的终端设备不支持定位，请使用超级App或企业微信应用进行填报！");
    var customUserAgent = 'superapp; app/Android';
    Object.defineProperty(navigator, 'userAgent', {
        value: customUserAgent,
        writable: false
    });

    console.log(navigator.userAgent);
    console.log($("#havelocation")
        .html());
    if (document.querySelector(".co4") == null) {
        //go_sub();
        go_subfx();
        document.querySelector(".co3")
            .click();
        //save();
        savefx();
    } else {
        alert("submited");
    }
    """
    okbrowser.fuckTb(js)

    # sleep(60)

