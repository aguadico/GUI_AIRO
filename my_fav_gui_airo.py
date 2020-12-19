import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
import pandas as pd
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
import sys
sys.path.append("/Users/anagtv/Desktop/Visitas_Airo/File_analysis/")
import python_analysis_dataframe_20200416
import datetime
from datetime import timedelta
import datetime

ROTOR_SCAN = ["ReconstructionManager received scan protocol: ScanProtocol:","Category=","DICOMName=","#f11 Prepared","#r11 Prepared","FrameGrabber Started", "ReconstructionInitializer.FinalizeSetup setup marked bad pixel at row="
"XRaySummary is: kV:", "AirQualifyClass Loaded Current Scan","#n11 Completed","#xxm Y" ,"ReconstructionManager.TransitionStates: Starting FrameGrabber",
"ReconstructionManager.TransitionStates: FrameGrabber Started","New Status From X-Ray Control Board: Ymr","New Status From X-Ray Control Board: Ym","New Status From X-Ray Control Board: Yaw",
"New Status From X-Ray Control Board: Yxq","ScoutScanConsumer Finish method completed","New Status From X-Ray Control Board: YKY","New Mode From X-Ray Control Board: YT", "ReconstructionManager released frames"
"New Status From X-Ray Control Board: NN","New Status From X-Ray Control Board:","TubeCoolDownTimer Logged Scan:",
"New Mode From Power Control Board: DD", "New Mode From Power Control Board: XKX","New Mode From Power Control Board: XM","New Mode From Power Control Board: XM",
"New Mode From Power Control Board: ZZ","ReconstructionManager.TransitionStates","ReconstructionManager: transitioning to Completed","ReconstructionManager released frames","successfully completed","TubeCoolDownTimer Logged Scan"]
ROTOR_BEST = ["AirQualifyClass is unable to Load Candidate Scan","Too many bad detectors found!","Pleora Device Open Failed","NoGPUAvailable","ReconstructionInitializer.FullSetup failed","New Mode From X-Ray Control Board:",
"ReconstructionManager.TransitionStates:","Stopping Rotor Control Application","Starting Rotor Control Application","ConfigStore.Set: History/MaintenanceScans ->"]
ROTOR_MOTION = ["MotorController.LogRotorData"]
SYSTEM_SCAN = ["MQM message received: @D#s11 Prepared ","MQM send message: #*11 Prepared ","CsScriptEngine.RunScript, script=Prepare, args= ","-- Start PrepareFor","-- PrepareFor ","SystemManager.OnScriptCompleted SUCCESS","MQM message received: @D#s11 Completed ",
"MQM send message: #*11 Completed ","SystemStatusAgglomerator raising ReadyToScan event ","CsScriptEngine.RunScript, script=StartScan, args= ","SystemManager.OnScriptCompleted SUCCESS, id=G ","Component Status Changed: Address x | Completed | Transitioning | ","Component Status Changed: Address r | Completed | OK | ",
"Component Status Changed: Address x | Completed | Transitioning | ","Component Status Changed: Address x | Completed | Transitioning | ","Component Status Changed: Address x | Completed | OK | WarmupScan | ","CsScriptEngine.RunScript, script=CompleteScan",
"CompleteScan script dock LAN connected! ","MaintenanceManager recording ","Undocking","Moving","Accelerating","XRaying","ScanComplete","SystemManager.OnScriptCompleted SUCCESS"]
SYSTEM_BEST = ["MaintenanceManager recording WarmUp at","MaintenanceManager recording GainCal","MaintenanceManager recording EstopTest","MaintenanceManager recording QCSAB","MaintenanceManager recording QCSTB","ConfigStore.Set: Primary ->","ConfigStore.Set: User ->","ConfigStore.Set: System ->","ConfigStore.Set: History ->",
"MaintenanceManager recording WarmUp at","MaintenanceManager recording GainCal","MaintenanceManager recording EstopTest","MaintenanceManager recording QCSAB","MaintenanceManager recording QCSTB","System address n not registered with queue manager","System address x not registered with queue manager",
"System address g not registered with queue manager","System address r not registered with queue manager","System address f not registered with queue manager","PrepareForScan Script Failed","Error loading Config file",
"MIGimbal n","MIGimbal p","MIGimbal z","MIGimbal t", "MIRotor n", "MIRotor x", "MIRotor g", "MIRotor r","Script Failed"]
PENDANT_SCAN = ["UI: StateMachine: Fire"]
PENDANT_BEST =  ["Failed DB Integrity Check: DB Corruption Found","UI: StateMachine: Fire"]
GIMBAL_SCAN = ["Handling Client Message: #t11 Prepared","New Scan From Power Control Board: AA","New Scan From Power Control Board: DD","Handling Client Message: p11 Completed","New Scan From Power Control Board: XKX","New Scan From Power Control Board: XKS",
"New Scan From Power Control Board: XM","New Scan From Power Control Board: DD","New Scan From Power Control Board: ZZ"]
GIMBAL_BEST = []
SHUTDOWN_CODES =["FsI","FsN","FsP","FsB","FsW","FsF","FsK","FsZ"]
SHUTDOWN_CODES_MEANING = ["1st turn turning on after board is flashed",
"power to the control board failed unexpectedly",
"shutdown normally (Base: user power switch, Rotor: signal from Base)",
"battery error (Base only)",
"shutdown off automatically after timeout (Base only)",
"computer requested shutdown (currently Base only, but intend to add this to rotor to allow self-reboot)",
"timed out waiting for re-docking to complete", "timed out waiting for computer to acknowledge scan termination FsX – Rotor Control firmware fault"]



