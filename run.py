from selenium import webdriver
import time

class Spider:
    def __init__(self):
        # 修改参数尝试模拟浏览器
        options = webdriver.ChromeOptions()
        # 设置编码格式
        options.add_argument('lang=zh_CN.UTF-8')
        # 隐藏窗口
        # options.add_argument('--headless')
        # 不加载图片，爬取更快
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        # 隐藏webdriver特征
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        # 初始化webdriver
        self.browser = webdriver.Chrome(options=options)
        # 隐藏webdriver特征
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        self.browser.set_window_size(width=2048, height=960, windowHandle='current')


def send_comment(url="https://blog.roc136.top/others/"):
    browser = Spider().browser
    browser.get(url)
    nick = browser.find_element_by_name('nick')
    email = browser.find_element_by_name('mail')
    link = browser.find_element_by_name('link')
    veditor = browser.find_element_by_id('veditor')
    nick.send_keys('Roc')
    email.send_keys('1361050885@qq.com')
    link.send_keys('https://blog.roc136.top')
    veditor.send_keys('唤醒')
    submit = browser.find_element_by_xpath('//*[@id="comments"]/div[1]/div/div[3]/div[2]/button')
    submit.click()
    browser.close()


if __name__ == "__main__":
    url = "https://blog.roc136.top/others/"
    try:
        send_comment(url)
        now = time.asctime(time.localtime())
        print(now, "awake success")
    except:
        now = time.asctime(time.localtime())
        print(now, "awake failed")
