# Python 3 Cookie Webscraper | Windows x64 |

```
 __   _ _____ _  _  _   
 | \  ||     ||  |  |   
 |  \_||_____||__|__|   
 _  _  _ _____  _______     ________   _ ______  /
 |  |  ||     ||_____/|____/   |  | \  ||  ____ / 
 |__|__||_____||    \_|    \___|__|  \_||_____|.  
```

## Disclaimer

This script is for educational purposes only.
Script is intended to demonstrate the capabilities of webscraping.

# Setup

Steps for using this script.

## Executable

Download ``compiledEXE-Win64.zip`` in the [most recent release](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/releases/), extract it, and then run ``webscraperGrammarly.exe`` You may need to allow the program firewall access if you experience connection problems. You can also look at the [successful builds](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/actions/workflows/compileWin.yml?query=is%3Asuccess) and download the zip from there. [Download guide (download compiledEXE-Win64.zip)](https://files.catbox.moe/9eg2sh.webp).

## Importing cookies

Download a JSON cookie editor like [Cookie-Editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) on chrome web store. Firefox users will have to rethink their life decisions.

Then watch this video:

[![thumb](https://cdn.jwplayer.com/v2/media/hJQTmCmA/thumbnails/qDdGYZP3.jpg)](https://jwp.io/s/AwuwkVsG)

# Config.json

Config.json in drivers provides some settings you can toggle.

Here is a brief explaination of what the main settings do:

- nosplash: "true" removes the [splash screen](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/blob/main/build/ico.png) from showing on start. Default is "false" because I like the picture.
- headless: "false" makes the script show a browser window of the script testing out cookies. Default is "true" because it looks cooler with just a terminal window. Setting to "false" headless may increase performance on some machines.
- w{Height/Width}: Sets the height and width of the browser window. The setting don't matter if headless is set to "true."

# Other Installation Methods

Other ways to install and use this script.

## Compiled Python install

You will need to have [python installed](https://www.python.org/downloads/). Probably python 3.10.

Download and extract ``compiled-Win64.zip`` in the most recent [release](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/releases), extract, run ``run pip install -r requirements.txt``, and then run ``main.py``

You can also look at the [successful builds](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/actions/workflows/compileWin.yml?query=is%3Asuccess) and download the zip from there. [Download guide](https://files.catbox.moe/9eg2sh.webp).

## Alternatively,

1. Install a chromium-based browser. For example, [ungoogled-chromium for windows](https://github.com/ungoogled-software/ungoogled-chromium-windows/releases). Download the windows_x64 package and put the contents of the zip into 'drivers/browser'
2. Update chrome_path within main.py to match your chromium-based browser bianary executable. You can probably skip this step if you followed the second half of the previous one.
   1. To find a browser path, search your browser within Windows search, open the file location until you get an executable, not a link.
3. Go to the [ChromeDriver website](https://chromedriver.chromium.org/downloads) and install the proper chromedriver for your browser version. To find your browser version go to [chrome://settings/help](chrome://settings/help) and [look at the version number for Chromium](https://files.catbox.moe/ukxxjn.png).
   1. If you're downloading ungoogled-chromium:
   2. ![image1](https://files.catbox.moe/am62um.png)
4. Place chromedriver.exe within the drivers path, or anywhere, just make sure to update the driver_path within main.py
5. After running the script, import the cookies into grammarly.com with an extension like [cookie-editor](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm).
   1. I recommend downloading the Microsoft Word Grammarly addon and then logging into the account there so you don't have to deal with people logging out.

## Requirements.txt

To download python requirements send ``pip install -r requirements.txt``

## dont pay

I can assure you there are more worthwhile investments for your money than a glorified keylogger. Hopefully, another privacy oriented service is able to replace this.

```
Government agencies, regulators, and other authorized third parties. We may disclose your information to governmental agencies, regulators, and other third parties if we determine that such disclosure is reasonably necessary to (a) comply with any applicable law, regulation, legal process, or appropriate governmental request; (b) protect any person from death or serious bodily injury; (c) prevent fraud, harm, or abuse of Grammarly or our users; or (d) perform a task carried out in the public interest.
```

<div>
<img src="https://files.catbox.moe/9h2th9.png" height=100 /><img src="https://files.catbox.moe/af1wbx.jpg" height=100 />
</div>

# License

See [LICENSE](https://github.com/anthony1x6000/pythonGrammarlyWebscraper/blob/main/LICENSE)

```
This repository is under the GNU Affero General Public License v3.0 license. 
   Written by anthony1x6000 and Contributors, 2023
```
