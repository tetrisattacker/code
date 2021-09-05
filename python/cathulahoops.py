nachos_friends = ['athletic', 'not athletic', 'older', 'athetic', 
'younger', 'athletic', 'not athletic', 'older', 'athletic', 'older', 
'athletic']

hula_hoops_by_swings = 0
hula_hoops_by_basketball_court = 0
for i in range(len(nachos_friends)):
    if nachos_friends[i] == 'athletic' or nachos_friends[i] == 'younger':
     hula_hoops_by_swings += 1
    elif nachos_friends[i] == 'not athletic' or nachos_friends[i] == 'older':
     hula_hoops_by_basketball_court += 1

print(f"Cats at hula hoops by swings: {hula_hoops_by_swings}")
print(f"""Cats at hula hoops by basketball court:
{hula_hoops_by_basketball_court}""")