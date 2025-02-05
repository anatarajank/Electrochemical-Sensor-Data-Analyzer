## **Electrochemical Sensor Data Analyzer**

### **Summary**

This repository notebook demonstrates a typical workflow for analyzing the Differential Pulse Voltammetry (DPV) experimental data from an **Autolab PGSTAT 302N** to determine the relationship between the concentration of analytes Hydroquinone (HQ) and Catechol (CC) and their corresponding peak currents. It involves data loading, preprocessing, visualization, peak detection, and ultimately the construction of a calibration curve using linear regression to quantify the relationship between analyte concentration and peak current. This information is crucial for determining unknown concentrations of HQ and CC in samples using DPV.

Moreover, this notebook is designed for electrochemists with less technical experience in Python, making it easy to use and implement.

---

### **Atribution**

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/anatarajank/Electrochemical-Data-Analyzer">Electrochemical Sensor Data Analyzer</a> &#169; 2019-2025 by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.linkedin.com/in/anatarajank/">Aravindan Natarajan</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

---

### **Citation**
If you use this repository in your work, please cite using the following:

Natarajan, Aravindan, and Preethi Sankaranarayanan. 2025. “A User-friendly Jupyter Notebook for Simplified Differential Pulse Voltammetry Analysis of Dihydroxy Phenols.” ECSarXiv. February 5. [doi:10.1149/osf.io/mgujh_v1] (https://doi.org/10.1149/osf.io/mgujh_v1) ![Static Badge](https://img.shields.io/badge/doi-https%3A%2F%2Fdoi.org%2F10.1149%2Fosf.io%2Fmgujh__v1-blue)

And please cite this repository using the following:
[Electrochemical Data Analyzer, Aravindan Natarajan, https://github.com/anatarajank/Electrochemical-Sensor-Data-Analyzer](https://github.com/anatarajank/Electrochemical-Sensor-Data-Analyzer)

---

### **Authors**
- **Aravindan Natarajan** - Corresponding Author
- **Preethi Sankaranarayanan** - Manuscript Contributor

---

### **Steps Overview**

1.  **Data Loading and Preprocessing:**
    -   Imports necessary libraries like pandas, numpy, matplotlib, and seaborn.
    -   Loads data from text files into pandas DataFrames.
    -   Extracts relevant columns (potential and current) and renames them for clarity.
2.  **Data Visualization:**
    -   Plots the DPV data for all concentrations using seaborn's `lineplot`.
    -   Creates a legend with clear labels for each concentration.
3.  **Peak Detection and Analysis:**
    -   Defines a function `find_peaks_and_values` to locate peaks in the current data and extract corresponding potentials and currents.
    -   Applies this function to each concentration's data and stores the peak information in a new DataFrame called `peak_df`.
    -   Adds a 'Concentration' column to `peak_df`.
    -   Plots the DPV data again with peak locations highlighted using `scatter`.
4.  **Calibration Curve and Linear Regression:**
    -   Uses `stats.linregress` to perform linear regression on the concentration and peak current data for both HQ and CC.
    -   Plots the calibration curves using `sns.regplot` with the regression equation and R-squared value displayed in the legend.

---

### **Getting Started**
This notebook can be run either locally or in Google Colab.

**Running Locally**

To run this notebook locally, you will need to have the following software installed:

- Python 3.x
- Jupyter Notebook
- The required Python packages: numpy, pandas, scipy, os, seaborn, matplotlib, stats and jupyterlab.

Once you have the required software installed, you can download the notebook file and open it in Jupyter Notebook. Then, you can run the cells in the notebook to execute the code.

Before installing the required Python packages you need to create a virtual environment by navigating to the folder where the Jupyter notebook is kept by running the following command in terminal:

```python
python -m venv myvenv
```

Replace ```myvenv``` with your preferred name

To install the required Python packages, you can use the following command in your terminal:

```python
pip install numpy pandas scipy seaborn matplotlib stats jupyterlab
```

Alternatively you can install by running the following command after downloading this repository

```python
pip install -r requirements.txt
```

Please make sure that you are running this command from the directory where the requirements.txt file is placed. Use code with caution.

**Running in Google Colab**

To run this notebook in [Google Colab](https://colab.research.google.com/), you will need to have a Google account. Once you have a Google account, you can open the notebook in Google Colab by clicking on the "Open in Colab" badge in the notebook file.

Once the notebook is open in Google Colab, you can run the cells in the notebook to execute the code. Google Colab will automatically install the required Python packages for you.

**Data**

The data for this notebook is the experimental data collected by the author and they are stored in the data folder. You will need to create this folder for your own experimental data and place it in the same directory as the notebook file for the code to run without any errors.

---

### **Versioning**
The notebooks and the repositories are versioned using [SemVer](http://semver.org/) for versioning. The current version is 2.0.

### **Sample Output**

**Differential Pulse Voltammograms with legends**

<img src="https://github.com/anatarajank/Electrochemical-Sensor-Data-Analyzer/blob/main/images/DPV_w_legends.png" alt="Differential Pulse Voltammograms with legends" width="75%" height="auto"> 

**Differential Pulse Voltammograms with peaks identified**

<img src="https://github.com/anatarajank/Electrochemical-Sensor-Data-Analyzer/blob/main/images/DPV_w_legends_w_peaks.png" alt="Differential Pulse Voltammograms with peaks identified" width="75%" height="auto"> 

**Linear calibration curve**

<img src="https://github.com/anatarajank/Electrochemical-Sensor-Data-Analyzer/blob/main/images/Linear_calibration_plot_HQ.png" alt="Linear calibration curve" width="75%" height="auto">
