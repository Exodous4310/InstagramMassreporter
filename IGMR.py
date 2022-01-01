from selenium import webdriver
import time
import pyautogui

#Print logo
print("""


██╗░██████╗░███╗░░░███╗██████╗░
██║██╔════╝░████╗░████║██╔══██╗
██║██║░░██╗░██╔████╔██║██████╔╝
██║██║░░╚██╗██║╚██╔╝██║██╔══██╗
██║╚██████╔╝██║░╚═╝░██║██║░░██║
╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝

""")

print("Pls note the tool is not slow or you pc is not slow i have\n kept sleep function in order to make it less laggy :)")

#change the postion of the chrome webdriver

driver = webdriver.Chrome(executable_path=r'C:\\Webdrivers\\chromedriver.exe')

#change the path in 'D:\server...'make sure to type chromedriver.exe in end

driver.get("https://instagram.com/")

time.sleep(3)

with open('usern.txt', 'r') as f:
    username = f.read()

username_textbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username_textbox.send_keys(username)
username_textbox.click()

with open('passw.txt', 'r') as f:
    password = f.read()

password_text = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_text.send_keys(password)
password_text.click()

login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

print("Sucessfully Logged in...")
print(f"you are logged in :- {username}")

time.sleep(10)

print("it will bypass all the not now options :)...")

notnow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notnow.click()

for i in range(1):
    pyautogui.click(x=676, y=574)

#if you are using firefox dont change anything...
#if you are using chrome change it to x=676, y=574

time.sleep(5)

print("Now wait 5 seconds till your browser loads everything")

time.sleep(10)

search = input("Enter the victim name it's case sensitive:- ")

print("Pls wait I am finding it make sure you have written it correct...\n")

time.sleep(4)

driver.get("https://instagram.com/"+search)

time.sleep(5)

report = driver.find_element_by_class_name('wpO6b  ')
report.click()

report_user = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/button[3]')
report_user.click()

time.sleep(3)
#for report user
for i in range(1):
    pyautogui.leftClick(x=639, y=479)

time.sleep(3)
#after report user
for i in range(1):
    pyautogui.click(x=728, y=402)

time.sleep(3)
#sucide and self injury report
for i in range(1):
    pyautogui.click(x=654, y=344)

time.sleep(3)

for i in range(1):
    pyautogui.click(x=681, y=501)

time.sleep(3)
#before submit
for i in range(1):
    pyautogui.click(x=651, y=613)

time.sleep(3)
#submit button
for i in range(1):
    pyautogui.click(x=681, y=607)

print("Thanks for using it :D\n")
print("Note:- I wont be  updating this tool\n")
print("Credits:- https://github.com/Exodous4310\n")

print("Now the Browser will close automatically After 10 seconds =) make sure you dont close the browser by yourself =D\n")

time.sleep(10)

driver.quit()