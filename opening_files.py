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
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
import matplotlib.pyplot as plt
#import saving_files_summary
#import saving_files_summary_list
#import plotting_summary_files_one_target
import numpy as np
import os
import tfs
import python_analysis_dataframe_20200416
from datetime import datetime

def file_folder_opening(self):
    #options = QFileDialog.Options()
    #options |= QFileDialog.DontUseNativeDialog
    #self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', '/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Visitas_Airo/', QFileDialog.ShowDirsOnly)
    [self.rotor_control_app_path_output,self.gimbal_control_app_path_output,self.pendant_control_app_path_output,self.system_control_app_path_output] = python_analysis_dataframe_20200416.writing_files(self,self.dir_)
    # NOW ITS OPENING THE FILES HAVE BEEN JUST WRITTEN
    self.logfile_rotor = open(self.rotor_control_app_path_output,'r') 
    self.logfile_gimbal = open(self.gimbal_control_app_path_output,'r') 
    self.logfile_system = open(self.system_control_app_path_output,'r') 
    self.logfile_pendant = open(self.pendant_control_app_path_output,'r') 
    #SCAN, HOUR AND DAY RECORDED EACH DAY
    self.df_scans_rotor = python_analysis_dataframe_20200416.selecting_entries(self.logfile_rotor,"ROTOR") 
    self.df_scans_gimbal = python_analysis_dataframe_20200416.selecting_entries(self.logfile_gimbal,"GIMBAL") 
    self.df_scans_system = python_analysis_dataframe_20200416.selecting_entries(self.logfile_system,"SYSTEM") 
    self.df_scans_pendant = python_analysis_dataframe_20200416.selecting_entries(self.logfile_pendant,"PENDANT") 
    self.data_df_all_subsystems = (pd.concat([self.df_scans_rotor,self.df_scans_gimbal,self.df_scans_system,self.df_scans_pendant], axis=1, sort=False))
    open_files = ["RotorControlApp.log","GimbalControlApp.log","SystemManagerApp.log","PendantUIApp.log"]
    #column_names  = ["DAY_ROTOR","HOUR_ROTOR","SCAN_ROTOR"]
    column_names = ["DAY_GIMBAL","HOUR_GIMBAL","SCAN_GIMBAL"]
    hours = (getattr(self.df_scans_gimbal,column_names[1])).dropna()
    scans = (getattr(self.df_scans_gimbal,column_names[2])).dropna()
    days = (getattr(self.df_scans_gimbal,column_names[0])).dropna()
    print ("SCANS")
    print (scans)
    scan_type = ["ScoutScan","AxialScan","HelicalScan","WarmupScan","GainCal","QCAxialFullScan","QCFullScan","QCDailyScan","QCAxialDailyScan","EStopTest"]
    print (self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == "GainCal"])
    for i in range(len(scan_type)):
        print (scan_type[i])
        self.total_scans[i] = (len(self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == scan_type[i]]))
        print (len(self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == scan_type[i]]))
    for i in range (len(hours)):
       self.tablefiles_tab2.setItem(self.current_row_files,0, QTableWidgetItem(str(days.iloc[i])))
       self.tablefiles_tab2.setItem(self.current_row_files,1, QTableWidgetItem(str(hours.iloc[i])))
       self.tablefiles_tab2.setItem(self.current_row_files,2, QTableWidgetItem(str(scans.iloc[i])))
       self.current_row_files +=1 
    print (self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == "QCAxialFullScan"])
    print (self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == "QCAxialDailyScan"])
    print (self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == "QCFullScan"])
    print (self.df_scans_gimbal[self.df_scans_gimbal.SCAN_GIMBAL == "QCDailyScan"])
    self.textbox_initial_date_value.setPlainText(str(self.df_scans_gimbal.DAY_GIMBAL.loc[0]))
    self.textbox_final_date_value.setPlainText(str(self.df_scans_gimbal.DAY_GIMBAL.iloc[-1]))
    self.textbox_total_axial_value.setPlainText(str(self.total_scans[1]))
    self.textbox_total_helical_value.setPlainText(str(self.total_scans[2]))
    self.textbox_gain_cal_value.setPlainText(str(self.total_scans[4]))
    self.textbox_total_socut_value.setPlainText(str(self.total_scans[0]))
    self.textbox_emergency_value.setPlainText(str(self.total_scans[9]))
    self.textbox_total_wu_value.setPlainText(str(self.total_scans[3]))
    self.textbox_total_axial_qc_full_value.setPlainText(str(self.total_scans[5]))
    self.textbox_total_helical_qc_full_value.setPlainText(str(self.total_scans[6]))
    self.textbox_total_axial_qc_daily_value.setPlainText(str(self.total_scans[8]))
    self.textbox_helical_qc_daily_value.setPlainText(str(self.total_scans[7]))
    print (str(len(self.dates_df.HELICALDAILYQC.drop_duplicates()[self.dates_df.HELICALDAILYQC.drop_duplicates() >= self.df_scans_gimbal.DAY_GIMBAL.loc[0]])))
    self.textbox_total_axial_qc_full_s_value.setPlainText(str(len(self.dates_df.AXIALFULLQC.drop_duplicates()[self.dates_df.AXIALFULLQC.drop_duplicates() >= self.df_scans_gimbal.DAY_GIMBAL.loc[0]])))
    self.textbox_total_helical_qc_full_s_value.setPlainText(str(len(self.dates_df.HELICALFULLQC.drop_duplicates()[self.dates_df.HELICALFULLQC.drop_duplicates() >= self.df_scans_gimbal.DAY_GIMBAL.loc[0]])))
    #self.textbox_total_axial_qc_daily_s_value.setPlainText(str(len(self.dates_df.AXIALDAILYQC.drop_duplicates()[self.dates_df.AXIALDAILYQC.drop_duplicates() >= self.df_scans_gimbal.DAY_GIMBAL.loc[0]])))
    self.textbox_total_gain_cal_fail_value.setPlainText(str(len(self.dates_gaincal.GAINCALFAIL.drop_duplicates()[self.dates_gaincal.GAINCALFAIL.drop_duplicates() >= self.df_scans_gimbal.DAY_GIMBAL.loc[0]])))
    print ("REASONS")
    print (self.total_reasons)
    self.textbox_reasos_gain_cal_fail.setPlainText(self.total_reasons)
    print ("DATAFRAMEEEEEEEEEEE")
    print (self.dates_df.drop_duplicates())
    print ("DAILY HELICAL SUCCESFUL")
    print (self.dates_df.HELICALFULLQC.drop_duplicates())
    print (len(self.dates_df.HELICALFULLQC.drop_duplicates()))
    print ("INITIAL DATE")
    print (self.df_scans_gimbal.DAY_GIMBAL.loc[0])
    print ("GAINCAL")
    print (self.dates_gaincal)
    #print (datetime.strptime(self.df_scans_gimbal.DAY_GIMBAL.loc[0],'%Y-%m-%d'))
    #print (self.dates_df.HELICALDAILYQC.drop_duplicates().iloc[0])
    print (self.dates_df.HELICALDAILYQC.drop_duplicates() < self.df_scans_gimbal.DAY_GIMBAL.loc[0])
    print ("QC SCANS PERFORMED AFTER THE INITIAL DAY")
    print (self.dates_df.HELICALFULLQC.drop_duplicates()[self.dates_df.HELICALFULLQC.drop_duplicates() > self.df_scans_gimbal.DAY_GIMBAL.loc[0]])
    
