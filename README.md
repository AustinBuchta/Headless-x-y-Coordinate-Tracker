# Desktop Coordinate Overlay Tracker

A lightweight, borderless Python Tkinter desktop overlay that tracks mouse cursor coordinates in real time. Built with Windows API calls to run as a quiet background utility, featuring screen boundary clamping and drag-and-drop repositioning.

## Features

* **Real-Time Tracking:** Polls screen-wide cursor coordinates at ~33Hz (`winfo_pointerx`/`winfo_pointery`) with uniform text alignment.
* **Borderless & Transparent:** Utilizes custom color-keying (`-transparentcolor`) and native window decorations removal (`overrideredirect`) for a floating HUD aesthetic.
* **Screen Edge Snapping:** Math-clamped window dragging (`<B1-Motion>`) keeps the overlay contained within monitor display boundaries.
* **Hidden Console Execution:** Invokes native `user32.dll` and `kernel32.dll` functions via `ctypes` to hide the attached terminal window on launch.
* **Always-On-Top:** Configured to stay pinned above full-screen desktop applications and active browser windows.

## Controls

* **Left Click + Drag:** Reposition the overlay anywhere on screen.
* **Right Click / Escape:** Terminate the application immediately.

## Requirements & Setup

* **OS:** Windows (required for `ctypes` console hiding and window transparency keys).
* **Python Version:** Python 3.x (uses built-in `tkinter` and `ctypes` standard libraries—no `pip` installs required).

### Execution

```bash
python main.py
