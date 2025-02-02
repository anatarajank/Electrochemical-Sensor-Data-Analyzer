### **Electrochemical Sensor Data Analyzer**

---

**Version: 2.0**

**License: CC BY 4.0**

**Author: Aravindan Natarajan**

---


**Atribution**

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/anatarajank/Electrochemical-Data-Analyzer">Electrochemical Sensor Data Analyzer</a> &#169; 2019-2025 by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.linkedin.com/in/anatarajank/">Aravindan Natarajan</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

**Overview**

This repository features a notebook that analyzes the Differential Pulse Voltammetry (DPV) experimental data from a Autolab PGSTAT 302N to determine the relationship between the concentration of analytes Hydroquinone (HQ) and Catechol (CC) and their corresponding peak currents.

**Steps:**

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

**Summary**

The notebook demonstrates a typical workflow for analyzing electrochemical data. It involves data loading, preprocessing, visualization, peak detection, and ultimately the construction of a calibration curve using linear regression to quantify the relationship between analyte concentration and peak current. This information is crucial for determining unknown concentrations of HQ and CC in samples using DPV.