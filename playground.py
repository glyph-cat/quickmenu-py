from quickmenu import Component, start

class SubMenu(Component):

    def __init__(self, props):
        super().__init__(props)

    def render(self):
        return {
            "head": "",
            "body": [{
                "text": "Say Hello",
                "component": "HELLO"
            }]
        }

class MainMenu(Component):

    def __init__(self, props):
        super().__init__(props)
        self.style["grid"] = "v-3"
        # self.test = [1, 0]
        self.autoCommit = 1

    def componentDidMount(self):
        self.style["grid"] = "h-4"

    def fn(self):
        self.navigate(SubMenu)

    def render(self):
        return {
            "head": "Main Menu",
            "body": [{
                "text": "Hey",
                "component": "hey"
            }, {
                "text": "goto submenu",
                "component": self.fn
            }, {
                "text": "foo",
                "component": "HI"
            }, {
                "text": "bar",
                "component": "HI"
            }, {
                "text": "baz",
                "component": "HI"
            }, {
                "text": "hello",
                "component": "HI"
            }, {
                "text": "world",
                "component": "HI"
            }, {
                "text": "meow",
                "component": "HI"
            }, {
                "text": "HI",
                "component": "HI"
            }, {
                "text": "foo",
                "component": "HI"
            }, {
                "text": "bar",
                "component": "HI"
            }, {
                "text": "baz",
                "component": "HI"
            }, {
                "text": "hello",
                "component": "HI"
            }]
        }

start(MainMenu)