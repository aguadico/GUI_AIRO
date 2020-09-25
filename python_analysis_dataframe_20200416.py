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
from mpl_interaction import figure_pz
import matplotlib.pyplot as plt
import tfs
from collections import OrderedDict
import datetime
from datetime import timedelta

class Selection_axial:
   def __init__(self):
        self.verification = False
        self.verification_delay = False
   def check_line(self,line,scan_type,hours,day):
    if "#f11 Prepared " + str(scan_type) in line and hours in line:
         print ("YEEEEEEY")
         print (line)
         self.verification = True
         self.verification_delay = True 
         print (self.verification)
         print (self.verification_delay)
    elif "ReconstructionManager: transitioning to Completed" in line and self.verification_delay == True:
         print ("OR HERE")
         print (self.verification)
         print (self.verification_delay)
         self.verification_delay = False
         self.verification = True
    else:
         self.verification = self.verification and self.verification_delay
    return self.verification 


class Selection_gimbal:
   def __init__(self):
        self.verification = False
        self.verification_delay = False
   def check_line(self,line,scan_type,hours,day):
    if "#t11 Prepared " + str(scan_type) in line and hours in line:
         self.verification = True
         self.verification_delay = True
    elif ("New Status From Power Control Board: ZZ" in line or "New Mode From Power Control Board: ZZ" in line) and self.verification_delay == True:
         self.verification_delay = False
         self.verification = True
    else:
         self.verification = self.verification and self.verification_delay
    return self.verification 

class Selection_pendant:
   def __init__(self):
        self.verification = False
        self.verification_delay = False
   def check_line(self,line,scan_type,hours,day):
    if "#i11 Prepared " + str(scan_type) in line and hours in line:
         print (line)
         self.verification = True
         self.verification_delay = True
    elif "$s00 Completed OK " + str(scan_type) in line or "WaitFor3DScan:ScanTerminatedEarly" in line and self.verification_delay == True:
         self.verification_delay = False
         self.verification = True
    else:
         self.verification = self.verification and self.verification_delay
    return self.verification 

class Selection_system:
   def __init__(self):
        self.verification = False
        self.verification_delay = False
   def check_line(self,line,scan_type,hours,day):
    if "#s11 Prepared " + str(scan_type) in line and hours in line:
         print (line)
         self.verification = True
         self.verification_delay = True
    elif "SuccessfulScan" in line and self.verification_delay == True:
         self.verification_delay = False
         self.verification = True
    else:
         self.verification = self.verification and self.verification_delay
    return self.verification 



def _check_scout_scan(line):
    test = "#f11 Prepared ScoutScan" in line
    return test

def _check_scan_rotor(line):
    testd = "#f11 Prepared ScoutScan" in line
    testd2 = "#f11 Prepared AxialScan" in line 
    testd3 = "#f11 Prepared HelicalScan" in line
    testd4 = "#f11 Prepared WarmupScan" in line
    testd5 = "#f11 Prepared GainCal" in line
    testd6 = "#f11 Prepared QCFullScan" in line
    testd7 = "#f11 Prepared EStopTest" in line
    testd8 = "2020-07-" in line
    testd9 = ((testd or testd2 or testd3 or testd4 or testd5 or testd6 or testd7) and testd8)
    return testd9

def _check_scan_gimbal(line):
    testd = "#z11 Prepared ScoutScan" in line
    testd2 = "#z11 Prepared AxialScan" in line 
    testd3 = "#z11 Prepared HelicalScan" in line
    testd4 = "#z11 Prepared WarmupScan" in line
    testd5 = "#z11 Prepared GainCal" in line
    testd6 = "#z11 Prepared QCFullScan" in line
    testd7 = "#z11 Prepared EStopTest" in line 
    testd8 = "2020-07-" in line
    testd9 = ((testd or testd2 or testd3 or testd4 or testd5 or testd6 or testd7) and testd8)
    return testd9

