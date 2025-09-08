---
title: Tracking FLARM-enabled aircraft using Raspberry Pi and RTL-SDR dongle
categories:
  - Blog
tags:
  - Raspberry Pi
  - Tracking
  - RTL-SDR
---

- I am currently building a comprehensive ground station for tracking different kinds of aircraft and other vehicles, like vessels, and weather balloons.
- I started creating a project page for collecting all the information regarding my ground station here.
- There you also find an overview of the hardware setup and all the posts describing how to setup different trackers.

- The most popular one seems to be the ADS-B tracker.
- However, some aircraft, especially gliders are rather equipped with FLARM transponders, instead of ADS-B.
- TODO: explain FLARM here or link to a specific page describing it? Maybe wikipedia for the beginning, later add some info here.
- tracking FLARM is a bit more challenging that ADS-B:
  1. FLARM is a proprietary, encrypted protocol
  2. signals are 1000 to 10000 times (30-40dB) weaker. Even though data rate is 20 times slower (50kbps) than ADS-B (1Mbps), in total its still a factor of 100-1000 worse.
  3. Gliders fly lower than airliners thus antenna height and obstacles count much more

# Setup

- First, there is an OGN image available that one can use to write on a SD card, put it into the Raspberry Pi, boot up and done, at least theoretically, I never tried this way.
- However, this gives little control over what's running on your Pi.
- I like to use a clean Raspbian OS Lite image and install all the software by myself.

