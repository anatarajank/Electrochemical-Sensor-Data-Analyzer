import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks
import re
from scipy import stats
import numpy as np

# Helper functions
def LegendNameSetter(filename):
    """
    Helper function to format legend names based on filename.
    """
    mu = '\u03BC'

    if "_mu_" in filename:
        for i, c in enumerate(filename):
            if c.isdigit():
                continue
            if re.search(r'\.',c):
              continue
            else:
                index_of_digit = i
                break

        alpha_in_filename = filename[index_of_digit:]
        converted_filename = filename[:index_of_digit] + mu + alpha_in_filename.strip("_mu_")

        return converted_filename

    elif "_n_" in filename:
        for i, c in enumerate(filename):
            if c.isdigit():
                continue
            if re.search(r'\.',c):
                continue
            else:
                index_of_digit = i
                break

        alpha_in_filename = filename[index_of_digit:]
        converted_filename = filename[:index_of_digit] + 'n' + alpha_in_filename.strip("_n_")

        return converted_filename
    else:
        return filename

def find_peaks_and_values(data, key):
    """Finds peaks in the data and extracts corresponding potentials and currents."""
    peaks, _ = find_peaks(data[key]['Current(A)'])
    potentials = data[key]['Potential(V)'].values.tolist()
    currents = data[key]['Current(A)'].values.tolist()
    peak_potentials = [potentials[i] for i in peaks]
    peak_currents = [currents[i] for i in peaks]
    return peak_potentials, peak_currents

# Streamlit App Title
st.title("Electrochemical Sensor Data Analyzer")
st.markdown("* Please note that this app can currently only process .txt and .csv files for the differential pulse data from a **AUTOLAB 302N** system only. The files should contain the columns 'Potential applied (V)' and 'WE(1).δ.Current (A)'.")
st.markdown("* The app will analyze, plot the differential pulse voltammograms, and perform peak analysis.")
st.markdown("* Data files must be named according to the following format, corresponding to concentration units: xx_nM (nanomolar), xx_uM (micromolar), xx_mM (millimolar), and xx_M (molar).")

# File Uploader
uploaded_files = st.file_uploader("Upload your .txt or .csv files", accept_multiple_files=True, type=['txt', 'csv'])

