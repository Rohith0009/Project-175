import matplotlib.pyplot as plt
import psutil as p

TheList = {}
count = 0

for process in p.process_iter():
    count += 1
    if count < 7:
        PN = process.name()
        PU = p.cpu_percent()
        TheList.update({PN: PU})

TheMax = max(TheList, key=TheList.get)
TheMin = min(TheList, key=TheList.get)
App_nix = [TheMax, TheMin]

idk = TheList.values()
MaxCPU = max(idk)
MinCPU = min(idk)
Cpu_nix = [MaxCPU, MinCPU]


plt.figure(figsize=(15, 7))
plt.xlabel("Applications")
plt.ylabel("CPU Usage")
plt.bar(
    App_nix,
    Cpu_nix,
    width=1,
    color=("Green", "Blue"),
)
plt.show()
