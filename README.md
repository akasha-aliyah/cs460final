# The Torchbearer

**Student Name:** Akasha Barron
**Student ID:** 827977287
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
A single shortest-path run from S is not enough to solve this because it would only consider the immediate cheapest path,
which could ignore the fact that the next step after that could be incredibly expensive. It only compares the immediate
step, not the entire sequence of required nodes that end at T.

- **What decision remains after all inter-location costs are known:**
After considering all the inter-location costs, the decision to make it how to connect all the costs into one overall
lower costs that visits every relic chamber and ends at T.

- **Why this requires a search over orders (one sentence):**
We start by knowing the shortest travel costs, but different orders produce different total costs, which is why we need
to search over entire orders.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type  | Why it is a source                                                                         |
|-------------------|--------------------------------------------------------------------------------------------|
| Spawn Node (S)    | We must start at the spawn node, and from there we compute each initial travel cost.       |
| Relic Nodes (R_i) | All subsequent travel costs are calculated here, from relic to relic and then to the exit. |

### Part 2b: Distance Storage

| Property | Your answer                                                             |
|---|-------------------------------------------------------------------------|
| Data structure name | dictionary of dictionaries : distance_tbl                               |
| What the keys represent | outer key : source node ; inner key : destination node                  |
| What the values represent | minimum amount of fuel needed to get from current source to destination |
| Lookup time complexity | O(1)                                                                    |
| Why O(1) lookup is possible | dictionary hashing gives us constant-time access to stored distances    |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log(n))
- **Total complexity:** O((k + 1)m log(n))
- **Justification (one line):** The cost of a run is given to us, and we have to run it k + 1 times, once for S and once
for each of the k relics.

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
For already finalized nodes, the true shortest path from the source has already been found! It won't change because it
has already been proven to be the shortest.

- **For nodes not yet finalized (not in S):**
If the node has not yet been finalized, then the distances represent the current shortest paths that we have, but that
could change and hopefully improve as we work toward finalization.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
Before we iterate anything, we only know that the source has a distance of 0 (because we're already there) and all other
nodes with currently unknown paths have not been discovered yet, so they are set to float("inf").

- **Maintenance : why finalizing the min-dist node is always correct:**
We are picking the node with the smallest distance, as far as we know, but because all the edge weights are non-negative,
there is really no shorter path that can suddenly spring up later to that node from a different one.

- **Termination : what the invariant guarantees when the algorithm ends:**
After all iterations have happened, the nodes are finalized and we are guaranteed to know the true shortest path from
the source to each separate node.

### Part 3c: Why This Matters for the Route Planner

By knowing all of our correct shortest path distances, the route planner can accurately choose the optimal route because
it has all correct the fuel costs between locations on hand.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** The greedy algorithm can choose the current closest relic without realizing it forces an
incredibly expensive choice later on, because that simply isn't taken into account!
- **Counter-example setup:** Let us say that `S -> B = 1`, `S -> C = 2`, `C -> B = 3`, `B -> C = 100`, `B -> T = 5`, `C 
-> T = 1`.
- **What greedy picks:** When we are starting at `S`, our greedy choice picks `B` to be our next node, but after that, 
the cost to get from `B` to `C` jumps to 100, which throws a wrench in the whole path. 
- **What optimal picks:** The optimal solution picks the overall shortest path, `S -> C -> B -> T = 10`.
- **Why greedy loses:** Greedy doesn't pay attention to how its pick affects the order of the rest of the traversing,
and what it costs the future.

### What the Algorithm Must Explore

The algorithm must explore different order choices to see the full cost of one entire path, because the total is what
really matters.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
