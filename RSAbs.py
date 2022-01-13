from scipy.signal import find_peaks
import pandas as pd
import numpy as np

##################### BELOW WORKS FOR MAKING DATAFRAME OF ALL ABSORPTION FEATURES ################
def absorptions(spectra_df, wavelength_df, integrity='ASD_CR'):
    if isinstance(spectra_df, pd.DataFrame)==False: #Check whether spectra_df argument is satisfactory
            print('Error: spectra_df argument not identified as pd.DataFrame')
    if isinstance(wavelength_df, pd.DataFrame)==False: #Check whether spectra_df argument is satisfactory
            print('Error: spectra_df argument not identified as pd.DataFrame')
    def abs_features(spectra_df, wavelength_df):        
        spectra_array = spectra_df.values.flatten()
        wavelength_array = wavelength_df.values.flatten()
        if integrity=='ASD_CR':
            absorps, _ = find_peaks(-spectra_array, width = 6, distance = 25, prominence = 0.001) #For using continuum removed spectra
        elif integrity=='ASD_Normal':
            absorps, _ = find_peaks(-spectra_array, width = 5, distance = 15, prominence = 0.001) #For using non-continuum removed spectra
        elif integrity=='HyMap_CR':
            absorps, _ = find_peaks(-spectra_array, width = 3, distance = 5, prominence = 0.001) #For using continuum removed HYMAP spectra
        else:
            print('Enter integrity argument based on avaiable options:"ASD_CR" for ASD continuum removed spectra, "ASD_Normal" for ASD non-continuum removed spectra, or "HyMap_CR" for HyMap continuum removed spectra. Default is "ASD_CR".')

        absorp_locs = wavelength_array[absorps]
        return pd.Series(absorp_locs) #For normal spectra
    
    return pd.DataFrame(spectra.apply(abs_features, wavelength_df=wavelength_df, axis=0)) #apply is used because the abs_features function only works for one column at a time, so apply iterates the function through the columns and a new df is created. Returns a dataframe of all absorptions for each spectra/column in spectra_df

##################### BELOW WORKS FOR MAKING DATAFRAME OF ABSORPTION FEATURES AND THUS SAMPLES IN DESIRED WAVELENGTH RANGE ################
def seek_absorptions(absorptions_df, start_wavelength, end_wavelength, wavelength_unit='nanometer'):
    wvls_range = end_wavelength-start_wavelength
    if wavelength_unit=='nanometer':
        steps = int(wvls_range+1)
    elif wavelength_unit=='micrometer':
        steps = int(wvls_range*1000+1)
    else: 
        print('Error: Incorrect wavelength_unit argument. Choose from "nanometer" or "micrometer" and ensure they are the correct units. Default is set to nanometer.')
    wvls_array = np.linspace(start_wavelength, end_wavelength, num=steps)
    seek_samples = absorptions_df.columns[absorptions_df.isin(wvls_array).any()]
    samples = absorptions_df[seek_samples]
    return samples[samples[seek_samples].isin(wvls_array)].apply(lambda x: pd.Series(x.dropna().values)) #[0:1]