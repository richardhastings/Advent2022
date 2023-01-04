import advent

inputs = advent.re_input(
    "Valve ([A-Z][A-Z]) has flow rate=(\d*); tunnels? leads? to valves? (.*)", 16
)

valves = {}
flow_valves = []

for i in inputs:
    tunnels = i[2].split(", ")
    flow = int(i[1])
    valves[i[0]] = {"flow": int(i[1]), "tunnels": tunnels}
    if flow > 0:
        flow_valves.append(i[0])

shortest_routes = {}

for valve1 in valves:
    shortest_routes[valve1] = {}
    for valve2 in valves:
        if valve1 == valve2:
            shortest_routes[valve1][valve2] = {"path": None, "distance": 0}
        else:
            shortest_routes[valve1][valve2] = {"path": None, "distance": 1000}

# print(shortest_routes)


def find_shortest_route(start, path, target, distance):
    distance += 1
    neighbours = valves[path[-1]]["tunnels"]
    for n in neighbours:
        if target == n:
            if shortest_routes[start][n]["distance"] > distance:
                shortest_routes[start][n]["distance"] = distance
                shortest_routes[start][n]["path"] = path + [n]
            break
        if n not in path:
            find_shortest_route(start, path + [n], target, distance)


for valve1 in valves:
    for valve2 in valves:
        find_shortest_route(valve1, [valve1], valve2, 0)

for valve1 in valves:
    print("---", valve1, "---")
    print(shortest_routes[valve1])
    print("==================")


best_path = []
best_pressure = 0


def find_best_pressure(path, minutes, pressure):
    global best_pressure
    global best_path
    minutes = minutes - shortest_routes[path[-2]][path[-1]]["distance"] - 1
    if minutes >= 0:
        pressure = pressure + (valves[path[-1]]["flow"] * minutes)
    if minutes <= 0 or len(path) - 1 == len(flow_valves):
        if best_pressure < pressure:
            best_pressure = pressure
            best_path = path
            print("New best ", path, minutes, pressure, best_pressure)
        return
    # print('loop', path, minutes, pressure, best_pressure)
    for v in flow_valves:
        if v not in path:
            find_best_pressure(path + [v], minutes, pressure)


for v in flow_valves:
    find_best_pressure(["AA", v], 30, 0)

print(best_path, best_pressure)
print(best_pressure)
advent.clip(best_pressure)
