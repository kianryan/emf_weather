from tidal import *
from . import config
import vga2_8x8 as font

from app import App

import urequests
import wifi

class MyApp(App):

    TITLE = "Weather App" # if defined, adds a title bar to the window. Edit later with self.window.set_title()

    def update_weather(self):
	json = self.try_fetch_weather_json()
	if (json):
            current_weather = json['current']['weather'][0]
	    next_weather = json['hourly'][12]['weather'][0]

	    # Clear display and show now/next weather
            self.draw_image(current_weather['icon'], 0)
            lines = self.split_lines(f'Now: {current_weather["description"]}', 17)
	    print (lines)
            self.update_display(0, lines)
            self.draw_image(current_weather['icon'], 120)
            lines = self.split_lines(f'Next: {next_weather["description"]}', 17)
            print (lines)
            self.update_display(120, lines)
        else:
            self.update_display(0, ['Unable to fetch'])

    def try_fetch_weather_json(self):

	print('Connecting to Wifi')
	if not wifi.status():
            wifi.connect()
            wifi.wait()
	    print('Wifi connected')
        if not wifi.status():
            print('No wifi')
            return None

        url = f'http://api.openweathermap.org/data/2.5/onecall?lat={config.lat}&lon={config.lon}&units=metric&appid={config.api_key}'
        response = urequests.get(url)
        json = response.json()
	wifi.disconnect()
	print('Return response')
	return json

    def split_lines(self, line, max_length):
        lines = []
        words = line.split(' ')
        line = ''
        for word in words:
            if len(line + ' ' + word) > max_length:
                lines.append(line[:-1])
                line = ""
            line = line + word + ' '
        lines.append(line[:-1])
        return lines

    def update_display(self, y, lines):
	for idx, line in enumerate(lines):
                ypos = (font.HEIGHT + 1) * idx + y
		display.text(font, line, 0, ypos, BLUE, WHITE)

    def draw_image(self, icon, y):
	display.jpg(f'/apps/emf_weather/jpg/{icon}.jpg', 0, y)

    def on_activate(self):
	super().on_activate()
	display.fill(WHITE)
	self.update_display(0, ['Loading...'])
        self.update_weather()

main = MyApp
