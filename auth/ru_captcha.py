from twocaptcha import TwoCaptcha


solver = TwoCaptcha('e92882eb54763f3178b08a4feea0c053')

dict_resut = {}

def sender_solve(path='other/captcha_image.jpg'):
    print('2) Изображение отправленно для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ: ', result)
    #API вернёт словарь {'captchaId': '72447681441', 'code': 'gbkd'}
    #Обновляем словарь для дальнейшего извлечения ID капчи и отправки репорта
    dict_resut.update(result)
    return result['code']

def coorect_captcha():
    print(f"Отправлен репорт о успешном разгадывании. id:{dict_resut['captchaId']}")
    solver.report(dict_resut['captchaId'], True)

def report_captcha():
    print("Капча решена не верно, повторяем попытку")
    # Репортим о неудачной попытки разагадать капчу
    print(f"Отправлен репорт о не успешной попытке. id:{dict_resut['captchaId']}")
    solver.report(dict_resut['captchaId'], False)