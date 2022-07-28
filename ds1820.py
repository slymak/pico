import machine, onewire, ds18x20, time, binascii
from machine import Pin
 
ds_pin = machine.Pin(17)
led = machine.Pin(25, Pin.OUT)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
 
  for rom in roms:
    print('{0} : {1}'.format(binascii.hexlify(rom), ds_sensor.read_temp(rom)))
 
  time.sleep(1)
  led.toggle()
  time.sleep(4)
  led.toggle()
