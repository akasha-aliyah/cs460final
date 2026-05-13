# Development Log – The Torchbearer

**Student Name:** Akasha Barron
**Student ID:** 827977287
---

## Entry 1 – [5/12 - 4pm]: Initial Plan

I am writing this as I have just created my github repository. Looking over the assignment, this seems like a fun one! 
I like the creativity that was put into spicing up the questions just for our amusement. First, I needed to read
everything like four times because having this assignment split into three separate files that have different pieces of
the same question took me a second to make sure I understood everything.

The hardest thing that I think I'm going to struggle with is the pruning part of this, because the limited amount of
fuel doesn't allow for any backtracking. That makes unreachable routes so much more difficult, because of the inability 
to fix a mistake. I am going to start largely in order because I think that it's laid out nicely for students to tackle,
but I think I'll do run_dijkstra first and make everything else around those ideas. I'll test this with really simple 
graphs to just make sure it works so that I'm not stuck misunderstanding what the errors are.

Just so that the grader knows, I did do this entire project in basically one go besides some eating and sleeping, so the
dates on these entry logs are going to be pretty much all the same. That's why I'm also leaving the hour that I'm doing 
this, so yes this is going to be all in one day but like bear with me.

---

## Entry 2 – [5/12 - 10:30pm]: Time to Grind

This is when I started the majority of my work, because I had finished all the things I needed to do and was ready to
just sit with a cold can of Coke and really get down to it. I work best at night after I feel like I've enjoyed my day,
eaten nutritious food, and relaxed, so I was ready to focus and get to work.

A struggle I encountered in this section was when I was building my run_dijkstra function, because when creating my 
dictionary to save the distance between the current source node and its neighbors, I set dictionary = {0 : source},
which would have been fine if the next line was not overriding all the nodes from our source list (select_sources) with
the float("inf") value. I noticed when I tested this with a simple graph and kept getting an output that said inf. Any 
new distance that I tried to calculate would stay at inf because nothing could be different (new_dist = current_dist + 
cost). Everything literally stays completely still! It broke my distance_tbl because all nodes were considered 
unreachable. I had to change it to initialize it first, run the loop, and then set the source to 0.

---

## Entry 3 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [5/12 - Done as I went along.]: Time Estimate

| Part | Estimated Hours                                                                                                             |
|---|-----------------------------------------------------------------------------------------------------------------------------|
| Part 1: Problem Analysis | About 30 minutes because my friends were around talking to me when I was trying to read.                                    |
| Part 2: Precomputation Design | Roughly 1 hour and a half, because I kept taking small breaks to Google other stuff (graduation prep is stressing me out!). |
| Part 3: Algorithm Correctness |                                                                                                                             |
| Part 4: Search Design |                                                                                                                             |
| Part 5: State and Search Space |                                                                                                                             |
| Part 6: Pruning |                                                                                                                             |
| Part 7: Implementation |                                                                                                                             |
| README and DEVLOG writing |                                                                                                                             |
| **Total** |                                                                                                                             |
