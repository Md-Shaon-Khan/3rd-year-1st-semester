# First Come First Serve (FCFS) Scheduling Algorithm

number_of_processes = int(input("Enter number of processes: "))
processes = []

# Input Section
for i in range(number_of_processes):
    print(f"\n--- Process {i + 1} ---")
    name = input("Name: ")
    arrival = int(input("Arrival Time: "))
    burst = int(input("Burst Time: "))
    
    processes.append({
        "name": name,
        "arrival": arrival,
        "burst": burst
    })

# Step 1: Sort processes by Arrival Time
processes.sort(key=lambda p: p["arrival"])

# Step 2: Calculate Times
current_time = 0
total_waiting_time = 0
total_turnaround_time = 0

for p in processes:
    # Handle CPU idle time if process arrives after previous one finishes
    if current_time < p["arrival"]:
        current_time = p["arrival"]
        
    p["completion"] = current_time + p["burst"]
    p["turnaround"] = p["completion"] - p["arrival"]
    p["waiting"] = p["turnaround"] - p["burst"]
    
    # Update running total for next iteration
    current_time = p["completion"]
    total_waiting_time += p["waiting"]
    total_turnaround_time += p["turnaround"]

# Step 3: Print Results
print("\n" + "=" * 65)
print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<12}{'Waiting':<10}")
print("=" * 65)

for p in processes:
    print(f"{p['name']:<10}{p['arrival']:<10}{p['burst']:<10}{p['completion']:<15}{p['turnaround']:<12}{p['waiting']:<10}")

print("=" * 65)
print(f"Average Waiting Time    : {total_waiting_time / number_of_processes:.2f}")
print(f"Average Turnaround Time : {total_turnaround_time / number_of_processes:.2f}")