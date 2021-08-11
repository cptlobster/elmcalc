# import necessary classes
import efl.elementary as elm
from efl.elementary.window import StandardWindow, DialogWindow
from efl.elementary.label import Label
from efl.elementary.box import Box
from efl.elementary.table import Table
from efl.elementary.button import Button
from efl.elementary.segment_control import SegmentControl
from stack import Stack, Memory
from buttons import ButtonArrays

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
import numpy as np

# set up evas hints
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

# create main window class
class MainWindow(StandardWindow):
    def __init__(self):
        # create window
        StandardWindow.__init__(self, "elmcalc", "Calculator", size=(600, 400))
        self.callback_delete_request_add(lambda o: elm.exit())

        # create layout box
        self.box = Box(self)
        self.box.size_hint_weight = EXPAND_BOTH
        self.box.size_hint_align = FILL_BOTH
        self.box.show()

        # create button table
        self.button_table = Table(self)
        self.button_table.homogeneous_set(True)
        self.button_table.size_hint_weight = EXPAND_BOTH
        self.button_table.size_hint_align = FILL_BOTH

        # create button row above button
        self.toprow = Table(self)
        self.toprow.size_hint_weight = (EVAS_HINT_EXPAND, 0.01)
        self.toprow.size_hint_align = (0, EVAS_HINT_FILL)

        # create calculator mode selector menu
        # rework this maybe?
        self.selector = SegmentControl(self)
        self.subselector = SegmentControl(self)
        self.selector.item_add(None, "Calculator")
        self.subselector.item_add(None, "Standard")
        self.subselector.item_add(None, "Scientific")
        # self.subselector.item_add(None, "RPN")
        self.selector.item_add(None, "Geometry")
        self.selector.item_add(None, "Converter")
        self.selector.item_add(None, "Settings")
        # adjust 0 to change launch state, may set up command flag for end user (--mode [std, sci, etc.])
        self.selector.item_get(0).selected = True
        # adjust 0 to change launch state, may set up command flag for end user (--mode [std, sci, etc.])
        self.subselector.item_get(0).selected = True
        self.selector.callback_changed_add(self.setCalcMode)
        self.subselector.callback_changed_add(self.setDispMode)
        self.selector.scale_set(1.4)
        self.selector.size_hint_weight = (EVAS_HINT_EXPAND, 0.01)
        self.selector.size_hint_align = FILL_BOTH
        # self.selector.show()
        # self.box.pack_end(self.selector)
        self.subselector.scale_set(1.4)
        self.subselector.size_hint_weight = (EVAS_HINT_EXPAND, 0.01)
        self.subselector.size_hint_align = FILL_BOTH
        self.subselector.show()
        self.box.pack_end(self.subselector)

        # create input fields
        self.stackdisp = Label(self)
        self.stackdisp.text = "0"
        self.stackdisp.scale_set(1.4)
        self.stackdisp.size_hint_weight = (EVAS_HINT_EXPAND, 0.02)
        self.stackdisp.size_hint_align = (0.95, EVAS_HINT_FILL)
        self.stackdisp.show()
        self.box.pack_end(self.stackdisp)
        self.entry = Label(self)
        self.entry.text = "0"
        self.entry.scale_set(3)
        self.entry.size_hint_weight = (EVAS_HINT_EXPAND, 0.1)
        self.entry.size_hint_align = (0.95, EVAS_HINT_FILL)
        self.entry.show()
        self.box.pack_end(self.entry)

        # create stack vars
        self.stack = Stack()
        self.memory = Memory()

        # run display setup
        self.setDispMode()

        # set layout box as resize-object
        self.resize_object_add(self.box)

    def update(self):
        # update UI
        stackinput = self.stack.get_end_raw()
        entryvar = self.stack.get_end()

        self.stackdisp.text = self.stack.get_stack()

        # this doesn't work with current stack evaluation method; will try to implement later
        # if stackinput["type"] == "operation":
        #     if self.stack.expressions > 1:
        #         entryvar = self.stack.calculate()["value"]

        if stackinput["type"] == "execute":
            value = self.stack.calculate()
            self.memory.push_stack(self.stack.values, value)
            self.stack.reset()
            self.stack.values.append(value)
            entryvar = value["value"]

        self.entry.text = str(entryvar)

    def buttonPressed(self, btn):
        # append button value to stack and update
        self.stack.push(btn.text)
        self.update()

    def topButtonPressed(self, btn):
        # print history
        if btn.text == "History":
            print(
                f"-=-=-= CALCULATION HISTORY ({len(self.memory.history)} entries) =-=-=-")
            for i in self.memory.history:
                print(self.stack.get_stack(i))

        # print variables
        elif btn.text == "Variables":
            print(
                f"-=-=-= ACTIVE USER VARIABLES ({len(self.memory.vars)} entries) =-=-=-")
            for i in self.memory.vars.keys:
                print(f"{i}: self.stack.get_var(i)")

        # clear history
        if btn.text == "Clear History":
            self.memory.clear_history()

        if btn.text == "Clear Variables":
            self.memory.clear_vars()

        if btn.text == "Clear Memory":
            self.memory.clear_memory()
            self.stack.reset()

        if btn.text == "About":
            dia = DialogWindow(self, "elmcalc-dialog", "About",
                               size=(250, 150), autodel=True)
            with open("about.txt", "r") as f:
                about_desc = f.read()
            lb = Label(dia, text=about_desc, size_hint_weight=EXPAND_BOTH)
            lb.line_wrap_set(elm.ELM_WRAP_WORD)
            lb.scale_set(1.4)
            lb.show()
            dia.resize_object_add(lb)
            dia.show()

        self.update()

    def setAngleMode(self, btn):
        if not self.stack.radians:
            self.stack.radians = True
            btn.text = "RAD"
        else:
            self.stack.radians = False
            btn.text = "DEG"

    def setBase(self, btn):
        pass

    def setCalcMode(self, btn=None, value=None):
        pass

    def setDispMode(self, btn=None, value=None):
        # create calculator buttons
        btns = ButtonArrays()
        if self.subselector.item_selected == self.subselector.item_get(0):
            bdict = btns.standard(self)
        elif self.subselector.item_selected == self.subselector.item_get(1):
            bdict = btns.scientific(self)
        else:
            bdict = btns.standard(self)

        stackrow = bdict["stackrow"]
        srcallbacks = bdict["srcallbacks"]
        buttons = bdict["buttons"]
        callbacks = bdict["callbacks"]
        positions = bdict["positions"]

        if btn is not None:
            self.button_table.clear(True)
            self.toprow.clear(True)

        # add buttons to tables
        for j in range(0, len(stackrow)):
            stackrow[j].callback_clicked_add(srcallbacks[j])
            stackrow[j].scale_set(1.4)
            stackrow[j].size_hint_weight = (1, 1)
            stackrow[j].size_hint_align = FILL_BOTH
            stackrow[j].show()
            self.toprow.pack(stackrow[j], j, 0, 1, 1)

        for i in range(0, len(buttons)):
            for j in range(0, len(buttons[i])):
                buttons[i][j].callback_clicked_add(callbacks[i][j])
                buttons[i][j].scale_set(2)
                buttons[i][j].size_hint_weight = (1, 1)
                buttons[i][j].size_hint_align = FILL_BOTH
                buttons[i][j].show()
                self.button_table.pack(
                    buttons[i][j], positions[i][j][0], positions[i][j][1], positions[i][j][2], positions[i][j][3])

        # show tables
        self.toprow.show()
        self.box.pack_end(self.toprow)
        self.button_table.show()
        self.box.pack_end(self.button_table)


if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