def classify_display_file(self,file_to_display):
    if "ROTOR" in self.file_to_display:
        self.file_to_display_rotor = file_to_display
    elif "GIMBAL" in self.file_to_display:
        self.file_to_display_gimbal = file_to_display
    elif "SYSTEM" in self.file_to_display:
        self.file_to_display_system = file_to_display
    elif "PENDANT" in self.file_to_display:
        self.file_to_display_pendant = file_to_display


def file_output_filtering(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
    column_file_names = "FILE_NAME_" + str(self.logfile_type) 
    column_day = "DAY_" + str(self.logfile_type)
    scan_day = "SCAN_" + str(self.logfile_type)
    hour_day = "HOUR_" + str(self.logfile_type)
    column_names  = [scan_day,column_day,hour_day,column_file_names]
    #checking_values = []
    #date_values = list((getattr(self.data_df_all_subsystems,column_day)))
    date_format = "%Y-%m-%d"
    date_stamp = datetime.strptime(self.day_selected,date_format).date()
    condition_1 = (getattr(self.data_df_all_subsystems,column_day) == date_stamp) 
    condition_2 = (getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected) 
    condition_3 = (getattr(self.data_df_all_subsystems,hour_day).str.contains(self.hour_selected[0:4]))
    self.index_scan = np.array((self.data_df_all_subsystems[condition_1 & condition_2 & condition_3].index))[0]
    #self.index_scan = index_alternative[0]
    python_analysis_dataframe_20200416.generate_output_file(self,"/Users/javia/OneDrive/Escritorio/AIROs/output de lo de Ana",column_names )
    print (self.index_scan)
    name = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[self.index_scan]
    #name_2 = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[1]]
    self.file_to_display = (os.path.join(self.output_path,name))
    classify_display_file(self,self.file_to_display)
    file = open(str(self.file_to_display), "r")
    return file


def filter_general_file(self,file_summary,notebook,filters):
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[0],filters[0])
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[1],filters[1])      
        file_scan = open(str(file_summary[0]), "r")
        file_best = open(str(file_summary[1]), "r")
        print ("file_scan")
        print (file_summary[0])
        print ("file_best")
        print (file_summary[1])
        print (notebook[0])
        with file_scan:
            text_scan = file_scan.read()
            notebook[0].setText(text_scan)
        with file_best:
            text_best = file_best.read()
            notebook[1].setText(text_best)

def filter_rotor_speed(self,path_motion):
        file_motion = open(str(path_motion), "r")
        with file_motion:
            text_motion = (file_motion.readlines())
            speed_values_1 = []
            speed_values_2 = []
            for line in (text_motion):
                speed_values_1.append(float(line.split()[5][:-1]))
                speed_values_2.append(line.split()[-1])

def checking_functions(self,columns,selection):
        if len(getattr(self.data_df_all_subsystems,columns[0]).dropna()) != 0:
           condition_day = getattr(self.data_df_all_subsystems,columns[1]) == columns[3]
           condition_hour = getattr(self.data_df_all_subsystems,columns[0]).str.contains(selection[0][0:4]) 
           condition_rotor = getattr(self.data_df_all_subsystems,columns[2]).str.contains(selection[1])
           index_hour = getattr(self.data_df_all_subsystems,columns[0])[(condition_day) & (condition_hour) & (condition_rotor)]
        else:
           index_hour = []
        return index_hour

def main():
    print ("HOLA")

if __name__ == "__main__":
    #_input_path,_output_path,target_current = _parse_args()
    main()