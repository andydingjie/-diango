self.bases.open_url("http://test-ro-cms.raykite.com/login") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='username']","13730367945") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='password']","Raydata666") 
time.sleep(5) 
self.bases.click("xpath","//*[@type='submit']") 
time.sleep(5) 
self.bases.click("css"," li:nth-child(5) > div.ant-menu-submenu-title") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='/formal$Menu']/li[2]") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/span/span") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/input","成都中科大旗科技股份有限公司") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[1]/div/div/div[2]/span/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='rc_select_3']") 
time.sleep(5) 
self.bases.click("xpath","//*[text()='Designer' and @class='ant-select-item-option-content']") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='rc_select_3']") 
time.sleep(5) 
self.bases.click("xpath","//*[text()='Runner' and @class='ant-select-item-option-content']") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='rc_select_3']") 
time.sleep(5) 
self.bases.click("xpath","//*[text()='二合一' and @class='ant-select-item-option-content']") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='rc_select_3']") 
time.sleep(5) 
self.bases.click("xpath","//*[text()='全部' and @class='ant-select-item-option-content']") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[1]/div/div/div[2]/span/button") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/span/span") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[2]/div/div/button[1]") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='authorizationType']") 
time.sleep(5) 
self.bases.click("css","body > div:nth-child(7) > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='number']","123123") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='activateTime']","2021-03-15") 
time.sleep(5) 
self.bases.send_keys("xpath","//*[@id='expireTime']","2021-12-31") 
time.sleep(5) 
self.bases.click("css","div.ant-modal-footer > div > button.ant-btn.ant-btn-primary") 
time.sleep(5) 
self.bases.click("xpath","//*[@id='root']/div/section/section/div/main/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input") 
time.sleep(5) 
self.bases.click("xpath","//button[.='导出数据']") 
time.sleep(5) 
self.bases.click("xpath","//li[.='全部']") 
time.sleep(5) 
这是错误的页面名称: 正式用户-授权管理,这是错误的页面元素名称: 取消导出，这是错误的步骤: 35,这是异常信息: 'bool' object has no attribute 'click'
click('css', "body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button:nth-child(1)") 
time.sleep(5) 