class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()

        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))
        self.current_row = 0
        self.current_row_folder = 0
        self.current_row_analysis = 0 
        self.current_row_files = 0
        self.current_row_logfiles = 0
        self.fileName = ""
        #self.rotor_control_app_path_output = os.path.join(self.dir_,"all_scans_rotor")
        zero_data = np.zeros(shape=(4,4))
        self.df_scans = pd.DataFrame(zero_data,columns=["SCAN_ROTOR","DAY_ROTOR","HOUR_ROTOR","FILE_NAME_ROTOR"])
        self.index_scan = 0
        self.logfile_type = "ROTOR"



        openFile = QAction('Open File', self)
        openFolder = QAction('Open Folder', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        openFolder.triggered.connect(self.file_folder)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(openFolder)

 
        self.setWindowTitle("AIRO logfile Analysis")

        self.fileMenu = QtWidgets.QMenu('&File', self)
        self.fileMenu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.fileMenu)
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.main_widget = QtWidgets.QWidget(self)
        self.plot_widget = QWidget(self.main_widget)
        self.plot_widget.setGeometry(250,180,500,600)
        

        l = QtWidgets.QVBoxLayout(self.main_widget)
        m = QtWidgets.QVBoxLayout(self.plot_widget)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.home(l)
        self.setMinimumSize(1000, 800)

       
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


    def file_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        python_analysis_dataframe_20200416.writing_files(file)
        self.tablefiles_tab2.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
        self.tablefiles_tab2.setItem(self.current_row,1, QTableWidgetItem(str(target_number)))
        self.current_row += 1
        self.datos = [self.tableWidget.item(0,0).text()]
        with file:
            text = file.read()
            self.textEdit2.setText(text)


    def file_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', '/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Visitas_Airo/', QFileDialog.ShowDirsOnly)
        [self.rotor_control_app_path_output,self.gimbal_control_app_path_output,self.pendant_control_app_path_output,self.system_control_app_path_output] = python_analysis_dataframe_20200416.writing_files(self.dir_)
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
        print ("ALL DATAFRAMES")
        print (self.data_df_all_subsystems)
        open_files = ["RotorControlApp.log","GimbalControlApp.log","SystemManagerApp.log","PendantUIApp.log"]
        column_names  = ["DAY_ROTOR","HOUR_ROTOR","SCAN_ROTOR"]
        hours = (getattr(self.df_scans_rotor,column_names[1])).dropna()
        scans = (getattr(self.df_scans_rotor,column_names[2])).dropna()
        days = (getattr(self.df_scans_rotor,column_names[0])).dropna()
        for i in range (len(hours)):
           self.tablefiles_tab2.setItem(self.current_row_files,0, QTableWidgetItem(str(days.iloc[i])))
           self.tablefiles_tab2.setItem(self.current_row_files,1, QTableWidgetItem(str(hours.iloc[i])))
           self.tablefiles_tab2.setItem(self.current_row_files,2, QTableWidgetItem(str(scans.iloc[i])))
           self.current_row_files +=1 


    def handleSelectionChanged_component(self, selected, deselected):
        index=(self.tablestatistic_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        if self.fileName == "SystemManagerApp.log":
           self.logfile_type = "SYSTEM"
        elif self.fileName == "RotorControlApp.log":
           self.logfile_type = "ROTOR"
        elif self.fileName == "PendantUIApp.log":
           self.logfile_type = "PENDANT"
        elif self.fileName == "GimbalControlApp.log":
           self.logfile_type = "GIMBAL"

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
        column_names  = [scan_day,column_day ,hour_day,column_file_names]
        checking_values = []
        #date_values = list((getattr(self.data_df_all_subsystems,column_day)))
        date_format = "%Y-%m-%d"
        date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
        condition_1 = (getattr(self.data_df_all_subsystems,column_day) == date_stamp) 
        condition_2 = (getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected) 
        condition_3 = (getattr(self.data_df_all_subsystems,hour_day).str.contains(self.hour_selected[0:4]))
        self.index_scan = np.array((self.data_df_all_subsystems[condition_1 & condition_2 & condition_3].index))[0]
        #self.index_scan = index_alternative[0]
        python_analysis_dataframe_20200416.generate_output_file(self,"/Users/anagtv/Desktop/Visitas_Airo/File_analysis",column_names )
        print (self.index_scan)
        name = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[self.index_scan]
        #name_2 = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[1]]
        self.file_to_display = (os.path.join(self.output_path,name))
        self.classify_display_file(self.file_to_display)
        file = open(str(self.file_to_display), "r")
        return file

    #def logfile_writing(self):
    #    with 
        
    def file_output(self):
        file_first_window = self.file_output_filtering()
        with file_first_window:
            text = file_first_window.read()
            self.textEdit_files.setText(text)

    def file_output_second(self):
        file_second_window = self.file_output_filtering()
        with file_second_window:
            text = file_second_window.read()
            self.textEdit_files_2.setText(text)

    def filter_general_file(self,file_summary,notebook,filters):
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[0],filters[0])
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[1],filters[1])      
        file_scan = open(str(file_summary[0]), "r")
        file_best = open(str(file_summary[1]), "r")
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

    def filter_output_scan_rotor(self):
        rotor_control_app_path_scan = os.path.join(self.output_path,"motion_rotor_scan")
        rotor_control_app_path_best = os.path.join(self.output_path,"motion_rotor_best")
        rotor_control_motion = os.path.join(self.output_path,"motion_rotor_summary")
        file_summary =  [rotor_control_app_path_scan,rotor_control_app_path_best,self.file_to_display_rotor]
        notebooks = [self.textEdit_files_selection_rotor,self.textEdit_files_selection_2_rotor]  
        filters = [ROTOR_SCAN,ROTOR_BEST]    
        self.filter_general_file(file_summary,notebooks,filters)
        self.filter_rotor_speed(rotor_control_motion)
        
    def filter_output_scan_gimbal(self):
        rotor_gimbal_app_path_scan = os.path.join(self.output_path,"motion_gimbal_scan")
        rotor_gimbal_app_path_best = os.path.join(self.output_path,"motion_gimbal_best")
        file_summary = [rotor_gimbal_app_path_scan,rotor_gimbal_app_path_best,self.file_to_display_gimbal]
        notebooks = [self.textEdit_files_selection_gimbal,self.textEdit_files_selection_2_gimbal]
        filters = [GIMBAL_SCAN,GIMBAL_BEST]
        self.filter_general_file(file_summary,notebooks,filters)
        
        #self.sc3.axes.errorbar(speed_values_1,yerr=0,"o",label= "SPEED ROTOR 1", picker=5)
        #self.sc3.axes.errorbar(speed_values_2,yerr=0,"o",label= "SPEED ROTOR 2", picker=5)
        #saving_files_summary_list.main(self,"/Users/anagtv/Desktop",0)

    def question_output(self,number):
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.show()
        if number == "1":
            self.question.buttonClicked.connect(self.file_output)
        else: 
            self.question.buttonClicked.connect(self.file_output_second)


    def analyze_selected_files(self,values):
        self.question_output("1")
        

    def analyze_selected_files_second(self,values):
        self.question_output("2")
        
    


    def set_analysis_output_file(self,values):
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)


    def set_output_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileanalysis_outputpath, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)

    def checking_functions(self,hour_column,day_column,scan_column,date_stamp,hour_selected,scan_selected):
        if len(getattr(self.data_df_all_subsystems,hour_column).dropna()) != 0:
           condition_day = getattr(self.data_df_all_subsystems,day_column) == date_stamp
           condition_hour = getattr(self.data_df_all_subsystems,hour_column).str.contains(self.hour_selected[0:4]) 
           condition_rotor = getattr(self.data_df_all_subsystems,scan_column).str.contains(self.scan_selected)
           index_hour = getattr(self.data_df_all_subsystems,hour_column)[(condition_day) & (condition_hour) & (condition_rotor)]
        else:
           index_hour = []
        return index_hour
  
    def handleSelectionChanged_scan(self, selected, deselected):
        self.indexs =(self.tablefiles_tab2.selectionModel().currentIndex())
        self.index_scan = self.indexs.row()
        self.day_selected = self.indexs.sibling(self.index_scan,0).data()
        self.hour_selected = self.indexs.sibling(self.index_scan,1).data()
        self.scan_selected = self.indexs.sibling(self.index_scan,2).data()
        date_format = "%Y-%m-%d"
        date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
        self.names_components = ["ROTOR","PENDANT","SYSTEM","GIMBAL"]
        self.columns_names_components = ["FILE_NAME_ROTOR","FILE_NAME_PENDANT","FILE_NAME_SYSTEM","FILE_NAME_GIMBAL"]
        #selection of the scan in the dataframen
        df_day = (self.data_df_all_subsystems[self.data_df_all_subsystems["DAY_ROTOR"] == date_stamp])
        df_day_scan = (df_day[df_day["SCAN_ROTOR"] == self.scan_selected])
        self.df_day_scan_hour = (df_day_scan[df_day_scan["HOUR_ROTOR"] == self.hour_selected])
        index_hour_rotor = ((df_day_scan.HOUR_ROTOR[df_day_scan["HOUR_ROTOR"] == self.hour_selected]).dropna())
        condition_day = getattr(self.data_df_all_subsystems,"DAY_ROTOR") == date_stamp
        condition_hour = getattr(self.data_df_all_subsystems,"HOUR_ROTOR").str.contains(self.hour_selected[0:4]) 
        condition_rotor = getattr(self.data_df_all_subsystems,"SCAN_ROTOR").str.contains(self.scan_selected)
        index_hour_rotor_all = self.data_df_all_subsystems.HOUR_ROTOR[(condition_day) & (condition_hour) & (condition_rotor)]
        self.index_hour_all = []
        self.len_index_hour_all = []
        for i in range(len(self.names_components)):
            day_column = "DAY_" + str(self.names_components[i])
            scan_column = "SCAN_" + str(self.names_components[i])
            hour_column = "HOUR_" + str(self.names_components[i])
            index_hour_i = self.checking_functions(hour_column,day_column,scan_column,date_stamp,self.hour_selected,self.scan_selected)
            len_index_i = len(index_hour_i)
            self.index_hour_all.append(index_hour_i)
            self.len_index_hour_all.append(len_index_i)
        # select index of 0 values 
        zero_index = [m for m, e in enumerate(self.len_index_hour_all) if e == 0]
        # select files not maximum
        self.open_files = ["RotorControlApp.log","PendantUIApp.log","SystemManagerApp.log","GimbalControlApp.log"]
        # Remove the files with 0 length
        for l in range(len(zero_index)): 
            self.index_hour_all.pop(zero_index[l]-l)
            self.names_components.pop(zero_index[l]-l)
            self.columns_names_components.pop(zero_index[l]-l)
            self.open_files.pop(zero_index[l]-l)
        for ind_logfile in self.open_files: 
           self.tablestatistic_tab2.setItem(self.current_row_logfiles,0, QTableWidgetItem(str(ind_logfile))) 
           self.current_row_logfiles += 1
        self.current_row_logfiles = 0

    def folder_analyze(self,values):
        print (self.lis_files_names)
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.location = "First"
        self.question.buttonClicked.connect(self.file_output(self.textEdit_files))
        self.question.show()

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget{background-color: %s}' % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def tab1_layout(self):
        self.widget_tab2 = QtWidgets.QWidget(self.tab1)
        self.widget_tab2.setGeometry(QtCore.QRect(20, 20, 280, 230))
        self.widget_tab2.setObjectName("widget")
        self.textEdit_files = QtWidgets.QTextEdit(self.tab1)
        self.textEdit_files.setGeometry(QtCore.QRect(340, 10, 450, 600))
        self.textEdit_files_2 = QtWidgets.QTextEdit(self.tab1)
        self.textEdit_files_2.setGeometry(QtCore.QRect(800, 10, 450, 600))


    def tab1_buttons(self):
        self.tablefiles_tab2 = QtWidgets.QTableWidget(self.tab1)
        self.tablefiles_tab2.setGeometry(QtCore.QRect(20, 10, 310, 350))
        self.tablefiles_tab2.setObjectName("tableWidget")
        self.tablefiles_tab2.setRowCount(100)
        self.tablefiles_tab2.setColumnCount(3)
        self.tablefiles_tab2.setHorizontalHeaderLabels(["Day","Hour","Scan"])
        self.tablestatistic_tab2 = QtWidgets.QTableWidget(self.tab1)
        self.tablestatistic_tab2.setGeometry(QtCore.QRect(20, 370, 221, 100))
        self.tablestatistic_tab2.setRowCount(5)
        self.tablestatistic_tab2.setColumnCount(1)
        self.tablestatistic_tab2.setHorizontalHeaderLabels(["Log Files"]) 
        self.tablestatistic_tab2.setObjectName("tableView")
        self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(1,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(2,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(3,0, QTableWidgetItem(str())) 

    def tab1_activities(self):
        self.pushButton_analyze = QtWidgets.QPushButton('Analyze', self.tab1)
        self.pushButton_analyze.setGeometry(QtCore.QRect(20, 490, 221, 30))
        #
        self.pushButton_analyze_second = QtWidgets.QPushButton('Analyze on second screen', self.tab1)
        self.pushButton_analyze_second.setGeometry(QtCore.QRect(20, 530, 221, 30))
        #
        self.pushButton_analyze.clicked.connect(self.analyze_selected_files)
        self.pushButton_analyze_second.clicked.connect(self.analyze_selected_files_second)
        #
        self.selection_scan_tpye = self.tablefiles_tab2.selectionModel()
        self.selection_scan_tpye.selectionChanged.connect(self.handleSelectionChanged_scan)
        self.selection_logfile = self.tablestatistic_tab2.selectionModel()
        self.selection_logfile.selectionChanged.connect(self.handleSelectionChanged_component)

    def tab2_layout(self):
        self.plot_central = Canvas_tab2(width=8, height=20, dpi=100, parent=self.tab2) 
        self.plot_central.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.textEdit_files_selection_rotor = QtWidgets.QTextEdit(self.tab2)
        self.textEdit_files_selection_rotor.setGeometry(QtCore.QRect(520, 10, 350, 430))
        self.textEdit_files_selection_2_rotor = QtWidgets.QTextEdit(self.tab2)
        self.textEdit_files_selection_2_rotor.setGeometry(QtCore.QRect(880, 10, 350, 430))
        self.pushButton_analyze_rotor = QtWidgets.QPushButton('Summarize Rotor', self.tab2)
        self.pushButton_analyze_rotor.setGeometry(QtCore.QRect(20, 490, 221, 30))
        self.pushButton_analyze_rotor.clicked.connect(self.filter_output_scan_rotor)

    def tab3_layout(self):
        self.plot_central = Canvas_tab2(width=8, height=20, dpi=100, parent=self.tab3) 
        self.plot_central.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.textEdit_files_selection_gimbal = QtWidgets.QTextEdit(self.tab3)
        self.textEdit_files_selection_gimbal.setGeometry(QtCore.QRect(520, 10, 350, 430))
        self.textEdit_files_selection_2_gimbal = QtWidgets.QTextEdit(self.tab3)
        self.textEdit_files_selection_2_gimbal.setGeometry(QtCore.QRect(880, 10, 350, 430))
        self.pushButton_analyze_gimbal = QtWidgets.QPushButton('Summarize Gimbal', self.tab3)
        self.pushButton_analyze_gimbal.setGeometry(QtCore.QRect(20, 490, 221, 30))
        self.pushButton_analyze_gimbal.clicked.connect(self.filter_output_scan_gimbal)

    def tab4_layout(self):
        self.label_best_pendant = QLabel("Best Search Pendant:",self.tab4)
        self.label_best_pendant.setGeometry(QtCore.QRect(10, 5, 200, 30))
        self.textEdit_files_selection_system = QtWidgets.QTextEdit(self.tab4)
        self.textEdit_files_selection_system.setGeometry(QtCore.QRect(10, 50, 400, 430))
        self.label_best_pendant = QLabel("Best Search System:",self.tab4)
        self.label_best_pendant.setGeometry(QtCore.QRect(450, 5, 200, 30))
        self.textEdit_files_selection_system = QtWidgets.QTextEdit(self.tab4)
        self.textEdit_files_selection_system.setGeometry(QtCore.QRect(450, 50, 400, 430))
        self.label_best_pendant = QLabel("Summary Scan Pendant:",self.tab4)
        self.label_best_pendant.setGeometry(QtCore.QRect(880, 5, 200, 30))
        self.textEdit_files_selection_2_system = QtWidgets.QTextEdit(self.tab4)
        self.textEdit_files_selection_2_system.setGeometry(QtCore.QRect(880, 50, 400, 430))
        self.pushButton_analyze = QtWidgets.QPushButton('Analyze', self.tab4)
        self.pushButton_analyze.setGeometry(QtCore.QRect(20, 490, 221, 30))

    def home(self, main_layout):
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()
        self.tabs.resize(300,200)
        # Add tabs
        self.tabs.addTab(self.tab1,"Overview")
        self.tabs.addTab(self.tab2,"Rotor")
        self.tabs.addTab(self.tab3,"Gimbal")
        self.tabs.addTab(self.tab4,"SystemManager/Pendant")
        self.tab2.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.main_layout)
        # TAB 1        
        self.tab1_layout()
        self.tab1_buttons()
        self.tab1_activities()
        # TAB 2 
        self.tab2_layout()
        # TAB 3
        self.tab3_layout()
        # TAB 4
        self.tab4_layout()
        self.show()
        # Add tabs to widget
        main_layout.addWidget(self.tabs)

    def Clear(self):
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.draw()
        self.axes_1.clear()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.ax.clear()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.ax.clear()
        self.ui.widget_4.canvas.draw()



class Canvas(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(3, sharex=True)
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes[0].tick_params(labelsize=10)
        self.axes[1].tick_params(labelsize=10)
        self.axes[2].tick_params(labelsize=10)
        plt.xticks(rotation=90)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

class Canvas_tab2(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(1, sharex=True,figsize=(width,height))
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes.tick_params(labelsize=10)
        plt.xticks(rotation=90)
        #self.axes[1].tick_params(labelsize=10)
        #self.axes[2].tick_params(labelsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
