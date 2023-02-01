from bs4 import BeautifulSoup
import requests, sys, re

recentX64Xpath = "/html/body/div[1]/div[5]/div/main/turbo-frame/div/div[3]/section[1]/div/div[2]/div/div[2]/div[1]/details/div/div/ul/li[3]/div[1]/a"
site = "https://github.com/ungoogled-software/ungoogled-chromium-windows/releases"
site = requests.get(site).content
soup = BeautifulSoup(site, 'html.parser')

mostRecent = soup.find('a', attrs={'class':'Link--primary'}).text

x64DL = f"https://github.com/ungoogled-software/ungoogled-chromium-windows/releases/download/{mostRecent}/ungoogled-chromium_{mostRecent}_windows_x64.zip"
print(x64DL)
# 109.0.5414.120-1.1

site = "https://chromedriver.chromium.org/downloads"
site = requests.get(site).content
soup = BeautifulSoup(site, 'html.parser')

closeEnough = str(mostRecent[:10])
exact = soup.find('a').text

webdriverMatches = []
for link in soup.find_all('a'):
    href = str(link.get('href'))
    if (closeEnough in href):
        webdriverMatches.append(link.get('href'))
URLpattern = "^https://chromedriver\.storage\.googleapis\.com/index\.html\?path=[0-9]+\.0[0-9]*\.[0-9]+\.[0-9]+/$"
versionPattern = "[0-9]*\.[0-9]+[0-9]*\.[0-9]+[0-9]*\.[0-9]+"
for i in webdriverMatches:
    reMatches = re.findall(URLpattern, i)
    if reMatches:
        webdriverFTP = i
        break
webdriverVersion = re.findall(versionPattern, webdriverFTP)
# https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_win32.zip
webdriverDL = f"https://chromedriver.storage.googleapis.com/{webdriverVersion[0]}/chromedriver_win32.zip"
print(webdriverDL)

with open("variables.txt", "w") as file:
    file.write(f"webdriverDL={webdriverDL}\n")
    file.write(f"x64DL={x64DL}\n")
    file.write(f"chromium=ungoogled-chromium_{mostRecent}_windows_x64.zip\n")
    file.write(f"driver=chromedriver_win32.zip\n")