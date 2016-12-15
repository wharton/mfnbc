# MFNBC

###Setup (Likeihood Input File)
It is assumed you have a word based likelihood table (csv file) where the headers consists of the literal word `Word` and the remaining columns are the features you would like to classify. 

For example:

<table style="border-collapse: collapse; width: 260pt;" border="1" width="348" cellspacing="0" cellpadding="0">
<colgroup>
<col style="width: 65pt;" span="4" width="87" /> </colgroup>
<tbody>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt; width: 65pt;" width="87" height="21"><strong>Word</strong></td>
<td style="width: 65pt;" width="87">Animal</td>
<td style="width: 65pt;" width="87">Human</td>
<td style="width: 65pt;" width="87">Plant</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">cat</td>
<td align="right">0.33</td>
<td align="right">0.03</td>
<td align="right">0.05</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">dog</td>
<td align="right">0.33</td>
<td align="right">0.02</td>
<td align="right">0.05</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">leaves</td>
<td align="right">0.05</td>
<td align="right">0.03</td>
<td align="right">0.4</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">tree</td>
<td align="right">0.05</td>
<td align="right">0.02</td>
<td align="right">0.4</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">man</td>
<td align="right">0.12</td>
<td align="right">0.45</td>
<td align="right">0.05</td>
</tr>
<tr style="height: 16.0pt;">
<td style="height: 16.0pt;" height="21">women</td>
<td align="right">0.12</td>
<td align="right">0.45</td>
<td align="right">0.05</td>
</tr>
</tbody>
</table>

###Setup (Unlabeled Data File)
The key is having the header titled  `Text` any other fields will be included unmodified in the output file.


<table style="border-collapse: collapse; width: 460pt;" border="1" width="348" cellspacing="0" cellpadding="0">
<colgroup>
<col style="width: 65pt;" span="4" width="87" /> </colgroup>
<tbody>
<tbody>
<tr>
<td width="87">ID</td>
<td width="356"><strong>Text</strong></td>
</tr>
<tr>
<td>1</td>
<td>The cat is my pet and he is lovley. A dog will not do.</td>
</tr>
<tr>
<td>2</td>
<td>The man and women had a cat and lived under a tree</td>
</tr>
<tr>
<td>3</td>
<td>The tree had lots of leaves</td>
</tr>
<tr>
<td>4</td>
<td>A man lives under a tree with many leaves. A women has a cat as a pet</td>
</tr>
<tr>
<td>5</td>
<td>The dog and cat chanse the man under the tree</td>
</tr>
<tr>
<td>6</td>
<td>The man and women live in a house.</td>
</tr>
</tbody>
</table>

###Import

```python
from mfnbc import MFNBC
```
### Instantiate

```python
m = MFNBC(<likelihoods_input_file - location of Likelihood table (str)>,
          <unlabeled_data_file - Location of unlabeled data file (str)>,
          <verbose output - Turn on of off verbose output, default: off>
```
###Example
```python
m = MFNBC('likeli_sample.csv', 'input_sample.csv', False)
m.write_csv()
```
You can also print the probability table by

```python
m.print_probs
```