def _check_scan_pendant(line):
    testd = "#i11 Prepared ScoutScan" in line
    testd2 = "#i11 Prepared AxialScan" in line 
    testd3 = "#i11 Prepared HelicalScan" in line
    testd4 = "#i11 Prepared WarmupScan" in line
    testd5 = "#i11 Prepared GainCal" in line
    testd6 = "#i11 Prepared QCFullScan" in line
    testd7 = "#i11 Prepared EStopTest" in line 
    testd8 = "2020-07-" in line
    testd9 = ((testd or testd2 or testd3 or testd4 or testd5 or testd6 or testd7) and testd8)
    return testd9

def _check_scan_system(line):
    testd = "#s11 Prepared ScoutScan" in line
    testd2 = "#s11 Prepared AxialScan" in line 
    testd3 = "#s11 Prepared HelicalScan" in line
    testd4 = "#s11 Prepared WarmupScan" in line
    testd5 = "#s11 Prepared GainCal" in line
    testd6 = "#s11 Prepared QCFullScan" in line
    testd7 = "#s11 Prepared EStopTest" in line    
    testd8 = "2020-07-" in line 
    testd9 = ((testd or testd2 or testd3 or testd4 or testd5 or testd6 or testd7) and testd8) 
    return testd9

def _check_rotor_scan(line):
    best_1 = "ReconstructionManager received scan protocol: ScanProtocol:" in line
    best_2 = "Category=" in line
    best_3 = "DICOMName=" in line
    best_4 = "FrameGrabber Started" in line
    best_5 = "Completed ScoutScan" in line
    best_6 = "#xxm Y" in line
    best_7 = "New Status From X-Ray Control Board: Ymr" in line
    best_8 = "New Status From X-Ray Control Board: Yaw" in line
    best_9 = "New Status From X-Ray Control Board: Yxq" in line
    best_10 = "ScoutScanConsumer Finish method completed" in line
    best_11 = "New Status From X-Ray Control Board: YKY" in line
    best_12 = "New Status From X-Ray Control Board: NN" in line
    best_13 = "New Status From X-Ray Control Board:" in line
    best_14 = "ReconstructionManager.TransitionStates" in line
    best_15 = "ReconstructionManager: transitioning to Completed" in line
    result = (best_1 or best_2 or best_3 or best_4 or best_5 or best_6 or best_7 or best_8 or best_9 or best_10 or best_11 or best_12 or best_13 or best_14)
    return result


def _check_rotor_best(line): 
    best_1 = "AirQualifyClass is unable to Load Candidate Scan" in line
    best_2 = "Too many bad detectors found!" in line
    best_3 = "Pleora Device Open Failed" in line
    best_4 = "NoGPUAvailable" in line
    best_5 = "New Mode From X-Ray Control Board:" in line
    best_6 = "Stopping Rotor Control Application" in line
    best_7 = "Starting Rotor Control Application" in line
    best_8 = "ConfigStore.Set: History/MaintenanceScans ->" in line
    result = (best_1 or best_2 or best_3 or best_4 or best_5 or best_6 or best_7 or best_8)
    return result

def _check_rotor_motion(line):
    rotor_motion = "MotorController.LogRotorData" in line
    return rotor_motion

def _check_system_scan(line):
    best_1 = "-- Start PrepareForScan Script --" in line
    best_2 = "-- PrepareForScan Script Succeeded --"  in line  
    best_3 = "CsScriptEngine.RunScript, script=StartScan, args=" in line
    best_4 = "SystemManager.OnScriptCompleted SUCCESS" in line
    best_5 = "Undocking" in line
    best_6 = "Moving" in line
    best_7 = "Accelerating" in line
    best_8 = "XRaying" in line
    best_9 = "ScanComplete" in line
    best_10 = "CompleteScan script dock LAN connected!" in line
    best_11 = "MaintenanceManager recording WarmUp" in line
    best_12 = "SystemManager.OnScriptCompleted SUCCESS, id=H" in line
    result = (best_1 or best_2 or best_3 or best_4 or best_5 or best_6 or best_7 or best_8 or best_9 or best_10 or best_11 or best_12)
    return result


