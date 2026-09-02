n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival time (AT) for P{i+1}: "))
    bt = int(input(f"Enter Burst time (BT) for P{i+1}: "))
    processes.append([i+1, at, bt])

# First sort by Arrival Time
processes.sort(key=lambda x: x[1])

current_time = 0
twt = 0
ttat = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

while len(processes) > 0:

    # If CPU is idle, take the first arrived process
    if current_time < processes[0][1]:
        current_time = processes[0][1]

    # Find all processes that have arrived
    available = []

    for process in processes:
        if process[1] <= current_time:
            available.append(process)

    # Sort available processes by Burst Time
    available.sort(key=lambda x: x[2])

    # Take the process with shortest BT
    process = available[0]

    pid, at, bt = process

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    twt += wt
    ttat += tat

    print(f"P{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    current_time = ct

    # Remove completed process
    processes.remove(process)

avg_wt = twt / n
avg_tat = ttat / n

print(f"\nAverage waiting time = {avg_wt:.2f}")
print(f"Average turnaround time = {avg_tat:.2f}")