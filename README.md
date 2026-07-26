# Python Basics

A collection of small, standalone Python scripts for practicing core language
features: printing, loops, list comprehensions, recursion, and basic OOP.

## Requirements

- Python 3
- No third-party packages (see `requirements.txt`)

## Files

| File            | Concept                                                              |
| --------------- | --------------------------------------------------------------------- |
| `helloWorld.py` | Basic `print` statement                                               |
| `foreach.py`    | `for` loops over a list and a dict, conditionals, `%` string formatting |
| `listcomp.py`   | List comprehensions with a filter condition                           |
| `listcomp2.py`  | List comprehensions filtering/transforming strings                    |
| `quickSort.py`  | Recursive quicksort using list comprehensions                         |
| `shop.py`       | `FruitShop` class demonstrating basic OOP, with inventory tracking, restocking, and order discounts |
| `shopTest.py`   | Demo script that imports `shop.py` and exercises `FruitShop`          |
| `test_shop.py`  | `unittest` suite covering `FruitShop`, including stock limits and discounts |

## Running

Each script can be run directly, e.g.:

```bash
python helloWorld.py
python quickSort.py
python shopTest.py
```

`shopTest.py` imports `shop.py`, so both files must stay in the same directory.

Run the automated test suite with:

```bash
python -m unittest test_shop.py
```
