# sagittal average

This is a library that calculate the averages through a sagittal plane.

## Installation

Browse to the directory where this file lives, and run:
```bash
pip install .
```
That command will download any dependencies we have


## Usage

Right now we have only one function, you can use it as shown below:


```python
from sagittal_averages import sagittal_brain
sagittal_brain.run_averages("input_file.csv", "ouput_file.csv")
```

Or alternativaly you can run it from the terminal as:

```bash
$ sagverage input_file.csv -o output_file.csv
```

## Contributing

We accept contributions via GitHub!!

To install the development version, clone this repository and install it on 
a virtual environment

```bash
git clone git@github.com:UCL-MPHY0021-21-22/sagittal_average.git
python -m venv brain
soruce brain/bin/activate
cd sagittal_average
pip install -e .
... code code code ...
deactivate
```

or using a conda environment as

```bash
git clone git@github.com:UCL-MPHY0021-21-22/sagittal_average.git
conda create -n brain python=3.8
conda activate brain
cd sagittal_average
pip install -e .
... code code code ...
conda deactivate
```