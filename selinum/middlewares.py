from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from scrapy.http import HtmlResponse

class SeleniumMiddleware:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

    def process_request(self, request, spider):
        url = request.url
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='dataContent']/thead/tr[2]/td[3]"))

            )
        except Exception as e:
            spider.logger.info(f"Error occurred while waiting for page to load: {e}")

        # 获取加载完成后的页面内容
        data = self.driver.page_source
        response = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
        return response

    def close_spider(self, spider):
        spider.logger.info('Closing spider and attempting to shut down browser...')
        try:
            self.driver.quit()
            spider.logger.info('Browser closed successfully')
        except Exception as e:
            spider.logger.info(f'Failed to close browser: {e}')
