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
from datetime import datetime
import sqlite3



def _check_scan(line,scan_type):
    test_scout =scan_type + " Completed ScoutScan" in line
    test_axial_scan = scan_type + " Completed AxialScan" in line 
    test_helical_scan = scan_type + " Completed HelicalScan" in line
    test_warm_up_scan = scan_type + " Completed WarmupScan" in line
    test_gain_cal = scan_type + " Completed GainCal" in line
    test_QC = scan_type + " Completed QCAxialFullScan" in line 
    test_QC_full_helical = scan_type + " Completed QCFullScan" in line 
    test_QC_daily_helical = scan_type + " Completed QCDailyScan" in line 
    test_QC_daily = scan_type + " Completed QCAxialDailyScan" in line 
    test_emergency = scan_type + " Completed EStopTest" in line
    testd_month = "202" in line
    test = ((test_scout or test_axial_scan or test_helical_scan or test_warm_up_scan or test_gain_cal or test_QC or test_QC_full_helical or test_QC_daily or test_QC_daily_helical or test_emergency) and testd_month)
    return test


class Maintenance:
    def __init__(self):
      self.warmup = []
      self.estop = []
      self.gaincal = []
      self.helicaldaily = []
      self.helicalfull = []
      self.axialdaily = []
      self.axialfull = []
      self.gaincal_fail_total = []
      self.gaincal_fail_dates = []
      self.scan_parameters = []
      self.total_reasons = []

    
    def _check_generator(self,line):
        current = "ConfigStore.Set: History/Generator" in line
        if current == True:
          #print ("HEREEEEEE")
          for number in list(range(5,len(line.split(" ")[-1].split("><"))-2,6)):
             scan_parameters = []
             scan_parameters.append(line.split(" ")[-1].split("><")[number-2].split(">")[1].split("<")[0])
             scan_parameters.append(line.split(" ")[-1].split("><")[number-1].split(">")[1].split("<")[0])
             scan_parameters.append(datetime.strptime(line.split(" ")[-1].split("><")[number].split(">")[1].split("<")[0][0:10],'%Y-%m-%d').date())
             scan_parameters.append(line.split(" ")[-1].split("><")[number].split(">")[1].split("<")[0][11:19])
             #print ("VALUE")
             #print (line.split(" ")[-1].split("><")[number].split(">")[1].split("<")[0][0:10])
             #print (line.split(" ")[-1].split("><")[number].split(">")[1].split("<")[0][11:19])
             self.scan_parameters.append(scan_parameters)
             #print ("SCAN PARAMTERES!!!!!!")
             #print (self.scan_parameters)
        return current

    def _check_config(self,line):
        maintenance = "History/MaintenanceScans ->" in line
        if maintenance == True:
            self.warmup.append(datetime.strptime(line.split(" ")[-1].split("><")[3][6:16],'%Y-%m-%d').date())
            self.estop.append(datetime.strptime(line.split(" ")[-1].split("><")[7][6:16],'%Y-%m-%d').date())
            self.gaincal.append(datetime.strptime(line.split(" ")[-1].split("><")[11][6:16],'%Y-%m-%d').date())
            self.helicaldaily.append(datetime.strptime(line.split(" ")[-1].split("><")[15][6:16],'%Y-%m-%d').date())
            self.helicalfull.append(datetime.strptime(line.split(" ")[-1].split("><")[19][6:16],'%Y-%m-%d').date())
            self.axialdaily.append(datetime.strptime(line.split(" ")[-1].split("><")[23][6:16],'%Y-%m-%d').date())
            self.axialfull.append(datetime.strptime(line.split(" ")[-1].split("><")[27][6:16],'%Y-%m-%d').date())       
        return maintenance

    def _check_gain_cal(self,line):
        fail_cal = "History/GimbalPC/LastGainCalError" in line 
        fail_cal_reason = "History/GimbalPC/LastGainCalError ->" in line
        if fail_cal_reason == True:
           print ("REASON!!!!!!!!!!")
           print (line)
           self.total_reasons.append((line.split(" ")[6:]))
           print (self.total_reasons)
        if fail_cal == True:
            self.gaincal_fail_total.append(line.split(" ")[-1][0:10])
        self.gaincal_fail_dates = [datetime.strptime(number,'%Y-%m-%d').date() for number in self.gaincal_fail_total if '2' in number]
        return fail_cal
 
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


