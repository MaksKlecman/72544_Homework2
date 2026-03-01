from datetime import datetime

HOURLY_RATES = {
    ("micro", "Linux"): 0.01,
    ("micro", "Windows"): 0.015,
    ("small", "Linux"): 0.02,
    ("small", "Windows"): 0.03,
    ("medium", "Linux"): 0.05,
    ("medium", "Windows"): 0.07,
    ("large", "Linux"): 0.1,
    ("large", "Windows"): 0.13,
}

instances = []
terminated_instances = []

def calculate_cost(instance):
    end_time = datetime.now()
    hours = (end_time - instance["start_time"]).total_seconds() / 3600
    rate = HOURLY_RATES[(instance["type"], instance["os"])]
    return hours * rate, hours

def provision():
    name = input("Instance name ")
    
    for inst in instances:
        if inst["name"] == name:
            
            print("Instance with this name already exists")
            return
    
    inst_type = input("Type (micro/small/medium/large): ").lower()
    os = input("OS (Linux/Windows): ")

    if (inst_type, os) not in HOURLY_RATES:
        print("Invalid configuration")
        return

    instance = {
        "name": name,
        "type": inst_type,
        "os": os,
        "start_time": datetime.now()
    }

    instances.append(instance)
    print("Instance provisioned successfull")

def list_instances():
    total = 0
    print("\nRunning instances")
    for inst in instances:
        cost, hours = calculate_cost(inst)
        total += cost
        print(f"{inst['name']} | {inst['type']} | {inst['os']} | {hours:.2f} hrs | ${cost:.4f}")
    print(f"Total current bill: ${total:.4f}")

def terminate():
    name = input("Instance name to terminate: ")
    for inst in instances:
        if inst["name"] == name:
            cost, hours = calculate_cost(inst)
            instances.remove(inst)
            terminated_instances.append(cost)
            print(f"Terminated. Final cost: ${cost:.4f}")
            return
    print("Instance not found")

def total_bill():
    running_total = sum(calculate_cost(inst)[0] for inst in instances)
    terminated_total = sum(terminated_instances)
    
    
    print(f"Total bill (all instances): ${running_total + terminated_total:.4f}")

def main():
    while True:
        print("\n1. Provision")
        print("2. List")
        print("3. Terminate")
        print("4. Total bill")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            provision()
            
        elif choice == "2":
            list_instances()
        elif choice == "3":
            terminate()
        elif choice == "4":
            total_bill()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()