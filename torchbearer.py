"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Akasha Barron
Student ID:   827977287

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq

from openpyxl.styles.builtins import total


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    answer1 = "A single shortest-path run from S is not enough to solve this because it would only consider the immediate cheapest path, which could ignore the fact that the next step after that could be incredibly expensive. It only compares the immediate step, not the entire sequence of required nodes that end at T."
    answer2 = "After considering all the inter-location costs, the decision to make it how to connect all the costs into one overall lower costs that visits every relic chamber and ends at T."
    answer3 = "We start by knowing the shortest travel costs, but different orders produce different total costs, which is why we need to search over entire orders."
    return answer1 + "\n" + answer2 + "\n" + answer3

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    sources = [spawn]   # starting with add spawn because we begin from there
    for relic in relics:
        if relic not in sources:
            sources.append(relic)
    # exit_node is intentionally excluded because we do not need shortest path from exit ; follows with readme
    return sources

def run_dijkstra(graph, source):
    distance = {}      # initialize dictionary
    for node in graph:
        distance[node] = float("inf")   # add locations, but unknown if reachable yet
    distance[source] = 0    # zero cost to get where we already are

    queue = []      # priority queue ; holds all candidates for exploration
    heapq.heappush(queue, (0, source))
    while len(queue) > 0:         # while there are still nodes to be looked at
        current_dist, current_node = heapq.heappop(queue)   # cheapest node to reach
        if current_dist > distance[current_node]:   # clear out if path is more expensive than others to same node
            continue
        for neighbor, cost in graph[current_node]:
            new_dist = current_dist + cost          # cost to reach neighbor from current node
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))     # schedule for further exploration
    return distance     # list of minimum cost from current source to any other node in the graph

def precompute_distances(graph, spawn, relics, exit_node):
    sources = select_sources(spawn, relics, exit_node)      # all possible places to start from
    distance_tbl = {}
    for source in sources:
        distance_tbl[source] = run_dijkstra(graph, source)  # current source : dict of minimum distances from source
    return distance_tbl     # look up table of distances from all possible sources


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    answer1 = "For already finalized nodes, the true shortest path from the source has already been found! It won't change because it has already been proven to be the shortest. If the node has not yet been finalized, then the distances represent the current shortest paths that we have, but that could change and hopefully improve as we work toward finalization."
    answer2 = "(Init) Before we iterate anything, we only know that the source has a distance of 0 (because we're already there) and all other nodes with currently unknown paths have not been discovered yet, so they are set to float(inf). \n(Maint) We are picking the node with the smallest distance, as far as we know, but because all the edge weights are non-negative, there is really no shorter path that can suddenly spring up later to that node from a different one. \n(Term) After all iterations have happened, the nodes are finalized and we are guaranteed to know the true shortest path from the source to each separate node."
    answer3 = "By knowing all of our correct shortest path distances, the route planner can accurately choose the optimal route because it has all correct the fuel costs between locations on hand."
    return answer1 + "\n" + answer2 + "\n" + answer3


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    answer1 = "(Fail) The greedy algorithm can choose the current closest relic without realizing it forces an incredibly expensive choice later on, because that simply isn't taken into account!"
    answer2 = "(Counter) Let us say that `S -> B = 1`, `S -> C = 2`, `C -> B = 3`, `B -> C = 100`, `B -> T = 5`, `C -> T = 1`."
    answer3 = "(Greedy) When we are starting at `S`, our greedy choice picks `B` to be our next node, but after that, the cost to get from `B` to `C` jumps to 100, which throws a wrench in the whole path."
    answer4 = "(Optimal) The optimal solution picks the overall shortest path, `S -> C -> B -> T = 10`."
    answer5 = "(Loses) Greedy doesn't pay attention to how its pick affects the order of the rest of the traversing, and what it costs the future."
    answer6 = "The algorithm must explore different order choices to see the full cost of one entire path, because the total is what really matters."
    return answer1 + "\n" + answer2 + "\n" + answer3 + "\n" + answer4 + "\n" + answer5 + "\n" + answer6


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    current_loc = spawn     # current location must start at origin
    relics_remaining = set(relics)  # all possible relics to visit
    relics_visited_order = []     # empty list
    cost_so_far = 0          # haven't gone anywhere yet!
    best = [float("inf"), []]   # going to store the best cost as float and best order as list of nodes

    _explore(dist_table, current_loc, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

    return tuple(best)     # says to specifically return a tuple

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if len(relics_remaining) == 0:      # successfully reached all relics ; base case
        cost_to_exit = dist_table[current_loc][exit_node]
        if cost_to_exit != float("inf"):    # distance is not infinity, therefore reachable
            total_cost = cost_so_far + cost_to_exit
            if total_cost < best[0]:
                best[0] = total_cost    # now minimum cost
                best[1] = relics_visited_order.copy()   # copy so that any future work does not modify this piece later
            return
    for relic in relics_remaining.copy():
        cost_to_relic = dist_table[current_loc][relic]
        if cost_to_relic == float("inf"):
            continue
        else:
            relics_remaining.remove(relic)
            relics_visited_order.append(relic)

            _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + cost_to_relic, exit_node, best)

            relics_visited_order.pop()      # putting back for future backtracking
            relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")

if __name__ == "__main__":
    _run_tests()
