# RSAbs
## Python package to detect Reflectance Spectroscopy Absorptions (RSAbs)


RSAbs is a python package dedicated to easily detecting absorption features for any number of spectra, designed to be used with higher reslution spectral data such as what would be acquired from an ASD spectroradiometer. The main functionality of the package builds off of the scipy.signal.find_peaks package.



## Features

- Import a pd.DataFrame of spectral measurements and output another pd.DataFrame of all detectable absorptions
- Works with continuum-removed and non-continuum-removed data 
- Works with ASD and HyMap data
- Works for wavelengths of nanometers and micrometers
- User can choose range of wavelengths to detect absorptions and returns only the samples/columns that contain absorptions in the desired range (useful for investigating a specific absorption)



## Installation

One can install RSAbs using pip or by copying the GitHub repo to their working directory.

**PIP**: 
```sh
pip install RSAbs
```
## Function Parameters
There are four functions which make up the RSAbs package. 
1) ```sh
    absorptions(spectra_df, wavelength_df, integrity='ASD_CR') 
    ``` 
Functionality: creates DataFrame of all absorption wavelength positions

spectra_df: dataframe with spectra as columns (leave out wavelength column, if applicable)

wavelength_df: dataframe with wavelength as column

integrity: spectra type, indicates resolution and continuum removal status. Options: 'ASD_CR' for continuum removed ASD data, 'ASD_normal' for non-continuum-removed ASD data, or 'HyMap_CR' for continuum-removed HyMap data. Default is 'ASD_CR'

If you desire compatibility with another sensor/data type, please let me know.

2) ```sh
    seek_absorptions(absorptions_df, start_wavelength, end_wavelength, wavelength_unit='nanometer') 
    ```

Functionality: creates narrowed down DataFrame of absorption wavelength positions in a given wavelength range, and only returns data for samples that contain an absorption in the given range.

absorptions_df: dataframe from absorptions() function

start_wavelength: starting wavelength value for range of interest (smaller wavelength)

end_wavelength: ending wavelength value for range of interest (larger wavelength)

wavelength_unit: specify unit of wavelength. Options: 'nanometer' OR 'micrometer'. PLEASE ensure these are chosen correctly. Default is 'nanometer'.

3) ```sh
    absorptions_depth(spectra_df, integrity='ASD_CR') 
    ```

Functionality: creates DataFrame of all absorption depths

spectra_df: dataframe with spectra as columns (leave out wavelength column, if applicable)

integrity: spectra type, indicates resolution and continuum removal status. Options: 'ASD_CR' for continuum removed ASD data, 'ASD_normal' for non-continuum-removed ASD data, or 'HyMap_CR' for continuum-removed HyMap data. Default is 'ASD_CR'

4) ```sh
    seek_absorptions_depth(spectra_df, wavelength_df, integrity='ASD_CR', start_wavelength=350, end_wavelength=2500, wavelength_unit='nanometer') 
    ```

Functionality: creates narrowed down DataFrame of absorption depths in a given wavelength range,
and only returns data for samples that contain an absorption in the given wavelength range. 

spectra_df: dataframe with spectra as columns (leave out wavelength column, if applicable)

wavelength_df: dataframe with wavelength as column

integrity: spectra type, indicates resolution and continuum removal status. Options: 'ASD_CR' for continuum removed ASD data, 'ASD_normal' for non-continuum-removed ASD data, or 'HyMap_CR' for continuum-removed HyMap data. Default is 'ASD_CR'

start_wavelength: starting wavelength value for range of interest (smaller wavelength)

end_wavelength: ending wavelength value for range of interest (larger wavelength)

wavelength_unit: specify unit of wavelength. Options: 'nanometer' OR 'micrometer'. PLEASE ensure these are chosen correctly. Default is 'nanometer'.


## Usage 

To use the functions, either import the RSAbs package and use 

```sh
RSAbs.absorptions(spectra_df, wavelength_df)
```
or import the package as

```sh
from RSAbs import absorptions, seek_absorptions
```

which will allow for a general call of each function as

```sh
absorptions(spectra_df, wavelength_df)
```
Additionally, ensure the input datasets for the spectra_df and wavelength_df parameters are pandas DataFrames, where the data are separated by columns.

## License

MIT
**Free Software, Lets Go!**