def spaceshipBuilding(cans):
    total_cans = 0
    for week in range(1,53):
        total_cans = total_cans + cans
        print('week %s = %s cans'%(week,total_cans))
spaceshipBuilding(2)     
