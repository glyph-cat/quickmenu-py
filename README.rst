QuickMenu Readme
================

.. contents::

Introduction
------------
Quickmenu is a framework for creating menu-driven interfaces inspired by `React <https://reactjs.org>`_.
By structuring your menus as components, you can keep your syntax cleaner and focus on the core logic of your program while Quick Menu handles the looping part.

QuickMenu was first created in Python, but since it's the logic behind it that makes this framework what it is, there are plannings to convert QuickMenu to other languages as well. With that said, anything new will most probably be implemented in the Python version of the framework first, then added to the frameworks for other languages shortly.

Currently targeting:

+------------+-------------+
| Language   | Status      |
+============+=============+
| Python     | Beta stage  |
+------------+-------------+
| C++        | Pending     |
+------------+-------------+
| Java       | Pending     |
+------------+-------------+
| JavaScript | Alpha stage |
+------------+-------------+

Getting Started
---------------

Setup
~~~~~

In your project's entry point (presummably `__main__.py`), add in these three lines

    ::

        from QuickMenu import start
        from MainMenu import MainMenu
        start(MainMenu)

Then create another file called ``MainMenu.py``, and add in these contents.

    ::

        from QuickMenu import Component

        class MainMenu(Component):

            def __init__(self, props):
                super(self, props)

            def render(self):
                return {
                    "head": "Hello World",
                }

Now open up your terminal and try to run ``__main__.py``, you should be able to see the following output in the terminal:

    ::

        Hello World

        0. Exit

        >

Type ``0`` and press Enter to exit the program. The setup is pretty much complete here.

Adding components
~~~~~~~~~~~~~~~~~

Now, in the render method, add something to the body:

    ::

        def render(self):
            return {
                "head": "Hello World",
                "body": [{
                    "text": "Say hi",
                    "component": "Hi"
                }]
            }

Run the program again, type ``1`` and press Enter, and you should be able to see this:

    ::

        Hello World

        0. Exit
        1. Say hi

        > 1
        Hi

And so, this is how items can be added to the menu. Specify the text and component, and that's it.

Generally speaking, there can be three types of child components: **Any Data Type**, **Function** or **QuickMenu Component**, and this is what happens when you select an item on the menu if the child component is ...

* Simply any data type, it will be printed out
* A function, the function will be called
* A QuickMenu Component, the component will be mounted

So let's add the other two now!

1. Add :code:`from SubMenu import SubMenu` at the beginning of ``MainMenu.py``.
2. Add a method called :code:`sayHi` to the class
3. Add :code:`sayHi` and :code:`SubMenu` to the body.
4. Your file should look like this:

    ::

        from QuickMenu import Component
        from SubMenu import SubMenu

        class MainMenu(Component):

            def __init__(self, props):
                super(self, props)

            def sayHi(self):
                print("Hi (this is from a function)")

            def render(self):
                return {
                    "head": "Hello World",
                    "body": [{
                        "text": "Say hi",
                        "component": "Hi"
                    }, {
                        "text": "Say hi (Func)",
                        "component": self.sayHi
                    }, {
                        "text": "SubMenu",
                        "component": SubMenu
                    }]
                }

The syntax is correct but you won't be able to run it just yet. In the next chapter, we'll be adding another QuickMenu Component.

Nesting Components
~~~~~~~~~~~~~~~~~~

Create another file called ``SubMenu.py`` and populate it with the following contents:

    ::

        from QuickMenu import Component

        class SubMenu(Component):

            def __init__(self, props):
                super(self, props)

            def render(self):
                return {
                    "head": "This is a submenu"
                    "body": [{
                        "text": "Item 1",
                        "component": "I am the first item"
                    }, {
                        "text": "Item 2",
                        "component": "I am the second item"
                    }]
                }

Now import SubMenu and nested in the body of MainMenu as shown below:

    ::

        from SubMenu import SubMenu

        # ...

            }, {
                "text": "SubMenu",
                "component": SubMenu
            }]

        # ...

Run your program again and it should work now.

Below is an output you that can expect from what we've built so far:

    ::

        Hello World

        0. Exit
        1. Say hi
        2. Say hi (Func)
        3. SubMenu

        > 1
        Hi

        Hello World

        0. Exit
        1. Say hi
        2. Say hi (Func)
        3. SubMenu

        > 2
        Hi (this is from a function)

        Hello World

        0. Exit
        1. Say hi
        2. Say hi (Func)
        3. SubMenu

        > 3

        This is a submenu

        0. Back
        1. Item 1
        2. Item 2

        > 1
        I am the first item

        This is a submenu

        0. Back
        1. Item 1
        2. Item 2

        > 2
        I am the second item

        This is a submenu

        0. Back
        1. Item 1
        2. Item 2

        > 0

        Hello World

        0. Exit
        1. Say hi
        2. Say hi (Func)
        3. SubMenu

        > 0

You first program built with QuickMenu is ready!
