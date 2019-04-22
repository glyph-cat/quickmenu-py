Props
=====

.. contents::

Components
----------

Like in React, you can pass props to child components.

    ::

        "body": [
            {
                "text": "Child Menu",
                "component": ChildComponent,
                "props": {
                    "name": "Anon",
                    "age": 18
                }
            }
        ]

Then access the props in child components like this:

    ::

        def __init__(self, props}):
            super().__init__(props=props)
            self.name = self.props["name"]
            self.age = self.props["age"]

        def render(self):
            return {
                "head": "",
                "body": []
                "foot": self.name + " is " + str(self.age) + " years old. ")
            }

Functions
---------

For functions, just type in its name. Remember to leave out the brackets like how it is done with a Component.

    ::

        "body": [
            {
                "text": "Child Function",
                "component": someFunction,
                "props": {
                    "name": "Anon",
                    "age": 18
                }
            }
        ]

Your props will then be made accessible as arguments.

    ::

        def someFunction(name, age):
            print(name + " is " + str(age) + " years old. ")

Other Data Types
----------------

Props will be ignored if the child component belongs to data types other then mentioned above.


Reserved Props
--------------

There are some names of props that are reserved. It is important to remember that to prevent conflicts when giving variable names. The reserved props are:

* :code:`test`
* :code:`loop`
* :code:`showOnceHead`
* :code:`showOnceBody`
* :code:`showOnceFoot`
* :code:`skipIfInvalid`
* :code:`style`