def _check_system_best(line):
    best_1 = "MaintenanceManager recording WarmUp at" in line
    best_2 = "MaintenanceManager recording GainCal" in line
    best_3 = "MaintenanceManager recording EstopTest" in line
    best_4 = "MaintenanceManager recording QCSAB" in line
    best_5 = "MaintenanceManager recording QCSTB"
    best_6 = "ConfigStore.Set: Primary ->" in line
    best_7 = "ConfigStore.Set: User ->" in line
    best_8 = "ConfigStore.Set: System ->" in line
    best_9 = "ConfigStore.Set: History ->" in line
    best_10 = "MaintenanceManager recording WarmUp at" in line
    best_11 = "MaintenanceManager recording GainCal" in line
    best_12 = "MaintenanceManager recording EstopTest" in line
    best_13 = "MaintenanceManager recording QCSAB" in line
    best_14 = "MaintenanceManager recording QCSTB" in line
    best_15 = "System address n not registered with queue manager" in line
    best_16 = "System address x not registered with queue manager" in line
    best_17 = "System address g not registered with queue manager" in line
    best_18 = "System address r not registered with queue manager" in line
    best_19 = "System address f not registered with queue manager" in line
    best_20 = "PrepareForScan Script Failed" in line
    best_21 = "Error loading Config file" in line
    best_22 = "MIGimbal n"
    best_23 = "MIGimbal p"
    best_24 = "MIGimbal z"
    best_25 = "MIGimbal t"
    best_26 = "MIRotor n"
    best_27 = "MIRotor x"
    best_28 = "MIRotor g"
    best_29 = "MIRotor r"
    return (best_1 or best_2 or best_3 or best_4 or best_5 or best_6 or best_7 or best_8 or best_9 or best_10 or best_11 or best_12)

def _check_pendant_best(line):
    best_1 = "Failed DB Integrity Check: DB Corruption Found"
    best_2 = "UI: StateMachine: Fire"
    best = (best_1 or best_2)
    return best

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
         print ("DAYYYYY")
         print (date_stamp)
         day_no_format.append(parts[0][1:11].replace("-", "_"))
         day.append(date_stamp)
         hours.append(parts[0][12:22].replace(":", "_"))
         scan.append(parts[-1])
    data_df = pd.DataFrame.from_records({column_names[0]:scan, column_names[1]: day, column_names[2]:hours})
    data_df_no_format = pd.DataFrame.from_records({column_names[0]:scan, column_names[1]: day_no_format, column_names[2]:hours})
    new_column = data_df_no_format[[column_names[0],column_names[1], column_names[2]]].agg('_'.join, axis=1)
    new_column =  (component + '_' + new_column.astype(str))
    data_df[column_names[3]] = pd.Series(new_column, index=data_df.index)    
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
    print ("checking scans")
    with open(rotor_control_app_path, "r") as reader, open(rotor_control_app_path_output, "w") as writer: 
          writer.writelines(line for line in reader if _check_scan_rotor(line))
    with open(gimbal_control_app_path, "r") as reader, open(gimbal_control_app_path_output, "w") as writer: 
          writer.writelines(line for line in reader if _check_scan_gimbal(line))
    with open(pendant_ui_app_path, "r") as reader, open(pendant_ui_app_path_output, "w") as writer: 
          writer.writelines(line for line in reader if _check_scan_pendant(line))
    with open(system_manager_app_path, "r") as reader, open(system_manager_app_path_output, "w") as writer: 
          writer.writelines(line for line in reader if _check_scan_system(line))


def reading_rotor_best_scan(self,output_path):
    #INPUT FILES 
    rotor_control_app_path_scan = os.path.join(output_path,"scan_rotor_summary")
    rotor_control_app_path_best = os.path.join(output_path,"best_rotor_summary")
    with open(self.file_to_display, "r") as reader, open(rotor_control_app_path_scan, "w") as writer: 
          writer.writelines(line for line in reader if _check_rotor_scan(line))
    with open(self.file_to_display, "r") as reader, open(rotor_control_app_path_best, "w") as writer: 
          writer.writelines(line for line in reader if _check_rotor_best(line))


