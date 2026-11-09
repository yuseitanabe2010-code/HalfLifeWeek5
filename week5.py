import network
import time
from machine import Pin, SPI
import st7789
import urequests

SSID = "DECO1"
PASSWORD = "Tanabe@2017"
SERVER_URL = "http://192.168.68.103:5000/now-playing"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

spi = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
display = st7789.ST7789(
    spi, 240, 280,
    reset=Pin(4, Pin.OUT),
    dc=Pin(1, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    rotation=0
)
Pin(6, Pin.OUT).value(1)
display.init()
display.fill(0)

while True:
    try:
        response = urequests.get(SERVER_URL)
        data = response.json()
        response.close()

        title = data["title"]
        artist = data["artist"]
        curr_str = data["curr"]
        tot_str = data["total"]
        ratio = data["ratio"]

        display.fill(0)
        display.text(st7789.font.sysfont, title, 15, 60, 0xFFFF, 0)
        display.text(st7789.font.sysfont, artist, 15, 100, 0x8410, 0)

        display.rect(20, 160, 200, 12, 0xFFFF)
        filled_width = int(198 * ratio)
        unfilled_width = 198 - filled_width

        if filled_width > 0:
            display.fill_rect(21, 161, filled_width, 10, 0x07E0)
        if unfilled_width > 0:
            display.fill_rect(21 + filled_width, 161, unfilled_width, 10, 0x8410)

        display.text(st7789.font.sysfont, curr_str, 20, 176, 0x8410, 0)
        display.text(st7789.font.sysfont, tot_str, 188, 176, 0x8410, 0)
    except Exception:
        pass

    time.sleep(1)
