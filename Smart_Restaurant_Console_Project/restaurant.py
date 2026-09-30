class RestaurantSystem:
    """Main logic for restaurant occupancy, queue and waiting time."""

    def __init__(self, name, capacity, average_turnover=25):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.name = name
        self.capacity = capacity
        self.average_turnover = average_turnover
        self.occupied = 0
        self.queue_groups = 0

    def person_entered(self):
        if self.occupied >= self.capacity:
            raise ValueError("Restaurant is full.")
        self.occupied += 1

    def person_left(self):
        if self.occupied <= 0:
            raise ValueError("Nobody is inside the restaurant.")
        self.occupied -= 1

    def set_occupancy(self, value):
        if value < 0 or value > self.capacity:
            raise ValueError(f"Occupancy must be between 0 and {self.capacity}.")
        self.occupied = value

    def add_queue_group(self):
        self.queue_groups += 1

    def remove_queue_group(self):
        if self.queue_groups <= 0:
            raise ValueError("Queue is already empty.")
        self.queue_groups -= 1

    def set_queue(self, value):
        if value < 0:
            raise ValueError("Queue cannot be negative.")
        self.queue_groups = value

    def available_seats(self):
        return self.capacity - self.occupied

    def occupancy_percentage(self):
        return (self.occupied / self.capacity) * 100

    def estimated_wait(self):
        return self.queue_groups * self.average_turnover

    def get_state(self):
        return {
            "name": self.name,
            "capacity": self.capacity,
            "average_turnover": self.average_turnover,
            "occupied": self.occupied,
            "queue_groups": self.queue_groups
        }

    def load_state(self, data):
        self.name = data.get("name", self.name)
        self.capacity = int(data.get("capacity", self.capacity))
        self.average_turnover = int(data.get("average_turnover", self.average_turnover))
        self.set_occupancy(int(data.get("occupied", 0)))
        self.set_queue(int(data.get("queue_groups", 0)))

    def reset(self):
        self.occupied = 0
        self.queue_groups = 0
