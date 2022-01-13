from scipy.signal import find_peaks
import pandas as pd
import numpy as np
import itertools

def seek_absorptions(absorptions_df, start_wavelength=350, end_wavelength=2500, wavelength_unit='nanometer'):
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
    return samples[samples[seek_samples].isin(wvls_array)].apply(lambda x: pd.Series(x.dropna().values))