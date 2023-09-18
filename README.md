# Reflectify
## A Setup for a Smart Mirror, based on Raspberry Pi Model 4B, Tkinter and Arduino
The intention was to build up a mirror and add the capability of taking pictures using a raspberry pi camera option as well as enable access to subprocesses like YouTube, SoundCloud, Spotify, and daily news. The project, however, was also not restricted to these options; there was an interest in making it user-friendly by adding a keyboard, speaker, and the ability to detect when someone is close enough to the mirror in order to show welcoming messages.

Note: This is a prototype and still in the developing. More information in "Future implementation".

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
Soundcloud, Youtube, a Camera and News can be shown at the current state. More options are going to be implemented.

![Soundcloud](https://github.com/SparkPusher/Reflectify/blob/main/Images/Soundcloud.png)
![Youtube](https://github.com/SparkPusher/Reflectify/blob/main/Images/Youtube.png)
![News](https://github.com/SparkPusher/Reflectify/blob/main/Images/News.png)
![Cam](https://github.com/SparkPusher/Reflectify/blob/main/Images/Camera.png)

## Mirror Frame and building up
The frame has ventilation slots for getting sure there is no overheating behind the mirror.

![Ventilation slots](https://github.com/SparkPusher/Reflectify/blob/main/Images/Ventilation_Slot.jpg)

The frame has two holes for the ultrasonic sensors, one for the pi cam and one big opening for the touchpad.

![holes](https://github.com/SparkPusher/Reflectify/blob/main/Images/Top_View.jpg)

The back of the mirror can be opened to insert the touchpad and the monitor.

![opened back](https://github.com/SparkPusher/Reflectify/blob/main/Images/Open_Back.jpg)

The sensors are connected to an arduino. The arduino transmits the data via serial connection to the pi.

![connection](https://github.com/SparkPusher/Reflectify/blob/main/Images/Closeup_Pi_Uno.jpg)

After wiring, everything is pinned to the back of the monitor.

![wired back](https://github.com/SparkPusher/Reflectify/blob/main/Images/Setup_Back.jpg)

After closing the back looks like the following.

![closed back](https://github.com/SparkPusher/Reflectify/blob/main/Images/Full_Setup_Back.jpg)

## Future implementation

Since the mirror is a prototype, there are still a number of additional features planned to be implemented to better interact with the user. This includes, for example, a better use of the Pi Cam with face recognition to adjust the greeting accordingly or the optimized runtime when passing the mirror. To work with different smart home systems, a connection between the Python program and IFTTT should be established. IFTTT represents various possible uses that can be integrated into the smart home. For example, the ESP8266, IFTTT, and the Adafruit dashboard have already been used and implemented to connect ws2812b led strips and the Google Home system, and this has been stated as successful (This is going to be uploaded in another repository in the future). In the first place, this possibility should be able to be displayed in the mirror to ensure control of the individual devices. In addition, an even more distinctive use of the smart home devices should be created, and possibly a Google Nest speaker should be attached to the frame in order to be able to carry out actions in the smart home with voice control
First and foremost, the mirror was concerned with ensuring that the individual functionalities were successfully tested and implemented. The functionality is already guaranteed at the current time. However, the performance can still be optimized, as, for example, opening a YouTube video takes about 1-4 seconds, depending on how busy the Raspberry Pi is. For this, you can make sure that the PyQT webengine for the Raspberry Pi is supported or that you work with the Chrome web browser, which also guarantees an improvement in performance. In addition, various programming approaches are to be used to speed up some processes.

## Hint

The program is not one hundred percent ready to share, because of that in the "model" the api key for the weather is deleted. Here the official api key has to be inserted. Also the Location in the model for the weather can or has to be changed for the usage.
