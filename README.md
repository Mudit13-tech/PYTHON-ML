# Python for ML

The Python groundwork I'm doing before moving into machine learning: first
object-oriented programming, then the scientific stack (NumPy, then pandas,
Matplotlib and Seaborn).

## What's here

All the files are in `OOPS/` for now:

| File | Concept |
| --- | --- |
| `bankkingapp.py` | Classes, constructors, private attributes and static members, through a menu-driven ATM |
| `coordinate.py` | `Point` and `Line` classes: distance, distance from origin |
| `fractions.py` | A `Fraction` class with operator overloading (`+`, `-`, `*`, `/`) |
| `aggregation.py` | Aggregation: a `Customer` that holds an `Address` |
| `inheritance.py`, `inhertiancesnip.py` | Inheritance, private attributes in a parent class, method overriding |
| `super_constructor.py` | Calling a parent constructor with `super()` |
| `nums.py` | NumPy basics: creating arrays, dtypes, `arange`, `reshape`, `ones`/`zeros` |

## Running

Each file runs on its own:

```bash
python OOPS/fractions.py
```

`nums.py` needs NumPy (`pip install numpy`).
