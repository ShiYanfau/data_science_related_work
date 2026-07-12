# Data Science Coursework

This repository contains notebook-based coursework from two applied data science
courses:

- ` Applied Data Science in Medicine & Psychology/`
- `Data Science Survival Skills/`

The material is centered on Python, Jupyter/Google Colab notebooks, data
analysis, visualization, machine learning, biomedical examples, optimization,
and deployment.

Note: the ` Applied Data Science in Medicine & Psychology/` directory name starts
with a leading space in this checkout, so quote the path when using terminal
commands.

## Repository Structure

```text
.
├── README.md
├──  Applied Data Science in Medicine & Psychology/
│   ├── 0 setup notebook
│   ├── 1_python_basics_I.ipynb
│   ├── 2_python_basics_II.ipynb
│   ├── 3_control_flow.ipynb
│   ├── 4_dicts_classes.ipynb
│   ├── 5_numpy_scipy.ipynb
│   ├── 6_pandas.ipynb
│   ├── 7_statistics.ipynb
│   └── 8_visualization.ipynb
└── Data Science Survival Skills/
    ├── README.md
    ├── exercise2/
    ├── exercise3/
    ├── exercise4/
    ├── exercise7/
    ├── exercise8/
    ├── exercise9/
    ├── exercise10/
    ├── exercise11/
    └── exercise12/
```

## Applied Data Science in Medicine & Psychology

This course introduces Python programming and scientific data analysis with
examples from medicine and psychology. The notebooks are assignment-style
exercises and include completed code cells plus automated assertion checks.

| Assignment | Notebook | What it does |
| --- | --- | --- |
| 0 | setup notebook | Sets up Google Colab and GitHub, confirms access to the course workflow, and explains assignment submission. |
| 1 | `1_python_basics_I.ipynb` | Introduces Python as a calculator, `print`, variables, arithmetic/comparison/logical operators, comments, and simple sine plotting. |
| 2 | `2_python_basics_II.ipynb` | Covers functions, data types, lists, slicing, list editing, `if`/`elif`/`else`, loops, type casting, and medical threshold checks. |
| 3 | `3_control_flow.ipynb` | Practices advanced control flow with `range`, `pass`, `continue`, `break`, list comprehensions, study-name validation, and error handling. |
| 4 | `4_dicts_classes.ipynb` | Builds dictionaries and object-oriented classes for a small medical records system with patients, sessions, medication, physicians, and referrals. |
| 5 | `5_numpy_scipy.ipynb` | Uses NumPy, SciPy, Pandas, and Matplotlib for Perceived Stress Scale scoring and ECG filtering, R-peak detection, and heart-rate calculation. |
| 6 | `6_pandas.ipynb` | Uses Pandas DataFrames for patient/glucose-test examples, filtering, grouping, multi-index data, and cold-face-test heart-rate analysis. |
| 7 | `7_statistics.ipynb` | Generates distributions, calculates mean/median/mode, corrects outliers, and runs statistical checks/tests on questionnaire and cortisol data. |
| 8 | `8_visualization.ipynb` | Creates ECG and heart-rate visualizations with Matplotlib, including R-peak plots, corrected heart-rate distributions, and box plots. |

## Data Science Survival Skills

This course focuses on practical tools and workflows used in data science:
exploration, visualization, machine learning, evaluation, APIs, parallel
computing, optimization, and deployment. Most folders include an empty exercise
notebook and a solution notebook.

Exercises 1, 5, and 6 are not present in this checkout.

| Exercise | Main files | What it does |
| --- | --- | --- |
| 2 | `exercise2/Ex_2_solution.ipynb`, `Exercise_2.pdf` | Works with BAGLS image/video data, explores JPEG compression, calculates PSNR, and loads glottis video data. |
| 3 | `exercise3/Ex_3*.ipynb`, `Exercise03_dash*.ipynb`, CSV files | Explores salary-survey and COVID data, handles outliers and correlations, uses PCA and t-SNE, and builds Dash/Plotly dashboard examples. |
| 4 | `exercise4/DSSS_Ex_4*.ipynb` | Builds visualizations with Matplotlib and Seaborn, including heatmaps, line plots, histograms, box plots, violin plots, strip plots, swarm plots, and exportable figures. |
| 7 | `exercise7/Exercise_7*.ipynb` | Introduces machine learning with regression, curve fitting, kNN, SVM, K-Means, Adaline, gradient descent, and logistic regression. |
| 8 | `exercise8/Ex8_empty.ipynb`, `Exercise_8_solution.ipynb`, `dsss_ex8_unet*.ipynb` | Covers confusion matrices, precision/recall/specificity/F1, ROC curves, k-fold cross validation, TensorFlow datasets, and U-Net semantic segmentation. |
| 9 | `exercise9/Exercise_9*.ipynb` | Demonstrates REST API usage with Flickr image search/download workflows and Telegram bot examples. |
| 10 | `exercise10/exercise_10*.ipynb`, `multiprocessing_example.py` | Covers code profiling, multithreading, multiprocessing, I/O-bound tasks, `concurrent.futures`, and Ray. |
| 11 | `exercise11/exercise_11*.ipynb`, `sum.c`, `sum.h` | Compares Cython and Numba, including static typing, typed memoryviews, C-style loops, compile optimization, multithreading, and calling C code. |
| 12 | `exercise12/exercise_12*.ipynb`, `labelfile.txt` | Converts models to TensorFlow Lite, applies quantization, and adds metadata for deployment to edge devices such as smartphones or microcontrollers. |

## Data Files and Assets

- `Data Science Survival Skills/exercise3/IT Salary Survey EU  2020.csv`:
  salary-survey data used for exploration and visualization.
- `Data Science Survival Skills/exercise3/covid_19.csv`: COVID time-series data.
- `Data Science Survival Skills/exercise8/BAGLS_4096.zip`: image dataset archive
  for segmentation work.
- `Data Science Survival Skills/exercise8/uneth5.sec`: saved U-Net model file.
- `Data Science Survival Skills/exercise8/history.csv`: training history with
  loss, accuracy, and IoU score.
- `Data Science Survival Skills/exercise11/sum.c` and `sum.h`: small C helper
  used in the Cython exercise.
- `Data Science Survival Skills/exercise12/labelfile.txt`: class labels for
  TensorFlow Lite metadata.

## Running the Notebooks

The notebooks can be opened in Google Colab or JupyterLab.

Recommended local setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas matplotlib seaborn scipy scikit-learn scikit-image opencv-python pillow imageio ipywidgets plotly dash jupyter-dash tensorflow tensorflow-datasets cython numba ray flammkuchen biopsykit pingouin neurokit2 ipympl
jupyter lab
```

Some exercises require extra or version-sensitive packages, including
`pandas-profiling`, `nutil`, `segmentation-models`, `albumentations`,
`line_profiler`, and `tflite-support`.

When running notebooks from a clean state, use:

- Colab: `Runtime > Restart and run all`
- Jupyter: `Kernel > Restart Kernel and Run All Cells`

## Notes

- Some notebooks contain Colab-specific commands such as `!pip install`,
  `google.colab` imports, or widget setup.
- API exercises may require personal API keys or tokens.
- Deep-learning and segmentation notebooks may take longer to run locally and
  may benefit from a GPU runtime.
- Large files in `Data Science Survival Skills/exercise8/` can make cloning or
  syncing slower.
