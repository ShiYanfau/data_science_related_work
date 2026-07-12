# Data Science Survival Skills

This directory contains Jupyter notebook exercises and supporting files for a
Data Science Survival Skills course. The material focuses on practical Python
tools for data exploration, visualization, machine learning, model evaluation,
APIs, parallel computing, performance optimization, and deployment.

Most exercises are provided as notebook pairs:

- `*_empty.ipynb` or similarly named notebooks for the exercise version
- `*_solution.ipynb` for completed solutions

The included exercises start at exercise 2. Exercises 1, 5, and 6 are not present
in this checkout.

## Contents

| Folder | Main files | Topic |
| --- | --- | --- |
| `exercise2/` | `Ex_2_solution.ipynb`, `Exercise_2.pdf` | BAGLS image/video data, JPEG compression, PSNR, glottis video loading |
| `exercise3/` | `Ex_3.ipynb`, `Ex_3_solution.ipynb`, `Exercise03_dash*.ipynb`, CSV data | data exploration, salary survey analysis, COVID data, PCA, t-SNE, Dash/Plotly dashboards |
| `exercise4/` | `DSSS_Ex_4.ipynb`, `DSSS_Ex_4_solution.ipynb` | visualization with Matplotlib and Seaborn, heatmaps, line plots, histograms, box/violin/strip/swarm plots, export for Inkscape |
| `exercise7/` | `Exercise_7_empty.ipynb`, `Exercise_7_solution.ipynb` | machine learning basics, regression, curve fitting, kNN, SVM, K-Means, Adaline, logistic regression |
| `exercise8/` | `Ex8_empty.ipynb`, `Exercise_8_solution.ipynb`, `dsss_ex8_unet*.ipynb`, data/model files | confusion matrices, ROC curves, cross validation, TensorFlow datasets, U-Net semantic segmentation |
| `exercise9/` | `Exercise_9_empty.ipynb`, `Exercise_9_solution.ipynb` | REST APIs, Flickr API requests, image download URLs, Telegram bot examples |
| `exercise10/` | `exercise_10_empty.ipynb`, `exercise_10_solution (1).ipynb`, `multiprocessing_example.py` | profiling, multithreading, multiprocessing, `concurrent.futures`, Ray |
| `exercise11/` | `exercise_11_empty.ipynb`, `exercise_11_solution.ipynb`, `sum.c`, `sum.h` | Cython, typed memoryviews, C-style loops, C extensions, Numba |
| `exercise12/` | `exercise_12_empty.ipynb`, `exercise_12_solution.ipynb`, `labelfile.txt` | model deployment, TensorFlow Lite conversion, quantization, metadata for edge devices |

## Data and Supporting Files

- `exercise3/IT Salary Survey EU  2020.csv` contains 1,253 rows and 23 columns
  for salary survey exploration.
- `exercise3/covid_19.csv` contains 690 rows and 10 columns with COVID case and
  reproduction-number time series.
- `exercise8/BAGLS_4096.zip` is a large image dataset archive used for the
  segmentation material.
- `exercise8/uneth5.sec` is a pretrained or saved U-Net model file used by the
  segmentation notebooks.
- `exercise8/history.csv` stores 100 epochs of training history with loss,
  accuracy, and IoU score.
- `exercise11/sum.c` and `exercise11/sum.h` provide a small C function used in
  the Cython/C-interfacing exercise.
- `exercise12/labelfile.txt` lists the CIFAR-like class labels used for TFLite
  metadata: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and
  truck.

## Environment

The notebooks can be run in JupyterLab or Google Colab. A broad local
environment for most exercises can be created with:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas matplotlib seaborn scipy scikit-learn scikit-image opencv-python pillow imageio ipywidgets plotly dash jupyter-dash tensorflow tensorflow-datasets cython numba ray flammkuchen
```

Some exercises need additional or version-sensitive packages:

- `exercise3` and `exercise4`: `pandas-profiling` and `nutil`
- `exercise8`: `segmentation-models` and `albumentations`
- `exercise10`: optional `line_profiler`
- `exercise12`: `tflite-support`

Several notebooks include commented or inline `pip install` cells. In a local
environment, install dependencies once before running the notebooks.

## How to Run

1. Open the desired exercise folder.
2. Start with the `empty` notebook if you want to work through the exercise.
3. Open the `solution` notebook to inspect a completed implementation.
4. In Jupyter, use `Kernel > Restart Kernel and Run All Cells` to verify that a
   notebook runs from a clean state.
5. In Colab, use `Runtime > Restart and run all`.

For terminal access:

```bash
cd "Data Science Survival Skills"
jupyter lab
```

## Notes

- The notebooks are course materials, so some cells are intentionally written as
  exercises with missing code in the empty versions.
- API-related notebooks may require personal API keys or tokens, especially for
  Flickr and Telegram examples.
- Deep-learning notebooks may take longer to run locally and may benefit from a
  GPU runtime.
- Large files in `exercise8/` can make cloning or syncing slower.
