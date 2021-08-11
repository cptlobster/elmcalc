import numpy as np


class Stack():
    def __init__(self):
        # create stack
        self.values = []
        self.executed = False
        self.expressions = 0
        self.radians = True

    def get_stack(self, stack=None):
        # get stack as a string
        stackinput = ""
        if stack == None:
            stack = self.values
        for i in stack:
            stackinput += str(i["value"])

        if stackinput == "":
            stackinput = "0"

        return stackinput

    def get_end_raw(self):
        # get end of the stack as a raw stack value
        entryinputstack = [""]
        if self.values == []:
            entryinput = {"value": "0", "type": "number"}

        else:
            for i in self.values:
                if i["type"] == "number" or i["type"] == "point":
                    entryinputstack[-1] += str(i["value"])
                else:
                    entryinputstack.append("")

            entryinput = {"value": entryinputstack[-1], "type": "number"}
            if entryinput["value"] == "":
                entryinput = self.values[-1]

        return entryinput

    def get_end(self):
        # get value at end of the stack as a string
        value = self.get_end_raw()
        if value["type"] != "number":
            vs = "0"
        else:
            vs = value["value"]

        return vs

    def push(self, value):
        # push a value to the stack
        # determine value type and return dict
        value = {
            "value": value,
            "type": "operation"
        }

        # create type for values
        if value["value"] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # Number value
            value["value"] = int(value["value"])
            value["type"] = "number"
            if self.executed:
                self.reset()

        elif value["value"] == ".":
            # Decimal point
            value["type"] = "point"
            if self.executed:
                self.reset()

        elif value["value"] == "+/-":
            if (self.values[-1]["type"] == "number"):
                self.values[-1]["value"] *= -1
            value["type"] = "clear"

        elif value["value"] == "CLEAR":
            # Clear all
            self.reset()
            value["type"] = "clear"

        elif value["value"] == "CE":
            # Clear entry
            if len(self.values) > 0:
                if self.values[-1]["type"] == "operation":
                    self.expressions -= 1
                self.values.pop()
            value["type"] = "clear"

        elif value["value"] == "BKSP":
            # Backspace
            if self.executed:
                self.reset()
            if len(self.values) > 0:
                if self.values[-1]["type"] != "number" or self.values[-1]["value"] < 10:
                    self.values.pop()
                    if len(self.values) > 0 and self.values[-1]["type"] == "operation":
                        self.expressions -= 1
                else:
                    self.values[-1]["value"] = int(
                        np.floor(self.values[-1]["value"] / 10))
            value["type"] = "clear"

        elif value["value"] == "=":
            # Execute
            value["type"] = "execute"
            self.executed = True

        if self.executed and value["type"] != "execute":
            self.executed = False

        # add value to stack based on type
        if value["type"] != "clear":
            if len(self.values) != 0:
                # do not allow multiple decimal points in single number
                if {"value": ".", "type": "point"} in self.values[-3:] and value["type"] == "point":
                    pass
                # do not allow multiple simple operations next to each other
                elif self.values[-1] != "operation" or value["type"] != "operation":
                    # combine numbers into single stack entries
                    if value["type"] != "number" or self.values[-1]["type"] != "number":
                        if value["type"] == "operation":
                            self.expressions += 1
                        self.values.append(value)
                    else:
                        self.values[-1]["value"] = self.values[-1]["value"] * \
                            10 + value["value"]

            elif value["type"] == "number" or value["type"] == "point":
                if value["value"] != 0:
                    self.values.append(value)

        return value

    def calculate(self, stack=None):
        # execute all calculations currently on the stack
        evalstring = ""
        if stack == None:
            stack = self.values
        for i in stack:
            if i["type"] != "execute":
                evalstring += str(i["value"])
            else:
                break

        result = eval(evalstring)
        return {"value": result, "type": "number"}

    def reset(self):
        # reset stack
        self.values = []
        self.expressions = 0


class Memory():
    def __init__(self):
        self.history = []
        self.vars = {}

    def create_var(self, name, value):
        var = {name: value}
        self.vars = {**self.vars, **var}

    def get_var(self, name):
        return self.vars[name]

    def del_var(self, name):
        self.vars.pop(name)

    def clear_vars(self):
        self.vars = {}

    def push_stack(self, value, result):
        value.append(result)
        self.history.append(value)

    def get_stack(self, index):
        return self.history[index]

    def clear_history(self):
        self.history = []

    def clear_memory(self):
        self.clear_history()
        self.clear_vars()


if __name__ == "__main__":
    print("You seem lost, friend.\nPerhaps you should try running main.py instead?")
