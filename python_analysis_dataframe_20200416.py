import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser
import os
from tkinter import *
from pandas import ExcelWriter
plt.rcParams.update({'font.size': 16})
plt.rcParams["figure.figsize"] = (15,10)
import sys
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python")
sys.path.append("/Users/anagtv/Documents/Beta-Beat.src-master")
#from tfs_files import tfs_pandas
#from mpl_interaction import figure_pz
import matplotlib.pyplot as plt
import tfs
from collections import OrderedDict
import datetime
from datetime import timedelta




class Selection_axial:
   def __init__(self):
        self.verification = False
        self.verification_delay = False
   def check_line(self,line,scan_type,hours,day,initial,final):
    #print (initial)
    #print (final)
    if initial in line and hours in line:
         self.verification = True
         self.verification_delay = True 
    elif (final[0] in line or final[1] in line) and self.verification_delay == True:
         self.verification_delay = False
         self.verification = True
    else:
         self.verification = self.verification and self.verification_delay
    return self.verification 


def _check_scan(line,scan_type):
    test_scout =scan_type + " Prepared ScoutScan" in line
    test_axial_scan = scan_type + " Prepared AxialScan" in line 
    test_helical_scan = scan_type + " Prepared HelicalScan" in line
    test_warm_up_scan = scan_type + " Prepared WarmupScan" in line
    test_gain_cal = scan_type + " Prepared GainCal" in line
    test_QC = scan_type + " Prepared QCAxialFullScan" in line 
    testd_month = "2020-" in line
    test = ((test_scout or test_axial_scan or test_helical_scan or test_warm_up_scan or test_gain_cal or test_QC) and testd_month)
    return test


def _check_general(line,search):
    results = []
    results_true = []
    for best in search:
        results.append(best in line)
        if (best in line)== True:
            results_true.append(best in line)
    if len(results_true) >= 1:
       result = True
    else:
       result = False 
    return result


def _combinig_different_files(rotor_file,gimbal_file):
    set_c = set_a + set_c 
    set_c = set_a + set_b
    set_d = []
    for a in set_c:
       set_d.append(a[11:27])
    hours_sorted = [set_c for _,set_c in sorted(zip(set_d,set_c))]
    hours_sorted

def selecting_entries(logfile,component):
    column_names  = ["SCAN_" + component,"DAY_" + component,"HOUR_" + component,'FILE_NAME_' + component]
    hours = []
    day = []
    day_no_format = []
    scan = []
    for line in logfile:
         parts = line.split()
         date_format = "%Y-%m-%d"
         date_stamp = datetime.datetime.strptime(parts[0][1:11],date_format).date()
         day_no_format.append(parts[0][1:11].replace("-", "_"))
         day.append(date_stamp)
         hours.append(parts[0][12:22].replace(":", "_"))
         scan.append(parts[-1])
    data_df = pd.DataFrame.from_records({column_names[0]:scan, column_names[1]: day, column_names[2]:hours})
    data_df_no_format = pd.DataFrame.from_records({column_names[0]:scan, column_names[1]: day_no_format, column_names[2]:hours})
    ID_column = data_df_no_format[[column_names[0],column_names[1], column_names[2]]].agg('_'.join, axis=1)
    ID_column =  (component + '_' + ID_column.astype(str))
    data_df[column_names[3]] = pd.Series(ID_column, index=data_df.index)    
    return data_df

def writing_files(input_path):
    #INPUT FILES 
    rotor_control_app_path = os.path.join(input_path,"RotorControlApp.log")
    gimbal_control_app_path = os.path.join(input_path,"GimbalControlApp.log")
    pendant_ui_app_path = os.path.join(input_path,"PendantUIApp.log")
    system_manager_app_path =  os.path.join(input_path,"SystemManagerApp.log")
    #OUTPUT FILES
    rotor_control_app_path_output = os.path.join(input_path,"all_scans_rotor")
    gimbal_control_app_path_output = os.path.join(input_path,"all_scans_gimbal")
    pendant_ui_app_path_output = os.path.join(input_path,"all_scans_pendant")
    system_manager_app_path_output =  os.path.join(input_path,"all_scans_system")
    files_control_input = [rotor_control_app_path,gimbal_control_app_path,pendant_ui_app_path,system_manager_app_path]
    files_control_output = [rotor_control_app_path_output,gimbal_control_app_path_output,pendant_ui_app_path_output,system_manager_app_path_output]
    codes_control = ["#f11","#z11","#i11","#s11"]
    for i in range(len(files_control_input)):
        print (files_control_input[i])
        print (files_control_output[i])
        with open(files_control_input[i], "r") as reader, open(files_control_output[i], "w") as writer: 
          writer.writelines(line for line in reader if _check_scan(line,codes_control[i]))
    #with open(rotor_control_app_path, "r") as reader, open(rotor_control_app_path_output, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_scan(line,"#f11"))
    #with open(gimbal_control_app_path, "r") as reader, open(gimbal_control_app_path_output, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_scan(line,"#z11"))
    #with open(pendant_ui_app_path, "r") as reader, open(pendant_ui_app_path_output, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_scan(line,"#i11"))
    #with open(system_manager_app_path, "r") as reader, open(system_manager_app_path_output, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_scan(line,"#s11"))
    return rotor_control_app_path_output,gimbal_control_app_path_output,pendant_ui_app_path_output,system_manager_app_path_output


    
