import os
import platform
import time
import subprocess
import optparse
import shutil

#Allows manual input for release date - must be in YYYYMMDD format.
parser = optparse.OptionParser()
parser.add_option('-d', '--date', dest="dt", help="This is a file listing. Reach out to Justin Weisgerber for any issues with this script.")
(options, args) = parser.parse_args()
if options.dt is None:
	date = input("Enter the release date to apply in (YYYYMMDD) format: ")#.strip()
else:
	date = options.dt.strip()
#print(date)
CAPS_to_PR = os.listdir("Z:\\Montana\\CAPS\\CAPS_to_PR")
# shutil.copy("Z:\\Montana\\CAPS\\archive\\CAPS\\"+str(date)+"\\table10_whdr.txt", "Z:\\Montana\\CAPS\\CAPS_to_PR")
# shutil.copy("Z:\\Montana\\CAPS\\archive\\CAPS\\"+str(date)+"\\table04_whdr.txt", "Z:\\Montana\\CAPS\\CAPS_to_PR")
# shutil.copy("Z:\\Montana\\CAPS\\archive\\CAPS\\"+str(date)+"\\table02_whdr.txt", "Z:\\Montana\\CAPS\\CAPS_to_PR")

#HIDUU the ref file (table10) first
if "table10_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('62534461-4a22-4401-9253-f356ee72e8f2')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_CODE_REF')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('SINGLE_FILE')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table10_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running VAL HIDUU Command for table10***")

#HIDUU table04
if "table04_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('62534461-4a22-4401-9253-f356ee72e8f2')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_MEMBERS')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('FILE_1')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table04_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running VAL HIDUU Command for table04***")

#HIDUU table02
if "table02_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('62534461-4a22-4401-9253-f356ee72e8f2')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_MEMBERS')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('FILE_2')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table02_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running VAL HIDUU Command for table02***")

#HIDUU the ref file (table10) first
if "table10_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('7eb620f9-cbcc-4c97-adc4-d61be2654ee6')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_CODE_REF')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('SINGLE_FILE')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table10_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running PROD HIDUU Command for table10***")

#HIDUU table04		
if "table04_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('7eb620f9-cbcc-4c97-adc4-d61be2654ee6')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_MEMBERS')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('FILE_1')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table04_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running PROD HIDUU Command for table04***")

#HIDUU table02	
if "table02_whdr.txt" in CAPS_to_PR:
	HIDUU_Command=[]
	HIDUU_Command.append('Z:\\Montana\\hi-data-upload-utility-1.6-USZONE1\\bin\\hi-data-upload-utility.bat')
	HIDUU_Command.append('uploadDataSetFile')
	HIDUU_Command.append('-said')
	HIDUU_Command.append('eb969c73-87cf-4c3e-88e8-1ea3eccd5816')
	HIDUU_Command.append('-sas')
	HIDUU_Command.append('P_D7tQ839fCHOZCyIAu32Gk3C20FjewW')
	HIDUU_Command.append('-sid')
	HIDUU_Command.append('7eb620f9-cbcc-4c97-adc4-d61be2654ee6')
	HIDUU_Command.append('-dsid')
	HIDUU_Command.append('MDCD_MT_CAPS_MEMBERS')
	HIDUU_Command.append('-fid')
	HIDUU_Command.append('FILE_2')
	HIDUU_Command.append('-rl')
	HIDUU_Command.append(str(date))
	HIDUU_Command.append('-sv')
	HIDUU_Command.append('2')
	HIDUU_Command.append('-cm')
	HIDUU_Command.append('mtdphhs')
	HIDUU_Command.append('-f')
	filepath = "Z:\\Montana\\CAPS\\CAPS_to_PR\\table02_whdr.txt"
	HIDUU_Command.append(filepath)
	#print(filepath)
	#print(HIDUU_Command)
	p = subprocess.Popen(HIDUU_Command, stdout=subprocess.PIPE)
	output, err=p.communicate()
	print("***Running PROD HIDUU Command for table02***")
	
# os.remove("Z:\\Montana\\CAPS\\CAPS_to_PR\\table10_whdr.txt")
# os.remove("Z:\\Montana\\CAPS\\CAPS_to_PR\\table04_whdr.txt")
# os.remove("Z:\\Montana\\CAPS\\CAPS_to_PR\\table02_whdr.txt")
