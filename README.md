# Welcome to PyModisAtm

This a python routine for download MODIS Atmospheric Data from LADSFTP ftp://ladsftp.nascom.nasa.gov

In order to download data you must be logged in [LADSWEB](https://ladsweb.modaps.eosdis.nasa.gov/profile/login/)

The following variables can be modified to download your own and specific data, check on [Reverb](https://reverb.echo.nasa.gov/reverb/) for the specific time zone. 

This script only search over LADSFTP, use [pyModis](http://www.pymodis.org) for terrestrial MODIS data, converts a HDF, reproject, and other resources. 

Copyright Tomás Acuña - 2017 

#### Adjust the following variables to search over the FTP. This script will create a MODIS folder (C:/MODIS) with the selected products, downloading each HDF file for and specific hour and day for the givin years. 
_________________________________________

**Product and version**
```
product=['MOD07_L2','MOD04_L2','MOD05_L2']
version=['6'] 
```
**Day of year**
```
doy = ['001']
```
**Year/s of data**
```
year = [2010,2011]
```
**Time Zone**
Example: Adquire at 2215 UTC 

_MOD07_L2.A2011001.**2215**.006.2015047180723.hdf_
```
time='2215'
time='.'+time+'.'
```
__________________________________________

Best regards!
