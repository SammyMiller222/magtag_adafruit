# Magtag - Project Selector

This is a fork from the original presented on [Adafruit](https://learn.adafruit.com/adafruit-magtag-project-selector).

## Notes on Setup

- That `.gitignore` file is very important and something I originally forgot to add. It tells which file not to share in your repo. In our case we do not want our WI-FI information online via the `secrets.py` file. 🤦

- Some of the projects use online Application Programming Interfaces (APIs). Which is a fancy way of saying a way to access something, usually data. Some of these APIs require setting up a free account and generating keys. This includes: `'openweather_token'` and `'openweather_location'`.

- Some of the data and setup is customized to how *I like it*! e.g. The weather app is using `Barrie, CA` and set metric to `True` in the `weather.py`. As well I like the order of the applications listed in `code.py`, but this can always be changed.

- I manually edited the `bmp/year.bmp` icon from `2020` to `2021` using a free paint app, [GIMP](https://www.gimp.org/).

- Some of these apps can and *WILL BE* changed to something more useful for me. Consider this the *beta* version.

- After some constant deleting and tweaking files I ran out of the very little space available on the Magtag. Ended up using a free app called [Clean My Drive 2](https://macpaw.com/cleanmydrive). This was based on a suggestion someone mentioned on [StackExchange](https://apple.stackexchange.com/questions/6707/how-to-stop-os-x-from-writing-spotlight-and-trash-files-to-memory-cards-and-usb).

## Dumping this Repo onto the Magtag

Until I can find someone to tell me a more efficient way here's my suggestion:

1. Start over with loading [CircuitPython](https://learn.adafruit.com/adafruit-magtag-project-selector/install-circuitpython)

    a. Hit the reset button twice.
    b. You should see `MAGTAGBOOT` in Finder.
    c. Dump that `adafruit-circuitpython-adafruit_magtag_2.9_grayscale-en_US-x.x.x.uf2` file onto `MAGTAGBOOT`.
    d. You might see a normal error, but `CIRCUITPY` should show up in Finder.

2. Copy the repo files and directory one at a time.
3. Use [Clean My Drive 2](https://macpaw.com/cleanmydrive) between copies.

Sadly this device has only about __1 MB__ of on-board storage, so slowly copying things over are required as there appears to be __*junk*__ and temporary files generated if you try a quick dump.

### How to Use Magtag

I did not understand the instructions on the original project website and really have to read through some of the code.

So I'll try to do better.

1. Restart the Magtag with `reset` button.

2. Hold any of the buttons down.

3. Menu with 8 icon squares should pop up.

4. Navigate to the icon you want using the arrow buttons.

5. Hold down first and last buttons for 5 seconds. Sometimes you have to try a few times.

6. If you reset again without holding a button the last selected project will be opened. __IF__ there's a problem with loading something, you will get the first project in the list. I had to change the order one at a time to confirm each project loaded correctly and worked as intended.  
