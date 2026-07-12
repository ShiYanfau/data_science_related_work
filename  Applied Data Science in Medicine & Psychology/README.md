# Applied Data Science in Medicine & Psychology

This repository collects completed Jupyter/Google Colab notebooks for the
**Applied Data Science in Medicine & Psychology** course. The notebooks progress
from basic Python syntax to data handling, scientific computing, statistics, and
biomedical signal visualization.

The main course material is stored in:

```text
 Applied Data Science in Medicine & Psychology/
```

Note: in this checkout, the folder name starts with a leading space. Quote the
path when using terminal commands.

## Contents

| Notebook | Topic | Main skills |
| --- | --- | --- |
| `“0_setup.ipynb”` | Setup | Google Colab setup, GitHub setup, assignment submission workflow |
| `1_python_basics_I.ipynb` | Python Basics I | calculations, variables, operators, comments, simple plotting |
| `2_python_basics_II.ipynb` | Python Basics II | functions, data types, lists, conditionals, loops, type casting |
| `3_control_flow.ipynb` | Control Flow and Order of Operations | `range`, `pass`, `continue`, `break`, list comprehension, validation checks, error handling |
| `4_dicts_classes.ipynb` | Dictionaries and Classes | dictionaries, patient records, classes, inheritance, simple medical record objects |
| `5_numpy_scipy.ipynb` | NumPy and SciPy | arrays, questionnaire scoring, Perceived Stress Scale, ECG filtering, R-peak based heart-rate estimation |
| `6_pandas.ipynb` | Pandas | DataFrames, indexing, filtering, grouping, multi-index data, glucose test and stress-study examples |
| `7_statistics.ipynb` | Statistics | distributions, outlier correction, normality checks, homoscedasticity checks, statistical tests |
| `8_visualization.ipynb` | Visualization | Matplotlib figures, ECG visualization, R-peak plotting, heart-rate distributions, box plots |

`Untitled0.ipynb` appears to be an empty temporary notebook and is not part of
the assignment sequence.

## Repository Structure

```text
.
├── README.md
├──  Applied Data Science in Medicine & Psychology/
│   ├── “0_setup.ipynb”
│   ├── 1_python_basics_I.ipynb
│   ├── 2_python_basics_II.ipynb
│   ├── 3_control_flow.ipynb
│   ├── 4_dicts_classes.ipynb
│   ├── 5_numpy_scipy.ipynb
│   ├── 6_pandas.ipynb
│   ├── 7_statistics.ipynb
│   ├── 8_visualization.ipynb
│   └── Untitled0.ipynb
└── Data Science Survival Skills/
```

The `Data Science Survival Skills/` directory contains additional coursework
material from a separate data-science course.

## Environment

The notebooks were written for Google Colab, but most of them can also be run
locally with Jupyter.

Recommended local setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas scipy matplotlib biopsykit pingouin neurokit2 ipympl
jupyter lab
```

Some notebooks install packages inside Colab cells with `!pip install`. When
running locally, install the packages once in your environment instead.

## How to Run

1. Open the repository in Google Colab or JupyterLab.
2. Start with `“0_setup.ipynb”` if you want to reproduce the original course
   workflow.
3. Run the assignment notebooks in order from `1_python_basics_I.ipynb` to
   `8_visualization.ipynb`.
4. Use `Runtime > Restart and run all` in Colab, or `Kernel > Restart Kernel and
   Run All Cells` in Jupyter, to check that a notebook runs from a clean state.

For local terminal access to the course folder:

```bash
cd " Applied Data Science in Medicine & Psychology"
```

## Data and External Resources

Several notebooks load example data from package datasets or public URLs, such
as:

- `scipy.datasets.electrocardiogram`
- BioPsyKit example data
- public questionnaire CSV files from the BioPsyKit GitHub repository

An internet connection may be required when running those notebooks for the
first time.

## Notes

- The notebooks contain completed assignment code cells and automated assertion
  checks.
- Some cells are Colab-specific, especially package installation commands,
  widget setup, and `google.colab` imports.
- Before sharing a derived copy publicly, review assignment identity cells and
  notebook metadata.
