###############
 pandas-sphinx
###############

Render a `pandas <https://pandas.pydata.org/>`_ DataFrame as an
opinionated table for `Sphinx <https://www.sphinx-doc.org/>`_.

A pandas DataFrame like…

+----+--------+-------+
|    | item   | qty   |
+====+========+=======+
| 0  | spam   | 42    |
+----+--------+-------+
| 1  | eggs   | 451   |
+----+--------+-------+
| 2  | bacon  | 0     |
+----+--------+-------+

… is converted to…

.. code::

   +--------+-------+
   | item   |   qty |
   +========+=======+
   | spam   |    42 |
   +--------+-------+
   | …      | …     |
   +--------+-------+

… and in the documentation, it looks like this:

+--------+-------+
| item   | qty   |
+========+=======+
| spam   | 42    |
+--------+-------+
| …      | …     |
+--------+-------+

.. toctree::
   :hidden:
   :maxdepth: 1

   installation
   reference
