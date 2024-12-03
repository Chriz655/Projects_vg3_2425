import machine, neopixel
import time
np = neopixel.NeoPixel(machine.Pin(16), 8)

np[0] = (127, 0, 0) # set to red, half brightness
np[1] = (0, 127, 0) # set to green, half brightness
np[2] = (0, 0, 127)  # set to blue, half brightness
np[3] = (127, 0, 0) 
np[4] = (0, 127, 0) 
np[5] = (0, 0, 127)  
np[6] = (127, 0, 0) 
np[7] = (0, 127, 0) 

np.write() # Skriver verdiene til leds

time.sleep(10) # Venter 10 sekunder før en setter alle til 0 (av)
for n in range(len(np)):
    np[n] = (0,0,0)
np.write()

time.sleep(2) # Trenger noe tid på så skrive verdiene, så en må vente litt
np.write()
time.sleep(1)