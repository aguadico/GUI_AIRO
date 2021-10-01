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
import matplotlib.pyplot as plt
import numpy as np
import os
import tfs
import sys
import python_analysis_dataframe_20200416
import opening_files 
import searches
import datetime
from datetime import timedelta
import datetime


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
        opening_files.file_folder_opening(self)


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

    def file_output(self):
        file_first_window = opening_files.file_output_filtering(self)
        with file_first_window:
            text = file_first_window.read()
            self.textEdit_files.setText(text)

    def file_output_second(self):
        file_second_window = opening_files.file_output_filtering(self)
        with file_second_window:
            text = file_second_window.read()
            self.textEdit_files_2.setText(text)
        
    def filter_output_scan_rotor(self):
        rotor_control_app_path_scan = os.path.join(self.output_path,"motion_rotor_scan")
        rotor_control_app_path_best = os.path.join(self.output_path,"motion_rotor_best")
        #rotor_control_motion = os.path.join(self.output_path,"motion_rotor_summary")
        file_summary =  [rotor_control_app_path_scan,rotor_control_app_path_best,self.file_to_display_rotor]
        notebooks = [self.textEdit_files_selection_rotor,self.textEdit_files_selection_2_rotor]  
        filters = [searches.ROTOR_SCAN,searches.ROTOR_BEST]    
        opening_files.filter_general_file(self,file_summary,notebooks,filters)
        #opening_files.filter_rotor_speed(self,rotor_control_motion)
        
    def filter_output_scan_gimbal(self):
        rotor_gimbal_app_path_scan = os.path.join(self.output_path,"motion_gimbal_scan")
        rotor_gimbal_app_path_best = os.path.join(self.output_path,"motion_gimbal_best")
        file_summary = [rotor_gimbal_app_path_scan,rotor_gimbal_app_path_best,self.file_to_display_gimbal]
        notebooks = [self.textEdit_files_selection_gimbal,self.textEdit_files_selection_2_gimbal]
        filters = [searches.GIMBAL_SCAN,searches.GIMBAL_BEST]
        opening_files.filter_general_file(self,file_summary,notebooks,filters)


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
        df_day = (self.data_df_all_subsystems[self.data_df_all_subsystems["DAY_GIMBAL"] == date_stamp])
        df_day_scan = (df_day[df_day["SCAN_GIMBAL"] == self.scan_selected])
        self.df_day_scan_hour = (df_day_scan[df_day_scan["HOUR_GIMBAL"] == self.hour_selected])
        index_hour_rotor = ((df_day_scan.HOUR_ROTOR[df_day_scan["HOUR_GIMBAL"] == self.hour_selected]).dropna())
        condition_day = getattr(self.data_df_all_subsystems,"DAY_GIMBAL") == date_stamp
        condition_hour = getattr(self.data_df_all_subsystems,"HOUR_GIMBAL").str.contains(self.hour_selected[0:4]) 
        condition_rotor = getattr(self.data_df_all_subsystems,"SCAN_GIMBAL").str.contains(self.scan_selected)
        index_hour_rotor_all = self.data_df_all_subsystems.HOUR_ROTOR[(condition_day) & (condition_hour) & (condition_rotor)]
        self.index_hour_all = []
        self.len_index_hour_all = []
        for i in range(len(self.names_components)):
            day_column = "DAY_" + str(self.names_components[i])
            scan_column = "SCAN_" + str(self.names_components[i])
            hour_column = "HOUR_" + str(self.names_components[i])
            checking_functions = [hour_column,day_column,scan_column,date_stamp]
            selection = [self.hour_selected,self.scan_selected]
            index_hour_i = opening_files.checking_functions(self,checking_functions,selection)
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

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()
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
        self.tablefiles_tab2.setRowCount(400)
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
        self.pushButton_analyze_second = QtWidgets.QPushButton('Analyze on second screen', self.tab1)
        self.pushButton_analyze_second.setGeometry(QtCore.QRect(20, 530, 221, 30))
        self.pushButton_analyze.clicked.connect(self.analyze_selected_files)
        self.pushButton_analyze_second.clicked.connect(self.analyze_selected_files_second)
        self.selection_scan_tpye = self.tablefiles_tab2.selectionModel()
        self.selection_scan_tpye.selectionChanged.connect(self.handleSelectionChanged_scan)
        self.selection_logfile = self.tablestatistic_tab2.selectionModel()
        self.selection_logfile.selectionChanged.connect(self.handleSelectionChanged_component)

    def function_buttons(self,function_to_call,pushButton_analyze):
        pushButton_analyze.setGeometry(QtCore.QRect(20, 490, 221, 30))
        pushButton_analyze.clicked.connect(function_to_call)

    def general_layout(self,location,name,function_to_call):
        self.plot_central = Canvas_tab2(width=8, height=20, dpi=100, parent=location) 
        self.plot_central.setGeometry(QtCore.QRect(10, 10, 500, 500))
        if name == "Rotor":
            self.textEdit_files_selection_rotor = QtWidgets.QTextEdit(location)
            self.textEdit_files_selection_rotor.setGeometry(QtCore.QRect(520, 10, 350, 430))
            self.textEdit_files_selection_2_rotor = QtWidgets.QTextEdit(location)
            self.textEdit_files_selection_2_rotor.setGeometry(QtCore.QRect(880, 10, 350, 430)) 
            self.pushButton_analyze_rotor = QtWidgets.QPushButton('Summarize ' + name, location)
            self.function_buttons(function_to_call,self.pushButton_analyze_rotor)
        else:
            self.textEdit_files_selection_gimbal = QtWidgets.QTextEdit(location)
            self.textEdit_files_selection_gimbal.setGeometry(QtCore.QRect(520, 10, 350, 430))
            self.textEdit_files_selection_2_gimbal = QtWidgets.QTextEdit(location)
            self.textEdit_files_selection_2_gimbal.setGeometry(QtCore.QRect(880, 10, 350, 430)) 
            self.pushButton_analyze_gimbal = QtWidgets.QPushButton('Summarize ' + name, location)
            self.function_buttons(function_to_call,self.pushButton_analyze_gimbal)


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
        self.general_layout(self.tab2,"Rotor",self.filter_output_scan_rotor)
        # TAB 3
        self.general_layout(self.tab3,"Gimbal",self.filter_output_scan_gimbal)
        # TAB 4
        self.tab4_layout()
        self.show()
        # Add tabs to widget
        main_layout.addWidget(self.tabs)

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
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
