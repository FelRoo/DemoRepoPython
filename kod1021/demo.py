import Larm

alarms = [
    Larm.Larm(10, "CPU"),
    Larm.Larm(15, "Memory"),
    Larm.Larm(25, "Disk"),
    Larm.Larm(40, "CPU")
]

sorted_alarms = sorted(alarms, key=lambda alarm: alarm.alarm_level)

for alarm in sorted_alarms:
   print(f"Alarm Level: {alarm.alarm_level}, Alarm Type: {alarm.alarm_type}")



addera = lambda x, y: x + y
print(addera(7, 4))  # Output: 7


siffror = [1, 3, 2, 6, 4, 5]

sorterande_siffror = sorted(siffror)

print(sorterande_siffror)

