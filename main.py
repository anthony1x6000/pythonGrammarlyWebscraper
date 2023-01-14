import requests, shutil, os, pyperclip, json, random, string, logging, sys, datetime, threading, base64
from selenium import webdriver
from contextlib import suppress
from time import sleep
from urllib.parse import urlparse
#############################################################
# \/\/ Webdriver & browser stuff \/\/
driver_path = 'drivers/chromedriver.exe'
chrome_path = 'drivers/browser/chrome.exe'
# chrome_path = 'drivers/browser/brave-portable.exe'
option = webdriver.ChromeOptions()
option.binary_location = chrome_path
option.add_argument("--disable-gpu, --window-size=640,480")
option.add_experimental_option("excludeSwitches", ["enable-logging"])
with suppress(Exception): # Load prefrences file
    with open('drivers/Preferences') as jsonFile:
        pref = json.load(jsonFile)
    option.add_experimental_option("prefs", pref)
# /\/\ Webdriver & browser stuff /\/\
# \/\/\/ Constants \/\/\/
siteSet = "https://www.grammarly.com/"
loggedIn = "https://app.grammarly.com/" # Logged in page, you can tell from the "app" subdomain.
tCount = 0
ranAlready = False
foundWorking = False
Debug = False
noscrape = False
# /\/\/\ Constants /\/\/\
print("Starting Script")
if (noscrape):
    print("!!!WARNING!!!")
    print(" noscrape is TRUE")
if (Debug):
    print("!!!WARNING!!!")
    print(" Debug is TRUE")
print("Starting browser...")
browser = webdriver.Chrome(executable_path=driver_path, options=option)
# \/\/\/ Classes & Def \/\/\/
def SiteScrape(siteList, xpath):
    global tCount
    global xPathTxt
    print("Starting to scrape...")
    try: 
        if (noscrape):
            raise Exception("  noscrape is True")
        if (foundWorking):
            raise Exception("  Already found working cookie.")
        domain = urlparse(siteList[0]).netloc
        print("Using site:", domain)
        for site in siteList:
            browser.get(site)
            print(" URL: ", browser.current_url)
            xPathTxt = browser.find_element_by_xpath(xpath) # Get cookie found in xpath provided
            print("Got text")
            Verify(xPathTxt.text)
            tCount += 1
        print("Scraped through %d page(s)" % tCount)
    except Exception as e:
        print("!!!EXCEPTION!!!")
        print("", e)
def Verify(verifyThis):
    global siteSet
    global foundWorking
    try:
        print("\nVerifying JSON cookie...")
        browser.get(siteSet)
        print("Importing cookie")
        cookieList = json.loads(verifyThis)
        for cookie in cookieList:
            browser.add_cookie({k: cookie[k] for k in {'name','value'}})
        print("Imported Cookie")
        browser.get(siteSet)
        print("\nChecking login status...")
        print("Current URL =", browser.current_url)
        print("================================")
        if (loggedIn == browser.current_url):
            print("URL OK, working.\n================================")
            pyperclip.copy(verifyThis)
            print("Copied cookie to clipboard.")
            foundWorking = True
            raise Exception('''
 _       __              __    _                                      __    _          ____                          __
| |     / /____   _____ / /__ (_)____   ____ _   _____ ____   ____   / /__ (_)___     / __/____   __  __ ____   ____/ /
| | /| / // __ \ / ___// //_// // __ \ / __ `/  / ___// __ \ / __ \ / //_// // _ \   / /_ / __ \ / / / // __ \ / __  / 
| |/ |/ // /_/ // /   / ,<  / // / / // /_/ /  / /__ / /_/ // /_/ // ,<  / //  __/  / __// /_/ // /_/ // / / // /_/ /  
|__/|__/ \____//_/   /_/|_|/_//_/ /_/ \__, /   \___/ \____/ \____//_/|_|/_/ \___/  /_/   \____/ \__,_//_/ /_/ \__,_/   
                                     /____/                                                                            
            ''')
        elif (loggedIn != browser.current_url):
            print("URL BAD, Cookie didn't work\n================================")
    except Exception as e:
        print("Exception:", e)
        browser.quit()
def dec64(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    return decoded_string.decode()
def postNum(): 
    onePath = '//*[@id="post-'
    twoPath = '"]/div/pre/code'
    pathPostNumbers = [109, 112, 115, 119, 121, 123]
    finalPaths = []
    count = 0
    for i in range(6): 
        finalPath = onePath + str(pathPostNumbers[count]) + twoPath
        count += 1
        finalPaths.append(finalPath)
    return finalPaths
def siteInit(baseurl, postXpath, urlCount, *countBypass):
    baseurl = dec64(baseurl)
    if noscrape:
        print("noscrape is", noscrape)
        return
    sites = []
    if (countBypass):
        count = countBypass[0]['ovride']
        finalURL = (baseurl % count)
        sites.append(finalURL)
    else:
        count = 1
        for i in range(urlCount):
            finalURL = (baseurl % (count))
            count += 1
            sites.append(finalURL)
    if not (foundWorking):
        SiteScrape(sites, postXpath)
# /\/\/\ Classes & Def /\/\/\
vcount = 0
# siteInit("URL", "XPATH", COOKIESITECOUNT)
siteInit("aHR0cHM6Ly9pbmZva2lrLmNvbS9ncmFtbWFybHktJWQ=", '/html/body/div[7]/div[2]/div/div[2]/div[1]/div/div[2]/pre/code', 4) # American (better) english is more common here.
siteInit("aHR0cHM6Ly93d3cubGlua3N0cmlja3MuY29tL2dyYW1tYXJseS1jb29raWVzLSVk", '/html/body/div[2]/section[1]/div/div[2]/div/div[4]/div/pre/code', 6)

print("Trying JS sites. May be slower with security risks.")
siteInit("aHR0cHM6Ly9mcmVlZmlyZXJldmlld3MuY29tL2dyYW1tYXJseS1jb29raWVzLSVkLXVwZGF0ZWQv", '/html/body/div[3]/div/div/div[1]/main/article/div/pre/div/div[1]/code', 1, {'ovride':1})
siteInit("aHR0cHM6Ly9mcmVlZmlyZXJldmlld3MuY29tL2dyYW1tYXJseS1jb29raWUtJWQtdXBkYXRlZC8=", '/html/body/div[3]/div/div/div[1]/main/article/div/pre/div/div[1]/code', 6)

# Other random sites
siteInit("aHR0cHM6Ly9ncGxzaHViLmNvbS9ncmFtbWFybHktY29va2llcy0lZA==", '/html/body/div[1]/div/div[1]/main/article/div/div/pre', 2)
siteInit("aHR0cHM6Ly90cnl0ZWNobmljYWwuY29tL3dvcmtpbmctZ3JhbW1hcmx5LWNvb2tpZXMtaG91cmx5LXVwZGF0ZWQtJWQ=", '//*[@id="primary"]/div/div/pre', 3) # Low priority - doesn't seem to work.
# \/\/\/ Final Section \/\/\/
if(foundWorking):
    print("Check your clipboard. Ctrl + V")
else:
    print("Could not find cookie.")
    print("May have hit an exception. Look at previous output or log. ")
print("Cleaning up...")
try:
    browser.quit()
    print(" Browser closed.")
except Exception as e:
    print(" Exception when running browser.quit():", e)
    if ('invalid' in str(e)):
        print('exception:', e)
print(" Script Finished.")
# /\/\/\ Final Section /\/\/\