def summarising_file(self,file_input,file_scan,search):
    #INPUT FILES 
    with open(file_input, "r") as reader, open(file_scan, "w") as writer: 
          writer.writelines(line for line in reader if _check_general(line,search))
    #with open(self.file_to_display, "r") as reader, open(file_best, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_general(line,ROTOR_BEST))


def generate_output_file(self,output_path,column_names):
    hour = (getattr(self.data_df_all_subsystems,column_names[2])).dropna().iloc[self.index_scan]
    name = (getattr(self.data_df_all_subsystems,column_names[3])).dropna().iloc[self.index_scan]
    scan = (getattr(self.data_df_all_subsystems,column_names[0])).dropna().iloc[self.index_scan]
    day = (getattr(self.data_df_all_subsystems,column_names[1])).dropna().iloc[self.index_scan]
    # DEFINTION: SAVING DAYS ASSOCIATED TO EACH FILE IN DATA FRAME
    #df_dates[all_scan_different_components_names[j]] = (days)       
    # DEFINITION: READING FILES AND WRITING THE SELECTED LINES INTO FILE
    open_files = str(os.path.join(self.dir_,self.fileName))
    file_path_name = os.path.join(self.output_path,str(name))
    self.list_files = ["RotorControlApp.log","GimbalControlApp.log","SystemManagerApp.log","PendantUIApp.log"]
    self.initial_verification = ["#f11 Prepared " + str(scan),"#t11 Prepared " + str(scan),"#i11 Prepared " + str(scan), "#s11 Prepared " + str(scan)]
    self.end_verification = [["ReconstructionManager: transitioning to Completed","aaaaaaaa"],["New Status From Power Control Board: ZZ","New Mode From Power Control Board: ZZ"], ["$s00 Completed OK ", "WaitFor3DScan:ScanTerminatedEarly"],["SuccessfulScan","aaaaa"]]
    sel = Selection_axial()
    index = self.list_files.index(self.fileName)
    with open(str(open_files), "r") as reader, open(file_path_name, "w") as writer:        
          writer.writelines(line for line in reader if sel.check_line(line,scan,hour.replace("_", ":"),day,self.initial_verification[index],self.end_verification[index]))

   

def main():
    # TO DO: set the input, output and conditions.
    sel = Selection_axial()
    sel_gimbal = Selection_gimbal()
    sel_pendant = Selection_pendant()
    sel_system = Selection_system()
    # DEFINITION: FINDING THE DIFFERENT SCANS INSIDE THE LOG FILES AND WRITING THEM INTO A NEW FILE
    writing_files()

    # DEFINITION: READING THE PREVIOUS FILES
    logfile_rotor = open("all_scans_rotor","r")
    logfile_gimbal = open("all_scans_gimbal","r")
    logfile_pendant = open("all_scans_pendant","r")
    logfile_system = open("all_scans_system","r")

    # DEFINTION: CREATING DATAFRAMES WITH THE INFORMATION NEEDED, SCAN, DAY, HOUR AND FILENAME THAT WILL BE LATER USED FOR SAVING THE COMMANDS 
    data_df_rotor = selecting_entries(logfile_rotor,"ROTOR")
    data_df_gimbal = selecting_entries(logfile_gimbal,"GIMBAL")
    data_df_pendant = selecting_entries(logfile_pendant,"PENDANT")
    data_df_system = selecting_entries(logfile_system,"SYSTEM")
    # DEFINITION: CONCATENATING ALL THE SUB DATA FRAMES IN ORDER TO HAVE A INDIVIDUAL DATA FRAME
    data_df_all_subsystems = (pd.concat([data_df_system,data_df_rotor,data_df_pendant,data_df_gimbal], axis=1, sort=False))



if __name__ == "__main__":
    #_input_path,_output_path,target_current = _parse_args()
    main()
