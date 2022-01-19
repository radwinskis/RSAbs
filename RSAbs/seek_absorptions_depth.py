from scipy.signal import find_peaks
import pandas as pd
import numpy as np
import itertools

def seek_absorptions_depth(spectra_df, wavelength_df, integrity='ASD_CR', start_wavelength=350, end_wavelength=2500, wavelength_unit='nanometer'):
    if isinstance(spectra_df, pd.DataFrame)==False: #Check whether spectra_df argument is satisfactory
            print('Error: spectra_df argument not identified as pd.DataFrame')
    if isinstance(wavelength_df, pd.DataFrame)==False: #Check whether spectra_df argument is satisfactory
            print('Error: spectra_df argument not identified as pd.DataFrame')
    def abs_features(spectra_df, wavelength_df):        
        spectra_array = spectra_df.values.flatten()
        wavelength_array = wavelength_df.values.flatten()
        if integrity=='ASD_CR':
            absorps, props = find_peaks(-spectra_array, width = 6, distance = 25, prominence = 0.001) #For using continuum removed spectra
        elif integrity=='ASD_Normal':
            absorps, props = find_peaks(-spectra_array, width = 5, distance = 15, prominence = 0.001) #For using non-continuum removed spectra
        elif integrity=='HyMap_CR':
            absorps, props = find_peaks(-spectra_array, width = 3, distance = 5, prominence = 0.001) #For using continuum removed HYMAP spectra
        else:
            print('Enter integrity argument based on avaiable options:"ASD_CR" for ASD continuum removed spectra, "ASD_Normal" for ASD non-continuum removed spectra, or "HyMap_CR" for HyMap continuum removed spectra. Default is "ASD_CR".')

        absorp_locs = wavelength_array[absorps]
        depths = props["prominences"]
        return pd.Series(absorp_locs) #For normal spectra
    
    abs_wvls = pd.DataFrame(spectra_df.apply(abs_features, wavelength_df=wavelength_df, axis=0))
    
    def abs_depths(spectra_df, wavelength_df):        
        spectra_array = spectra_df.values.flatten()
        wavelength_array = wavelength_df.values.flatten()
        if integrity=='ASD_CR':
            absorps, props = find_peaks(-spectra_array, width = 6, distance = 25, prominence = 0.001) #For using continuum removed spectra
        elif integrity=='ASD_Normal':
            absorps, props = find_peaks(-spectra_array, width = 5, distance = 15, prominence = 0.001) #For using non-continuum removed spectra
        elif integrity=='HyMap_CR':
            absorps, props = find_peaks(-spectra_array, width = 3, distance = 5, prominence = 0.001) #For using continuum removed HYMAP spectra
        else:
            print('Enter integrity argument based on avaiable options:"ASD_CR" for ASD continuum removed spectra, "ASD_Normal" for ASD non-continuum removed spectra, or "HyMap_CR" for HyMap continuum removed spectra. Default is "ASD_CR".')

        absorp_locs = wavelength_array[absorps]
        depths = props["prominences"]
        return pd.Series(depths) #For normal spectra
    
    abs_depths = pd.DataFrame(spectra_df.apply(abs_depths, wavelength_df=wavelength_df, axis=0))
    
    wvls_range = end_wavelength-start_wavelength
    if wavelength_unit=='nanometer':
        steps = int(wvls_range+1)
    elif wavelength_unit=='micrometer':
        steps = int(wvls_range*1000+1)
    else: 
        print('Error: Incorrect wavelength_unit argument. Choose from "nanometer" or "micrometer" and ensure they are the correct units. Default is set to nanometer.')
    wvls_array = np.linspace(start_wavelength, end_wavelength, num=steps)
    seek_samples = abs_wvls.columns[abs_wvls.isin(wvls_array).any()]
    samples = abs_wvls[seek_samples]
    wvls_of_samples_of_interest = samples[samples[seek_samples].isin(wvls_array)].apply(lambda x: pd.Series(x.dropna().values))
    depths_of_samples_of_interest = abs_depths[seek_samples]
    depths_final = depths_of_samples_of_interest[samples[seek_samples].isin(wvls_array)].apply(lambda x: pd.Series(x.dropna().values))
    return depths_final