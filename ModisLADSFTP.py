# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:02:35 2017
@author: Tomás Acuña y Italo Moletto
mail: tomasacuna@ug.uchile.cl
Modified from : http://www.science-emergence.com/Codes/Download-a-file-of-MODIS-MYD08-M3-from-ladsftp-using-python/
"""

from ftplib import FTP
import numpy as np
import os
import calendar
import glob

def ModisLADS(doy,year,version,time,product,MODIS_FOLD):

    time='.'+time+'.'
    
    # Create a local folder call MODIS
    if not os.path.exists(MODIS_FOLD):
        os.makedirs(MODIS_FOLD)
        os.chdir(MODIS_FOLD)
    
    ####### Atention ############
    # You must be login https://ladsweb.modaps.eosdis.nasa.gov/profile/login/ in order to connected to the FTP
    ####### Atention ############
            
    for mm in range(0,len(product)):
        prod_path=MODIS_FOLD + '\\' +product[mm]
        
        # Create sub folder for each product 
        if not os.path.exists(prod_path):
            os.makedirs(prod_path)    
        if not os.path.exists(prod_path+"\hdf"):
            os.makedirs(prod_path+"\hdf")
            os.chdir(prod_path+"\hdf")
        else:
            os.chdir(prod_path+"\hdf")      
        #----------------------------------------------------------------------------------------#
        #  download data from ladsftp   
        for yy in range(0,len(year)):
            directory= 'allData/' + version[0] +'/' + product[mm] + '/' + str(year[yy]) + '/' + doy[0]
            ftp = FTP('ladsftp.nascom.nasa.gov')
            ftp.login('anonymous','')
            ftp.cwd(directory)
            yyy = []
            ftp.retrlines('NLST', yyy.append)
        
        # Search for specific time zone in the list of scenes 
            inx = [i for i, s in enumerate(yyy) if time in s]
            ooo=["NA"]
            ooo[0]=yyy[inx[0]]
            if len(ooo) == 1:
               file_name = ooo[0]
               print('Download file: ', file_name)
               e = 1
               while e == 1 :
                     try:
                         ftp.retrbinary('RETR ' + file_name, open(file_name, 'wb').write)
                         e = 0 
                     except:
                         print("Error while downloading")

             
        #----------------------------------------------------------------------------------------#
        # Closing FTP connection
        
        print('Closing FTP connection')
        ftp.close()
        
        
#Example
    # Adquisition time of MODIS --> Review on Reverb or directly from the FTP
    # example MOD07_L2.A2011001.2215.006.2015047180723.hdf
    # Adquire at 2215 UT
# Day of year
doy = ['001']
# Years of data 
year = [2010,2011]
# Product version
version=['6']
# version =['51','6']
time='2215'
#product to download
product=['MOD07_L2','MOD04_L2','MOD05_L2']
#create FOLDER
MODIS_FOLD='E:\MODIS'
MODIS_FOLD='C:\MODIS'

"""DOWNLOAD SELECTED IMAGERY"""
ModisLADS(doy,year,version,time,product,MODIS_FOLD)
