# Getting started with Python on Windows
These are my preferences for getting started on a new Windows machine to match my workflow. There are many
 ways to go about using Python on Windows, but this is how I learned and it works just fine.

### Install git
git is a Software Configuration Management tool. It's not too important to describe all the details of git–
the most important aspect is version control. Essentially this lets you take snapshots of your files/project
and travel between them. Using version control is very important for any software development and it's essential
when working on a team. 

Follow [this link](https://git-scm.com/downloads/win) for the git installer. 

### Install conda
**NOTE**:  This isn't strictly required for working with the Raspberry Pico, but I highly recommend this for general
programming in Python.

conda is a distribution platform and dependency manager for Python. When writing Python we take advantage of the
hardwork from many other open source software developers around the world by downloading and using their packages.
Instead of having to reinvent the wheel everytime, we can often find a package that already does what we want. When
we use another package inside our project, that is called a dependency. conda helps us to find, install, and maintain
these dependencies. It is possible to do this manually, but it's tedious and somewhat complicated. 

Another challenge is as we start working on more Python projects they will most likely need different dependencies.
All of the packages comprising our dependencies also have dependencies of their own. Sometimes these dependencies
conflict so they are not compatible within the same environment. The "environment" is a term for all the
software packages and versions on your machine (i.e. python version, the dependencies and their versions)

For example, we have a new project and would like to use package A. Package A requires package B with a version
requirement >=2.0. But we have another project that already uses package B, and it requires version <=1.9
because the package B developers introduced major changes in verion 2.0. This is a version conflict.

conda helps us by allowing us to create new environments so we can keep our dependencies organized and
separate between projects. Think of your machine as a house and dependencies as items within that house.
If your house has no walls then your kitchen stove isn't separated from your bed or toilet. Do you want
someone using the toilet in the same room you are cooking? Or splattering cooking grease on your bed? No!
So you have rooms dedicated to certain tasks and activities that contain the right items/tools for those
purposes. conda lets us divide the house (our machine) into different rooms (environments)

Follow [this link](https://www.anaconda.com/download/success) and download a Miniconda installer. The Anaconda
installer bundles a lot of python packages with it. Sometimes that's nice, but it's a lot of uneccesary packages.
Plus, we want to get practice with setting up a new environment and adding new packages to it.

### Install an IDE
The intedgrated development environment (IDE) is where we'll spend most time coding. An IDE isn't strictly
necessary since you can write code in a text editor, but IDEs are convenient and help you to be more
productive. My recommendation is Visual Studio Code. It's fully featured and relatively language-agnostic.
The tradeoff extensions must be found and installed to get many language-specific features that are
included in purpose built IDEs. That said, extensions are very easy to find and install in VScode.

Follow [this link](https://code.visualstudio.com/download) for the VScode installer.

The CraftingTable tutorial recommends downloading [Thonny](https://thonny.org/), it's a very basic IDE, so it doesn't
have many of the convenience features included in VSCode; however, if you find VSCode overwhelming to get started in,
then it's worth going with Thonny so you can spend more time actually coding and less time learning how to use the IDE.


### Set up GitHub
This part is not strictly necessary, either, but it's good practice to get in the habit of creating a new code
repository (repo) for each project you are working on. 


### Installing packages onto Raspberry Pico
Use the package [`pipkin`](https://github.com/aivarannamaa/pipkin) to manage packages that are loaded onto the microcontroller environment. It is designed similarly
to `pip` but tailored for micropython. The IDE Thonny uses this under the hood through it's GUI. First install `pipkin`
onto your development machine
```
pip install pipkin
```

From the pipking docs:
> The basic structure of the command line is pipkin <target selection> <command> <command arguments>. For example:
>
> pipkin --port /dev/ttyACM0 install micropython-logging
> pipkin --mount G:\lib install adafruit-circuitpython-ssd1306
> pipkin --mount G:\lib install --compile adafruit-circuitpython-ssd1306
> pipkin --dir my_project/lib install micropython-logging micropython-oled
> pipkin --port COM5 uninstall micropython-logging micropython-oled
> pipkin --port COM5 list --outdated

Note that the microcontroller board cannot be connected to another application while interacting with `pipkin`.