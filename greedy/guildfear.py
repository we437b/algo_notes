# each adventurer needs at least their fear rating number of people in their guild to go on adventure.
# maximum number of guilds to go on the adventure
# some can stay

import sys

guilds = []

# Reading Arguments
n = int(sys.argv[1])
ppl = [int(i) for i in sys.argv[2:n+2]]

sorted_ppl = sorted(ppl)
temp_guild = []
for i in sorted_ppl:
    temp_guild.append(i)
    if len(temp_guild) >= temp_guild[-1]:
        guilds.append(temp_guild)
        temp_guild = []
    
    

print(len(guilds))