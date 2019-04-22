loop = True
loopB = True
attendanceList = ["P", "P", "A", "L"]
choiceWasValid = True

def invalidHandler():
    global choiceWasValid
    choiceWasValid = False

def exitMenu():
    global loop
    loop = False

def addAttendance():
    global attendanceList, loopB
    choiceBWasValid = True
    def exitLoopB(loopB = loopB): loopB = False
    while loopB:
        menuToPrint = "Add an attendance\n\n"
        menuToPrint += "0. Back\n"
        menuToPrint += "1. Punctual\n"
        menuToPrint += "2. Late\n"
        menuToPrint += "3. Absent\n"
        if choiceBWasValid: print(menuToPrint)
        def addPunctual(): attendanceList.append("P")
        def addLate(): attendanceList.append("L")
        def addAbsent(): attendanceList.append("A")
        switch = {
            0: exitLoopB,
            1: lambda: addPunctual,
            2: lambda: addLate,
            3: lambda: addAbsent,
        }
        response = input("Add an attendance: ")
        action = switch.get(response, invalidHandler)
        action()
        if choiceBWasValid: addAgain = input("Add another attendance? (Y/n)")
        def ifYes(): pass
        if addAgain == "":
            addAgain = "Y"
            print("(DEFAULT=Y)")
        else: addAgain = addAgain.lower()
        if addAgain == "Y": ifYes()
        else: exitLoopB()

def showAbsentCount():
    count = 0
    for a in attendanceList:
        if a == "A": count += 1

def showKeys():
    print("P = Punctual\nA = Absent\nL = Late")

while loop:
    menuToPrint = "Main Menu\n\n"
    menuToPrint += "0. Exit"
    menuToPrint += "1. Add Attendance"
    menuToPrint += "2. Show Absent count"
    menuToPrint += "3. Show Keys"
    if choiceWasValid: print(menuToPrint)
    switch = {
        0: exitMenu,
        1: addAttendance,
        2: showAbsentCount,
        3: showKeys
    }
    response = input("Please enter a choice: ")
    action = switch.get(response, invalidHandler)
    action()