def selecting_entries(logfile,component):
    column_names  = ["SCAN_" + component,"DAY_" + component,"HOUR_" + component,'FILE_NAME_' + component]
    hours = []
    day = []
    day_no_format = []
    scan = []
    for line in logfile:
         parts = line.split()
         date_format = "%Y-%m-%d"
         date_stamp = datetime.strptime(parts[0][1:11],date_format).date()
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

def writing_files(self,input_path):
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
    xray_file = os.path.join(input_path,"xray_summary")
    maintenace_file = os.path.join(input_path,"maintenance_summary")
    gaincal_file = os.path.join(input_path,"gaincal_summary")
    files_control_input = [rotor_control_app_path,gimbal_control_app_path,pendant_ui_app_path,system_manager_app_path]
    files_control_output = [rotor_control_app_path_output,gimbal_control_app_path_output,pendant_ui_app_path_output,system_manager_app_path_output]
    codes_control = ["#f11","#z11","#i11","#s11"]
    maintenance_analysis = Maintenance()
    for i in range(len(files_control_input)):
        print ("READING AND WRITING FILES ")
        print (files_control_input[i])
        print (files_control_output[i])
        with open(files_control_input[i], "r") as reader, open(files_control_output[i], "w") as writer: 
          writer.writelines(line for line in reader if _check_scan(line,codes_control[i]))
    with open(files_control_input[1], "r") as reader, open(maintenace_file, "w") as writer: 
          writer.writelines(line for line in reader if maintenance_analysis._check_config(line))
    with open(files_control_input[1], "r") as reader, open(xray_file, "w") as writer: 
          writer.writelines(line for line in reader if maintenance_analysis._check_generator(line))
    with open(files_control_input[1], "r") as reader, open(gaincal_file, "w") as writer: 
          writer.writelines(line for line in reader if maintenance_analysis._check_gain_cal(line))
    print ("MAINTENANCE")
    print (maintenance_analysis.warmup)
    print (maintenance_analysis.helicaldaily)
    print (maintenance_analysis.axialfull)
    self.dates_df = pd.DataFrame(list(zip(
      maintenance_analysis.helicaldaily,
      maintenance_analysis.helicalfull,
      maintenance_analysis.axialdaily,
      maintenance_analysis.axialfull)),columns=["HELICALDAILYQC","HELICALFULLQC","AXIALDAILYQC","AXIALFULLQC"])
    self.total_reasons = ""
    for reason in maintenance_analysis.total_reasons[0]:
        self.total_reasons += reason
        self.total_reasons += " "
    print ("HEREEEEEEE")
    #print (self.dates_df)
    self.dates_gaincal = pd.DataFrame(maintenance_analysis.gaincal_fail_dates,columns=["GAINCALFAIL"])
    print ("GAIN CAL")
    print (self.dates_gaincal)
    self.scan_parameters_df = pd.DataFrame(maintenance_analysis.scan_parameters,columns = ["CURRENT","TIME","DAY","HOUR"]).drop_duplicates()
    #dates_no_repeat = (self.scan_parameters_df.DAY.drop_duplicates())
    con = sqlite3.connect('scans_database.db')
    cursorObj = con.cursor()
    try:
       cursorObj.execute("CREATE TABLE scans_values(ID text PRIMARY KEY,DAY text, CURRENT text, HOUR text, DURATION text)")
       cursorObj.execute("CREATE TABLE scans_values_no_filter(ID text PRIMARY KEY,DAY text, CURRENT text, HOUR text, DURATION text)")
    except:
       print ("CONTINUE")
    for current,length,day,hour in zip(self.scan_parameters_df.CURRENT,self.scan_parameters_df.TIME,self.scan_parameters_df.DAY,self.scan_parameters_df.HOUR):
        entities = (day.strftime('%Y-%m-%d') + "T"+ hour[0:2]+"C"+current[0:3]+"D"+length[0:3], day, current,hour, length)
        entities_no_filter = (day.strftime('%Y-%m-%d') + "T"+ hour, day, current,hour, length)
        try:
            cursorObj.execute('INSERT INTO scans_values(ID,DAY, CURRENT, HOUR, DURATION) VALUES(?,?, ?, ?, ?)', entities)
            con.commit()
        except:
            print ("ALREADY IN THE DATABASE")
        try:
            cursorObj.execute('INSERT INTO scans_values_no_filter(ID,DAY, CURRENT, HOUR, DURATION) VALUES(?,?, ?, ?, ?)', entities_no_filter)
            con.commit()
        except:
            print ("ALREADY IN THE DATABASE")
    cursorObj.execute('SELECT SUM(CURRENT),SUM(DURATION) FROM scans_values WHERE DAY > "2021-01-01"')
    rows = cursorObj.fetchall()
    for row in rows:
        print (row[0])
        print (row[1])
        print (row[0]*row[1])
    print ("NO FILTER")
    cursorObj.execute('SELECT SUM(CURRENT),SUM(DURATION) FROM scans_values_no_filter WHERE DAY > "2021-01-01"')
    rows = cursorObj.fetchall()
    for row in rows:
        print (row[0])
        print (row[1])
        print (row[0]*row[1])
    #for date in dates_no_repeat:
    #    print ("DATE")
    #    print (date)
    #    print ((self.scan_parameters_df.CURRENT[self.scan_parameters_df.DAY== date]))
    #    print ((self.scan_parameters_df.TIME[self.scan_parameters_df.DAY == date]))
    return rotor_control_app_path_output,gimbal_control_app_path_output,pendant_ui_app_path_output,system_manager_app_path_output


    
