from appium import webdriver
import time

def androidConnectAppium():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'Appium'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # <查找包名: aapt apk_name |findstr 'package'>
    desired_caps['appPackage'] = 'com.speedstae.dcbox'
    # <查找类名:aapt apk_name | findstr 'launchable'>
    desired_caps['appActivity'] = 'com.speedstae.dcbox.MainActivity'
    # <指定设备的编号>
    # desired_caps['udid'] = 'YGC6R19122004060'

    # <是否重置>
    # desired_caps['no-reset']=False
    # <发送请求给appium服务器，特征是以上caps>
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print(driver)
    return driver
def backto_previous(self):
    self.driver.find_element_by_class_name('android.widget.ImageView').click()
def clicklogin(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='钱包余额 (USDT)\n点击登入\n账单 登录后查看']").click()
def logout(self):
    self.driver.find_element_by_xpath("//android.view.View[@text='我的\n第 2 个标签，共 2 个']").click()
    getxy(self)
    try:
       time.sleep(1)
       self.driver.find_element_by_xpath("//android.widget.Button[@text='登出']").click()


    except:
       self.driver.find_element_by_xpath("//android.widget.Button[@text='登出']").click()
    # self.driver.find_element_by_xpath("//android.widget.ImageView[@text='金库号\nWA564777']").click()
def getxy(self):
        w=self.driver.get_window_size()['width']
        print('屏幕宽度',w)
        h=self.driver.get_window_size()['height']
        print('屏幕高度',h)
        x1=0.13*int(w)
        y1=0.13*int(h)
        self.driver.tap([(x1,y1),(x1,y1)],duration=100)
        self.driver.tap([(x1,y1),(x1,y1)],duration=100)
        print('是否登出？')


def xy(self):
    w = self.driver.get_window_size()['width']
    print('屏幕宽度', w)
    h = self.driver.get_window_size()['height']
    print('屏幕高度', h)
    x1 = 0.13 * int(w)
    y1 = 0.13* int(h)
    self.driver.tap([(x1, y1), (x1, y1)], duration=100)
    self.driver.tap([(x1, y1), (x1, y1)], duration=100)
    print('是否登出？')
