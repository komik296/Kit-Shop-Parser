import re
import time

from bs4 import BeautifulSoup
import lxml
import requests

from auth.ru_captcha import sender_solve, report_captcha, coorect_captcha
from auth.captcha import capthca_install
from config import headers, payload_captcha, headers_token, payload_token, cookies_affiliates, headers_sign_in, headers_cookie



url_sign = 'https://kitshop.ru/Public/SignIn'
url_sign_token = 'https://kitshop.ru/Public/SignIn'


def authorizetion(login, password, affiliate):
    if 'Cookie' in headers_sign_in:
        del headers_sign_in['Cookie']

    req = requests.get(url_sign, headers=headers_cookie)

    soup = BeautifulSoup(req.text, 'lxml')
    challenge_guid = soup.find('img', id='myCaptcha').get('src').lstrip('CaptchaImage/Render?challengeGuid=')
    cookie = f'ASP.NET_SessionId={req.cookies.values()[0]}'

    capthca_install(challenge_guid, cookie)

    headers_sign_in['Cookie'] = cookie
    payload_captcha['login'] = login
    payload_captcha['password'] = password
    payload_captcha['myCaptcha'] = challenge_guid
    payload_captcha['attemp'] = sender_solve()


    req_sign = requests.post(url_sign, headers=headers_sign_in, data=payload_captcha, allow_redirects=False)
    text_sign = req_sign.text

    if req_sign.status_code != 302:
        while 'Символы с картинки введены неверно' in text_sign or 'Превышено число неудачных попыток входа' in text_sign or req_sign.status_code == 200:
                report_captcha()

                capthca_install(challenge_guid, cookie)
                payload_captcha['attemp'] = sender_solve()
                req_sign = requests.post(url_sign, headers=headers_sign_in, data=payload_captcha, allow_redirects=False)
                text_sign = req_sign.text

                if 'Превышено число неудачных попыток входа' in text_sign:
                    print('Ошибка (Превышено число неудачных попыток входа)')
                    time.sleep(600)


        if 'Ой! Во время запроса произошла ошибка' in text_sign:
            raise ValueError('Ой! Во время запроса произошла ошибка')

    coorect_captcha()
    cookie += f'; {req_sign.cookies.keys()[0]}={req_sign.cookies.values()[0]}'
    cookies_affiliates[affiliate] = cookie
    print(cookie)


