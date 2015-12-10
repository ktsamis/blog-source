Pelican Installation and basic configuration
============================================

This is the classic post that deals with the creation of the blog itself.
I would normally skip this entirely but I wanted to record this for posterity
and well, this is the *purpose* of the blog. To keep notes. So here goes:


**Don't use jekyll**

Seriously, if there is one thing I learned in the creation of this blog is that.
Jekyll is the most used static html generator but I really don't understand why.
It may be great for markdown but since I want to use `rst` I needed to install a plugin
to make that work. What is surprising to me was that I had problem with the installation
itself. I managed to get through them to have a page up and running but it still 
took me all day to configure rst with a them and have a page running. Anyway. Pelican.

1.Install
---------

Pelican site_

.. _site: http://docs.getpelican.com/en/3.6.3/quickstart.html

.. code-block:: text                                                                                                                                                                                               

  pip install pelican markdown

There are some questions about the name of your site, if you want to access it through ssh etc.
Answer them or if you don't understand them give the default :)




2.Create content
-----------------

Put your articles in ``~/path/to/site/content/``
If they are in ``rst`` format the filename needs to end with ``.rst``
If they are in ``markdown`` format the filename needs to end with ``.md``




3.Generate your site
--------------------


.. code-block:: text

  pelican content/

The above will generate the html pages that will be used in the site from the 
``content/`` folder from the ``rst`` or ``md`` documents. The resulting ``html``
pages will be put in the ``output/`` folder by default. You can override the setting
of the input document location by giving:

.. code-block:: text                                                                                                                                                                                               

  pelican /path/to/your/content/

That't it. You have a ready site to be published.