if uploaded_files:
    mod_csvs = {}
    concentration_list = []

    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        try:
            if file_name.endswith('.txt'):
                # Assuming your .txt files are comma-separated, adjust if needed
                df = pd.read_csv(uploaded_file, sep=',')
            elif file_name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)

            # Check if required columns exist
            required_columns = ['Potential applied (V)', 'WE(1).δ.Current (A)']
            if not all(col in df.columns for col in required_columns):
                st.warning(f"Skipping file '{file_name}': Missing required columns ('Potential applied (V)' or 'WE(1).δ.Current (A)').")
                continue

            file_key = file_name.split('.')[0] # Use filename without extension as key
            mod_csvs[file_key] = pd.DataFrame(data = df, columns= required_columns)
            mod_csvs[file_key].rename(columns={'Potential applied (V)': 'Potential(V)', 'WE(1).δ.Current (A)': 'Current(A)'}, inplace=True)
            concentration_list.append(LegendNameSetter(file_key))

        except Exception as e:
            st.error(f"Error loading or processing file '{file_name}': {e}")

    if mod_csvs:
        # Plot the data
        st.subheader("Differential Pulse Voltammograms")
        fig, ax = plt.subplots(figsize=(15, 10))
        lines = []
        for i, keys in enumerate(mod_csvs.keys()):
            line, = ax.plot(mod_csvs[keys]['Potential(V)'], mod_csvs[keys]['Current(A)'], label=concentration_list[i])
            lines.append(line)
        ax.set_title("Differential Pulse Voltammograms")
        ax.set_xlabel("Potential(V)")
        ax.set_ylabel("Current(A)")
        ax.legend(handles=lines)
        st.pyplot(fig)
        plt.close(fig) # Close the figure to free up memory

        # Find and display peaks
        st.subheader("Peak Analysis")
        peak_data = {'File': [], 'HQ_Peak_Potential(V)': [], 'CC_Peak_Potential(V)': [],
                     'HQ_Peak_Current(A)': [], 'CC_Peak_Current(A)': []}

        for key in mod_csvs.keys():
            peak_potentials, peak_currents = find_peaks_and_values(mod_csvs, key)
            peak_data['File'].append(key)
            peak_data['HQ_Peak_Potential(V)'].append(peak_potentials[0] if len(peak_potentials) >= 1 else np.nan)
            peak_data['CC_Peak_Potential(V)'].append(peak_potentials[1] if len(peak_potentials) >= 2 else np.nan)
            peak_data['HQ_Peak_Current(A)'].append(peak_currents[0] if len(peak_currents) >= 1 else np.nan)
            peak_data['CC_Peak_Current(A)'].append(peak_currents[1] if len(peak_currents) >= 2 else np.nan)

        peak_df = pd.DataFrame(peak_data)

        # Add Concentration column
        concentration_values = []
        for file_key in peak_df['File']:
            formatted_name = LegendNameSetter(file_key)
            try:
                concentration_values.append(float(formatted_name.replace('μM','')))
            except ValueError:
                concentration_values.append(np.nan) # Handle cases where conversion fails

        peak_df['Concentration(μM)'] = concentration_values
        peak_df.sort_values(by='Concentration(μM)', ascending=True, inplace=True)
        peak_df.set_index('File', inplace=True) # Set File as index for better display

        # Format the current columns to scientific notation
        formatted_peak_df = peak_df.copy()
        formatted_peak_df['HQ_Peak_Current(A)'] = formatted_peak_df['HQ_Peak_Current(A)'].apply(lambda x: f'{x:.2e}' if pd.notna(x) else '')
        formatted_peak_df['CC_Peak_Current(A)'] = formatted_peak_df['CC_Peak_Current(A)'].apply(lambda x: f'{x:.2e}' if pd.notna(x) else '')

        st.dataframe(formatted_peak_df)

        # Plot peaks on the main plot
        st.subheader("Differential Pulse Voltammograms with Peaks")
        fig_peaks, ax_peaks = plt.subplots(figsize=(15, 10))
        lines_peaks = []
        for i, keys in enumerate(mod_csvs.keys()):
            line_peaks, = ax_peaks.plot(mod_csvs[keys]['Potential(V)'], mod_csvs[keys]['Current(A)'], label=concentration_list[i])
            lines_peaks.append(line_peaks)
        ax_peaks.set_title("Differential Pulse Voltammograms with Peaks")
        ax_peaks.set_xlabel("Potential(V)")
        ax_peaks.set_ylabel("Current(A)")

        # Plot the scatter points from the peak_df
        ax_peaks.scatter(peak_df['HQ_Peak_Potential(V)'], peak_df['HQ_Peak_Current(A)'], color='red', marker='x', label='HQ Peaks')
        ax_peaks.scatter(peak_df['CC_Peak_Potential(V)'], peak_df['CC_Peak_Current(A)'], color='blue', marker='o', label='CC Peaks')
        ax_peaks.legend()
        st.pyplot(fig_peaks)
        plt.close(fig_peaks) # Close the figure

        # Linear Regression
        st.subheader("Linear Regression Analysis")

        # Filter out rows with NaN in the current column for regression
        peak_df_hq_reg = peak_df.dropna(subset=['HQ_Peak_Current(A)'])
        peak_df_cc_reg = peak_df.dropna(subset=['CC_Peak_Current(A)'])


        if not peak_df_hq_reg.empty:
            st.write("Linear Regression for HQ Peaks:")
            slope_hq, intercept_hq, r_value_hq, p_value_hq, std_err_hq = stats.linregress(peak_df_hq_reg['Concentration(μM)'], peak_df_hq_reg['HQ_Peak_Current(A)'])
            fig_hq_reg = sns.regplot(x="Concentration(μM)", y="HQ_Peak_Current(A)", data=peak_df_hq_reg, color='b',  line_kws={'label':"Current(A)={0:.2g}[HQ]+{1:.2g}, R^2={2:.3f}".format(slope_hq,intercept_hq, r_value_hq)})
            fig_hq_reg.legend(loc='upper left')
            plt.title("Concentration vs. Current Plot for HQ")
            plt.xlabel("Concentration(μM)")
            plt.ylabel("Current(A)")
            st.pyplot(fig_hq_reg.figure)
            plt.close(fig_hq_reg.figure)

        if not peak_df_cc_reg.empty:
            st.write("Linear Regression for CC Peaks:")
            slope_cc, intercept_cc, r_value_cc, p_value_cc, std_err_cc = stats.linregress(peak_df_cc_reg['Concentration(μM)'], peak_df_cc_reg['CC_Peak_Current(A)'])
            fig_cc_reg = sns.regplot(x="Concentration(μM)", y="CC_Peak_Current(A)", data=peak_df_cc_reg, color='r',  line_kws={'label':"Current(A)={0:.2g}[CC]+{1:.2g}, R^2={2:.3f}".format(slope_cc,intercept_cc, r_value_cc)})
            fig_cc_reg.legend(loc='upper left')
            plt.title("Concentration vs. Current Plot for CC")
            plt.xlabel("Concentration(μM)")
            plt.ylabel("Current(A)")
            st.pyplot(fig_cc_reg.figure)
            plt.close(fig_cc_reg.figure)