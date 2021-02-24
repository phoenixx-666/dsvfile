# dsvfile
A parser library for the [Dyson Sphere Program](https://store.steampowered.com/app/1366540) save files (.dsv)

## Installation

Clone the repository or download the code.

From the directory containing the ```setup.py``` file run:

```
python setup.py install
```

or install using ```pip```:

```
pip install .
```

## Usage

### Parsing

```python
from dsvfile import GameSave

s = GameSave()
with open('save_file.dsv', 'rb') as f:
    s.read(f)
```

The ```GameSave``` object contains all the save data as a hierarchical structure of Python objects. Its ```read``` method must be supplied with an object providing a ```read(n)``` method that returns a ```bytes``` object with length specified by ```n```.

In case of successfully parsing a save file the number of bytes read must match the file length:

```python
assert(f.tell() == os.fstat(f.fileno()).st_size)
``` 

You may want to boost the performance for the cost of memory by first loading the file contents into memory and then reading data from it:

```python
import io
from dsvfile import GameSave

with open('save_file.dsv', 'rb') as f:
    bio = io.BytesIO(f.read())

s = GameSave()
s.read(bio)
``` 

### Editing

This library supports editing and saving data. Theoretically, you can even build a new save file from scratch.

Currently, the library does not provide many foolproof features, so edit at your own risk. 

### Saving

Once you've finished editing properties of your GameSave object, you will be able to convert it back to the .dsv format: 

```python
with open('save_file_edited.dsv', 'wb') as f:
    s.write(f)
```

## Note

As the library has not been extensively tested overall, use it at your own risk.
