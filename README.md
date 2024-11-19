# SmartBatteryController

This python script uses the psutil library to read the battery percentage of the laptop.
A donut battery indicator is used to display the current battery level on a small window.
The color of the donut changes based on the battery level.
Red: below 25% 
Orange: below 50%
Green: above 51%

The script enables automatic device charging with the use of TP-Link TapoP100 Smart Plug.
P100 firmware is the updated 1.2.1 version.
For this to work install and use the updated module from https://github.com/almottier/TapoP100

When battery level reaches 20%, the plug is activated enabling charghing.
When the battery level reaches 80%, the plug is turned off.
0.6 of a full charge cycle is maintained. Prolonging battery's life.

The program checks the battery level every 5 seconds to update the GUI.
The program checks if the plug needs to be turned on/off every 30 seconds.

Charging settings can be adjusted for different target objectives.
