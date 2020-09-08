from appium import webdriver

# w=webdriver.Remote('eee',desired_capabilities={})

a='a1111111'
d={'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,'a': 29}
for i in a:
    print(d[i])
    # w.press_keycode(d[i])
# w.press_keycode('')