def reading_rotor_motion(self,output_path):
    #INPUT FILES 
    rotor_motion_app_path_scan = os.path.join(output_path,"motion_rotor_summary")
    with open(self.file_to_display, "r") as reader, open(rotor_motion_app_path_scan, "w") as writer: 
          writer.writelines(line for line in reader if _check_rotor_motion(line))
    

def reading_system_best_scan(self,output_path):
    #INPUT FILES 
    rotor_control_app_path_scan = os.path.join(output_path,"scan_system_summary")
    rotor_control_app_path_best = os.path.join(output_path,"scan_system_summary")
    with open(self.file_to_display, "r") as reader, open(rotor_control_app_path_scan, "w") as writer: 
          writer.writelines(line for line in reader if _check_system_scan(line))
    with open(self.file_to_display, "r") as reader, open(rotor_control_app_path_best, "w") as writer: 
          writer.writelines(line for line in reader if _check_system_best(line))


def pendant_system_best_scan(self,output_path):
    #INPUT FILES 
    rotor_control_app_path_scan = os.path.join(output_path,"scan_pendant_summary")
    rotor_control_app_path_best = os.path.join(output_path,"scan_pendant_summary")
    with open(self.file_to_display, "r") as reader, open(rotor_control_app_path_best, "w") as writer: 
          writer.writelines(line for line in reader if _check_pendant_best(line))


