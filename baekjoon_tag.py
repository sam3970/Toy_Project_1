#!/usr/bin/python3

# -*- coding:utf-8 -*-

from selenium import webdriver

backJoonCategoryUrl = "https://www.acmicpc.net/problem/tags";

#Path Selection
path='/home/chromedriver'
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')

# selenium webdriver
browser = webdriver.Chrome(executable_path="/home/chromedriver",chrome_options=chrome_options)

# 문제 분류 초기페이지
browser.get(backJoonCategoryUrl);

# 카테고리 tr태그 한 줄 묶음으로 분류
categorys = browser.find_elements_by_css_selector('table.table.table-bordered.table-striped tbody tr');

categoryNames = []
for category in categorys:
    categoryName = category.find_element_by_css_selector('td > a').text
    categoryNames.append(categoryName)

print(categoryNames)
