MFNBC
=====

Links
~~~~~

- PyPi - https://pypi.python.org/pypi/mfnbc/
- Github - https://github.com/wharton/mfnbc

About The Math
~~~~~~~~~~~~~~
This package computes a set of simple arithmetic to calculate the final posterior probabilities for a set of features over a set of texts within a corpus.

So for each text in the corpus, the package looks to see if the word in contained in the provided likelihood table. If it is found, the posterior probabilities for each feature is updated as using `Bayesian statistics
<https://en.wikipedia.org/wiki/Posterior_probability>`_.


.. image:: https://research-it.wharton.upenn.edu/wp-content/uploads/2016/12/eq1.gif

where

.. image:: https://research-it.wharton.upenn.edu/wp-content/uploads/2016/12/eq2.gif

is:

.. image:: https://research-it.wharton.upenn.edu/wp-content/uploads/2016/12/eq3.gif

Requirements
~~~~~~~~~~~~

Python >= 3.3

Install
~~~~~~~

``pip install mfnbc``

Setup (Likelihood Input File)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is assumed you have a word based likelihood table (csv file) where
the headers consists of the literal word ``Word`` and the remaining
columns are the features you would like to classify.

For example:

+----------+----------+---------+---------+
| Word     | Animal   | Human   | Plant   |
+----------+----------+---------+---------+
| cat      | 0.33     | 0.03    | 0.05    |
+----------+----------+---------+---------+
| dog      | 0.33     | 0.02    | 0.05    |
+----------+----------+---------+---------+
| leaves   | 0.05     | 0.03    | 0.4     |
+----------+----------+---------+---------+
| tree     | 0.05     | 0.02    | 0.4     |
+----------+----------+---------+---------+
| man      | 0.12     | 0.45    | 0.05    |
+----------+----------+---------+---------+
| women    | 0.12     | 0.45    | 0.05    |
+----------+----------+---------+---------+

Setup (Unlabeled Data File)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------------------------------------------------------------+
| ID | Text                                                                  |
+----+-----------------------------------------------------------------------+
| 1  | The cat is my pet and he is lovely. A dog will not do.                |
+----+-----------------------------------------------------------------------+
| 2  | The man and women had a cat and lived under a tree                    |
+----+-----------------------------------------------------------------------+
| 3  | The tree had lots of leaves                                           |
+----+-----------------------------------------------------------------------+
| 4  | A man lives under a tree with many leaves. A women has a cat as a pet |
+----+-----------------------------------------------------------------------+
| 5  | The dog and cat chase the man under the tree                          |
+----+-----------------------------------------------------------------------+
| 6  | The man and women live in a house.                                    |
+----+-----------------------------------------------------------------------+

The key is having the header titled ``Text`` any other fields will be
included unmodified in the output file.


Import
~~~~~~

.. code:: python

    from mfnbc import MFNBC

Instantiate
~~~~~~~~~~~

.. code-block:: python

    m = MFNBC(<likelihoods_input_file - location of Likelihood table (str)>,
              <unlabeled_data_file - Location of unlabeled data file (str)>,
              <verbose output - Turn on of off verbose output, default: off>

Example
~~~~~~~

.. code:: python

    m = MFNBC('likeli_sample.csv', 'input_sample.csv', False)
    m.read_likelihoods()
    m.calc_posteriors()
    m.write_csv()

or you can do it all in a single command

.. code:: python

    m = MFNBC('likeli_sample.csv', 'input_sample.csv', False).write_csv()


Example Results
~~~~~~~~~~~~~~~

+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| ID | Text                                                                  | Animal      | Human       | Plant       |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 1  | The cat is my pet and he is lovely. A dog will not do.                | 0.972321429 | 0.005357143 | 0.022321429 |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 2  | The man and women had a cat and lived under a tree                    | 0.580787094 | 0.2969934   | 0.122219506 |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 3  | The tree had lots of leaves                                           | 0.01532802  | 0.003678725 | 0.980993256 |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 4  | A man lives under a tree with many leaves. A women has a cat as a pet | 0.334412386 | 0.1026038   | 0.562983814 |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 5  | The dog and cat chase the man under the tree                         | 0.921839729 | 0.00761851  | 0.070541761  |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+
| 6  | The man and women live in a house.                                    | 0.065633546 | 0.922971741 | 0.011394713 |
+----+-----------------------------------------------------------------------+-------------+-------------+-------------+


