# System Architecture

## Current

User -> main.py -> RestaurantSystem -> storage.py -> restaurant_data.json

RestaurantSystem contains:
- Occupancy management
- Queue management
- Seat calculation
- Waiting-time estimation
- Customer time calculation

## Future

Camera/Sensor -> Detection Module -> RestaurantSystem -> Customer Information

The manual input in this version can later be replaced by automatic detection without changing the main restaurant logic.
