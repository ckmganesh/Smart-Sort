# Smart-Sort
Automate Waste Classification using IOT & ML

## What it does?
<ul>
<li>We have designed this system by using a camera interfaced with Raspberry Pi.</li>
<li>When trash is placed on the system, the camera is triggered to take a picture and Raspberry Pi sends it to the Heroku Cloud where we have deployed our Deep Learning model.</li>
<li>This DL image classification algorithm runs to decide if the waste being disposed is biodegradable or non-biodegradable.</li>
<li>The result is sent back to the Raspberry Pi module which then triggers motors which slides the trash into their respective bins.</li>
<li>We have created a frontend system, where we can view the activity of the bin. </li>
</ul>

## Architecture

<img src="https://i.ibb.co/GdjLvXg/Screenshot-2021-04-11-192839.jpg" class="center">

## Prototype and Output

<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/477/088/datas/original.jpg" height="400" width="600">
Prototype of the Bin
<br>
<br>
<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/477/097/datas/original.png" height="400" width="600">
Frontend UI to see details about the activity of the bin
<br><br>
<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/477/248/datas/original.jpeg" height="400" width="200">
Camera which captures and sends the image to the cloud
<br><br>
<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/477/245/datas/original.jpeg" height="400" width="600">
Raspberry pi connections
<br><br>

## Contributors

<a href="https://github.com/ckmganesh">Ganesh C K M</a><br>
<a href="https://github.com/siddharth1010">Siddharth M Nair</a><br>
<a href="https://github.com/ramcalm">Ram Gunasekaran A</a><br>
<a href="https://github.com/ssabarish2000">Sabarish S</a><br>
