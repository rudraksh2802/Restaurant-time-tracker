# Smart Restaurant Occupancy and Queue Management System

## 1. Introduction

Restaurant choice is not only about distance. A nearby restaurant may have a large crowd, while another restaurant farther away may have seats available.

This project creates a simple system to record restaurant occupancy and the outside queue and use that information to estimate waiting time.

The current version uses Python console input. The same core can later be connected to sensors or computer vision.

## 2. Problem Statement

Customers may know a restaurant's location and opening status but not its current crowd level. The system provides basic occupancy, queue and waiting-time information.

## 3. Objectives

- Track occupancy.
- Track outside queue.
- Calculate free seats.
- Estimate waiting time.
- Combine travel and waiting time.
- Save current data.
- Keep the program modular.

## 4. Requirements

The functional and nonfunctional requirements are listed in `requirements.md`.

## 5. Architecture

The program uses `main.py` for interaction, `restaurant.py` for core logic, `storage.py` for JSON storage and `test_project.py` for testing.

## 6. Implementation

The project demonstrates variables, functions, classes, loops, conditions, exception handling, dictionaries, file handling, JSON and unit testing.

## 7. Waiting-Time Logic

The prototype uses an average table turnover time.

Example: 3 waiting groups × 25 minutes = 75 minutes estimated waiting time.

This is an estimate because real waiting depends on group size, table size and dining duration.

## 8. Testing

Automated tests check occupancy, capacity, queue handling and waiting-time calculation.

## 9. Challenges

Restaurant conditions change continuously, so manually entered values can become outdated. Also, queue size alone cannot perfectly predict waiting time.

## 10. Learnings

The project demonstrates how a real-world problem can be divided into modules, how classes can represent real objects, how input can be validated and stored, and how basic testing can be added.

## 11. Future Enhancements

- Camera-based people detection
- Automatic queue detection
- Multiple restaurants
- Database storage
- Historical data
- Improved prediction
- Web/mobile interface
- Real-time updates

## 12. Conclusion

This project provides a working prototype for restaurant occupancy and queue management. The core Python logic is simple enough to understand and can later be extended with automatic detection and a larger user interface.
