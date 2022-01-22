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

## Demo

``` sh
from RSAbs import *
import os #Use whatever you would like to call your file

### Section for calling the file -- adjust if you need too ###
_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname("demo")))
file = os.path.join(_location_, 'demo_spectra.csv')

### open the csv or whatever datatype file with pandas
### in the case of using this package you can call pandas as pd without needing to import
main_df = pd.read_csv(file, delimiter = ',', low_memory = False)

### Index the dataframe to isolate the spectra columns - this can be used as input for the functions
### The file will need to be transposed using .T if the data are stored as rows rather than columns
spectra_df = main_df.iloc[:, 1:]

### Index the dataframe to isolate the wavelength column - this can be used as input for the functions
wavelength_df = main_df.iloc[:, 0:1]

### Print the data to see structure
print(spectra_df)
print(wavelength_df)


      Spectra 1  Spectra 2  Spectra 3  Spectra 4  Spectra 5
0      1.000000   1.000000   1.000000   1.000000   1.000000
1      0.975773   0.989696   0.952188   0.975604   0.973794
2      0.916169   0.979391   0.914538   0.941819   0.956133
3      0.900667   0.971362   0.896350   0.938824   0.941401
4      0.885164   0.955769   0.865520   0.935830   0.897178
...         ...        ...        ...        ...        ...
2146   0.994068   0.996252   0.998757   0.994969   0.998406
2147   0.993586   0.996415   1.000000   0.995003   0.998210
2148   0.993529   0.993466   1.000000   0.995476   0.997957
2149   0.994253   0.994404   1.000000   0.997780   0.999067
2150   1.000000   1.000000   1.000000   1.000000   1.000000


[2151 rows x 5 columns]
      Wavelength
0            350
1            351
2            352
3            353
4            354
...          ...
2146        2496
2147        2497
2148        2498
2149        2499
2150        2500

[2151 rows x 1 columns]
```

```sh
absorptions_results = absorptions(spectra_df=spectra_df, wavelength_df=wavelength_df) #Create DataFrame of all absorptions wavelength locations

seek_absorptions_results = seek_absorptions(absorptions_results, start_wavelength=800, end_wavelength=1000)#Create DataFrame of specific absorption wavelength locations, in this case between 800 and 900 nm

absorptions_depth_results = absorptions_depth(spectra_df=spectra_df)  #Create DataFrame of all absorption depths

seek_absorptions_depth_results = seek_absorptions_depth(spectra_df=spectra_df, wavelength_df=wavelength_df, start_wavelength=800, end_wavelength=1000) #Create DataFrame of specific absorption depths, in this case between 800 and 900 nm
```

```sh
print(absorptions_results)

    Spectra 1  Spectra 2  Spectra 3  Spectra 4  Spectra 5
0         382      384.0      383.0      379.0      384.0
1         435      434.0      434.0      434.0      435.0
2         621      936.0      920.0      631.0      940.0
3         666     1415.0     1414.0      935.0     1415.0
4         944     1467.0     1467.0     1334.0     1467.0
5        1470     1804.0     1804.0     1430.0     1804.0
6        1765     1854.0     1853.0     1473.0     1854.0
7        1802     1930.0     1931.0     1765.0     1937.0
8        1854     2212.0     2211.0     1930.0     2212.0
9        1935     2267.0     2267.0     2177.0     2267.0
10       2182     2388.0     2384.0     2208.0     2387.0
11       2210     2458.0     2456.0     2264.0     2460.0
12       2267        NaN        NaN     2324.0        NaN
13       2400        NaN        NaN     2438.0        NaN
14       2455        NaN        NaN        NaN        NaN
```

```sh
print(seek_absorptions_results)

   Spectra 1  Spectra 2  Spectra 3  Spectra 4  Spectra 5
0      944.0      936.0      920.0      935.0      940.0
```

```sh
print(absorptions_depth_results)

    Spectra 1  Spectra 2  Spectra 3  Spectra 4  Spectra 5
0    0.417564   0.455767   0.463062   0.337351   0.467325
1    0.105968   0.117736   0.077022   0.092891   0.111149
2    0.001259   0.255847   0.197308   0.001224   0.236165
3    0.001494   0.012465   0.092399   0.108506   0.015694
4    0.172838   0.077587   0.022838   0.002182   0.074491
5    0.088340   0.012866   0.008846   0.004006   0.012171
6    0.021673   0.051189   0.023738   0.095700   0.041488
7    0.001234   0.127349   0.160692   0.035386   0.142986
8    0.016996   0.194724   0.191051   0.190073   0.183658
9    0.162110   0.063734   0.025584   0.127044   0.054225
10   0.003060   0.020480   0.022847   0.004300   0.016954
11   0.141357   0.031822   0.029698   0.007792   0.026690
12   0.034780        NaN        NaN   0.017421        NaN
13   0.004581        NaN        NaN   0.053166        NaN
14   0.039951        NaN        NaN        NaN        NaN
```
```sh
print(seek_absorptions_depth_results)

   Spectra 1  Spectra 2  Spectra 3  Spectra 4  Spectra 5
0   0.172838   0.255847   0.197308   0.108506   0.236165
```

The DataFrames can then be exported again as a csv, or your preffered file type, to be used for further analysis.

## License

MIT
**Free Software, Lets Go!**