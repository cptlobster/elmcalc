# ELMCalc
This is a calculator written using the EFL libraries. It will be a fully featured calculator utility once completed.

In it's current iteration this is somewhat of a quick-and-dirty script. I intend to improve its quality for ease of management and improved speed.

# To Do

## Top Priority
 - Improve backend code
   - Respect order of operations
   - Further objectify code
   - Move some code to separate files
   - Comply with [Python standards](https://bodhilinux.boards.net/thread/100/python3-conversion-help-wanted)
 - Add scientific display mode
   - Add trig functions
   - Add log/exp functions
   - Add toggle for degrees/radians in angles
 - Add button keybinds (0-9 for number keys, +-*/ for simple operations, enter for equals, etc.)
 - Optimize interface element sizing
   - Increase button text size with window size somehow
   - Set constant padding sizes for calculator text
   - Make all buttons the same size (except for ones that aren't supposed to be the same size)

## Mid Priority
 - Add graphing interface
 - Add unit conversion interface
 - Display stack history as popup menu or sidebar rather than/in addition to above entry

## Low Priority
 - User assignable variables
 - Add geometry interface (part of graphing?)
   - include measurements of polygons and shapes based on mathematical formulas
 - RPN stack (use genlist for display?)