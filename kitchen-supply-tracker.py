# Kitchen Supply Tracker - ( functions & scope)

# available products 

available_milk_packets = 5
available_flour_packets = 2
available_sugar_packets = 3


def check_kitchen_stock():
    total_items = available_milk_packets + available_flour_packets + available_sugar_packets
    print(f"\nCurrent Stock: {total_items} items total.")
    print(f"- Milk_packets: {available_milk_packets} | Flour_packets: {available_flour_packets} | Sugar_packets: {available_sugar_packets}")


def use_item(item_name, current_stock, count_to_use):
    if count_to_use > current_stock:
        print(f"Warning: Not enough {item_name} available in inventory.")
        return current_stock

    print(f"Success: Used {count_to_use} {item_name}(s).")
    return current_stock - count_to_use


# Simulation Sequence
check_kitchen_stock()

# Simulating cooking consumption updates
available_milk = use_item("Milk_packets", available_milk_packets, 3)
available_flour = use_item("Flour_packets", available_flour_packets, 1)
available_sugar = use_item("Sugar_packets", available_sugar_packets, 1)

# Verifying updated inventory status
check_kitchen_stock()
