b2tob3
======

Easier migration from Boostrap 2 to Boostrap 3
----------------------------------------------

This is a simple Python script that replaces certain strings in the files
contained within the working directory and its subdirectories. It does not fully
automate migration, you'll most likely need to perform manual fixes too.

Installation
------------

    $ pip install b2tob3

Usage
-----

    $ cd /project/html/
    $ b2tob3

Follow these steps to avoid frustration:
----------------------------------------

* Put your HTML/template files under version control, if they aren't yet.
* Change to the directory with the files containing Boostrap 2 specific markup.
* Run the b2tob3 script once and only once.
* Review the changes with a diff tool suitable for the version control system you use.
* Perform the rest of the necessary changes manually.

Contributing
------------

* Let me know about bugs by posting an issue.
* Help reduce the manual work by improving the code.
* Write tests.

Contributors
------------

Thanks to `@demiurg <https://github.com/demiurg>`_ for adding more robust
replacements and command line options.