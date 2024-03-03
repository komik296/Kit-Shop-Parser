import requests


def capthca_install(challenge_guid, cookie):
    url = 'https://kitshop.ru/CaptchaImage/Render'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://kitshop.ru/Public/SignIn',
        'Cookie': cookie,
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }

    update_captcha(challenge_guid, cookie)

    response = requests.get(url, params={'challengeGuid': challenge_guid, 'rand': '0.31423'}, headers=headers)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Если запрос успешен, сохраняем изображение капчи в файл
        with open('other/captcha_image.jpg', 'wb') as f:
            f.write(response.content)
        print('Изображение капчи успешно сохранено в файл captcha_image.jpg')
    else:
        print('Произошла ошибка при загрузке изображения капчи:', response.status_code)


def update_captcha(challenge_guid, cookie):
    url = 'https://kitshop.ru/Public/ChangeCaptcha/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'TE': 'trailers'
    }

    params = {'challenge': challenge_guid,
              '_': 1707558718590}

    requests.get(url, params=params, headers=headers)


