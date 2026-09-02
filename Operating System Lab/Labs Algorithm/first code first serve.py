n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter the arrival time of P{i+1}: "))
    bt = int(input(f"Enter the burst time P{i+1}: "))
    processes.append([i+1, at, bt])

processes.sort(key=lambda x:x[1])

current_time = 0
ttat = 0
twt = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for process in processes:
    if current_time < process[1]:
       current_time = process[1]

    uid, at, bt = process

    ct = current_time + bt
    current_time = ct

    tat = ct - at
    wt = tat - bt

    ttat = ttat + tat
    twt = twt + wt

    print(f"{uid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

awt = twt / n
atat = ttat / n

print(awt, atat)