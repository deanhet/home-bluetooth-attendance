# home-bluetooth-attendance
Get google home to give you different notifications based on who's home. The idea is that when you walk into your home, bluetooth will be able to infer who's in right now and give you information relevant to you (location of your spouse, when they left, play an entrance song, etc). 

This is more a collection of scripts/code over the internet and I've found bundled them together. This project is aiming to expand on the notification side of things.

## What you'll need:
* A linux-based, bluetooth-enabled, always-on computer at home (raspberry pi with dongle is great for this)
* Bluetooth-enabled portable device(s)
* Google Home
* Patience

## Getting started
* Get your bluetooth server/pi configured by following [this guide](http://www.instructables.com/id/Raspberry-Pi-Bluetooth-InOut-Board-or-Whos-Hom/?ALLSTEPS). Grab the MAC addresses you want and edit `inoutboard.py` accordingly.
* Complete the [following steps](https://github.com/noelportugal/google-home-notifier#raspberry-pi) (except installing)
* Clone this repo and run `npm install`

### Usage
\* VERY MUCH AN ALPHA RIGHT NOW *

Running should just be a matter of `python inoutboard.py`. The script currently checks (and will ping!) your google home every 15 seconds regardless of previous statuses. This is just an inital proof of concept right now, smarter and less annoying statuses and notifications will be coming soon.

### Work in progress
* Way easier config and smarter setup
* Better installation instructions
* Ability to remember who's currently in and only notify when that changes
* Plugin notifications
