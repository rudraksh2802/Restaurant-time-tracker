# Smart Restaurant Occupancy and Queue Management System

## Idea

A restaurant can be close to a customer but still take a long time because of a crowd. This project records the number of people inside and the number of groups waiting outside, then estimates the waiting time.

The customer can also enter travel time to see the combined travel + waiting time.

## Current Version

This is a console-based Python prototype. Occupancy and queue values are entered manually. In a future version, camera/computer-vision or sensors can provide these values automatically.

## Main Modules

1. Occupancy Management
2. Queue Management
3. Waiting-Time Estimation
4. Customer Decision Calculation
5. Data Storage
6. Testing

## Run

    python main.py

## Test

    python -m unittest test_project.py

No external packages are required.
