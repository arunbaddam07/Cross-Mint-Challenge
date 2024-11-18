# Cross-Mint Challenge : Celestial Object Manager

## Overview
This Python script allows users to interact with the Celestial Object API, managing objects like POLYANETs, SOLOONs, and COMETHs on a virtual grid. The script handles creating, placing, and potentially deleting celestial objects based on a predefined goal map fetched from an API.

## Features
- **Fetch Goal Map**: Retrieves the goal map for the current challenge phase, showing where celestial objects need to be placed.
- **Place Objects**: Automatically places objects such as POLYANETs, SOLOONs, and COMETHs on the grid according to the goal map.
- **Adaptive Requests**: Dynamically uses POST or DELETE HTTP methods to manage objects on the grid based on server requirements.

## Requirements
- Python 3.x
- Requests library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the `requests` module if it's not already installed:
   ```bash
   pip install requests

## Running the Script
```python
python main.py
```
