Innocent hint - all your bus IDs are **PRIME** numbers.
# SPOILER from here on
If you look at just one bus, let’s say its id=7 (bus 7 we will call it). With one bus it is simple, it will be back every 7 time intervals (increment=7).
Now lets expand and look at two busses. Say second bus has id=13 and offset=1, same AoC example (and we will call it bus 13). We already know bus 7 rounds every 7 time intervals. So we are looking for timestamp **T** which is multiples of 7 where **T+1** (1 here is offset of bus 13) multiples of 13. First such T is 77.
At T=77 you can “fuse” bus 7 and bus 13 as they will repeat their alignment pattern from T point in time onwards every **X** time intervals. Here is the key part - your increment was 7, that’s how we got to 77, in order to “fuse” bas 7 and bus 13 you would multiply 7 by 13 and your new increment **X** is 91. Why you ask? Because every bus to be "fused" is a prime number. From time=77 bus 7 and bus 13 will align in the same formation every 91 time intervals. 

- T = 77+91 = 168. 168%7 = 0 and (168+1)%13 = 0 
- T = 168+91 = 259. 259%7 = 0 and (259+1)%13 = 0

Lets refer to this "fused" buses tuple as (7,13). Moving on to next bus, it is 59 with offset=4. We will be incrementing **T** by **X** until we find such **T** that (T+4)%59=0. AoC examples rule BTW, cause T = 259 + 91 = 350 is it:

- 350%7 = 0
- (350+1)%13 = 0
- (350 + 4)%59 = 0

### Hooray
And we already know that from T=350 every 5369 time intervals "fused" (7,13,59) will align in the same formation.
I will let you move on to the next bus without my help b(~_^)d
