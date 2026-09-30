from restaurant import RestaurantSystem
from storage import save_data, load_data

def show_status(system):
    print("\n" + "=" * 55)
    print("        SMART RESTAURANT OCCUPANCY SYSTEM")
    print("=" * 55)
    print(f"Restaurant       : {system.name}")
    print(f"Capacity         : {system.capacity} people")
    print(f"People inside    : {system.occupied}")
    print(f"Free seats       : {system.available_seats()}")
    print(f"Queue outside    : {system.queue_groups} group(s)")
    print(f"Estimated wait   : {system.estimated_wait()} minutes")
    print("=" * 55)

def main():
    system = RestaurantSystem("Food Corner", 40, 25)
    saved = load_data()
    if saved:
        system.load_state(saved)

    while True:
        show_status(system)
        print("\n1. Person entered")
        print("2. Person left")
        print("3. Add group to queue")
        print("4. Remove group from queue")
        print("5. Set current occupancy")
        print("6. Set current queue")
        print("7. Customer decision calculator")
        print("8. Save data")
        print("9. Reset restaurant")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                system.person_entered()
                print("Person added.")
            elif choice == "2":
                system.person_left()
                print("Person removed.")
            elif choice == "3":
                system.add_queue_group()
                print("Group added to queue.")
            elif choice == "4":
                system.remove_queue_group()
                print("Group removed from queue.")
            elif choice == "5":
                system.set_occupancy(int(input("Current people inside: ")))
                print("Occupancy updated.")
            elif choice == "6":
                system.set_queue(int(input("Current waiting groups: ")))
                print("Queue updated.")
            elif choice == "7":
                travel = float(input("Travel time to restaurant (minutes): "))
                wait = system.estimated_wait()
                print(f"Travel time : {travel:.1f} minutes")
                print(f"Wait time   : {wait} minutes")
                print(f"Total time  : {travel + wait:.1f} minutes")
            elif choice == "8":
                save_data(system.get_state())
                print("Data saved.")
            elif choice == "9":
                system.reset()
                print("Restaurant reset.")
            elif choice == "0":
                save_data(system.get_state())
                print("Data saved. Program closed.")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(f"Input error: {error}")

if __name__ == "__main__":
    main()
