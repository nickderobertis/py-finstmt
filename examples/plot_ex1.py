# -*- coding: utf-8 -*-
"""
Introductory example - Plotting sin
===================================

This is a general example demonstrating a Matplotlib plot output, embedded
rST, the use of math notation and cross-linking to other examples. It would be
useful to compare with the
output below.

.. math::

    x \\rightarrow \\sin(x)

Here the function :math:`\\sin` is evaluated at each point the variable
:math:`x` is defined.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$\sin(x)$')
# To avoid matplotlib text output
plt.show()

#%%
# To include embedded rST, use a line of >= 20 ``#``'s or ``#%%`` between your
# rST and your. This separates your example
# into distinct text and code blocks. You can continue writing code below the
# embedded rST text block:

print('This example shows a sin plot!')

#%%
from py_qs_example.mymodule import ExampleClass, example_function, less_important_function
ec = ExampleClass(5)
ec

#%%
output = example_function(ec, '_test')
output

#%%
# LaTeX syntax in the text blocks does not require backslashes to be escaped:
#
# .. math::
#    \sin
#
# Cross referencing
# ^^^^^^^^^^^^^^^^^
#
# You can refer to an example from any part of the documentation,
# including from other examples. Sphinx-Gallery automatically creates reference
# labels for each example. The label consists of the ``.py`` file name,
# prefixed with ``sphx_glr_`` and the name of the
# folder(s) the example is in. In this case, the example we want to
# cross-reference is in ``auto_examples`` (the ``gallery_dirs``; see