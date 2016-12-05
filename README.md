# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer: uploaded

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:
There are widgets for this, for example Tkinter. Tkinter needs to be imported in the beginning of the document.
Also requirement to define root (root=Tk()), a canvas (with its height and width) and a canvas.pack() commit before drawing the rectangle.
After drawing the shape, it is need to be closed it by root.mainloop() commit, at the end of the document.

### What does V stand for in MVC? [2p]
#### Your answer:
It's the 'View' from the Model-View-Controller design pattern.
The view displays the model data, and sends user actions to the controller.
The view contains all of the things the user can see and respond to on the screen, such as buttons, display boxes etc.
