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


for categoryN in categoryNames:
    browser.get('https://www.acmicpc.net/problem/tag/' + categoryN)
    trs = browser.find_elements_by_css_selector('table#problemset tbody tr')


for tr in trs:
        bj_num = tr.find_element_by_css_selector('td.list_problem_id').text
        title = tr.find_element_by_css_selector('td:nth-child(2)').text
        solvers = tr.find_element_by_css_selector('td:nth-child(4)').text
        submitCnt = tr.find_element_by_css_selector('td:nth-child(5)').text
        solveRate = tr.find_element_by_css_selector('td:nth-child(6)').text
        print("{0} {1} {2} {3} {4}".format(bj_num, title, solvers, submitCnt, solveRate))
'''
