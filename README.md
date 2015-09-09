<h1>Spark Fun H-Bridge Block for Edison Python Library</h1>

This is the library for controlling autonomous robot on the Intel Edison base by the Python.

<h2>What you need</h2>
<ul>
<li>Intel Edison - https://www.sparkfun.com/products/13024
<li>Spark Fun H-Bridge Block for Intel Edison - https://www.sparkfun.com/products/13043
<li>SparkFun Block Base (https://www.sparkfun.com/products/13045) or SparkFun Block Battery (https://www.sparkfun.com/products/13037)
<li>Any chassis with two motors and with the independent power supply
</ul>
You have to complete it as is shown on the pictures in the manual: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---dual-h-bridge?_ga=1.228897183.269440423.1434706829 
In these library is expected, that you connect left motor on the A1 and A2 pins and right motor on the B1 and B2 pins.
If you wil discover that direction of any motor is wrong then simply change A1 and A2 pin (or B1 and B2).

<h2>Preparation of the Intel Edison</h2>
I recommend use the Ubilinux distribution (http://www.emutexlabs.com/ubilinux). The guideline for the installations Ubilinux on the Intel Edison is good described here: https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison
After installation of the Ubilinux you need install mraa library for Intel Edison which is here: https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison

<h2>Using of the library</h2>
Main file of the library is the file <code>robot.py</code>. Simply it upload on any location in the Intel Edison. Example of it using is in the file <code>robot.py</code>. It is necessary the run it with root permission:
```
sudo python example.py
```
There are the six commands in this librarry. Each of the command has one parameter, which means duration of this move. The commands are:
<ul>
<li><code>forward(time)</code> - move direct
<li><code>back(time)</code> - move backward
</ul>

