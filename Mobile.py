from appium import webdriver

desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '7.1.2'
desired_capabilities['deviceName'] = 'M6Note'

desired_capabilities['app'] = 'E:\DingDing.apk'
desired_capabilities['udid'] = '721QECRB29Y29'

desired_capabilities['appPackage'] = 'com.alibaba.android.rimet'
desired_capabilities['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'

desired_capabilities['unicodeKeyboard'] = True
desired_capabilities['resetKeyboard'] = True
desired_capabilities['noReset'] = True


