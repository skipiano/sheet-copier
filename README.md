# sheet-copier
Copy two google sheets from each other

## Instructions

*Note: currently only supported on MacOS*

1. [Install python](https://www.python.org/ftp/python/3.10.7/python-3.10.7-macos11.pkg)
2. Open the terminal window by searching the spotlight.

![Terminal](https://i.imgur.com/MLhmGxe.png)

3. Install the required dependency by running the following command on terminal:
```bash
$ pip install pynput
```
4. Open the source airtable and the destination google sheet on tab 1 and 2 respectively. Make sure both of the cells are at the top left corner where the copying should start.

![Tabs](https://i.imgur.com/z3tJtM7.png)

5. Download the zip file of this repository: `Code > Download ZIP`
![Download](https://i.imgur.com/7UzQbiU.png)

6. Go to `Settings > Security & Privacy & Accessibility` and grant permission to `Python`.
![Settings](https://i.imgur.com/iq2e3Nf.png)

7. Open the file `main.py` with the IDLE application.
![IDLE](https://i.imgur.com/zUKCOoz.png)

8. **Make sure you are on the source airtable before starting the program!**
![Airtable](https://i.imgur.com/ZjJ9xk5.png)

9. `Run > Run Module` to run the program. You will be prompted to enter the amount of rows you want to copy.
![Rows](https://i.imgur.com/jBssJj9.png)

11. You will have 5 seconds to click back onto your browser so that the program starts copying properly.
![Running](https://i.imgur.com/9sqoeqY.png)

12. Force quit IDLE if you want to stop the copying operation midway. (`Cmd + opt + esc`)
![Force Quit](https://i.imgur.com/6sTDpnz.png)