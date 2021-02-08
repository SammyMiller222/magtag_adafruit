# Magtag - Project Selector

This is a fork from the original presented on [Adafruit](https://learn.adafruit.com/adafruit-magtag-project-selector).

### Notes on Setup

- That `.gitignore` file is very important and something I originally forgot to add. To tells which file not to share in your repo. In our case we do not want our WI-FI information online. 🤦

- Some of the projects use online Application Programming Interfaces (APIs). Which is a fancy way of saying a way to access something, usually data. Some of these APIs require setting up a free account and generating keys. I will share my `secrets.py` on the next Zoom call, which now includes: `'openweather_token'` and ` 'openweather_location'`.

- Some of the data and setup is customized to how *I like it*! e.g. The weather app is using `Barrie, CA` in the `weather.py`. As well I like the order of the applications listed in `code.py`, but this can always be changed.

- I manually edited the `bmp/year.bmp` and change the 2020 to 2021 using a free paint app, [GIMP](https://www.gimp.org/).

- Some of these apps can and *WILL BE* changed to something more useful. Consider this the *Beta* version.

- After some constant deleting and tweaking files I ran out of the very little space available on the Magtag. Ended up using a free app called [Clean My Drive 2](https://macpaw.com/cleanmydrive). This based on a suggestion someone mentioned on [StackExchange](https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb).

### How to Use Magtag 

I did not understand the instructions on the website and really have to read through some of the code.

So I'll try to do better.

1. Restart the Magtag with `reset` button.

2. Hold any of the buttons down.

3. Menu with 8 icon squares should pop up.

4. Navigate to the icon you want.

5. Hold down first and last button for 5 seconds. Sometimes you have to try a few times.

6. If you reset again and not holding a button the last selected will be opened.

