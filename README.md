# Reflectify
## A Setup for a Smart Mirror, based on Raspberry Pi Model 4B, Tkinter and Arduino
The intention was to build up a mirror and add the capability of taking pictures using a raspberry pi camera option as well as enable access to subprocesses like YouTube, SoundCloud, Spotify, and daily news. The project, however, was also not restricted to these options; there was an interest in making it user-friendly by adding a keyboard, speaker, and the ability to detect when someone is close enough to the mirror in order to show welcoming messages.

![Frontal Setup](https://github.com/sparklingPusher/Reflectify/blob/main/Images/Full_Setup_Front.jpg)

## Objectives
The project's primary goals and what they will accomplish are listed below, taking into account the aforementioned motivations:

* Continuous Visualization
   * Location
   * Current Weather
   * Forecast Weather
* Human Detection Visualization
   * Day, Date, Time
   * Room Temperature and Humidity
   * CPU Temperature
   * Functional Buttons
   * Greeting Messages
* Physical Devices
  * Mouspad
  * Speaker
  * Camera
* Button Deliveries
  * Youtube
  * News
  * SoundCloud
  * Spotify
  * Camera
  * Keyboard
  * Reboot
  * End Program


## Hardware and Sotware Components
### Hardware Components
Depicted below, the individual components and connections
![Hardware](https://github.com/sparklingPusher/Reflectify/blob/main/Images/Hardware_Components.png)

### List of Hardware Components
| Description | Component |
| --- | --- |
| Microcontroller | Arduino Uno |
| Microcontroller / PC | Raspberry Pi Model 4B |
| Ultrasonic Sensor | HC-SR04 |
| Temperature/Humidity Sensor | DHT20 |
| Cooling Fan | GeekPi Raspberry Pi 4 Fan |
| Touchpad | Perixx PERIPAD-504 |
| Speaker | HEANTTV Speaker 5.3 Soundbar |
| Monitor | Caixun 27 Inch Monitor 100 Hz |
| Mirror | Costum Order, Spy Glas |
| Camera | Raspberry Pi Cam 5 MP |
| Mirror Frame | Costum Order |

### Software Components
Below, the architecture of the software is shown. This includes the main, the MVC pattern architecture, and the individual subprocesses that can be triggered via the view.
![Software](https://github.com/sparklingPusher/Reflectify/blob/main/Images/Software_Components.png)

## Arduino Setup

For the implementation of the reading of the sensors platform.io was used, which can be integrated into the development environment of Visual Studio Code. For this purpose, the following parameters must be taken into account:
| Variable | Setting |
| --- | --- |
| Platform | atmelavr |
| Board | uno |
| Framework | Arduino |
| Lib_deps | dfrobot/DFRobot_DHT20@^1.0.0 |

## Raspberry Setup
### Update, upgrade and delete unnecessary parts:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt autoremove
```
### Create desktop file for autostart
```
nano ~/.config/autostart/reflectify.desktop
```
And fill in the following settings:
```
[Desktop Entry]
Type=Application
Name=Your Program Name
Exec=bash -c "sleep 3; /usr/bin/python3 /home/your_path.py"
Name[en_GB]=reflectify
```
### Dynamic menu bar of Raspberry
Panel Preferences → automatic hiding → minimize
when not in use → size when minimized: 0
### Install PyQt5
```
sudo apt install python3-pyqt5
sudo apt-get install build-essential pyqt5-dev pyqt5-dev-tools python3-pyqt5.qtwebkit
```
### Trigger background windows
```
sudo apt-get install wmctrl
```
### Hide mouse if not in use
```
sudo apt-get install unclutter
unclutter -idle 0
```
### Disable screensaver
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
and insert
```
@xset -dpms
@xset s off
```
### Raspberry Camera
Interface Options → Legacy Camera → Enable
### Change right Click to paste
Since a virtual keyboard is programmed, a possibility must be found to store text and to be able to integrate this in the search bars of, for example, Soundcloud. For this purpose, the right mouse button of the touchpad is converted in the settings so that it functions as a "paste".
```
sudo apt-get install xbindkeys xclip
xbindkeys --defaults > $HOME/.xbindkeysrc
nano ~/.xbindkeysrc
```
and insert
```
"echo -n | xclip -o | xte 'keydown Control_L' 'key v' 'keyup Control_L'"
b:3
```
then run in terminal
```
pkill xbindkeys
xbindkeys
```
### Raspotify for Spotify
```
Curl -sSL https://dtcooper.github.io/raspotify/key.asc
echo 'deb https://dtcooper.github.io/raspotify raspotify main'
sudo tee /etc/apt/sources.list.d/raspotify.list
sudo apt install raspotify
```
## Interface
### Not triggered Interface
If the ultrasonic sensors are not recognizing an obstacle in front of the mirror, just the weather information will be shown.
![NotTriggered](https://github.com/SparkPusher/Reflectify/blob/main/Images/No_Trigger_Screen.png)
### Triggered Screen
If there is an obstacle, the following interface is shown.
![Triggered](https://github.com/SparkPusher/Reflectify/blob/main/Images/Triggered_Screen.png)
### Full Interface with Keyboard
To type into Soundcloud, Youtube etc., a virtual keyboard is programmed, that save the input in the clipboard. The clipboard can then be pasted with the setting explained above, to paste it with the right click on the touchpad.
![Keyboard](https://github.com/SparkPusher/Reflectify/blob/main/Images/Keyboard.png)
### Example with Soundcloud
Soundcloud, Youtube and News can be shown at the current state. More options are going to be implemented.
![Keyboard](https://github.com/SparkPusher/Reflectify/blob/main/Images/Soundcloud.png)
