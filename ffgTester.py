import time
import findFriendlyGroups as ff

for i in range(26):
    enemies = []
    for j in range(i/2):
        enemies.append([1, (j*2)+1])

    start = time.clock()
    x = ff.findFriendlyGroups(range(26), enemies)
    stop = time.clock()
    runtime = stop - start
    print str(i) + ": " + str(runtime)
    print ff.operationCounter["ffsg"]

