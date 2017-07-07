#!/usr/bin/python
city = 'raipur'
from Tkinter import *

from weather import Weather

weather = Weather()
location = weather.lookup_by_location(city)
condition = location.condition()
astronomy = location.astronomy()
cel = (int(condition['temp']) - 32) * (5.0 / 9.0)
cel = round(cel, 1)
cel = str(cel)
root = Tk()
root.wm_title(" ")
w = 130
h = 100
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws) + (w / 5)
y = -(hs) + (h / 5)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background="black")
label_city = Label(root, text="City-" + city.upper(), fg='white', bg='black')
label_text = Label(root, text="Weather-" + condition['text'], fg='white', bg='black')
label_temp = Label(root, text="Temprature-" + cel + u'\u00b0' + "C", fg='white', bg='black')
label_sunrise = Label(root, text="Sunrise-" + astronomy['sunrise'], fg='white', bg='black')
label_sunset = Label(root, text="Sunset-" + astronomy['sunset'], fg='white', bg='black')
label_city.grid(row=0, column=0, sticky=W)
label_text.grid(row=1, column=0, sticky=W)
label_temp.grid(row=2, column=0, sticky=W)
label_sunrise.grid(row=3, column=0, sticky=W)
label_sunset.grid(row=4, column=0, sticky=W)
root.mainloop()
