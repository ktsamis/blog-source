README
======

This is the blog source for **tsamis73.github.io**.

The script **publish.sh** is committing (and pushing) the /output folder to the right repository
which is the blog_. After that it commits (and pushes) the source files without
the /output folder to the source_.


.. _blog: https://github.com/tsamis73/tsamis73.github.io.git
.. _source: https://github.com/tsamis73/blog-source.git

the .gitignore file in the source_ is ignoring the /output and the cache folder.
The important thing here and the *purpose* of the script is that the content is 
saved and pushed pretty easily.

Instructions
------------
To convert the /content folder that has all the rst documents to html you have
to run:

.. code-block:: text

  pelican content/

After that all you have to do is run the script:

.. code-block:: text

  ./publish.sh

You need to give the username and the passwords `twice`, once for the blog_
repository and once for the source_.

**And that's it!**
