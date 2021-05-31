# Minimal AR488 PCB

## Summary
This is a simple PCB that implements the minimum required circuitry for the AR488 using an Arduino Nano. In addtion this PCB was designed to be single sided with top copper for ease of fabrication on a cheap CNC router (1610 Pro). A capacitor in series with a slide switch was added to the Arduino Nano reset pin in order to disable to Arduino serial DTR reset function. 

## Fabrication
Flatcam was use to prepare all gcode based on the PCB gerbers/excellon. Since only top copper was used, no flipping/mirroring in flatcam was needed. Grblcontrol  (Candle) was used to send the gcode to the router. For isolation routing a 0.1mm 20deg engraver was used with cut depth of 0.12mm. The traces and spacing used in the design are close to the router's capability limits, and height mapping is absolutely required to acheive usable results. For holes and the cutout, a 0.8mm endmill was used with 0.8mm being the minimum hole size that was milled. 
