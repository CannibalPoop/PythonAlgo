def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for n in costs:
        if costs[n] < lowest_cost and n not in processed:
            lowest_cost = costs[n]
            lowest_cost_node = n
    return lowest_cost_node

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

node = find_lowest_cost_node(costs)
while node != None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + graph[node][n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs['fin'])