from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.github.com")

signinbutton = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signinbutton.click()

username = driver.find_element_by_xpath('//*[@id="login_field"]')
name=input("enter username:")
username.send_keys(name)

pass_word = driver.find_element_by_xpath('//*[@id="password"]')
password=input("enter password:")
pass_word.send_keys(password)

final_signin = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

driver.get("https://github.com/new")
repo_name = input("Enter Repository name:")
rep=driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(repo_name)

driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()

