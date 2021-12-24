[2021-07-05T12:45:35.2415412Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=AxialScan
[2021-07-05T12:45:35.2425413Z Messaging Info] Handling Client Message: #i11 Prepared AxialScan
[2021-07-05T12:45:35.2445414Z Messaging Info] Handling Client Message: #a11 Prepared AxialScan
[2021-07-05T12:45:35.2445414Z Application Info] [DicomManager] New State: Active-Prepared
[2021-07-05T12:45:35.2465415Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:45:35.2465415Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:45:35.3025447Z Messaging Info] Handling Client Message: #&22 History/Generator <Scans><ScanReport><kV>120</kV><mA>155.46666</mA><Duration>11.52</Duration><TimeStamp>2021-07-05T10:24:07.9788679+02:00</TimeStamp></ScanReport><ScanReport><kV>120</kV><mA>155.46666</mA><Duration>11.52</Duration><TimeStamp>2021-07-05T14:45:34.2420708+02:00</TimeStamp></ScanReport></Scans>
[2021-07-05T12:45:35.3025447Z Application Info] ConfigStore.Set: History/Generator -> <Scans><ScanReport><kV>120</kV><mA>155.46666</mA><Duration>11.52</Duration><TimeStamp>2021-07-05T10:24:07.9788679+02:00</TimeStamp></ScanReport><ScanReport><kV>120</kV><mA>155.46666</mA><Duration>11.52</Duration><TimeStamp>2021-07-05T14:45:34.2420708+02:00</TimeStamp></ScanReport></Scans>
[2021-07-05T12:45:35.3915498Z Messaging Info] Handling Client Message: #&22 History/MaintenanceScans <Entries><KeysAndValues><Key>WarmUp</Key><Value>2021-07-05T08:24:07.9868683Z</Value></KeysAndValues><KeysAndValues><Key>EstopTest</Key><Value>2021-07-05T07:05:50.5146015Z</Value></KeysAndValues><KeysAndValues><Key>GainCal</Key><Value>2021-07-05T07:22:43.0588111Z</Value></KeysAndValues><KeysAndValues><Key>HelicalDailyQC</Key><Value>2021-04-14T10:12:36.1979696Z</Value></KeysAndValues><KeysAndValues><Key>HelicalFullQC</Key><Value>2021-03-12T15:53:33.0106000Z</Value></KeysAndValues><KeysAndValues><Key>AxialDailyQC</Key><Value>2021-04-14T10:17:34.0070033Z</Value></KeysAndValues><KeysAndValues><Key>AxialFullQC</Key><Value>2021-04-14T10:17:34.0070033Z</Value></KeysAndValues></Entries>
[2021-07-05T12:45:35.3915498Z Application Info] ConfigStore.Set: History/MaintenanceScans -> <Entries><KeysAndValues><Key>WarmUp</Key><Value>2021-07-05T08:24:07.9868683Z</Value></KeysAndValues><KeysAndValues><Key>EstopTest</Key><Value>2021-07-05T07:05:50.5146015Z</Value></KeysAndValues><KeysAndValues><Key>GainCal</Key><Value>2021-07-05T07:22:43.0588111Z</Value></KeysAndValues><KeysAndValues><Key>HelicalDailyQC</Key><Value>2021-04-14T10:12:36.1979696Z</Value></KeysAndValues><KeysAndValues><Key>HelicalFullQC</Key><Value>2021-03-12T15:53:33.0106000Z</Value></KeysAndValues><KeysAndValues><Key>AxialDailyQC</Key><Value>2021-04-14T10:17:34.0070033Z</Value></KeysAndValues><KeysAndValues><Key>AxialFullQC</Key><Value>2021-04-14T10:17:34.0070033Z</Value></KeysAndValues></Entries>
[2021-07-05T12:45:35.8145740Z Messaging Info] Handling Client Message: $s00 Configured Transitioning AxialScan 25429032 0 1 0
[2021-07-05T12:45:35.8155740Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:35.8155740Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:35.9935842Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:37.8416899Z Messaging Info] Handling Client Message: $s00 Configured Transitioning AxialScan 25429032 0 1 0
[2021-07-05T12:45:37.8456902Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:37.8456902Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:38.0146998Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:39.8698059Z Messaging Info] Handling Client Message: $s00 Configured Transitioning AxialScan 25429032 0 1 0
[2021-07-05T12:45:39.8708060Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:39.8708060Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:40.0508163Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:41.5008992Z Messaging Info] Handling Client Message: $s00 Prepared OK AxialScan 25429032 0 1 0
[2021-07-05T12:45:41.5098997Z Application Info] UIClientQueueManager Requesting State=Completed, Mode=AxialScan
[2021-07-05T12:45:41.5118998Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:41.5118998Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:41.5128999Z Messaging Info] Handling Client Message: #i11 Completed AxialScan
[2021-07-05T12:45:41.5139000Z Messaging Info] Handling Client Message: #a11 Completed AxialScan
[2021-07-05T12:45:41.5139000Z Application Info] [DicomManager] New State: Active-Executing
[2021-07-05T12:45:41.5139000Z Application Info] [DicomManager] New State: Active-Completed
[2021-07-05T12:45:41.5149000Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:45:41.5149000Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:45:42.3239463Z Messaging Info] Handling Client Message: $s00 Executing OK AxialScan 25429032 0 1 0
[2021-07-05T12:45:42.3259464Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:42.3259464Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:42.3259464Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:42.3669488Z Application Info] UI: StateMachine: State: Verify3DScan
[2021-07-05T12:45:42.3669488Z Application Info] Previous Entry Repeats 1 Time(s)
[2021-07-05T12:45:42.5259579Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:42.5269579Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:42.5269579Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:44.2820583Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:44.5530738Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:44.5560740Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:44.5560740Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:46.3851786Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:46.6041911Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:46.6051912Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:46.6051912Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:48.4932992Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:48.6223065Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:48.6253067Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:48.6253067Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:50.5974195Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:50.6524227Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:50.6734239Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:50.6734239Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:52.6935394Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:52.7225411Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:52.7225411Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:52.7235411Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:54.7946596Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:54.8196610Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:54.8196610Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:54.8206611Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:56.4447540Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 8651816 0 31 0
[2021-07-05T12:45:56.4597548Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:56.4597548Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:56.8697783Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:56.8777787Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:56.8777787Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:56.9187811Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:45:58.9718985Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:45:58.9728986Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:45:58.9728986Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:45:59.0229014Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:00.9970143Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:00.9980144Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:00.9980144Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:01.1340222Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:03.0251303Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:03.0281305Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:03.0281305Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:03.2341423Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:05.1052493Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:05.1252505Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:05.1252505Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:05.3402628Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:07.1633670Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:07.1703674Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:07.1703674Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:07.4483833Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:09.1984834Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:09.2214847Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:09.2214847Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:09.5565039Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:11.2636015Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:11.2756022Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:11.2756022Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:11.6626244Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:13.3227193Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:13.3267196Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:13.3267196Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:13.7797455Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:15.3538355Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:15.3858373Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:15.3858373Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:15.9008668Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:17.4419549Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:17.4719566Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:17.4719566Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:18.1739968Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:19.4940723Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:19.5200738Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:19.5200738Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:20.2011127Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:21.5421895Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:21.5711911Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:21.5711911Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:22.2352291Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:23.5993071Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:23.6313089Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:23.6313089Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:24.3433497Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:25.1203941Z Messaging Info] Handling Client Message: #&22 History/RotorPC/LastKnownOnTime 2021-07-05T12:46:24.0609203Z
[2021-07-05T12:46:25.1203941Z Application Info] ConfigStore.Set: History/RotorPC/LastKnownOnTime -> 2021-07-05T12:46:24.0609203Z
[2021-07-05T12:46:25.1553961Z Messaging Info] Handling Client Message: #&22 History/RotorPC/DetectorOnTimeSeconds 21145.9221473
[2021-07-05T12:46:25.1553961Z Application Info] ConfigStore.Set: History/RotorPC/DetectorOnTimeSeconds -> 21145.9221473
[2021-07-05T12:46:25.6624251Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:25.6934269Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:25.6934269Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:25.8944384Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 8651816 0 31 0
[2021-07-05T12:46:25.8954384Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:25.8954384Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:26.4494701Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:26.9094964Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:26.9144967Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:26.9144967Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:28.7536019Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:28.9306120Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:28.9326122Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:28.9326122Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:30.8427214Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:30.9777291Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:30.9787292Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:30.9787292Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:32.8848382Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:33.0038450Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:33.0068452Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:33.0068452Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:34.8929531Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:35.0359613Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:35.0369613Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:35.0369613Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:36.9770723Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:37.0990793Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:37.1000793Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:37.1000793Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:39.0951934Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:39.1261952Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:39.1291954Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:39.1291954Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:41.1703121Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:41.2023139Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:41.2023139Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:41.2023139Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:43.2684321Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:43.2724323Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:43.2724323Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:43.4444422Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:45.3065487Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:45.3205495Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:45.3205495Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:45.4025542Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:47.3516657Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:47.3836675Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:47.3836675Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:47.5086746Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:49.4087833Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:49.4407852Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:49.4407852Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:49.6137951Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:51.4699012Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:51.4999029Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:51.4999029Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:51.7199155Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:53.5250188Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:53.5580207Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:53.5580207Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:53.8260360Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:55.5861367Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:55.5891368Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:55.5891368Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:55.9331565Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:57.6132526Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:57.6202530Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:57.6202530Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:46:58.1872854Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:46:59.6683701Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:46:59.6793708Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:46:59.6803708Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:00.1453974Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:01.7114870Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:47:01.7454889Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:01.7454889Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:02.2515179Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:03.7826055Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 25429032 0 31 0
[2021-07-05T12:47:03.8126072Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:03.8126072Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:04.0266194Z Messaging Info] Handling Client Message: $s00 Executing Transitioning AxialScan 8651816 0 31 0
[2021-07-05T12:47:04.0606214Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:04.0606214Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:04.2476321Z Application Info] UI: StateMachine: Fire: Verify3DScan:BackPressed
[2021-07-05T12:47:04.2496322Z Application Info] UI: StateMachine: Fire: VerifyDoseNotificationDLP:BackPressed
[2021-07-05T12:47:04.2496322Z Application Info] UI: StateMachine: Fire: WaitForXRaySummary:BackPressed
[2021-07-05T12:47:04.2506322Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:04.2506322Z Application Info] UIClientQueueManager Requesting State=Configured, Mode=AxialScan
[2021-07-05T12:47:04.2506322Z Application Info] UI: StateMachine: Fire: TubeCurrentSelection:BackPressed
[2021-07-05T12:47:04.2516323Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:04.2526323Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:04.2526323Z Application Info] [DicomManager] New State: Active-Executing
[2021-07-05T12:47:04.2526323Z Application Info] [DicomManager] New State: Active-Prepared
[2021-07-05T12:47:04.2526323Z Application Info] [DicomManager] New State: Active-Configured
[2021-07-05T12:47:04.2526323Z Application Info] [DicomManager] New State: Active-Started
[2021-07-05T12:47:04.2526323Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:04.2536324Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:04.2536324Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:04.2546325Z Messaging Info] Handling Client Message: #i11 Configured AxialScan
[2021-07-05T12:47:04.2566326Z Messaging Info] Handling Client Message: #a11 Configured AxialScan
[2021-07-05T12:47:04.2566326Z Application Info] [DicomManager] New State: Inactive-Started
[2021-07-05T12:47:04.2566326Z Application Info] [DicomManager] New State: Active-Configured
[2021-07-05T12:47:04.2576326Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:04.2576326Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:04.3886401Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:04.5106471Z Messaging Info] Handling Client Message: $s00 Executing OK Unknown 8651816 0 1 0
[2021-07-05T12:47:04.5116472Z Messaging Info] Handling Client Message: $ixd 59.3416266666667 1174.964208 1.2.826.0.1.3680043.9.1958.11.168.20210705102839.3884.1.393
[2021-07-05T12:47:04.5116472Z Application Info] #ixd received dose message: 1.2.826.0.1.3680043.9.1958.11.168.20210705102839.3884.1.393 59.341625213623 1174.96423339844
[2021-07-05T12:47:04.7836627Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:04.7836627Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:04.7836627Z Messaging Info] Handling Client Message: @c$sas 1
[2021-07-05T12:47:04.7836627Z Messaging Info] SystemCommanderBase received response = @c$sas 1
[2021-07-05T12:47:04.7836627Z Messaging Info] Handling Client Message: @J#igs
[2021-07-05T12:47:04.7846628Z Application Info] UI: StateMachine: Fire: MoveToRegistrationPosition:BackPressed
[2021-07-05T12:47:04.7856628Z Messaging Info] Handling Client Message: $s00 Started Waiting Unknown 8651816 0 1 0
[2021-07-05T12:47:04.7876630Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:04.7886630Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:05.2586899Z Application Info] UI: StateMachine: Fire: MoveToStartPosition3D:BackPressed
[2021-07-05T12:47:05.2586899Z Application Info] UI: Page: Switch: SetStartEnd3DScanPage
[2021-07-05T12:47:05.2606900Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2616901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2616901Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2616901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2616901Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2616901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2616901Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2616901Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2616901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2616901Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2626901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2626901Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:05.2626901Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:05.2626901Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2626901Z Application Info] [DicomManager] New State: Active-Started
[2021-07-05T12:47:05.2626901Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2636902Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2636902Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2656903Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2666903Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2666903Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2666903Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2666903Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2676904Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2696905Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2696905Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2696905Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2696905Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2706906Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2716906Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2726907Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2726907Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2726907Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2736907Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2746908Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2746908Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2756909Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2756909Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2756909Z Messaging Info] Handling Client Message: $s00 Started Waiting AxialScan 8651816 0 1 0
[2021-07-05T12:47:05.2776910Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:05.2796911Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:05.2796911Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:05.2806912Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:05.2806912Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:05.2896917Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:05.2896917Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:05.4427004Z Application Info] UI: StateMachine: Fire: MoveToEndPosition3D:BackPressed
[2021-07-05T12:47:05.4447005Z Application Info] UI: Page: Switch: ExamRegionPage
[2021-07-05T12:47:05.4507009Z Application Error] TransitionControl did not transfer: ( PendantUIApp.SetStartEnd3DScanPage -> PendantUIApp.ExamRegionPage )
[2021-07-05T12:47:05.4507009Z Application Info] UI: StateMachine: State: ScoutScan
[2021-07-05T12:47:05.4507009Z Messaging Info] Handling Client Message: @c$s1x 1
[2021-07-05T12:47:05.4507009Z Messaging Info] SystemCommanderBase received response = @c$s1x 1
[2021-07-05T12:47:05.4767024Z Messaging Info] Handling Client Message: $s00 Started Waiting Unknown 8651816 0 1 0
[2021-07-05T12:47:05.4777024Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:05.4777024Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:05.6777139Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 1 0
[2021-07-05T12:47:05.6837142Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:05.6837142Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:05.8807255Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:05.8817255Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:05.8817255Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:06.4857601Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:07.1437977Z Messaging Info] Handling Client Message: @J#ixr
[2021-07-05T12:47:07.1437977Z Application Info] [#ixr] Received 1 X-Ray Summaries:
[2021-07-05T12:47:07.1467979Z Messaging Info] Handling Client Message: @K#igt
[2021-07-05T12:47:07.9208422Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:07.9278426Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:07.9308427Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:08.5688792Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:09.9619589Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:09.9759597Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:09.9759597Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:10.2029727Z Messaging Info] Handling Client Message: @K#idc
[2021-07-05T12:47:10.3079787Z Messaging Info] Handling Client Message: @K$gvg 120
[2021-07-05T12:47:10.3329801Z Messaging Info] Handling Client Message: @K$gig 155.5
[2021-07-05T12:47:10.3829830Z Messaging Info] Handling Client Message: @K#isv
[2021-07-05T12:47:10.3829830Z Application Info] [#isv] Received Scan Verification:
[2021-07-05T12:47:10.8760112Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:11.5770513Z Application Info] UI: StateMachine: Fire: ScoutScan:NextPressed
[2021-07-05T12:47:11.8210652Z Application Info] UI: Page: Switch: SetStartEnd3DScanPage
[2021-07-05T12:47:11.8230654Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:11.8230654Z Application Info] UI: StateMachine: State: MoveToEndPosition3D
[2021-07-05T12:47:11.8230654Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:11.8240654Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:11.8240654Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:11.8250655Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:11.8250655Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:11.9990754Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:12.0010755Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:12.0010755Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:12.9551301Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:14.0171908Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:14.0361919Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:14.0361919Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:14.9642450Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:16.0643079Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651816 0 7 0
[2021-07-05T12:47:16.0843091Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:16.0843091Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:17.0183625Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:17.6093963Z Messaging Info] Handling Client Message: @c$sln 1
[2021-07-05T12:47:17.6093963Z Messaging Info] SystemCommanderBase received response = @c$sln 1
[2021-07-05T12:47:17.9014130Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651800 0 7 0
[2021-07-05T12:47:17.9024131Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:17.9024131Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:19.3164940Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:19.9455299Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651800 0 7 0
[2021-07-05T12:47:19.9645310Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:19.9645310Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:21.4336150Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:21.9896468Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651800 0 7 0
[2021-07-05T12:47:21.9916470Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:21.9916470Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:23.5297349Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:24.0177628Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651800 0 7 0
[2021-07-05T12:47:24.0187629Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:24.0187629Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:25.4698459Z Messaging Info] Handling Client Message: #&22 History/RotorPC/LastKnownOnTime 2021-07-05T12:47:24.4023716Z
[2021-07-05T12:47:25.4698459Z Application Info] ConfigStore.Set: History/RotorPC/LastKnownOnTime -> 2021-07-05T12:47:24.4023716Z
[2021-07-05T12:47:25.5018477Z Messaging Info] Handling Client Message: #&22 History/RotorPC/DetectorOnTimeSeconds 21206.2635986
[2021-07-05T12:47:25.5018477Z Application Info] ConfigStore.Set: History/RotorPC/DetectorOnTimeSeconds -> 21206.2635986
[2021-07-05T12:47:25.5068480Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:26.0648799Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8651800 0 7 0
[2021-07-05T12:47:26.0688802Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:26.0688802Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:26.6829153Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:26.7029164Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:26.7029164Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:27.6829725Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:28.7310324Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:28.7350327Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:28.7350327Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:29.6900873Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:30.7601485Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8389656 0 7 0
[2021-07-05T12:47:30.7651488Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:30.7651488Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:31.1801725Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:31.1971735Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:31.1971735Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:31.9622172Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:33.2382902Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8389656 0 7 0
[2021-07-05T12:47:33.2582914Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:33.2582914Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:34.0943392Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:34.1453421Z Application Info] UI: StateMachine: Fire: MoveToEndPosition3D:NextPressed
[2021-07-05T12:47:34.1463422Z Messaging Info] Handling Client Message: @c$shc 1
[2021-07-05T12:47:34.1463422Z Messaging Info] SystemCommanderBase received response = @c$shc 1
[2021-07-05T12:47:34.1543426Z Messaging Info] Handling Client Message: @L#igs
[2021-07-05T12:47:34.1623431Z Messaging Info] Handling Client Message: @c$sra 1
[2021-07-05T12:47:34.1633431Z Messaging Info] SystemCommanderBase received response = @c$sra 1
[2021-07-05T12:47:34.1633431Z Messaging Info] Handling Client Message: @c$scm 1
[2021-07-05T12:47:34.1633431Z Messaging Info] SystemCommanderBase received response = @c$scm 1
[2021-07-05T12:47:34.1773439Z Messaging Info] Handling Client Message: @c$sse OK 25
[2021-07-05T12:47:34.1773439Z Messaging Info] SystemCommanderBase received response = @c$sse OK 25
[2021-07-05T12:47:34.1823442Z Application Info] UI: Page: Switch: PerformScanPage
[2021-07-05T12:47:34.1833443Z Application Info] UIClientQueueManager Requesting State=Prepared, Mode=Z
[2021-07-05T12:47:34.1833443Z Application Info] UI: StateMachine: State: MoveToStartPosition3D
[2021-07-05T12:47:34.1843443Z Messaging Info] Handling Client Message: #i11 Prepared Z
[2021-07-05T12:47:34.1863445Z Messaging Info] Handling Client Message: #a11 Prepared Z
[2021-07-05T12:47:34.1863445Z Application Info] [DicomManager] New State: Inactive-Prepared
[2021-07-05T12:47:34.1873445Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:34.1873445Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:35.2844073Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8389656 0 7 0
[2021-07-05T12:47:35.2904076Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:35.2904076Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:36.1964594Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:36.5054771Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:36.5104774Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:36.5104774Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:38.3205809Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:38.5345932Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:38.5365933Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:38.5365933Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:40.4087004Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:40.5767100Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:40.6097119Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:40.6097119Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:42.5138208Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:42.6528287Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:42.6678296Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:42.6678296Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:44.6189412Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:44.6939455Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 25166872 0 7 0
[2021-07-05T12:47:44.6949455Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:44.6949455Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:45.0949684Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8389656 0 7 0
[2021-07-05T12:47:45.1179697Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:45.1179697Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:46.5820535Z Application Info] UI: StateMachine: Fire: MoveToStartPosition3D:NextPressed
[2021-07-05T12:47:46.5950542Z Messaging Info] Handling Client Message: @c$sss OK 14
[2021-07-05T12:47:46.5950542Z Messaging Info] SystemCommanderBase received response = @c$sss OK 14
[2021-07-05T12:47:46.6170555Z Messaging Info] Handling Client Message: @c$sgp -111267 -524852
[2021-07-05T12:47:46.6170555Z Messaging Info] SystemCommanderBase received response = @c$sgp -111267 -524852
[2021-07-05T12:47:46.7200613Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:47.1710871Z Messaging Info] Handling Client Message: $s00 Prepared OK Z 8389656 0 7 0
[2021-07-05T12:47:47.1720872Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:47.1720872Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:48.6651726Z Messaging Info] Handling Client Message: @c$sas 0
[2021-07-05T12:47:48.6651726Z Messaging Info] SystemCommanderBase received response = @c$sas 0
[2021-07-05T12:47:48.6651726Z Application Info] UIClientQueueManager Requesting State=Completed, Mode=MoveToStart
[2021-07-05T12:47:48.6691728Z Application Info] UI: Page: Switch: PerformScanPage
[2021-07-05T12:47:48.6701729Z Messaging Info] Handling Client Message: #i11 Completed MoveToStart
[2021-07-05T12:47:48.6701729Z Messaging Info] Handling Client Message: #a11 Completed MoveToStart
[2021-07-05T12:47:48.6711729Z Application Info] [DicomManager] New State: Inactive-Completed
[2021-07-05T12:47:48.6711729Z Messaging Info] Handling Client Message: @c$s11 1
[2021-07-05T12:47:48.6711729Z Messaging Info] SystemCommanderBase received response = @c$s11 1
[2021-07-05T12:47:48.6711729Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:48.7961801Z Messaging Info] Handling Client Message: $s00 Configured Transitioning Unknown 8389656 0 7 0
[2021-07-05T12:47:48.7971802Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:48.7971802Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:49.1982031Z Messaging Info] Handling Client Message: $s00 Configured Transitioning MoveToStart 8389656 0 7 0
[2021-07-05T12:47:49.2002032Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:49.2002032Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:49.8022376Z Messaging Info] Handling Client Message: $s00 Configured Transitioning MoveToStart 8389656 0 1 0
[2021-07-05T12:47:49.8032377Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:49.8032377Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:50.2172614Z Messaging Info] Handling Client Message: $s00 Configured Transitioning MoveToStart 8389656 0 17 0
[2021-07-05T12:47:50.2192615Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:50.2192615Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:50.7572923Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:52.2463774Z Messaging Info] Handling Client Message: $s00 Configured Transitioning MoveToStart 8389656 0 17 0
[2021-07-05T12:47:52.2483775Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:52.2483775Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:53.0104211Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:53.4554466Z Messaging Info] Handling Client Message: $s00 Prepared Transitioning MoveToStart 8389656 0 17 0
[2021-07-05T12:47:53.4564466Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:53.4564466Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:53.5054494Z Messaging Info] Handling Client Message: @c$s1x 1
[2021-07-05T12:47:53.5054494Z Messaging Info] SystemCommanderBase received response = @c$s1x 1
[2021-07-05T12:47:53.5064495Z Application Info] UI: StateMachine: State: MoveToRegistrationPosition
[2021-07-05T12:47:55.0515379Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:55.5155644Z Messaging Info] Handling Client Message: $s00 Prepared Transitioning MoveToStart 8389656 0 17 0
[2021-07-05T12:47:55.5205647Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:55.5205647Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:57.2636644Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:57.5636816Z Messaging Info] Handling Client Message: $s00 Prepared Transitioning MoveToStart 8389656 0 17 0
[2021-07-05T12:47:57.5886830Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:57.5886830Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:47:59.1797740Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:47:59.6157989Z Messaging Info] Handling Client Message: $s00 Prepared Transitioning MoveToStart 25166872 0 17 0
[2021-07-05T12:47:59.6177991Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:47:59.6177991Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:48:01.3538984Z Messaging Info] Handling Client Message: $ghg 0
[2021-07-05T12:48:01.6519154Z Messaging Info] Handling Client Message: $s00 Prepared Transitioning MoveToStart 25166872 0 17 0
[2021-07-05T12:48:01.6579157Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:48:01.6579157Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:48:02.0699393Z Messaging Info] Handling Client Message: $s00 Prepared OK MoveToStart 25166872 0 5 0
[2021-07-05T12:48:02.0939407Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:48:02.0939407Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:48:02.3249539Z Messaging Info] Handling Client Message: $s00 Prepared OK MoveToStart 25429016 0 5 0
[2021-07-05T12:48:02.3489553Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:48:02.3489553Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40
[2021-07-05T12:48:02.7619789Z Messaging Info] Handling Client Message: $s00 Completed OK MoveToStart 25429016 0 5 0
[2021-07-05T12:48:02.7809800Z Application Info] UI: StateMachine: Fire: MoveToRegistrationPosition:MovedToRegistrationPosition
[2021-07-05T12:48:02.7809800Z Application Info] UIClientQueueManager Requesting State=Configured, Mode=AxialScan
[2021-07-05T12:48:02.7819800Z Application Info] UI: StateMachine: Fire: TubeCurrentSelection:NextPressed
[2021-07-05T12:48:02.7819800Z Application Info] UI: StateMachine: State: WaitForXRaySummary
[2021-07-05T12:48:02.7819800Z Application Info] Previous Entry Repeats 1 Time(s)
[2021-07-05T12:48:02.7859803Z Messaging Info] Handling Client Message: @c$sgm 0 40
[2021-07-05T12:48:02.7859803Z Messaging Info] SystemCommanderBase received response = @c$sgm 0 40