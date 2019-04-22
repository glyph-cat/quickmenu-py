#!/usr/bin/env python3

"""A framework for designing menu-driven interface console programs inspired by React."""

from math import ceil, floor
from inspect import getargspec
from re import findall, compile as rgxCompile
from sys import exit
from traceback import format_exc

__author__ = "chin98edwin"
__license__ = "MIT"
__version__ = "0.1.0"
__errorcount__ = 0 # Do not tamper with this
__maxErrorCount__ = 999
DEFAULT_PAUSE = "Press any key to continue..."

# Customs Errors
class NotRenderedError(NotImplementedError): """The `render()` method must be overwritten."""
class NotReturnedError(NotImplementedError): """The `render()` method must return an object."""

def start(component, props={}):
    """Use this function to launch a component or start your program.

    :param component: The component to launch
    :type component: QuickMenu.Component
    :param props: The props to be passed
    :type props: dict

    """
    route = props["route"] if "route" in props else []
    route.append(findall(r"[A-z]{1,}(?='>)", str(component))[0])
    props.update({ "route": route })
    c = component(props)
    c.__launch__()

def prompt(text, ifYes, ifNo, defaultResponse="-"):
    """A simple function for showing boolean prompts.

    :param text: The prompt message
    :type text: str
    :param ifYes: Function to be triggered if "Y" is selected
    :type ifYes: function
    :param ifNo: Function to be triggered if "N" is selected
    :type ifNo: function
    :param defaultResponse: The default response of the prompt
    :type defaultResponse: One of "y" or "n"

    """

    # Configure hint for default response
    optionPreset = "(y/n)"
    defaultResponse = defaultResponse.upper()
    if defaultResponse == "Y": optionPreset = "(Y/n)"
    elif defaultResponse == "N": optionPreset = "(y/N)"

    # Show prompt
    response = input(text + " " + optionPreset + " ")
    if response == "":
        response = defaultResponse
        print("(DEFAULT=" + defaultResponse + ")")
    else: response = response.lower()

    # Call function according to response
    if defaultResponse == "Y":
        if response == "Y": ifYes()
        else: ifNo()
    elif defaultResponse == "N":
        if response == "N": ifNo()
        else: ifYes()

def setW(width, align, text):
    """Add padding to strings.

    :param width: Total width of the new string
    :type width: int
    :param align: Alignment of text
    :type align: One of "l", "c" or "r"
    :param text: The text to be formatted
    :type text: str

    :returns: The formatted string.
    :rType: str

    """
    diff = width - len(text)
    if align == "l": # "left"
        return text + (" " * diff)
    elif align == "c": # center
        halfDiff = floor(diff / 2)
        return (" " * (halfDiff if (diff % 2 == 0) else (halfDiff + 1))) + text + (" " * halfDiff)
    elif align == "r": # right
        return (" " * diff) + text
    else:
        raise ValueError("Expected `align` to be one of ['l', 'c', 'r'] but got " + str(type(align)) + " instead. ")

def getGridMenu(options, breakBy, bullet = "", vIndex = None, useText = False):
    """Creates a neatly arranged grid menu.

    :param options: The list
    :type options: list
    :param breakBy: Number of columns to break the grid by
    :type breakBy: int
    :param bullet: The bullet format
    :type bullet: str
    :param vIndex: Indices that corresponds to the options (for vertical list)
    :type vIndex: list
    :param useText: (Internal use) Use options[i]["text"] instead of options[i]
    :type useText: bool

    :returns: The formatted grid menu.
    :rType: str

    """
    output = ""
    maxLenPerRow = [0 for i in range(breakBy)]
    for i in range(len(options)):
        labelToMeasure = ""
        try:
            labelToMeasure = options[i]["text"] if useText else options[i]
            if len(labelToMeasure) > maxLenPerRow[i % breakBy]:
                maxLenPerRow[i % breakBy] = len(labelToMeasure)
        except: pass
    for i in range(len(options)):
        if i > 0 and i % breakBy == 0: output += "\n"
        maxBulletLen = len(bullet.replace("<b>", str(len(options) + 1)))
        blt = bullet.replace("<b>", str((vIndex[i] if vIndex else i) + 1))
        width = maxLenPerRow[i % breakBy]
        label = ""
        try: label = options[i]["text"] if useText else options[i]
        except: pass
        if label == "":
            output += setW(maxBulletLen + width + 2, "l", " " * len(blt) + "")
        else:
            output += setW(maxBulletLen + width + 2, "l", blt + label)
    return output

