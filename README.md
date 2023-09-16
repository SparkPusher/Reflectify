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
