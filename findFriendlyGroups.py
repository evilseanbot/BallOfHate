import copy

def getEnemies(person, enemies):    
    myEnemies = []
    for j in range(len(enemies)):
        if enemies[j][0] == person:
            myEnemies.append(enemies[j][1])
        elif enemies[j][1] == person:
            myEnemies.append(enemies[j][0])                

    return myEnemies

def isHappyGroup(group, enemies):
    groupEnemies = []

    for i in group:
        if i in groupEnemies:
            return False
        groupEnemies.extend(getEnemies(i, enemies))

    return True

def groupAlreadyExists(group, groups):
    groupAlreadyExists = False
    for i in range(len(groups)):
        if sorted(groups[i]) == sorted(group):
            groupAlreadyExists = True
    return groupAlreadyExists
    

def findFriendlySubGroups(conflictedGroup, unconflictedGroup, enemies):
    global friendlyGroups

    #for testing
    global operationCounter

    if not isHappyGroup(conflictedGroup, enemies):
        newConflictedGroup = getConflictedGroup(conflictedGroup, enemies)
        unconflictedGroup.extend(getUnconflictedGroup(conflictedGroup, enemies))

        bullyConflictedGroup = copy.copy(newConflictedGroup)
        bullyConflictedGroup.pop(0)

        findFriendlySubGroups(bullyConflictedGroup, copy.copy(unconflictedGroup), enemies)
        operationCounter["ffsg"] += 1

        weirdoConflictedGroup = copy.copy(newConflictedGroup)

        for i in getEnemies(newConflictedGroup[0], enemies):
            if i in weirdoConflictedGroup:
                weirdoConflictedGroup.remove(i)

        findFriendlySubGroups(weirdoConflictedGroup, copy.copy(unconflictedGroup), enemies)
        operationCounter["ffsg"] += 1 

    else:
        conflictedGroup.extend(unconflictedGroup)
        joinedGroup = conflictedGroup
        if not groupAlreadyExists(joinedGroup, friendlyGroups):    
            friendlyGroups.append(joinedGroup) 

def removeSubsets(groups):
    examinedGroup = copy.copy(groups)
    
    for i in examinedGroup:
        for j in examinedGroup:
            if i is not j:
                if isSubset(i, j):
                    if i in groups:
                        groups.remove(i)

def isSubset(groupA, groupB):
    if len(groupA) < len(groupB):
        for i in groupA:
            if i not in groupB:
                return False
        return True
    else:
        return False

def getConflictedGroup(group, enemies):     
    conflictedGroup = []
    for i in group:
        for j in group:
            if j in getEnemies(i, enemies):
                if j not in conflictedGroup:
                    conflictedGroup.append(j)
    return conflictedGroup

def getUnconflictedGroup(group, enemies):
    unconflictedGroup = copy.copy(group)
    for i in group:
        for j in group:
            if j in getEnemies(i, enemies):
                if j in unconflictedGroup:
                    unconflictedGroup.remove(j)
    return unconflictedGroup
    
def findFriendlyGroups(initialGroup, enemies):
    global friendlyGroups
    friendlyGroups = []

    # for testing
    global operationCounter
    operationCounter = {}
    operationCounter["ffsg"] = 0

    # conflictedGroup = getConflictedGroup(initialGroup, enemies)
    # unconflictedGroup = getUnconflictedGroup(initialGroup, enemies)   
 
    # findFriendlySubGroups(conflictedGroup, unconflictedGroup, enemies)
    findFriendlySubGroups(initialGroup, [], enemies)
    operationCounter["ffsg"] += 1

    friendlyGroups = sorted(friendlyGroups, key=len, reverse=True)
    removeSubsets(friendlyGroups)

    # for i in range(len(friendlyGroups)):
    #    friendlyGroups[i].extend(unconflictedGroup)
    
    return friendlyGroups



operationCounter = {}
operationCounter["ffsg"] = 0
