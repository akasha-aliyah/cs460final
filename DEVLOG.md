# Development Log – The Torchbearer

**Student Name:** Akasha Barron
**Student ID:** 827977287
---

## Entry 1 – [5/12 - Committed 6pm]: Initial Plan

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

## Entry 2 – [5/12 - Committed 12am]: Time to Grind

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

## Entry 3 – [5/13 - Committed 1am and 2:15am]: The Long Haul

I just realized that when I was putting the time on the two above entries, I put the time that I first looked at this
page for that particular coding session, instead of what time I finished the entry, so grader please forgive me for the
two times being both roughly two hours before I committed. I have changed them to be more accurate now.

Now while I don't recommend doing this kind of work this late into the night, this is what works for me. I never claimed
it to be healthy, but I do get uninterrupted work done basically for as long as I need because my roommates are already
and I can maintain the illusion of daytime with my lights on and blinds shut. My posture is aided by my computer sitting
far away and a second, closer keyboard directly in front of me. Grader, I have to confess, I love diary entries, and
unfortunately for you, you are stuck with me. If the grader happens to be Prof. Manju I actually apologize please don't 
take off points for this.

It is during question 3 that I realized how to make `these little boxes`, which is sick! I feel like I am way too deep
into my academic career to have just learned this.

It is about 1 am right now, and I am getting lazy, but I don't want to do this tomorrow so I'm at least finishing
question 6 me thinks. I am going to do an extra commit real quick just because I am slightly scared of losing progress.

Also, if you are wondering how to fall into a locked-in trance and really get into the zone, the answer comes from going
on YouTube and searching "Animal Crossing ASMR No Music", because those study aide videos genuinely changed my life.

I guess I lied because it is 2am, and I am tired now, so I am going to finish this in the morning. Honestly, it doesn't
look like I have much left and I have a self-imposed deadline of 7pm, so I really think I will be fine even though I
have to eat food and stuff. But at least I got to part 6 before I called it quits. Committing again for safety. Goodnight!

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [5/12 and 5/13 - Done as I went along.]: Time Estimate

| Part | Estimated Hours                                                                                                                                                                                                         |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Part 1: Problem Analysis | About 30 minutes because my friends were around talking to me when I was trying to read.                                                                                                                                |
| Part 2: Precomputation Design | Roughly 1 hour and a half, because I kept taking small breaks to Google other stuff (graduation prep is stressing me out!).                                                                                             |
| Part 3: Algorithm Correctness | 30 minutes? I take a lot of time to do anything, I feel like. I stop to do other things quite a bit (I stopped to online shop this time, so technically less than 30).                                                  |
| Part 4: Search Design | 20 minutes, because I was actually locked in and I have practice with greedy explanations from this exact class.                                                                                                        |
| Part 5: State and Search Space | I started this strong by taking a FaceTime call, but overall time doing this was, I think around an hour.                                                                                                               |
| Part 6: Pruning |                                                                                                                                                                                                                         |
| Part 7: Implementation |                                                                                                                                                                                                                         |
| README and DEVLOG writing | Honestly I don't know? I actually included the README times as part of the times above because I did the parts in tandem, so I would add like 30 minutes for DEVLOG writing but I think all the README time is covered. |
| **Total** |                                                                                                                                                                                                                         |
