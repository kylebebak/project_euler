## Project Euler Assignment
- 107 Minimal Network
- 230 Fibonacci Words
- 349 Langton's Ant

### Solution scripts (general invocation from root directory)
```sh
python euler/_107_minimal_network.py <path_to_graph_file>
python euler/_230_fibonacci_words.py <string_1> <string_2>
python euler/_349_langton_ant.py <num_steps>
```

#### 107 Minimal Network
```sh
python euler/_107_minimal_network.py euler/assets/107_network.txt

# 259679
# Duration: 0.0077478885650634766s
```

#### 230 Fibonacci Words
```sh
python euler/_230_fibonacci_words.py 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

# 850481152593119296
# Duration: 0.000453948974609375s
```

#### 349 Langton's Ant
```sh
python euler/_349_langton_ant.py 1000000000000000000

# 115384615384614952 black squares after 1000000000000000000 moves
# Duration: 0.05420112609863281s
```


### Unit tests
The unit tests cover all of the data structures by solution scripts. Because they use relative imports, they should be run as modules as opposed to python scripts. __They must be run from the project's root directory, or else the relative imports won't work.__
```sh
# run all unit tests
python -m unittest discover euler.tests -v

# run unit tests in a single module
python -m euler.tests.test_union_find -v
python -m euler.tests.test_graph_mst -v
python -m euler.tests.test_langton -v
```

### Doc tests
Only problem 230 uses doc tests. Invoking it without any arguments will cause the script to exit, but the doc tests will still execute.
```sh
python euler/_230_fibonacci_words.py -v
```




### Choice of problems


### Problem-solving process


### References
For inspiration on implementing data structures
http://algs4.cs.princeton.edu/code/

For information about Langton's Ant
http://mathworld.wolfram.com/LangtonsAnt.html

### Time spent
~15 hours
