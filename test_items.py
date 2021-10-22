# import pytest
# from selenium import webdriver
import time
# import math

# В коде реализован выбор языка для Chrome, так как это является достаточным для задания (см. п.5)
# В обновлении Chrome присутсвует баг, из-за чего в логе выполнения отображаются записи об
# ошибках "DevTools listening on ws..", если раскомментировать ожидание. На само прохождение теста не влияет

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket_button(browser):
    browser.get(link)
    # Расскоментировать time.sleep(30) для проверки задания (см. критерии проверки п.2)
    # time.sleep(30)
    button = browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    button_text = button.text
    # с помощью assert проверяем наличие кнопки, в случае отсутсвия появится сообщение 'Not Found'
    assert button_text is not None, 'Not Found'
