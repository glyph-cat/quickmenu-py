Built-in Functions and Values
=============================

.. contents::

Functions
---------

start
~~~~~

Use this function to launch a component or start your program.

+-----------+-------------------------+---------------------+
| Arguments | Description             | Type                |
+===========+=========================+=====================+
| component | The component to launch | QuicKMenu.Component |
+-----------+-------------------------+---------------------+
| props     | The props to be passed  | dict                |
+-----------+-------------------------+---------------------+

* Returns: :code:`None`

Usage:

    ::

        from QuickMenu import start
        from MainMenu import MainMenu
        start(MainMenu)

It is best that you only use this in your :code:`__main__.py` file. While you may still use it inside your components and functions, but you will have to manage the props by yourself. Components nested as children within the body of the render method are mounted with this function as well, but the prop passing are managed automatically. In short, using this function in your project's entry point and let QuickMenu handle the rest as child components will make your code less error prone.

prompt
~~~~~~
This is an extra function that makes it easier for you to create boolean prompts.

+-------------------------+---------------------------------------------+----------------------------------------------+
| Arguments               | Description                                 | Type                                         |
+=========================+=============================================+==============================================+
| :code:`text`            | The prompt message                          | str                                          |
+-------------------------+---------------------------------------------+----------------------------------------------+
| :code:`ifYes`           | Function to be triggered if "Y" is selected | function                                     |
+-------------------------+---------------------------------------------+----------------------------------------------+
| :code:`ifNo`            | Function to be triggered if "N" is selected | function                                     |
+-------------------------+---------------------------------------------+----------------------------------------------+
| :code:`defaultResponse` | The default response of the prompt          | One of :code:`"-"`, :code:`"y"`, :code:`"n"` |
+-------------------------+---------------------------------------------+----------------------------------------------+

* Returns: :code:`None`

Example:

    ::

        def componentDidReceive(self, response, body, injected):
            super().componentDidReceive(response, body, injected)
            def yes(): pass
            def no(): self.loop = False
            prompt("Add another data?", yes, no, "y")

setW
~~~~
This functions allow you to add padding to strings, making them look neater in tables.

+-----------+-------------------------------+----------------------------------------------+
| Arguments | Description                   | Type                                         |
+===========+===============================+==============================================+
| width     | Total width of the new string | int                                          |
+-----------+-------------------------------+----------------------------------------------+
| align     | Alignment of text             | One of :code:`"l"`, :code:`"c"`, :code:`"r"` |
+-----------+-------------------------------+----------------------------------------------+
| text      | The text to be formatted      | str                                          |
+-----------+-------------------------------+----------------------------------------------+

* Returns [:code:`str`]: The formatted string.

Example:

    ::

        myString = setW(9, "c", "foo")


getGridMenu
~~~~~~~~~~~

A built-in function to format arrays into neatly aligned grid menu.

+-----------+-------------------------------------------------------------+------+---------------+
| Arguments | Description                                                 | Type | Default       |
+===========+=============================================================+======+===============+
| options   | The list                                                    | list | :code:`None`  |
+-----------+-------------------------------------------------------------+------+---------------+
| breakBy   | Number of columns to break the grid by                      | int  | :code:`None`  |
+-----------+-------------------------------------------------------------+------+---------------+
| bullet    | The bullet format                                           | str  | :code:`""`    |
+-----------+-------------------------------------------------------------+------+---------------+
| vIndex    | Indices that corresponds to the options (for vertical list) | list | :code:`None`  |
+-----------+-------------------------------------------------------------+------+---------------+
| useText   | (Internal use) Use options[i]["text"] instead of options[i] | bool | :code:`False` |
+-----------+-------------------------------------------------------------+------+---------------+

* Returns [:code:`str`]: The formatted grid menu.

Example (Horizontal list):

    ::

        breakBy = 3
        options = ["A", "B", "C", "D", "E", "F", "G"]
        myString = getGridMenu(options, breakBy, "<b>. ")

Example (Vertical list):

    ::

        breakBy = 3
        options = ["A", "B", "C", "D", "E", "F", "G"]
        vOptions = vGridTransform(options, breakBy)
        myString = getGridMenu(vOptions["arr"], breakBy, "<b>. ", vOptions["ind"])

vGridTransform
~~~~~~~~~~~~~~

Rearranges an array to be printed as vertical menu.

+-----------+-------------------------------------------------------------+------+---------------+
| Arguments | Description                                                 | Type | Default       |
+===========+=============================================================+======+===============+
| options   | The list                                                    | list | :code:`None`  |
+-----------+-------------------------------------------------------------+------+---------------+
| breakBy   | Number of columns to break the grid by                      | int  | :code:`None`  |
+-----------+-------------------------------------------------------------+------+---------------+

Returns [:code:`{ "arr": list<str>, "ind": list<int> }`]: A rearranged list and their original indices.

Example:

    ::

        breakBy = 3
        options = ["A", "B", "C", "D", "E", "F", "G"]
        vOptions = vGridTransform(options, breakBy)

Values
------

DEFAULT_PAUSE
~~~~~~~~~~~~~

+---------------+------+----------------------------------------+
| Variable      | Type | Default                                |
+===============+======+========================================+
| DEFAULT_PAUSE | str  | :code:`"Press any key to continue..."` |
+---------------+------+----------------------------------------+

Usage:

    ::

        body: [{
            "text": "Show Attendance",
            "component": self.showAttendance
            "props": {
                "style": { "pause": QuickMenu.DEFAULT_PAUSE }
            }
        }]

