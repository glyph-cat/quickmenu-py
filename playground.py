from quickmenu import Component, start

class MainMenu(Component):

    def __init__(self, props):
        super().__init__(props)
        self.style["grid"] = "v-3"
        # self.test = [1, 0]
        self.autoCommit = True

    def componentDidMount(self):
        self.style["grid"] = "h-4"

    def render(self):
        return {
            "head": "Main Menu",
            "body": [{
                "text": "Hey",
                "component": "hey"
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