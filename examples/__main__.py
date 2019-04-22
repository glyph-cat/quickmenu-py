from quickmenu import start, Component, prompt

class MainMenu(Component):

    def __init__(self, props):
        super().__init__(props=props)
        self.attendanceList = ["P", "P", "A", "L"]

    def componentWillUnmount(self):
        print("Program has been terminated by user. ")

    def showAbsentCount(self):
        absCount = 0
        for a in self.attendanceList:
            if a == "A": absCount += 1
        print("Absent count: " + str(absCount))

    def setAttendance(self, status):
        self.attendanceList.append(status)

    def render(self):
        return {
            "head": "Simple Attendance System",
            "body": [{
                "text": "Show keys",
                "component": "P = Punctual\nA = Absent\nL = Late"
            }, {
                "text": "Show absent count",
                "component": self.showAbsentCount
            }, {
                "text": "Add attendance",
                "component": AddAttendanceMenu,
                "props": { "setAttendance": self.setAttendance }
            }]
        }

class AddAttendanceMenu(Component):

    def __init__(self, props):
        super().__init__(props=props)

    def componentDidReceive(self, response, body, injected):
        super().componentDidReceive(response, body, injected)
        def yes(): pass
        def no(): self.loop = False
        prompt("Add another attendance?", yes, no, "y")

    def render(self):
        return {
            "head": "Add an attendance",
            "body": [{
                "text": "Punctual",
                "component": self.props["setAttendance"],
                "props": { "status": "P" }
            }, {
                "text": "Late",
                "component": self.props["setAttendance"],
                "props": { "status": "L" }
            }, {
                "text": "Absent",
                "component": self.props["setAttendance"],
                "props": { "status": "A" }
            }]
        }

start(MainMenu)