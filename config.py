from datetime import date

AUTHORIZATION = {'ЮМВенд-74': ('SHOPCHEL', 'SHOPCHEL23'),
                 'ЮМВенд-Тюмень': ('SHOPTUM', 'SHOPTUM23'),
                 'ЮМВенд-Омск': ('SHOPOMSK', 'SHOPOMSK23'),
                 'ЮМВенд-Новосиб': ('SHOPNSK', 'SHOPNSK23'),
                 'ЮМВенд-Урал': ('SHOPEKB', 'SHOPEKB23')
}



cookies_affiliates = {
                 'ЮМВенд-74': 0,
                 'ЮМВенд-Тюмень': 0,
                 'ЮМВенд-Омск': 0,
                 'ЮМВенд-Новосиб': 0}
                 #'ЮМВенд-Урал': 0
#}

table_name_revenue_and_sales_per_day = {
    'ЮМВенд-74': 'revenue_sales_daily_74',
    'ЮМВенд-Тюмень': 'revenue_sales_daily_tyumen',
    'ЮМВенд-Омск': 'revenue_sales_daily_omsk',
    'ЮМВенд-Новосиб': 'revenue_sales_daily_novosibirsk',
    'ЮМВенд-Урал': 'revenue_sales_daily_ural'
}


currency_date_update = {
    'ЮМВенд-74': date.today(),
    'ЮМВенд-Тюмень': date.today(),
    'ЮМВенд-Омск': date.today(),
    'ЮМВенд-Новосиб': date.today(),
    'ЮМВенд-Урал': date.today()
}

affiliates_id = {
                 'ЮМВенд-74': 5,
                 'ЮМВенд-Тюмень': 4,
                 'ЮМВенд-Омск': 3,
                 'ЮМВенд-Новосиб': 2,
                 'ЮМВенд-Урал': 1
}

affiliates_utc = {
                 'ЮМВенд-74': 5,
                 'ЮМВенд-Тюмень': 5,
                 'ЮМВенд-Омск': 6,
                 'ЮМВенд-Новосиб': 7,
                 'ЮМВенд-Урал': 5
}


filter_params = {
    "filter.UpDateString": "",
    "filter.ToDateString": "",
    "filter.SubCompanyId": "0",
    "filter.ShopId": "0",
    "filter.DeviceId": "0",
    "filter.PayType": "0",
    "filter.FiscalSign": "-1",
}


db_config = {
    'host': '80.85.242.53',
    'user': 'admin',
    'password': 'eZPLh#jLHctng8cN',
    'database': 'kit_shop_umvend',
    'port': '3306',  # По умолчанию 3306
}

headers_cookie = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": r"\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": r"\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

headers_sign_in = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Content-Length": "94",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://kitshop.ru",
    "Referer": "https://kitshop.ru/Public/SignIn",
    "Sec-Ch-Ua": r"\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": r"\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://kitshop.ru/Public/SignIn',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

payload_captcha = {
    'login': '',
    'password': '',
    'attemp': '',
    'myCaptcha': ''
}

headers_token = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '76',
    'Origin': 'https://vending.kit-invest.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://vending.kit-invest.ru/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers'
}

payload_token = {
    'login': '',
    'password': '',
    'token': ''
}