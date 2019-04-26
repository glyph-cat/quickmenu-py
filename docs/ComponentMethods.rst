Component Methods
=================

.. contents::

_\_\init_\_
-----------
This is the constructor of the Component object. You MUST override the :code:`__init__()` method and call :code:`super().__init__(props=props)` regardless of props. If you are to modify control variables such as :code:`self.showOnce...`, :code:`self.skipIfInvalid` and :code:`self.test`, it is adviced that you do them here and not change their values later on to prevent confusion.


render
------
In this method, you can specify how you want your menu to be rendered. The render method should return a dictionary that looks like this:

    ::

        def render(self):
            # Rendering logic
            regHint = " (Empty)"
            if len(self.registrationList) > 0:
                regHint = len(self.registrationList)

            # Dictionary to return
            return {
                "head": "Welcome to MainMenu",
                "body": [{
                    "text": "Register",
                    "component": self.register
                }, {
                    "text": "View Registered" + regHint,
                    "component": self.showRegistered
                }]
            }

Then, your menu would look like this initially:

    ::

        Welcome to MainMenu

        0. Exit
        1. Register
        2. View Registered (Empty)

After making some registrations (assuming that you have written the :code:`self.register` method by yourself), the :code:`self.regitrationList` should have some elements inside already and its length would be greater than 0. Then, upon the next loop, your menu will look like this:

    ::

        Welcome to MainMenu

        0. Exit
        1. Register
        2. View Registered (1)

Apart from head and body, there are a few more things that you can specify. Below is a complete list of them.

+-------+-----------------------------------+-------+---------------+
| Name  | Description                       | Type  | Default       |
+=======+===================================+=======+===============+
| head  | Text shown above the menu         | str   | :code:`""`    |
+-------+-----------------------------------+-------+---------------+
| body  | The contents of the menu          | list  | :code:`[]`    |
+-------+-----------------------------------+-------+---------------+
| foot  | Text shown below the menu         | str   | :code:`""`    |
+-------+-----------------------------------+-------+---------------+

In each item of the body array, you are required to specify the :code:`text` and :code:`component`, :code:`props` are optional.



componentWillPrint
------------------
This is a method meant for debugging. You will be provided with three arguments, namely: :code:`head`, :code:`body` and :code:`foot`. This method will be called everytime before the head, body and foot are printed. You can use this function to perform comparisons programatically and check if the printed output meets your expectations.

componentDidCatch
-----------------
This method will be called when an error occurs in your component. You will be provided with an :code:`exception` argument and from there you can handle the error on your own. This method is supposed to be the last resort in case if a component cannot render correctly. For example, you can print a message saying that the function is not available and ask the user to restart the program then set :code:`self.loop` to :code:`False`.

# TODO: Show example error message

componentDidMount
-----------------
This method is called after a component is mounted. No arguments are provided in this method. Basically you can do anything here, but if it's for initializing the component, it is better place your code in the constructor.

componentDidLoop
----------------
This method is called after a loop has been completed. A loop means that the head, body and foot of the menu has been shown, a response has been prompted and received, and the actions corresponding to the response has been completed. No arguments are provided in this method.

componentDidReceive
-------------------
This method is called when the component receives a response. You are provided with three arguments:

+------------------+---------------------------------------------+------+
| Arguments        | Description                                 | Type |
+==================+=============================================+======+
| :code:`respose`  | The response received                       | str  |
+------------------+---------------------------------------------+------+
| :code:`body`     | The entire body from the render method      | list |
+------------------+---------------------------------------------+------+
| :code:`injected` | Indicates whether the response was injected | bool |
+------------------+---------------------------------------------+------+

By default, a very neat algorithm has been written. You can either override it and call :code:`super()`, then put your code below it, or completely rewrite the method for a more fine-tuned response handling experience. Of course, we hope hope that you will rarely find the need to rewrite this method as it is a tedious process.

TIP: Prompt messages such as "Add another data? (y/n)" should be place in this method (with :code:`super` called first or course). Then based on the input (y/n) change the value of :code:`self.loop`.

componentWillLoop
-----------------
This method is called if a component is going to loop again. No arguments are provided in this method.

componentWillUnmount
--------------------
This method is called right before a component unmounts itself. No arguments are provided in this method.

To give you a sense of what you can do with this method, you can for example, in your root component, override it and add a message like "Program has been terminated by the user".

stringifyBody
-------------
This method is used to create the body of the component. A :code:`body` argument is provided here. By default, there is also a nicely written code to handle how a menu is printed. You may override it to customize the appearance of your menu.

navigate
--------
This method is used to navigate from the current component to a child. Each time a selection from the menu is made, we make use of this function is as well.

_\_\launch_\_
-------------

The launch method is where the loop actually occurs. You should avoid overriding this method at all costs as it is rather complex and a minor mistake may break the entire component.
