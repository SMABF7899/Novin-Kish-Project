from Configs import seleniumConfig

configName = seleniumConfig.set_config(".env")


class StoreEvalDB():
    vars = {}


def highLight(element):
    driverHighLight = element._parent

    def apply_style(s):
        driverHighLight.execute_script("arguments[0].setAttribute('style', arguments[1]); ", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red; ")
    configName.time.sleep(.15)
    apply_style(original_style)


def convertToPersian(number):
    persianNumber: str = ""
    for i in range(len(number)):
        if int(number[i]) == 0:
            persianNumber += "۰"
        elif int(number[i]) == 1:
            persianNumber += "۱"
        elif int(number[i]) == 2:
            persianNumber += "۲"
        elif int(number[i]) == 3:
            persianNumber += "۳"
        elif int(number[i]) == 4:
            persianNumber += "۴"
        elif int(number[i]) == 5:
            persianNumber += "۵"
        elif int(number[i]) == 6:
            persianNumber += "۶"
        elif int(number[i]) == 7:
            persianNumber += "۷"
        elif int(number[i]) == 8:
            persianNumber += "۸"
        elif int(number[i]) == 9:
            persianNumber += "۹"
    return persianNumber


def convertToEnglish(number):
    englishNumber: str = ""
    for i in range(len(number)):
        if number[i] == "۰":
            englishNumber += "0"
        elif number[i] == "۱":
            englishNumber += "1"
        elif number[i] == "۲":
            englishNumber += "2"
        elif number[i] == "۳":
            englishNumber += "3"
        elif number[i] == "۴":
            englishNumber += "4"
        elif number[i] == "۵":
            englishNumber += "5"
        elif number[i] == "۶":
            englishNumber += "6"
        elif number[i] == "۷":
            englishNumber += "7"
        elif number[i] == "۸":
            englishNumber += "8"
        elif number[i] == "۹":
            englishNumber += "9"
    return englishNumber