# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT
# -------------------------------------------
# forked and modified: 2021 Paul Gamble 
import time
from adafruit_magtag.magtag import MagTag

# Change this to the hour you want to check the data at, for us its 8pm
# local time (eastern), which is 20:00 hrs
DAILY_UPDATE_HOUR = 20

# Replace with your country population
POPULATION = 38440000

# Set up where we'll be fetching data from
# Repelace with your country csv - https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/
DATA_SOURCE = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Canada.csv"

def parse_csv(raw_data):
    '''
    parses csv data from Our World in Data
    raw_data: raw csv data from github
    Returns: dictionary of the data
    '''

    # split the raw csv data string into a list of lines
    raw_data = raw_data.split('\n')

    # remove blank last line
    data = raw_data[:-1]

    for i in range(1,len(data)):
        # split each line of the csv into a list
        data[i] = data[i].split(',')

        data[i] = data[i][-3:]




    # intialize output dictionary
    vaccine_data = {}
    vaccine_data['date'] = raw_data[-2].split(',')[1]
    vaccine_data['total'] = int(data[-1][2])
    vaccine_data['last'] = int(data[-1][0]) - int(data[-2][0])
    vaccine_data['percent'] = (vaccine_data['total']/POPULATION) * 100

    if '"' in raw_data[-2]:
        vaccine_data['types'] = raw_data[-2].split('"')[1]
    else:
        vaccine_data['types'] = raw_data[-2].split(',')[2]

    return vaccine_data



magtag = MagTag(url=DATA_SOURCE)

# Title
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 10),
)

# Date stamp of info
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 40),
)
# Number vaccinated on last recorded date
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 60),
)
# Population
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 80),
)
# Total Vaccinated
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 100),
)
# Percent of Population Vaccinated
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(10, 120),
)


# updated time
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(245, 30),
    line_spacing=0.75,
)

magtag.graphics.qrcode(b"https://health-infobase.canada.ca/covid-19/vaccination-coverage/",
                       qr_size=2, x=225, y=55)

magtag.peripherals.neopixels.brightness = 0.1
magtag.peripherals.neopixel_disable = False # turn on lights
magtag.peripherals.neopixels.fill(0x0F0000) # red!

magtag.get_local_time()
try:

    # get data from the Our World in Data repository
    value = magtag.fetch()

    print("Response is", value)

    vaccine_data = parse_csv(value)

    print(vaccine_data)
    magtag.set_text("Canada Vaccinations", 0, False)
    magtag.set_text(f"Date:   {vaccine_data['date']}", 1, False)
    magtag.set_text(f"Last:   {vaccine_data['last']:,}", 2, False)
    magtag.set_text(f"Population:  {POPULATION}", 3, False)
    magtag.set_text(f"Fully Total:   {vaccine_data['total']:,}", 4, False)
    magtag.set_text(f"Percent:   {vaccine_data['percent']:.2f}%", 5, False)


    now = time.localtime()
    print("Now: ", now)

    # display the current time since its the last-update
    updated_at = "%d/%d\n%d:%02d" % now[1:5]

    magtag.set_text(updated_at, 6, True)

    # OK we're done!
    magtag.peripherals.neopixels.fill(0x000F00) # greten
except (ValueError, RuntimeError) as e:
    print("Some error occured, trying again later -", e)

time.sleep(2) # let screen finish updating

# we only wanna wake up once a day, around the event update time:
event_time = time.struct_time((now[0], now[1], now[2],
                               DAILY_UPDATE_HOUR, 0, 0,
                               -1, -1, now[8]))
# how long is that from now?
remaining = time.mktime(event_time) - time.mktime(now)
if remaining < 0:             # ah its aready happened today...
    remaining += 24 * 60 * 60 # wrap around to the next day
remaining_hrs = remaining // 3660
remaining_min = (remaining % 3600) // 60
print("Gonna zzz for %d hours, %d minutes" % (remaining_hrs, remaining_min))

# Turn it all off and go to bed till the next update time
magtag.exit_and_deep_sleep(remaining)