def generate_output_file(self,output_path):
    column_names  = ["SCAN_" + str(self.logfile_type),"DAY_" + str(self.logfile_type) ,"HOUR_" + str(self.logfile_type),'FILE_NAME_' + str(self.logfile_type)]
    print ("HEREEEEE")
    print (self.data_df_all_subsystems)
    print ((getattr(self.data_df_all_subsystems,column_names[2])).dropna())
    print (len((getattr(self.data_df_all_subsystems,column_names[2])).dropna()))
    hour = (getattr(self.data_df_all_subsystems,column_names[2])).dropna().iloc[self.index_scan]
    name = (getattr(self.data_df_all_subsystems,column_names[3])).dropna().iloc[self.index_scan]
    scan = (getattr(self.data_df_all_subsystems,column_names[0])).dropna().iloc[self.index_scan]
    day = (getattr(self.data_df_all_subsystems,column_names[1])).dropna().iloc[self.index_scan]
    # DEFINTION: SAVING DAYS ASSOCIATED TO EACH FILE IN DATA FRAME
    #df_dates[all_scan_different_components_names[j]] = (days)       
    # DEFINITION: READING FILES AND WRITING THE SELECTED LINES INTO FILE
    open_files = str(os.path.join(self.dir_,self.fileName))
    file_path_name = os.path.join(self.output_path,str(name))
    print ("open files")
    print (str(open_files))
    print (scan,hour)
    sel = Selection_axial()
    sel_gimbal = Selection_gimbal()
    sel_pendant = Selection_pendant()
    sel_system = Selection_system()
    with open(str(open_files), "r") as reader, open(file_path_name, "w") as writer:      
          if self.fileName == "RotorControlApp.log":
            print ("HEREEE ROTOR")
            writer.writelines(line for line in reader if sel.check_line(line,scan,hour.replace("_", ":"),day))
          elif self.fileName == "GimbalControlApp.log":
            print ("HEREEE")
            writer.writelines(line for line in reader if sel_gimbal.check_line(line,scan,hour.replace("_", ":"),day))
          elif self.fileName == "SystemManagerApp.log":
            print ("HEREEE ")
            writer.writelines(line for line in reader if sel_system.check_line(line,scan,hour.replace("_", ":"),day))
          elif self.fileName == "PendantUIApp.log":
            print ("HEREEE")
            writer.writelines(line for line in reader if sel_pendant.check_line(line,scan,hour.replace("_", ":"),day))
    

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


    print (data_df_rotor)
    print (data_df_gimbal)
    print (data_df_system)
    print (data_df_pendant)
    print ("this one")
    print (data_df_rotor)
    print (data_df_pendant)
    print (data_df_all_subsystems)

    open_files = ["SystemManagerApp.log","RotorControlApp.log","PendantUIApp.log","GimbalControlApp.log"]
    all_scan_different_components_names = ["SYSTEM","ROTOR","PENDANT","GIMBAL"]
    df_date_unique_columns_names = ["SYSTEM","ROTOR","PENDANT","GIMBAL","SCAN"]
    # DEFINITION: STARTING A DATAFRAME WITH DATES NO-REPEATED
    df_dates = pd.DataFrame(columns=df_date_unique_columns_names)
    
    # DEFINITION: ITERATION OVER ALL THE DIFFERENT LOG FILES ---- move to 
    for j in range(len(all_scan_different_components_names)):
       print ("COMPONENT")
       print (all_scan_different_components_names[j])        
       column_names  = ["SCAN_" + all_scan_different_components_names[j],"DAY_" + all_scan_different_components_names[j] ,"HOUR_" + all_scan_different_components_names[j],'FILE_NAME_' + all_scan_different_components_names[j]]
       hours = (getattr(data_df_all_subsystems,column_names[2])).dropna()
       names = (getattr(data_df_all_subsystems,column_names[3])).dropna()
       scans = (getattr(data_df_all_subsystems,column_names[0])).dropna()
       days = (getattr(data_df_all_subsystems,column_names[1])).dropna()
       print ("HEREEE")
       print (days)
       # DEFINTION: SAVING DAYS ASSOCIATED TO EACH FILE IN DATA FRAME
       df_dates[all_scan_different_components_names[j]] = (days)       
       # DEFINITION: READING FILES AND WRITING THE SELECTED LINES INTO FILE
       for i in range(len(days)):
           print (i)
           print (scans.iloc[i])
           print (scans[i])
           print (hours.iloc[i])
           print (hours[i])
           print (days.iloc[i])
           print (days[i])
           file_path_name = os.path.join("/Users/anagtv/Desktop/Visitas_Airo/File_analysis",names[i])
           #print (scans[i],hours[i]. ,days[i].replace("_", "-"))
           #print (file_path_name)
           with open(open_files[j], "r") as reader, open(file_path_name, "w") as writer:   
                 print (open_files[j])       
                 if open_files[j] == "RotorControlApp.log":
                   writer.writelines(line for line in reader if sel.check_line(line,scans[i],hours[i].replace("_", ":"),days[i]))
                 elif open_files[j] == "GimbalControlApp.log":
                   print ("HEREEE")
                   writer.writelines(line for line in reader if sel_gimbal.check_line(line,scans[i],hours[i].replace("_", ":"),days[i]))
                 elif open_files[j] == "SystemManagerApp.log":
                   print ("HEREEE ")
                   writer.writelines(line for line in reader if sel_system.check_line(line,scans[i],hours[i].replace("_", ":"),days[i]))
                 elif open_files[j] == "PendantUIApp.log":
                   print ("HEREEE")
                   writer.writelines(line for line in reader if sel_pendant.check_line(line,scans[i],hours[i].replace("_", ":"),days[i]))
    # DEFINTION: REMOVING THE NAN DATAFRAME ELEMENTS 
    df_dates["SCAN"] = (getattr(data_df_all_subsystems,"SCAN_ROTOR")).dropna()
    # TO DO: FinD THE LONGEST ELEMENT
    # STARTING THE DOCUMENT MERGING
    # Select the non-repeated dates
    df_date_unique = (df_dates.drop_duplicates(subset=all_scan_different_components_names[1],keep = "last"))
    print ("df_date_unique")
    print (df_date_unique)
    for i in range(len(df_date_unique.ROTOR)):
        print ("I 1")
        print (i)
        df_frame_one_day = (data_df_all_subsystems[data_df_all_subsystems["DAY_ROTOR"] == df_date_unique.ROTOR.iloc[i]])
        # DEFINITION: KNOWING HOW MANY LOG FILES COVER THAT GIVEN DAY AND THE INDEX
        # DEFINITION: FINDING THE INDEX OF THE SCANS AT THAT GIVEN DAY (IN THE COMPLETE MATRIX)
        index_day_rotor = np.array((data_df_all_subsystems[data_df_all_subsystems["DAY_ROTOR"] == df_date_unique.ROTOR.iloc[i]].index))
        index_day_pendant = np.array((data_df_all_subsystems[data_df_all_subsystems["DAY_PENDANT"] == df_date_unique.ROTOR.iloc[i]].index))
        index_day_system = np.array((data_df_all_subsystems[data_df_all_subsystems["DAY_SYSTEM"] == df_date_unique.ROTOR.iloc[i]].index))
        index_day_gimbal = np.array((data_df_all_subsystems[data_df_all_subsystems["DAY_GIMBAL"] == df_date_unique.ROTOR.iloc[i]].index))
        # DEFINTION: REPLACE THE : BY _ IN ORDER TO AVOID PROBLEMS WITH THE FILE NAME
        day_name = str(df_date_unique.ROTOR.iloc[i]).replace("_", ":")
        print (index_day_rotor,index_day_pendant,index_day_system,index_day_gimbal)
        # DEFINITION: CHECK HOW MANY SCANS ARE AT A GIVEN DAY
        len_index_day_rotor =   len(index_day_rotor)
        len_index_day_pendant = len(index_day_pendant)
        len_index_day_system =  len(index_day_system)
        len_index_day_gimbal =  len(index_day_gimbal)
        # DEFINTION: IF FOR A GIVEN DAY THERE IS NOT SCANS, THEN DO NOT CONSIDER THAT FILE.
        names_components = ["ROTOR","PENDANT","SYSTEM","GIMBAL"]
        columns_names_components = ["FILE_NAME_ROTOR","FILE_NAME_PENDANT","FILE_NAME_SYSTEM","FILE_NAME_GIMBAL"]
        index_day = [index_day_rotor,index_day_pendant,index_day_system,index_day_gimbal] 
        len_index_day = [len_index_day_rotor,len_index_day_pendant,len_index_day_system,len_index_day_gimbal] 
        zero_index = [m for m, e in enumerate(len_index_day) if e == 0]
        for l in range(len(zero_index)): 
            print (l)
            print (zero_index[l])
            index_day.pop(zero_index[l]-l)
            names_components.pop(zero_index[l]-l)
            columns_names_components.pop(zero_index[l]-l)
        # DEFINITION: ITERATES OVER THE LOG FILE WITH THE MAXIUM NUMBER OF SCANS FOR A GIVEN DAY
        for j in range(np.max(len_index_day)):  
            file_components_path = []   
            output_name = str(data_df_all_subsystems.SCAN_ROTOR.iloc[index_day[1][j]]) + "_" + day_name + "_" + str(data_df_all_subsystems.HOUR_ROTOR.iloc[index_day[1][j]])
            output_name_combined = str(data_df_all_subsystems.SCAN_ROTOR.iloc[index_day[1][j]]) + "_" + day_name + "_" + str(data_df_all_subsystems.HOUR_ROTOR.iloc[index_day[1][j]]) + "_combined"
            output_path = os.path.join("/Users/anagtv/Desktop/Visitas_Airo/File_analysis/",output_name)
            output_path_combined = os.path.join("/Users/anagtv/Desktop/Visitas_Airo/File_analysis/",output_name_combined)
            for k in range(len(names_components)):
                file_name_path = (getattr(data_df_all_subsystems,columns_names_components[k])).iloc[index_day[k][j]]
                file_components_path.append(os.path.join("/Users/anagtv/Desktop/Visitas_Airo/File_analysis/",file_name_path))
            combined_file = []
            combined_file_element = []
            combined_file_hours = []
            print ("OUTPUT PATH")
            print (output_path)
            for file_path_name in file_components_path:
                print ("HEREEE ARE INDIVIDUAL PATHS")
                print (file_path_name)
                file_path_name_rotor_read = open(file_path_name,"r")
                for line in file_path_name_rotor_read:
                   parts = line.split()
                   combined_file.append(parts)
                   combined_file_hours.append(parts[0][11:27])
                   if (file_path_name[49]) == "R":
                       combined_file_element.append("ROTOR")
                   elif (file_path_name[49]) == "G":
                       combined_file_element.append("GIMBAL")
                   elif (file_path_name[49]) == "S":
                       combined_file_element.append("SYSTEM")
                   elif (file_path_name[49]) == "P":
                       combined_file_element.append("PENDANT")
            # DEFINITION: SORTING COMBINED FILE BY HOUR           
            combined_file_sorted = [combined_file for _,combined_file in sorted(zip(combined_file_hours,combined_file))]
            combined_file_element_sorted = [combined_file_element for _,combined_file_element in sorted(zip(combined_file_hours,combined_file_element))]
            # DEFINITION: INITIALIZE VARIABLES
            time_stamp = []
            message_information = []
            action = []
            file_type = []
            for i in range(len(combined_file_sorted)):
            #    # REMOVING EXTRA LINES
                if ">" not in combined_file_sorted[i][0]:
                    time_stamp.append(combined_file_sorted[i][0][1:])
                    message_information.append('_'.join(combined_file_sorted[i][1:3]))
                    action.append('_'.join(combined_file_sorted[i][3:]))
                    file_type.append(combined_file_element_sorted[i])
            ## SETTING DATAFRAME FOR USING AS AN OUTPUT
            data_df_combined = pd.DataFrame.from_records({'TIME_STAMP':time_stamp, 'TYPE': message_information, 'ACTION':action, 'FILE_TYPE': file_type})
            data_df_combined =  data_df_combined.loc[:, ['FILE_TYPE', 'TIME_STAMP',   'TYPE',  'ACTION']]  
            #WRITING 
            file_path_name_combined = "test_" + str(j) + ".out"
            file_path_name_combined_filtered = "test_filtered_" + str(j) + ".out"
            tfs.write(output_path, data_df_combined, save_index="index_column")
            data_to_verify = tfs.read(output_path)
            #KEEP REMOVING UNNECESARY ELEMENTS
            data_to_verify_1 = (data_to_verify[~data_to_verify.ACTION.str.contains("Previous_Entry_Repeats")])
            data_to_verify_2 = (data_to_verify_1[~data_to_verify_1.ACTION.str.contains("$s00_Executing_Transitioning_ScoutScan")])
            data_to_verify_3 = (data_to_verify_2[~data_to_verify_2.ACTION.str.contains("Handling_Client_Message:_#&22_History/RotorPC/LastKnownOnTime")])
            data_to_verify_4 = (data_to_verify_3[~data_to_verify_3.ACTION.str.contains("ConfigStore.Set:_History/RotorPC/LastKnownOnTime")])
            print ("HEREEEEE")
            print (data_to_verify_4)
            #print (data_to_verify)
            tfs.write(output_path_combined, data_to_verify_4) 
    #file_path_name_gimbal_read = open(ffile_path_name[0],"r")
    #print (new_column.iloc[0])
    #file_path_name = os.path.join("/Users/anagtv/Desktop/Visitas_Airo/File_analysis",df_frame_one_day_one_hour)
    #print (file_path_name)
    #data_df_all_subsystems[all_scan_different_components_names[]][excel_data_df['Target_I'].astype(float) > float(current)]

    

if __name__ == "__main__":
    #_input_path,_output_path,target_current = _parse_args()
    main()