def vGridTransform(options, breakBy):
    """Rearranges an array for vertical menu printing.

    :param options: The list
    :type options: list
    :param breakBy: Number of columns to break the grid by
    :type breakBy: int

    :returns: A rearranged list and their original indices.
    :rType: { "arr": list<str>, "ind": list<int> }

    """
    breakBy_vert = ceil(len(options) / breakBy)
    vInd = [[] for i in range(breakBy_vert)]
    vArr = [[] for i in range(breakBy_vert)]
    for i in range(len(options)):
        vArr[i % breakBy_vert].append(str(options[i]))
        vInd[i % breakBy_vert].append(i)
    for i in range(len(vArr)):
        while len(vArr[i]) < breakBy:
            vArr[i].append(None)
            vInd[i].append(0)
    return {
        "ind": [j for sub in vInd for j in sub],
        "arr": [j for sub in vArr for j in sub],
    }

class Component(object):
    """Inherit this object to begin designing your menu."""

    def __init__(self, props):
        """You must call this method to initialize the component."""

        # Basic properties - DO NOT tamper with these values
        self.renderCount = 0
        self.props = props
        self.route = self.props["route"] if ("route" in self.props) else ["Unknown"]

        # Control variables - Modify to control how the component behaves
        self.responseWasValid = True
        self.test = self.props["test"] if ("test" in self.props) else []
        self.loop = self.props["loop"] if ("loop" in self.props) else True
        self.showOnceHead = self.props["showOnceHead"] if ("showOnceHead" in self.props) else False
        self.showOnceBody = self.props["showOnceBody"] if ("showOnceBody" in self.props) else False
        self.showOnceFoot = self.props["showOnceFoot"] if ("showOnceFoot" in self.props) else False
        self.skipIfInvalid = self.props["skipIfInvalid"] if ("skipIfInvalid" in self.props) else True

        # Configurable styles - Customize these values to your heart's content!
        self.style = {
            "grid": "none",
            "exitText": "Exit" if (len(self.route) <= 1) else "Back",
            "bullet": "<b>. ",
            "prompt": "> ",
            "pause": None
        }
        if "style" in self.props: self.style.update(self.props["style"])

    def render(self):
        """Called to process the rendarable contents."""
        return {}

    def componentWillPrint(self, head, body, foot):
        """Called before the rendered contents are actually printed.
        This method is intended for debug and testing purposes only."""
        pass

    def componentDidCatch(self, exception):
        """Called when the component catches an error.
        Call `self.__launch__()` in your overridden method if you wish to re-mount component."""
        print("\n\nAn error has occured in the following component:\n • " + " > ".join(self.route) + "\n\nWrap the component with an Error Boundary to handle this error. \n" + findall(r"([A-Z][A-z]{1,})", str(type(exception)))[-1] + ": " + exception.__doc__ + "\n\n" + format_exc())
        exit()

    def componentDidMount(self):
        """Called when the component is first loaded."""

    def componentDidLoop(self):
        """Called when the component has repeated itself."""

    def componentDidReceive(self, response, body, injected):
        """Called when the component receives a response.
        If overridden, you'll need to provide your own method for response validation.
        Do not call super on this method while overriding."""

        # To help automatically evaluate to invalid input
        try: response = int(response)
        except BaseException: response = -1

        if response == 0:
            # By default 0 should be reserved for exit purposes
            self.loop = False
        elif response > 0 and response <= len(body):
            selected = body[response - 1]; propPause = None
            def callPause(propPause=propPause):
                if injected: return
                try: propPause = selected["props"]["style"]["pause"]
                except: pass
                if self.style["pause"]: input(self.style["pause"])
                elif propPause: input(propPause)
            if hasattr(selected["component"], "__launch__"):
                # Is Component
                newProps = { "response": response, "route": self.route }
                if "props" in selected: newProps.update(selected["props"])
                start(selected["component"], newProps)
            elif hasattr(selected["component"], "__call__"):
                # Is function
                rawProps = { "response": response }
                if "props" in selected: rawProps.update(selected["props"])
                argList = getargspec(selected["component"]).args
                argToProps = []
                for arg in argList:
                    if arg in rawProps and arg != "self": argToProps.append(rawProps[arg])
                    elif arg != "self": argToProps.append(None)
                selected["component"](*argToProps)
                callPause()
            else:
                # Is other data type
                print(selected["component"])
                callPause()
        else:
            self.responseWasValid = False
            print("Invalid input. ")

    def componentWillLoop(self):
        """Called before the component repeats itself."""

    def componentWillUnmount(self):
        """Called right before the component exits."""

    def __stringifyBody__(self, body): # Override with caution
        """The function used to control how the body is printed.
        Do not call super on this method while overriding."""

        # Determine if grid is applicapable
        mode = "default"; breakBy = 1
        rgx = rgxCompile(r"(v|h)-\d{1,}")
        if bool(rgx.match(self.style["grid"])):
            bl = self.style["grid"].split("-")
            mode = bl[0]; breakBy = int(bl[1])

        def formatIndex(value, maxLen):
            value = str(value); maxLen = str(maxLen)
            return (" " * (len(maxLen) - len(value))) + value
        UNNAMED_LABEL = "<Unnamed component>"

        # Print exit text
        output = self.style["bullet"].replace("<b>", formatIndex(0, len(body)))
        output += self.style["exitText"] + "\n"

        # Compile the output based on specified mode
        index = 1
        if mode == "h":
            output += getGridMenu(body, breakBy, self.style["bullet"], None, True)
        elif mode == "v":
            vBody = vGridTransform(body, breakBy)
            output += getGridMenu(vBody["arr"], breakBy, self.style["bullet"], vBody["ind"], True)
        else: # Print as normal list
            for item in body:
                output += self.style["bullet"].replace("<b>", formatIndex(index, len(body)))
                output += item["text"] if ("text" in item) else UNNAMED_LABEL
                if index < len(body): output += "\n"
                index += 1

        return output.expandtabs(1)

    def __launch__(self): # DO NOT override
        """The function used to launch a component."""
        try:
            while (self.loop == True):

                # (1) Get items to render from the render method
                rendered = self.render()
                if rendered is None: raise NotReturnedError()
                elif rendered == {}: raise NotRenderedError()

                # (2) Fetch rendered contents
                # injectResp = rendered["injectResp"] if ("injectResp" in rendered) else []
                head = rendered["head"] if ("head" in rendered) else ""
                body = rendered["body"] if ("body" in rendered) else []
                foot = rendered["foot"] if ("foot" in rendered) else ""
                toPrint = ""

                # (3) Control when `head`|`body`|`foot` should be printed
                if self.responseWasValid or not self.skipIfInvalid:
                    if not(self.showOnceHead == True and self.renderCount != 0):
                        if head != "": toPrint += (head + "\n\n")
                    if not (self.showOnceBody == True and self.renderCount != 0):
                        toPrint += self.__stringifyBody__(body)
                    if not (self.showOnceFoot == True and self.renderCount != 0):
                        if foot != "": toPrint += ("\n\n" + foot)

                # (4) Printing of rendered contents
                self.componentWillPrint(head, body, foot)
                print(toPrint)

                # (5) Post-render processes
                self.responseWasValid = True
                self.renderCount += 1
                if self.renderCount == 1: self.componentDidMount()
                else: self.componentDidLoop()

                # (6) Handle response injection
                injected = False
                if len(self.test) > 0:
                    response = self.test.pop(0)
                    print("\n" + self.style["prompt"] + str(response) + " (INJECTED)")
                    injected = True
                else:
                    response = input("\n" + self.style["prompt"])

                # (7) Proceed with action selected by the response
                # Reprint component if response is empty in case console was cleared
                if response != "": self.componentDidReceive(response, body, injected)
                if self.loop: self.componentWillLoop()
                print("")

            # The method that will be called when component has break free of its loop
            self.componentWillUnmount()

        except SystemExit:
            exit()
        except KeyboardInterrupt:
            print("")
            exit()
        except BaseException as exception:
            global __errorcount__
            if __errorcount__ < __maxErrorCount__:
                __errorcount__ += 1
                self.componentDidCatch(exception)
            else:
                print("\n——— FATAL ERROR: The maximum error loop count has been reached ———\n")
                exit()
