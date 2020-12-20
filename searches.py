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