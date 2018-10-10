# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import aiohttp
# import lxml
# from bs4 import BeautifulSoup

# def main():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     driver.get("https://www.baidu.com")
#     #print(driver.page_source)
#     print(driver.page_source)
#     driver.close()


# if __name__ == '__main__':
#     main()
#     print(aiohttp.__version__)
#     soup = BeautifulSoup('<p>Hello</p>','lxml')
#     print(soup.p.string)

# def get_one_page():
#     a = 1
#     for i in range(5):
#         yield a
#         a = a * 2

# if __name__ == '__main__':
#     for item in get_one_page():
#         print(item)
#生成器yield也可以称为迭代器，用在函数中，当函数返回一个值后，生成器会保存当前位置，并开始迭代，
#等下次循环开始后，会从生成器的当前位置继续往下走，等生成新的可迭代值后，保留当前位置，这样往复循环下去
