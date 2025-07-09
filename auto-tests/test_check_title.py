#  Условие: Написать тест, который открывает веб-страницу https://playwright.dev/ и
#  проверяет что заголовок страницы соответствует ожидаемому значению.
#  Тест необходимо запустить минимум на 2 разных браузерах.
#  Ожидаемый результат: Тест успешно проходящий проверку заголовка.


import pytest
from playwright.sync_api import sync_playwright, expect

# Параметризуем тест для запуска в Chrome, Firefox и WebKit
@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_check_title(browser_name: str) -> None:
    # Запускаем Playwright
    with sync_playwright() as playwright:
        # Получаем тип браузера
        browser_type = getattr(playwright, browser_name)

        # Запускаем браузер (в режиме с GUI)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Переходим на сайт
            page.goto("https://playwright.dev/")

            # Ожидаемый текст заголовка
            expected_text = "Playwright enables reliable end-to-end testing for modern web apps."

            # Ищем заголовок по селектору и проверяем его текст
            locator = page.locator("h1.hero__title")
            expect(locator).to_have_text(expected_text)

        finally:
            # Закрываем контекст и браузер даже в случае ошибки
            context.close()
            browser.close()