from scipy.signal import find_peaks
import pandas as pd
import numpy as np
import itertools

def absorptions_depth(spectra_df, integrity='ASD_CR'): #returns dataframe with the depth of each feature, where the depth is from the top of the convex hull (1.00) minus the value of the absorption minima
    if isinstance(spectra_df, pd.DataFrame)==False: #Check whether spectra_df argument is satisfactory
            print('Error: spectra_df argument not identified as pd.DataFrame')
    def depth_props(spectra_df):        
        spectra_array = spectra_df.values.flatten()
        if integrity=='ASD_CR':
            absorps, props = find_peaks(-spectra_array, width = 6, distance = 25, prominence = 0.001) #For using continuum removed spectra
        elif integrity=='ASD_Normal':
            absorps, props = find_peaks(-spectra_array, width = 5, distance = 15, prominence = 0.001) #For using non-continuum removed spectra
        elif integrity=='HyMap_CR':
            absorps, props = find_peaks(-spectra_array, width = 3, distance = 5, prominence = 0.001) #For using continuum removed HYMAP spectra
        else:
            print('Enter integrity argument based on avaiable options:"ASD_CR" for ASD continuum removed spectra, "ASD_Normal" for ASD non-continuum removed spectra, or "HyMap_CR" for HyMap continuum removed spectra. Default is "ASD_CR".')

        depths = props["prominences"]
        return pd.Series(depths) #For normal spectra
    
    return pd.DataFrame(spectra_df.apply(depth_props, axis=0))