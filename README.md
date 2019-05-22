# IoT Fire Alarm System
-------

System proposal for thesis fulfilment created by:
+ [CJ Pastor](https://www.facebook.com/AmazingCid)
+ [Emmanuel Trinidad](https://www.facebook.com/profile.php?id=100013365908230)
+ [John Philip Roncale](https://www.facebook.com/johnphilip.roncale.39)

-------

![](https://balena.io/blog/content/images/2019/03/balenaSense_blog.jpg)
![](https://www.balena.io/blog/content/images/2019/03/dashboard-screenshot.png)

A Raspberry Pi starter project taking readings from a **Bosch BME680 sensor**, storing using InfluxDB and reporting using Grafana.

The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places.

### Hardware required

![](https://balena.io/blog/content/images/2019/03/hardware-required.jpg)

Here’s the shopping list for this project. Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, some require a little soldering.

* Raspberry Pi 2Bv1.2/3B/3B+/3A+/Zero
* 8GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
* Power supply & micro-USB cable
* Bosch BME680 sensor with breakout board (see below for places to find one) or...
* **Optional:** Male-to-female Dupont cables (optional)

### Software required

We’ve set up this project which contains all of the software, configuration and code you’ll need to start taking readings straight away. We’re going to deploy this project on [balenaCloud](https://www.balena.io/cloud/) using a free account to push the project and all the software to your Raspberry Pi as well as to provide remote access. Therefore, you’ll need:

* Tool to flash your SD card, such as [balenaEtcher](https://www.balena.io/etcher/)
* A [balenaCloud](https://www.balena.io/cloud/) account
* A clone or download of this project

### Putting the hardware together
You’ve got very little to do on the hardware front for this project; the goal here is to connect the sensor board to the Raspberry Pi general purpose input/output (GPIO) header.

The BME680 sensor communicates with the Raspberry Pi over a bus called I2C, which is a serial communication bus that requires 2 wires. These two communication wires are referred to as serial clock (SCK) and serial data (SDA). In addition to the two communication wires, we also need to provide the sensor with power (3.3V, or 3V3) and ground.

If you decided to connect a sensor directly to your Raspberry Pi, either the Pimoroni one or any one of the other breakout boards from one of the other suppliers, the main things to watch out for are that the pins described above (SDA, SCK, 3V3 and GND) are correctly connected.

### Setting up the Raspberry Pi
We’re going to flash an SD card with balenaOS via a download from the balenaCloud dashboard and add the device in order to push the project, and set things up in such a way it can easily be updated later.

The first thing to do is to get set up with a balenaCloud account; this means signing up if you haven’t already, adding an application and adding a device.

**Step 1 - Sign up to [balenaCloud](https://dashboard.balena-cloud.com/signup?utm_source=efp&utm_campaign=balena-sense)**

**Step 2 - Create an application**
Add an application selecting the correct device type for the device you’re using, and choosing Starter as the application type, then hit Create New Application. Using the starter application will provide you with all of the features of the microservices application and is free up to and including your tenth device.

**Step 3 - Add a device and download the OS**
Once your application has been created, you can setup and add a device within that application by clicking the green 'add device' button. When you add a device you specify your device type, which is important that it matches the device you’re using, and if you are connecting to a wireless network you can set your WiFI SSID and passphrase.

**Step 4 - Flash your SD card and boot the device**
Once the OS image has been downloaded, it’s time to flash your SD card. You can use [balenaEtcher](https://www.balena.io/etcher/) for this.

Once the flashing process has completed, insert your SD card into the Raspberry Pi and connect the power supply.
When the device boots for the first time, it connects to the balenaCloud dashboard, after which you’ll be able to see it listed as online.


![](https://assets.balena.io/blog-common/insert_sdcard_rpi.gif)

*You can view the complete tutorials [here](https://www.balena.io/blog/build-an-environment-and-air-quality-monitor-with-raspberry-pi/)*