def keycode():
    def getMobileKey():
        key = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
               'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
               'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
               'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
               'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
               'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
               'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
               'META_ALT_LEFT_ON': 16,
               'META_ALT_MASK': 50,
               'META_ALT_ON': 2,
               'META_ALT_RIGHT_ON': 32,
               'META_CAPS_LOCK_ON': 1048576,
               'META_CTRL_LEFT_ON': 8192,
               'META_CTRL_MASK': 28672,
               'META_CTRL_ON': 4096,
               'META_CTRL_RIGHT_ON': 16384,
               'META_FUNCTION_ON': 8,
               'META_META_LEFT_ON': 131072,
               'META_META_MASK': 458752,
               'META_META_ON': 65536,
               'META_META_RIGHT_ON': 262144,
               'META_NUM_LOCK_ON': 2097152,
               'META_SCROLL_LOCK_ON': 4194304,
               'META_SHIFT_LEFT_ON': 64,
               'META_SHIFT_MASK': 193,
               'META_SHIFT_ON': 1,
               'META_SHIFT_RIGHT_ON': 128,
               'META_SYM_ON': 4,
               'KEYCODE_APOSTROPHE': 75,
               'KEYCODE_AT': 77,
               'KEYCODE_BACKSLASH': 73,
               'KEYCODE_COMMA': 55,
               'KEYCODE_EQUALS': 70,
               'KEYCODE_GRAVE': 68,
               'KEYCODE_LEFT_BRACKET': 71,
               'KEYCODE_MINUS': 69,
               'KEYCODE_PERIOD': 56,
               'KEYCODE_PLUS': 81,
               'KEYCODE_POUND': 18,
               'KEYCODE_RIGHT_BRACKET': 72,
               'KEYCODE_SEMICOLON': 74,
               'KEYCODE_SLASH': 76,
               'KEYCODE_STAR': 17,
               'KEYCODE_SPACE': 62,
               'KEYCODE_TAB': 61,
               'KEYCODE_ENTER': 66,
               'KEYCODE_ESCAPE': 111,
               'KEYCODE_CAPS_LOCK': 115,
               'KEYCODE_CLEAR': 28,
               'KEYCODE_PAGE_DOWN': 93,
               'KEYCODE_PAGE_UP': 92,
               'KEYCODE_SCROLL_LOCK': 116,
               'KEYCODE_MOVE_END': 123,
               'KEYCODE_MOVE_HOME': 122,
               'KEYCODE_INSERT': 124,
               'KEYCODE_SHIFT_LEFT': 59,
               'KEYCODE_SHIFT_RIGHT': 60,
               'KEYCODE_F1': 131,
               'KEYCODE_F2': 132,
               'KEYCODE_F3': 133,
               'KEYCODE_F4': 134,
               'KEYCODE_F5': 135,
               'KEYCODE_F6': 136,
               'KEYCODE_F7': 137,
               'KEYCODE_F8': 138,
               'KEYCODE_F9': 139,
               'KEYCODE_F10': 140,
               'KEYCODE_F11': 141,
               'KEYCODE_F12': 142,
               'KEYCODE_BACK': 4,
               'KEYCODE_CALL': 5,
               'KEYCODE_ENDCALL': 6,
               'KEYCODE_CAMERA': 27,
               'KEYCODE_FOCUS': 80,
               'KEYCODE_VOLUME_UP': 24,
               'KEYCODE_VOLUME_DOWN': 25,
               'KEYCODE_VOLUME_MUTE': 164,
               'KEYCODE_MENU': 82,
               'KEYCODE_HOME': 3,
               'KEYCODE_POWER': 26,
               'KEYCODE_SEARCH': 84,
               'KEYCODE_NOTIFICATION': 83,
               'KEYCODE_NUM': 78,
               'KEYCODE_SYM': 63,
               'KEYCODE_SETTINGS': 176,
               'KEYCODE_DEL': 67,
               'KEYCODE_FORWARD_DEL': 112,
               'KEYCODE_NUMPAD_0': 144,
               'KEYCODE_NUMPAD_1': 145,
               'KEYCODE_NUMPAD_2': 146,
               'KEYCODE_NUMPAD_3': 147,
               'KEYCODE_NUMPAD_4': 148,
               'KEYCODE_NUMPAD_5': 149,
               'KEYCODE_NUMPAD_6': 150,
               'KEYCODE_NUMPAD_7': 151,
               'KEYCODE_NUMPAD_8': 152,
               'KEYCODE_NUMPAD_9': 153,
               'KEYCODE_NUMPAD_ADD': 157,
               'KEYCODE_NUMPAD_COMMA': 159,
               'KEYCODE_NUMPAD_DIVIDE': 154,
               'KEYCODE_NUMPAD_DOT': 158,
               'KEYCODE_NUMPAD_EQUALS': 161,
               'KEYCODE_NUMPAD_LEFT_PAREN': 162,
               'KEYCODE_NUMPAD_MULTIPLY': 155,
               'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
               'KEYCODE_NUMPAD_SUBTRACT': 156,
               'KEYCODE_NUMPAD_ENTER': 160,
               'KEYCODE_NUM_LOCK': 143,
               'KEYCODE_MEDIA_FAST_FORWARD': 90,
               'KEYCODE_MEDIA_NEXT': 87,
               'KEYCODE_MEDIA_PAUSE': 127,
               'KEYCODE_MEDIA_PLAY': 126,
               'KEYCODE_MEDIA_PLAY_PAUSE': 85,
               'KEYCODE_MEDIA_PREVIOUS': 88,
               'KEYCODE_MEDIA_RECORD': 130,
               'KEYCODE_MEDIA_REWIND': 89,
               'KEYCODE_MEDIA_STOP': 86,
               }

if __name__ == '__main__':
    androidConnectAppium()
