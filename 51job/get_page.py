import time
from playwright.sync_api import Playwright, sync_playwright
from db import MongoFunc

IS_PAGE_NORMAL = True

def run(playwright: Playwright) -> None:
    global IS_PAGE_NORMAL

    mongodb = MongoFunc()

    # browser = playwright.chromium.launch(headless=False)
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    while True:
        next_page_index = mongodb.get_next_index()
        if next_page_index == 0:
            # 已经全部获取完毕
            break
        next_page_url = f"https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25B8%25BB%25E6%2592%25AD,2,{next_page_index}.html?lang=c"
        page.goto(next_page_url)
        #page.get_by_role("listitem").filter(has_text=str(NOW_PAGE)).locator("a").click()
        page.wait_for_load_state('networkidle')
        if '滑动验证页面' in page.content():
            IS_PAGE_NORMAL = False
            input('WAIT TO PASS')
            page.wait_for_load_state('networkidle')

        mongodb.insert_html(page.content(),next_page_index)
        time.sleep(3)

    # ---------------------
    context.close()
    browser.close()

    print('ALL DONE')

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)

