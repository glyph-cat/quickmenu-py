Control Variables
=================

.. contents::

Overview
--------

The :code:`Component` class comes with several properties that you may change to control how it behaves.
You can either specify them in the :code:`__init__()` method like this:

    ::

        def __init__(self, props):
            super().__init__(props=props)
            self.showOnceHead = True

Or pass them by props like this:

    ::

        body: [{
            "text": "Submenu",
            "props": { "showOnceHead": True }
        }]

However, only the :code:`self.responseWasValid` control variable will not be passed as a prop. This is because it is meant to be controlled within the component itself and not by its parent component.

+------------------+----------------------------------------------+------+---------------+---------------------+
| Property         | Description                                  | Type | Default       | Accessible by Props |
+==================+==============================================+======+===============+=====================+
| responseWasValid | A flag incidating the validity of a response | bool | :code:`True`  | No                  |
+------------------+----------------------------------------------+------+---------------+---------------------+
| test             | Responses injected when prompted for input   | list | :code:`[]`    | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+
| loop             | Allows the component to loop                 | bool | :code:`True`  | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+
| showOnceHead     | Force component head to show only once       | bool | :code:`False` | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+
| showOnceBody     | Force component body to show only once       | bool | :code:`False` | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+
| showOnceFoot     | Force component foot to show only once       | bool | :code:`False` | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+
| skipIfInvalid    | Skips head/body/foot upon invalid response   | bool | :code:`True`  | Yes                 |
+------------------+----------------------------------------------+------+---------------+---------------------+

self.loop
---------

When set to :code:`True`, the component will keep looping:

* show the head/body/foot

* prompt for a response

* trigger the corresponding action

* repeat

When set to :code:`False`, the component will unmount when it reaches the end of it's current loop, which is after receiving a response and when it's corresponding functions have been completed. This variable can be changed at anytime or in any method of the class.

self.showOnceHead
-----------------

The head is usually the menu title for your component.
When set to :code:`True`, the it will only be shown once after it is mounted. If it has been unmounted previously and mounted again, the head will still be displayed. It is advised that you configure this once in the :code:`__init__()` function and leave it as it is.

self.showOnceBody
-----------------
The body is where your menu choices are displayed.
When set to :code:`True`, the it will only be shown once after it is mounted. If it has been unmounted previously and mounted again, the head will still be displayed. It is advised that you configure this once in the :code:`__init__()` function and leave it as it is.

self.showOnceFoot
-----------------
The foot is usually where you add in additional description that will be shown below the body.
When set to :code:`True`, the it will only be shown once after it is mounted. If it has been unmounted previously and mounted again, the head will still be displayed. It is advised that you configure this once in the :code:`__init__()` function and leave it as it is.

self.responseWasValid
---------------------
This specifies whether the received response is valid. By default, this has already handled in the :code:`componentWillReceive()` method. If you override the :code:`componentWillReceive()` method, you will need to write your own implementation to determine whether a response is valid there.

self.skipIfInvalid
-------------------------
By default, the head, body and foot will be omitted upon receiving an invalid response to reduce clutter on screen.
When set to :code:`False`, they will be printed upon every loop, regardless of the response.

self.test
-------------------
This control variable is intended for debugging only. This allows you to literally "inject" responses so that you can automate your tests.
For example, if your menu has two actions, you can specify your test like this :code:`[1, 2, 0]`)
This will automatically trigger the first and second functions by sequence and then exit the menu (Since by default, :code:`0` is reserved for exiting a menu)
