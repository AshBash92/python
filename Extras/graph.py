import matplotlib.pyplot as plt
import json
import datetime

with open('D:\\repo\\GitHub\\python\\Extras\\data.json', 'r') as f:
    data = json.load(f)

graph1 = data["graph1_unix"]
graph2 = data["graph2_unix"]

# x = [entry["time"] for entry in graph2]

# Convert Unix timestamps to datetime objects
graph1_times = [datetime.datetime.fromtimestamp(int(entry["time"])) for entry in graph1]
graph2_times = [datetime.datetime.fromtimestamp(int(entry["time"])) for entry in graph2]

# Extract hours and minutes from datetime objects
x1 = [time.strftime("%I:%M:%S %p") for time in graph1_times]
x2 = [time.strftime("%I:%M:%S %p") for time in graph2_times]

# graph1_hours = [datetime.datetime.fromtimestamp(int(entry["time"])).strftime("%H:%M") for entry in graph1]
# graph2_hours = [datetime.datetime.fromtimestamp(int(entry["time"])).strftime("%H:%M") for entry in graph2]


# Extract all unique keys from graph2 except "time"
keys = list(set().union(*[entry.keys() for entry in graph2]))

# Create the y_values dictionary dynamically
y_values = {key: [] for key in keys}
for entry in graph2:
    for key in keys:
        value = entry.get(key)
        if value is not None:
            try:
                y_values[key].append(float(value))
            except ValueError:
                y_values[key].append(None)
        else:
            y_values[key].append(None)

plt.figure(1)
plt.plot(x1, [float(entry["latency"]) for entry in graph1])
plt.title("Overall")
plt.xlabel("Time")
plt.ylabel("Latency")
plt.xticks(x1[::5], [time.strftime("%I:%M:%S %p") for time in graph1_times[::5]])
# plt.xticks(x1[::5] + [x1[-1]], [time.strftime("%I:%M %p") for time in graph1_times[::5]] + [graph1_times[-1].strftime("%I:%M:%S %p")])

# tick_locations = x1[::5] + [x1[-1]]
# tick_labels = [time.strftime("%I:%M %p") for time in graph1_times[::5]] + [graph1_times[-1].strftime("%I:%M:%S %p")]

# plt.xticks(tick_locations, tick_labels)

plt.show()

plt.figure(2)
for i, key in enumerate(keys):
    if key != "time":  # Exclude "time" from the legend
        plt.plot(x2[:len(y_values[key])], y_values[key], label=key)
plt.title("By Variables")
plt.xlabel("Time")
plt.ylabel("Latency")
plt.xticks(x2[::5], [time.strftime("%I:%M:%S %p") for time in graph2_times[::5]])
plt.legend()

plt.show()

print('\n\nCOMPLETE...\n')