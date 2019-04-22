Style
=====

.. contents::

Overview
--------
:code:`self.style` itself belongs to the dictionary data type.
Styles can be passed on to child components via the :code:`"style"` prop. When a :code:`"style"` prop is being passed, this is automatically merged into :code:`self.style` for you, hence, it is important to remember that :code:`"style"` is a reserved keyword when it comes to defining props.

+----------+--------------------------------------------------+-----------+--------------------------------+
| Property | Description                                      | Type      | Default                        |
+==========+==================================================+===========+================================+
| grid     | Controls the layout of the printed menu (body)   | str       | :code:`"none"`                 |
+----------+--------------------------------------------------+-----------+--------------------------------+
| exitText | The exit label showed on top of the printed menu | str       | :code:`"Exit"`, :code:`"Back"` |
+----------+--------------------------------------------------+-----------+--------------------------------+
| bullet   | The bullet format used in showing menu items     | str       | :code:`"<b>. "`                |
+----------+--------------------------------------------------+-----------+--------------------------------+
| prompt   | The prompt label showed below the foot           | str       | :code:`"> "`                   |
+----------+--------------------------------------------------+-----------+--------------------------------+
| pause    | The pause text shown after an action             | None, str | :code:`None`                   |
+----------+--------------------------------------------------+-----------+--------------------------------+

Defining Styles
---------------
There are three ways in which a component determines which styles to use:

1. Explicitly Defined
~~~~~~~~~~~~~~~~~~~~~
Component first try to use the styles explicitly defined in :code:`__init__()`

    ::

        def __init__(self, props}):
            super().__init__(props=props)
            self.style["grid"] = "h-3"
            self.style["pause"] = "Press any key"
            # or
            self.style = {
                "grid": "h-3",
                "pause": "Press any key"
            }

2. Through Props
~~~~~~~~~~~~~~~~
Else, styles passed in as props will be used

    ::

        "body": [
            {
                "text": "Submenu 1",
                "component": Submenu",
                "props": {
                    "style": {
                        "grid": "h-3",
                        "pause": "Press any key"
                    }
                }
            }
        ]

3. Default
~~~~~~~~~~
Otherwise, the default values as describe in the table above are used.

self.style["grid"]
-------------------------
Controls how your menu is printed. This does not apply if you override the :code:`stringifyBody()` method. However, this value is acessible and you can use it for your own implementation instead.

self.style["exitText"]
----------------------
Defaults to to "Exit" in a root component and "Back" in a nested component.

self.style["bullet"]
--------------------
You can specify any string for your bullet. The :code:`<b>` in the string will then be replaced with the indices of the menu items. For example, this bullet :code:`"-(<b>)-"` transpiles into :code:`-(1)-`

self.style["prompt"]
--------------------
The string that will be shown when asking for a response.
By default it looks like this:

    ::

        0. Exit
        1. Action 1
        2. Action 2

        > _

But you can still be creative and perhaps customize it to look like this:

    ::

        0. Exit
        1. Action 1
        2. Action 2

        Please enter a response: _

self.style["pause"]
-------------------
This pause text (if specified) only appears after a menu item is selected, if the child component is a function or any data type. Components do not "pause" because they are meant to loop and already pauses each time when asking for a response.
The pause text will not be shown during response injection.

*Example of a pause text shown, given that "Action 1" is a function:*

    ::

        0. Exit
        1. Action 1
        2. Action 2

        Please enter a response: 1

        Hello world
        Press any key to continue..._
