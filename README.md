# SmartBatteryController


<img align="left" src="https://github.com/user-attachments/assets/ea4e35a4-cf34-438e-9211-b5f07d635285">

&nbsp; This python script uses the psutil library to read the battery percentage of the laptop.

&nbsp; A donut battery indicator is used to display the current battery level on a small window.

&nbsp; The color of the donut changes based on the battery level.
<br clear="left"/>
<br>
Red: below 25% | 
Orange: below 50% | 
Green: above 51%


The script enables automatic device charging with the use of TP-Link TapoP100 Smart Plug.

P100 firmware is the updated 1.2.1 version.

For this to work install and use the updated library from https://github.com/almottier/TapoP100

When battery level reaches 20%, the plug is activated enabling charghing.

When the battery level reaches 80%, the plug is turned off.

0.6 of a full charge cycle is maintained. Prolonging battery's life.

The program checks the battery level every 5 seconds to update the GUI.

The program checks if the plug needs to be turned on/off every 30 seconds.

Charging settings can be adjusted for different charge cycles objectives.

## Main Requirements
* Tapo P100 Smart Plug
* Laptop Charger
* Network Access
* PyP100 Library
* psutil Library

## Installation
* Install PyP100 library by Almottier using:
```bash
pip install git+https://github.com/almottier/TapoP100.git@main
```
* Adjust the code with yours and device's credentials

* Connect to the same Network

* Execute The Program

## Usage
Run script from Terminal:
```bash
python3 ./SmartBatteryController.py
```
Make it into a Windows Executable:
```bash
pyinstaller --clean --noupx --onefile --windowed --icon=battery.ico SmartBatteryController.py
```
The executable is stored inside /dist folder

