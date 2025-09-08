---
title: List of Cube-Solving Robots
categories:
  - Wiki
tags:
  - Cubing
---

## Overview

### Architectures of Robots

There are several basic architectures of robots for solving cubes.

#### 5 and 6-Axis

This robot gets hold of a 3x3x3 cube on at least 5 sides, sometimes all 6, by connecting the centers to individual motor's axes.
This makes the solve very efficient, since no cube rotations are required and all sites are directly accessible by the robot's actuators.
This architecture is the most prominent one for breaking World Guinnes Records.
It is also used in commercially available robots, like the [GAN Cube Robot](https://www.gancube.com/products/gan-speed-cube-robot) or the [MoYu Cube Solving Robot](https://speedcubeshop.com/products/moyu-cube-solving-robot).

#### 3 and 4-Axis

This architecture is very similar to the 5 and 6 Axis one.
However, it requires to perform cube rotations around at least one axis.
Hence, the robot needs to be able to release two opposite faces.
This architecture makes use of grippers that hold the cube like with two fingers on 4 faces.
The grippers may either act like pliers, or the whole actuator mechanism moves back and forth to release or grap the cube.
With this architecture, it is usually not required to modify the cube.

#### 2-Axis

Similar to the previous one, this uses grippers to get hold of the cube.
Here, these are placed on orthotognal axes.

#### Tower

The cube sits on a "swing" that is able to rotate the whole cube around the x-Axis (`x`, `x2` and `x'` in [cube notation](https://www.speedsolving.com/wiki/index.php/NxNxN_Notation)).
A lift raises the cube into a cage that consists of a lower, static part, which holds the layers that are not to be rotated and an upper part that rotates the rest of the slices.
So, only `U`, `U2`, and `U'` (single and wide) turns are possible, as well as full cube rotations around the y-axis (i.e. `y`, `y2`, `y2'`) when the cube is moved fully up into the turning cage.

This architecture can easily be adapted to handle any size of cubes and does not require the puzzles to be modified.
Some builds are even able to handle different sizes of cubes without modifying the hardware as long as the dimensions of the cube stays in specific tolerances.
It's not suitable for solving cuboids, since the size of the cage is not adaptable to variable side length.
It has also been adapted to solve the Megaminx puzzle.

#### Pushing

Here, the cube sits on a cage that holds it in place while an actuator pushes against an upper edge of the cube.
The mechanism is tuned in a way that does not push the cube out of the cage.
Rather, it falls back on the platform, but turned by 90 degrees.

Another actuator can lower a second cage above the top layers of the cube.
This will hold it in place while the lower cage rotates to turn the down face.

This architecture is very popular for simple Lego-based robots, since it requires only few parts and electronics, thus featuring a very easy and achievable build.
It can even be build from a single Lego set, like the [51515 Robot Inventor](https://mindcuber.com/mindcuberri/mindcuberri.html), or the [45678 Education SPIKE Prime](https://mindcuber.com/primecuber/primecuber.html).

More sophosticated builds comprise multiple pushing arms that allow cube rotation in any direction without the need of rotating around the y-Axis first.
Furthermore, two pushers placed on opposite sites of the cube allow to hold it in place without the need for an additional upper cage while the platform roates.
Such an advanced architecture is also able to handle 4x4x4 cubes by incorporating a mechanism to raise and lower the cube to perform wide turns of the down face.

#### Summary

| Architecture | Supported puzzles | Supported Sizes | Requires Puzzle Modification |
| -- | -- | -- | -- |
| 5/6-Axis | Cubes | 3x3x3 | No |
| 4-Axis | Cubes | 3x3x3 | No |
| Tower | Cubes, Megaminx | Cubes: NxNxN, Megaminx | No |
| Pusher | Cubes | NxNxN | No |

## Robots

| Name | Creator | Architecture | Puzzles | Required Modification | Video | Hardware | Code | Articles | Record |
| - | - | - | - | - | - | - | - | - | - |
| CraneCuber | | Tower | 2x2x2 - 6x6x6 | No | [YouTube](https://www.youtube.com/watch?v=3HjKxTlLDLw) | [Lego EV3](https://rebrickable.com/mocs/MOC-12712/dwalton76/cranecuber/#details) | [GitHub](https://github.com/dwalton76/lego-crane-cuber) | [Rubiks Cube Tracker using OpenCV](https://programmablebrick.blogspot.com/2017/02/rubiks-cube-tracker-using-opencv.html), [Rubiks Cube Solver](https://programmablebrick.blogspot.com/2017/07/rubiks-cube-solver.html) |
| MindCuber | | Pusher | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=oX5yYhgJG2s) | Lego Prime | | [Project Website](https://mindcuber.com/) |
| Rubik's Cube solver PWS | Anuar Behari and Jonas Post | 6-Axis | 3x3x3 | Yes | [YouTube](https://www.youtube.com/watch?v=ZAsL1lT7-UQ) | 3D print, Arduino | [GitHub](https://github.com/JonasPost2006/RubiksCubeSolver/) | [Project Website](https://jonaspost2006.github.io/RubiksCubeSolver/media.html) | 2024: 0:13.17
| | | 4-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/shorts/8WRzlO0EjJo) | Wood, Arduino | | |
| MultiCuber 3 | David Gilday (@IAssemble) | Tower | 4x4x4 | No | [YouTube](https://www.youtube.com/watch?v=HUX6hkGFJTM) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/multicuber-3-fastest-robot-to-solve-a-4x4x4-cube.46769/) | 2014: 1:18.68 (incl. scan)
| Quad-Cub3r | | Pusher | 4x4x4 | No | [YouTube](https://www.youtube.com/watch?v=wSvf1AdIjxo) | Lego EV3 | | [Forum Post](https://www.speedsolving.com/threads/robot-37-61-4x4x4-uwr.57435/) | 2016: 0:37.61
| MultiCub3r-X | David Gilday (@IAssemble) | Pusher | 4x4x4 | No | [X](https://x.com/Arm/status/1823645833713111319) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/the-fastest-cube-machine-for-4x4x4.69231/post-1303943), [LinkedIn](https://www.linkedin.com/posts/cseidl_multicub3r-x-is-the-fastest-robot-in-the-activity-7230152062557171712-occA) | 2017: 0:21
| MultiCuber 666 | David Gilday (@IAssemble) | Tower | 6x6x6 | No | [YouTube](https://www.youtube.com/watch?v=8xfeTQIOHGw) | Lego NXT | | | 2010: 26:24.0 (incl. scan)
| MultiCuber 777 | | Tower | 7x7x7 | No | [YouTube](https://www.youtube.com/watch?v=b5b9BIBuOd4) | Lego NXT | | [Blog Post](https://web.archive.org/web/20110917004937/http://blogs.arm.com/smart-mobile-devices/254-how-i-created-the-arm-powered-android-lego-7x7x7-cube-solving-robot/) | 2010: 38:53.44 (excl. scan)
| MegaMinxer | David Gilday (@IAssemble) | Tower | Megaminx | No | [YouTube](https://www.youtube.com/watch?v=P-S30fS944M) | Lego NXT | | [Blog Post](https://web.archive.org/web/20110811101332/http://blogs.arm.com/smart-mobile-devices/451-oh-no-not-another-arm-powered-lego-rubiks-cube-solver/) | 2011: 8:04.00
| MultiCuber | David Gilday (@IAssemble) | Tower | 2x2x2 - 5x5x5 | No | [YouTube](https://www.youtube.com/watch?v=kWrJdkXp_n4) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/multicuber-lego-minstorm-solves-2x2x2-3x3x3-4x4x4-5x5x5-and-6x6x6.20899/), []()  | 2010
| MultiCuber 999 | David Gilday (@IAssemble) | Tower | 9x9x9 | No | [YouTube](https://www.youtube.com/watch?v=8bDCpWfrqJU) | Lego EV3 | | [Forum Post](https://www.speedsolving.com/threads/lego-multicuber-robot-solves-a-cube-how-big.46394/) | 2014: 33:21.6
| MindCuber | | Pusher | 3x3x3 Void | No | [YouTube](https://www.youtube.com/watch?v=9QL5DZBo8WQ) | Lego NXT | | |
| CubeStormer Prototype | | 3-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=pnV7oc2SMbc) | Lego RCX | | | 2008: sub 0:15.0
| CubeStormer | | 4-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=eaRcWB3jwMo) | Lego RCX | | | 2010: 0:10.75 (incl. scan) |
| CubeStormer II | | 4-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=_d0LfkIut2M) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/cubestormer-ii-robot-solves-rubiks-cube-faster-than-human-world-record.32911/) | 2011: 0:05.352 (incl. scan)
| CubeStormer 3 | | 4-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=X0pFZG7j5cE) | Lego EV3 | | | 2014: 0:03.253 (incl. scan)
| MultiCuber 3x3x5 | David Gilday (@IAssembler) | Tower | 3x3x5 | No | [YouTube](https://www.youtube.com/watch?v=u7eRhYLFfSo) | Lego NXT | | | 2012: 2:36.0
| MultiCuber 3x3x7 | David Gilday (@IAssembler) | Tower | 3x3x7 | No | [YouTube](https://www.youtube.com/watch?v=ttjYM0ix9UQ) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/lego-robot-solves-3x3x7-cube.37501/) | 2012
| MultiCuber 3x3x9 | David Gilday (@IAssembler) | Tower | 3x3x9 | No | [YouTube](https://www.youtube.com/watch?v=1ZnC8yaummg) | Lego NXT | | [Forum Post](https://www.speedsolving.com/threads/robot-solves-cubic-3x3x9.39800/) | 2012: 6:45.0
| Yellow Cube Machine | David Gilday (@IAssembler) | 4-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=GH4clQJ3VuA) | Lego NXT | | | 2010: 0:17.7
| V-Shaped Robot | Volker Hochholzer | 2-Axis | 3x3x3 | No | [YouTube](https://www.youtube.com/watch?v=Xv4a6-XM1M4) | 3D print, Raspberry | [GitHub](https://github.com/DrVoHo/Rubik_solver) | [Forum Post](https://forum.arduino.cc/t/rubiks-cube-robot-solver/262557)
| Skewbot | Matthew Hill | 3-Axis | Skewb | No | [YouTube](https://www.youtube.com/watch?v=KnrbZJdmEWg) | 3D print, Arduino | | [Forum Post](https://www.speedsolving.com/threads/worlds-first-skewb-solving-robot-known.73188/), [Idea Thread](https://www.speedsolving.com/threads/skewb-solving-robot.72268/) | 2019

---

TODOs:

- add type of recognition: Color sensor
  - phone camera for one side
  - mirrors to see all sides at once
  - etc.
- does record time include scan time?

## Other Lists

[Ruwix](https://ruwix.com/the-rubiks-cube/lego-rubiks-cube-robots-rubot2/)

[SpeedSolving Wiki](https://www.speedsolving.com/wiki/index.php/List_of_cube_solving_robots)
