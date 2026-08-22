import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import requests
import time
import pytest_playwright

def test_ui(page: Page):
    page.goto("https://test.staff-crm.cnett.ru/login")
    page.get_by_role("textbox", name="Электронная почта").click()
    time.sleep(1)
    page.get_by_role("textbox", name="Электронная почта").fill("yura.ulyanov.1997@mail.ru")
    time.sleep(1)
    page.get_by_role("textbox", name="Пароль").click()
    time.sleep(1)
    page.get_by_role("textbox", name="Пароль").fill("YU#2SVhoxU!I")
    time.sleep(1)
    #page.locator("#1E2n2vGJowd0OBKlUGT0j").check()
    #time.sleep(1)
    page.get_by_role("button", name="Войти").click()
    time.sleep(1)
    page.get_by_placeholder("Поиск...").click()
    time.sleep(1)
    page.get_by_placeholder("Поиск...").fill("Тестовый Ивано Вавич")
    time.sleep(1)
    page.locator("//*[@class='styles__searchButton__DrTvu btn btn-outline-primary']").click()
    time.sleep(1)
    page.get_by_role("link", name="Выход").click()