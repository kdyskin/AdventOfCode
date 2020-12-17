SPOILER
Lemme give you an innocent hint - all your bus IDs are PRIME numbers.

If you look at just one bus, let’s say its id=7. With one bus it is simple, it will be back every 7 minutes (increment=7).
Now lets expand and look at two busses. Say second bus has id=13 and offset 1, like in AoC example. We already know first bus rounds every 7 time intervals. So we are looking for timestamp X which is multiples of 7, and also X+1 multiples of 13. First such X is 77.
So at t=77 you can “fuse” bus 1 and bus 2 as they will repeat their alignment pattern from this point in time onwards every Xn time intervals. Here is the key part - your increment was 7, that’s how we got to 77, in order to “fuse” bas 1 and bus 2 you would multiply 7*13 and your new increment, a.k.a. Xn will be 91, so from time=77 bus 1 and bus 2 will align in the same formation every 91 time intervals. t = 77+91 = 168. 168%7 = 0 and (168+1)%13 = 0. Now you wanna align your fused buses with bus 3
