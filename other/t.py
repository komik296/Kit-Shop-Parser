import requests

url = "https://kitshop.ru/Common/Overview"
headers = {
    "Host": "kitshop.ru",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://kitshop.ru/Public/SignIn",
    "Connection": "keep-alive",
    "Cookie": "ASP.NET_SessionId=3njnx1w5gbc3vipd4gdqmrc5; .ASPXAUTH=17635B6F62413DC4921416F4A040FE13F92C9E7F484DA1B507ABC6967BAAE6B4B94C33042B24E1AF289B6FF6E044842E23BCC59011C5330747579B78F82DFAB06A2F3827394C71E889FB3B7C1CF59E178723A52004729A5A0831D812C51F44CBBF85D464EE7DFADA70523D9785E2848EB1EEF8958EFA7A2A7894C1555744F445",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

response = requests.get(url, headers=headers)

with open('file_site.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