def summarising_file(self,file_input,file_scan,search):
    #INPUT FILES 
    with open(file_input, "r") as reader, open(file_scan, "w") as writer: 
          writer.writelines(line for line in reader if _check_general(line,search))

    #with open(self.file_to_display, "r") as reader, open(file_best, "w") as writer: 
    #      writer.writelines(line for line in reader if _check_general(line,ROTOR_BEST))


def generate_output_file(self,output_path,column_names):
    complete_date = []
    for i in range(4):
        complete_date.append((getattr(self.data_df_all_subsystems,column_names[i])).dropna().iloc[self.index_scan])
    scan = complete_date[0]
    day = complete_date[1]
    hour = complete_date[2]
    name = complete_date[3]
    open_files = str(os.path.join(self.dir_,self.fileName))
    file_path_name = os.path.join(self.output_path,str(name))
    self.list_files = ["RotorControlApp.log","GimbalControlApp.log","SystemManagerApp.log","PendantUIApp.log"]
    self.initial_verification = ["#f11 Completed " + str(scan),"#t11 Completed " + str(scan),"#i11 Completed " + str(scan), "#s11 Completed " + str(scan)]
    self.end_verification = [["ReconstructionManager: transitioning to Completed","aaaaaaaa"],["New Status From Power Control Board: ZZ","New Mode From Power Control Board: ZZ"], ["$s00 Completed OK ", "WaitFor3DScan:ScanTerminatedEarly"],["SuccessfulScan","aaaaa"]]
    #sel = Selection_axial()
    index = self.list_files.index(self.fileName)
    with open(str(open_files), "r") as reader, open(file_path_name, "w") as writer:   
          verification = self.initial_verification[index],self.end_verification[index]     
          writer.writelines(line for line in reader if self.check_line(line,hour.replace("_", ":"),verification))
    print ("TIME TOTAL")
    print (self.time_total)
    print (self.difference)
    #self.time_total = sel.time_total

          #writer.writelines(line for line in reader if sel.check_z_motion(self,line))
          



if __name__ == "__main__":
    #_input_path,_output_path,target_current = _parse_args()
    main()
