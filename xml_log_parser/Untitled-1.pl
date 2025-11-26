[SYSTEM] {"fdrsVersion":"45.5.5","fdspServerURL":"https://www.fdspcl.dealerconnection.com","dependency":{"core":"11.10.5","comms":"33.13.1-hf","commsLibraries":"32.12.2-USA","commsRnd":"5.4.0-SNAPSHOT","complexTools":"45.5.14","dspDomain":"15.3.18","framework":"72.31.54","hmi":"73.13.13","otxCommon":"40.21.20"}}

2025-10-14T09:19:21,003 INFO otx.core.BaseApplication - Adding runtime logs appender to COMMS channel logger

2025-10-14T09:21:39,918 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.etis.runtime.apps.otx.utils.types.datatype.StructureVariable.getMapValue(StructureVariable.java:46) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at otxcontainer.G2056515.ParseFlashActionData(G2056515.java) [G2056515:?]
	at otxcontainer.G2056515.access$2600(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$16.run(G2056515.java:25237) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:39,928 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> null pointer =  java.lang.NullPointerException

2025-10-14T09:21:39,930 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> firstCondition is null, there are no HasAction conditions for this node

2025-10-14T09:21:39,933 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 

Flash Action DID = 8068
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H240-HL
assemblySoftware.softwareSize = 1994025
assemblySoftware.didValue (Decimal) = 32872
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F188
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H085-HL
assemblySoftware.softwareSize = 678033
assemblySoftware.didValue (Decimal) = 61832
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = D027
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H241-HL
assemblySoftware.softwareSize = 50860
assemblySoftware.didValue (Decimal) = 53287
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F121
assemblySoftware.type = STRATEGY
assemblySoftware.id = MU5T-14H090-BAZ
assemblySoftware.softwareSize = 48761810
assemblySoftware.didValue (Decimal) = 61729
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F120
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H090-AHL
assemblySoftware.softwareSize = 98168657
assemblySoftware.didValue (Decimal) = 61728
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type =

2025-10-14T09:21:39,974 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ParseFlashActionData

2025-10-14T09:21:39,976 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetFlashActionsProcess

2025-10-14T09:21:39,979 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ReMapFlashActionDataStructure

2025-10-14T09:21:39,982 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:39,984 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID: 8068

2025-10-14T09:21:39,985 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB

2025-10-14T09:21:39,987 INFO class otxcontainer.G2056515.authorLogs - bCANflashTYPE = false

2025-10-14T09:21:39,988 INFO class otxcontainer.G2056515.authorLogs - bCANflashDID = false

2025-10-14T09:21:39,990 INFO class otxcontainer.G2056515.authorLogs - bUSBflashDID = false

2025-10-14T09:21:39,991 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB for DID = 8068

2025-10-14T09:21:39,994 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:39,996 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:39,998 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID: F188

2025-10-14T09:21:40,000 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB

2025-10-14T09:21:40,001 INFO class otxcontainer.G2056515.authorLogs - bCANflashTYPE = false

2025-10-14T09:21:40,003 INFO class otxcontainer.G2056515.authorLogs - bCANflashDID = false

2025-10-14T09:21:40,004 INFO class otxcontainer.G2056515.authorLogs - bUSBflashDID = false

2025-10-14T09:21:40,006 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB for DID = F188

2025-10-14T09:21:40,009 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,011 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,014 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID: D027

2025-10-14T09:21:40,015 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB

2025-10-14T09:21:40,017 INFO class otxcontainer.G2056515.authorLogs - bCANflashTYPE = false

2025-10-14T09:21:40,018 INFO class otxcontainer.G2056515.authorLogs - bCANflashDID = false

2025-10-14T09:21:40,020 INFO class otxcontainer.G2056515.authorLogs - bUSBflashDID = false

2025-10-14T09:21:40,021 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB for DID = D027

2025-10-14T09:21:40,023 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,026 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,028 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID: F121

2025-10-14T09:21:40,035 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB

2025-10-14T09:21:40,037 INFO class otxcontainer.G2056515.authorLogs - bCANflashTYPE = false

2025-10-14T09:21:40,038 INFO class otxcontainer.G2056515.authorLogs - bCANflashDID = false

2025-10-14T09:21:40,040 INFO class otxcontainer.G2056515.authorLogs - bUSBflashDID = false

2025-10-14T09:21:40,042 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB for DID = F121

2025-10-14T09:21:40,044 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,046 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,049 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID: F120

2025-10-14T09:21:40,050 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB

2025-10-14T09:21:40,052 INFO class otxcontainer.G2056515.authorLogs - bCANflashTYPE = false

2025-10-14T09:21:40,053 INFO class otxcontainer.G2056515.authorLogs - bCANflashDID = false

2025-10-14T09:21:40,055 INFO class otxcontainer.G2056515.authorLogs - bUSBflashDID = false

2025-10-14T09:21:40,056 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> PNI = USB for DID = F120

2025-10-14T09:21:40,058 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetProgrammingNetworkInterface

2025-10-14T09:21:40,061 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Number of flash action parts= 5

2025-10-14T09:21:40,063 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ReMapFlashActionDataStructure

2025-10-14T09:21:40,065 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ParseAndCompareFlashActionApplications

2025-10-14T09:21:40,067 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash Action Applications count  = 0

2025-10-14T09:21:40,069 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> There are no Applications in the Flash Action List!

2025-10-14T09:21:40,072 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ParseAndCompareFlashActionApplications

2025-10-14T09:21:40,574 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetFlashActionContent

2025-10-14T09:21:40,577 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EndBargraph

2025-10-14T09:21:40,785 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:21:42,080 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EndBargraph

2025-10-14T09:21:42,083 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetFlashActionContentProcess

2025-10-14T09:21:42,087 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ SoftwareUpdateProcess

2025-10-14T09:21:42,091 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BargraphDisplayV2

2025-10-14T09:21:43,092 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProgramModule

2025-10-14T09:21:43,093 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ CheckSoftwareLevel

2025-10-14T09:21:43,095 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> About to check if all the files are already in the module

2025-10-14T09:21:43,098 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH

2025-10-14T09:21:43,101 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: CheckSoftwareLevel text: Handle exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: CheckSoftwareLevel text: Handle exception
	at otxcontainer.G2056515.CheckSoftwareLevel(G2056515.java:9195) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41188) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,110 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 SW on module is missing or not at latest level, FLASH!!

2025-10-14T09:21:43,113 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F188 Matches - No need to flash,  part number = SU5T-14H085-HL

2025-10-14T09:21:43,115 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> D027 Matches - No need to flash,  part number = SU5T-14H241-HL

2025-10-14T09:21:43,117 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F121 Matches - No need to flash,  part number = MU5T-14H090-BAZ

2025-10-14T09:21:43,120 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH

2025-10-14T09:21:43,123 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: CheckSoftwareLevel text: Handle exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: CheckSoftwareLevel text: Handle exception
	at otxcontainer.G2056515.CheckSoftwareLevel(G2056515.java:9195) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41188) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,134 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 SW on module is missing or not at latest level, FLASH!!

2025-10-14T09:21:43,137 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ CheckSoftwareLevel

2025-10-14T09:21:43,140 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ DownloadSoftwareBinaries

2025-10-14T09:21:43,143 INFO class otxcontainer.G2056515.authorLogs - ListGetLength(listOfFlashActionDIDs) = 5

2025-10-14T09:21:43,146 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bFlashALL = true

2025-10-14T09:21:43,149 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= 8068

2025-10-14T09:21:43,151 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H240-HL

2025-10-14T09:21:43,154 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 = SU5T-14H240-HL Software binary required - get ALL files

2025-10-14T09:21:43,157 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:21:43,159 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:21:43,162 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,293 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:21:43,296 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F188

2025-10-14T09:21:43,297 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H085-HL

2025-10-14T09:21:43,300 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F188 = SU5T-14H085-HL Software binary required - get ALL files

2025-10-14T09:21:43,302 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:21:43,304 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:21:43,305 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,499 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:21:43,501 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= D027

2025-10-14T09:21:43,503 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H241-HL

2025-10-14T09:21:43,504 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> D027 = SU5T-14H241-HL Software binary required - get ALL files

2025-10-14T09:21:43,507 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:21:43,510 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:21:43,511 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,642 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:21:43,644 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F121

2025-10-14T09:21:43,646 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = MU5T-14H090-BAZ

2025-10-14T09:21:43,648 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F121 = MU5T-14H090-BAZ Software binary required - get ALL files

2025-10-14T09:21:43,652 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:21:43,654 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:21:43,656 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,825 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:21:43,828 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F120

2025-10-14T09:21:43,831 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H090-AHL

2025-10-14T09:21:43,834 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 = SU5T-14H090-AHL Software binary required - get ALL files

2025-10-14T09:21:43,838 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:21:43,840 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:21:43,843 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:21:43,995 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:21:43,998 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ DownloadSoftwareBinaries

2025-10-14T09:21:44,001 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ DetermineProgrammingMethod

2025-10-14T09:21:44,003 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 is USB flashed

2025-10-14T09:21:44,006 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bfProgrammingMethod = 02

2025-10-14T09:21:44,010 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 is USB flashed

2025-10-14T09:21:44,013 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bfProgrammingMethod = 02

2025-10-14T09:21:44,016 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> No Applications to install

2025-10-14T09:21:44,019 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ DetermineProgrammingMethod

2025-10-14T09:21:44,022 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BatteryCheck

2025-10-14T09:21:44,057 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:21:45,114 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:21:45,116 DEBUG api.service.Channel - ISO15765 TX         -> 0,000,000,000 - [00,00,07,26,22,40,28]

2025-10-14T09:21:45,119 DEBUG api.service.Channel - ISO15765 TX         -> 0,231,010,064 - [00,00,07,26]

2025-10-14T09:21:45,127 DEBUG api.service.Channel - ISO15765 RX         <- 0,231,019,765 - [00,00,07,2E,62,40,28,64]

2025-10-14T09:21:45,127 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Battery State of Charge SOC (percent) = 100

2025-10-14T09:21:45,129 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Battery voltage = 12.933

2025-10-14T09:21:45,151 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BatteryCheck

2025-10-14T09:21:45,151 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:21:45,154 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Programming method (0-CAN, 1-USB, or 2-BOTH)? = 1

2025-10-14T09:21:45,157 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Programming method: USB

2025-10-14T09:21:45,159 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ UpdateSoftwareOverUSB

2025-10-14T09:21:45,161 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> g_ParsedFlashActionData.removeApplicationsList count =  0

2025-10-14T09:21:45,164 INFO class otxcontainer.G2056515.authorLogs - g_ParsedFlashActionData.removeApplicationsList count = 0

2025-10-14T09:21:45,168 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ SetApplicationState

2025-10-14T09:21:45,173 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Setting ApplicationState = APPLICATION_SKIPPED

2025-10-14T09:21:45,176 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ SetApplicationState

2025-10-14T09:21:45,179 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetFenixUSBPackage

2025-10-14T09:21:45,183 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File to flash over USB =  SU5T-14H240-HL

2025-10-14T09:21:45,187 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File to flash over USB =  SU5T-14H090-AHL

2025-10-14T09:21:45,191 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> addSoftware set to null

2025-10-14T09:21:45,202 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ getFenixData

2025-10-14T09:21:45,212 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> LOG FENIX REQUEST:

2025-10-14T09:21:45,215 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VIN = 1FBAX2YG0PKA54057

2025-10-14T09:21:45,218 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECG ESN = 1EH1BIQJ

2025-10-14T09:21:45,221 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECG Hardware = NU5T-14H026-EB

2025-10-14T09:21:45,224 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Requested node(0) = 754

2025-10-14T09:21:45,227 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Requested software part(0) =

2025-10-14T09:21:45,230 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Remove software part(0) = ""

2025-10-14T09:21:45,236 INFO fdsp.command.RequestFenixData - Requesting GetFenix for 1FBAX2YG0PKA54057

2025-10-14T09:21:49,419 INFO fdsp.command.RequestFenixData - GetFenix received for 1FBAX2YG0PKA54057

2025-10-14T09:21:49,424 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Execute FENIX_SERVICE GET_DATA - SUCCESS

2025-10-14T09:21:49,428 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ getFenixData

2025-10-14T09:21:49,431 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ outputFenixData

2025-10-14T09:21:49,432 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,441 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU CCPU bootchain images"}

2025-10-14T09:21:49,444 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H240-HL

2025-10-14T09:21:49,448 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:21:49,449 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf

2025-10-14T09:21:49,452 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H240-HL.VBF

2025-10-14T09:21:49,454 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: BOOT_IMAGE

2025-10-14T09:21:49,458 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 1994025

2025-10-14T09:21:49,460 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:21:49,462 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: 8068

2025-10-14T09:21:49,463 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,465 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU VMCU load"}

2025-10-14T09:21:49,467 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H085-HL

2025-10-14T09:21:49,469 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:21:49,470 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf

2025-10-14T09:21:49,474 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H085-HL.VBF

2025-10-14T09:21:49,478 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:21:49,480 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 678033

2025-10-14T09:21:49,482 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:21:49,483 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F188

2025-10-14T09:21:49,485 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,486 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU VMCU Bootloader"}

2025-10-14T09:21:49,489 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H241-HL

2025-10-14T09:21:49,491 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:21:49,494 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf

2025-10-14T09:21:49,499 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H241-HL.VBF

2025-10-14T09:21:49,503 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: BOOT_IMAGE

2025-10-14T09:21:49,506 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 50860

2025-10-14T09:21:49,508 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:21:49,510 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: D027

2025-10-14T09:21:49,512 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,514 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU MP images"}

2025-10-14T09:21:49,516 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: MU5T-14H090-BAZ

2025-10-14T09:21:49,518 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:21:49,520 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf

2025-10-14T09:21:49,523 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/MU5T-14H090-BAZ.VBF

2025-10-14T09:21:49,526 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:21:49,528 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 48761810

2025-10-14T09:21:49,530 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:21:49,531 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F121

2025-10-14T09:21:49,533 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,535 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU AP images"}

2025-10-14T09:21:49,537 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H090-AHL

2025-10-14T09:21:49,539 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:21:49,542 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf

2025-10-14T09:21:49,545 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H090-AHL.VBF

2025-10-14T09:21:49,547 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:21:49,549 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 98168657

2025-10-14T09:21:49,550 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:21:49,552 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F120

2025-10-14T09:21:49,554 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:21:49,555 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: MANIFEST

2025-10-14T09:21:49,557 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: FordSoftwareManifest

2025-10-14T09:21:49,560 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: SIGNED

2025-10-14T09:21:49,561 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://www.gsug.vehicleupdates.files.ford.com/M_7057e5f9-8c36-47c9-b1cc-72799b626f06

2025-10-14T09:21:49,564 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: 1FBAX2YG0PKA54057_FordSoftwareManifest.der

2025-10-14T09:21:49,566 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: TRANSIENT

2025-10-14T09:21:49,568 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 0

2025-10-14T09:21:49,570 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 716

2025-10-14T09:21:49,571 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: null

2025-10-14T09:21:49,573 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> errorDetails = SUCCESS

2025-10-14T09:21:49,575 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> errorSource = FENIX.

2025-10-14T09:21:49,578 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ outputFenixData

2025-10-14T09:21:49,579 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ParseManifestPresence

2025-10-14T09:21:49,581 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 0

2025-10-14T09:21:49,583 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 1

2025-10-14T09:21:49,586 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 2

2025-10-14T09:21:49,593 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 3

2025-10-14T09:21:49,595 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 4

2025-10-14T09:21:49,597 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bManifestFound =true

2025-10-14T09:21:49,599 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ParseManifestPresence

2025-10-14T09:22:04,316 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB drive location = D:\

2025-10-14T09:22:04,319 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ downloadFenixSoftware

2025-10-14T09:22:05,930 INFO resource.util.ResumableFileTransfer - Attempting to download FordSoftwareManifest from https://www.gsug.vehicleupdates.files.ford.com/M_7057e5f9-8c36-47c9-b1cc-72799b626f06. Initial size: 0. Expected size: null.

2025-10-14T09:22:05,940 INFO util.download.QueuedFileDownload - Request headers: {Range=bytes=0-}

2025-10-14T09:22:06,517 INFO util.download.QueuedFileDownload - Response headers: {x-guploader-uploadid=AAwnv3IsMvG5tdEu90eAd8uWR5EAHlnOuCvZDglgaT8nsfLK4dK61NTRxJ8N1ya4AgXmbVPPsq5cToQ, date=Tue, 14 Oct 2025 13:22:07 GMT, server=UploadServer, expires=Tue, 14 Oct 2025 13:22:07 GMT, x-goog-stored-content-length=4546, Alt-Svc=h3=":443"; ma=2592000,h3-29=":443"; ma=2592000, x-goog-metageneration=1, Connection=close, x-goog-hash=md5=9KiWwxz000WHoelJ7xsbVg==, via=1.1 google, last-modified=Tue, 14 Oct 2025 13:21:49 GMT, x-goog-stored-content-encoding=identity, content-range=bytes 0-4545/4546, content-type=application/octet-stream, etag="f4a896c31cf4d34587a1e949ef1b1b56", x-goog-generation=1760448109671492, cache-control=private, max-age=0, accept-ranges=bytes, Content-Length=4546, x-goog-storage-class=STANDARD}

2025-10-14T09:22:06,536 INFO util.download.QueuedFileDownload - Receiving 4546 of 4546/4546 bytes

2025-10-14T09:22:06,540 INFO util.download.QueuedFileTransfer - Copied 4546 bytes at offset 0 to disk

2025-10-14T09:22:06,542 INFO resource.util.ResumableFileTransfer - Download of FordSoftwareManifest finished

2025-10-14T09:22:06,550 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> executeDownloadFenixSoftware SUCCESS

2025-10-14T09:22:06,554 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ downloadFenixSoftware

2025-10-14T09:22:06,557 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetFenixUSBPackage

2025-10-14T09:22:06,560 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ InstallUSBSoftware

2025-10-14T09:25:28,436 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB installation success was selected.

2025-10-14T09:25:28,440 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ InstallUSBSoftware

2025-10-14T09:25:29,443 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ValidateSoftwareUpdateProcess

2025-10-14T09:25:29,445 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Validation for flash method (0 = CAN, 1 = USB, 2 = BOTH):  1

2025-10-14T09:25:29,447 INFO class otxcontainer.G2056515.authorLogs - listOfApplicationDIDs = 0

2025-10-14T09:25:29,449 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB flash DID count:  2

2025-10-14T09:25:29,451 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB and CAN DID count (including Apps):  2

2025-10-14T09:25:30,954 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EstablishCommsProcess

2025-10-14T09:25:32,417 INFO dflt.memory.MemoryMonitor - [MEMORY] Available virtual memory: 497 MB

2025-10-14T09:25:33,960 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ PingModule

2025-10-14T09:25:33,962 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Pinging node = 754

2025-10-14T09:25:33,964 INFO class otxcontainer.G2056515.authorLogs - g_comChannelSet = false

2025-10-14T09:25:33,966 INFO class otxcontainer.G2056515.authorLogs - Com channel null, need to initialize

2025-10-14T09:25:33,968 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECU does not support CAN FD try CAN Classic for node: 754

2025-10-14T09:25:33,970 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: PingModule text: ECU does not support CAN FD
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: PingModule text: ECU does not support CAN FD
	at otxcontainer.G2056515$20.run(G2056515.java:35948) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:34,480 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:25:34,482 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422D100

2025-10-14T09:25:34,484 INFO impl.core.AbstractServiceFactory - Using pin switched protocol: ISO15765_PS instead of ISO15765

2025-10-14T09:25:34,539 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:25:34,541 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,D1,00]

2025-10-14T09:25:34,543 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,460,425,434 - [00,00,07,54]

2025-10-14T09:25:34,548 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,460,431,560 - [00,00,07,5C,62,D1,00,01]

2025-10-14T09:25:34,548 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62D10001

2025-10-14T09:25:34,550 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Comms ok, protocol = CAN Classic for node: 754

2025-10-14T09:25:34,553 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VCI supports CAN FD =  false

2025-10-14T09:25:34,555 ERROR otxcontainer.G2056515 - Error in application, message was: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
java.lang.ClassCastException: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:22) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.GuardedValue.setValue(GuardedValue.java:147) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:136) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at otxcontainer.G2056515$20.run(G2056515.java:36907) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:34,566 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Exception in StMin NOT overrided

2025-10-14T09:25:34,568 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases

2025-10-14T09:25:34,572 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37

2025-10-14T09:25:34,574 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37

2025-10-14T09:25:34,577 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ PingModule

2025-10-14T09:25:34,579 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EstablishCommsProcess

2025-10-14T09:25:34,580 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ReadPartNumDids

2025-10-14T09:25:34,583 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:25:34,586 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  00000754228068

2025-10-14T09:25:34,598 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,80,68]

2025-10-14T09:25:34,600 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,460,483,040 - [00,00,07,54]

2025-10-14T09:25:34,609 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,460,491,538 - [00,00,07,5C]

2025-10-14T09:25:34,609 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,460,493,423 - [00,00,07,5C,62,80,68,53,55,35,54,2D,31,34,48,32,34,30,2D,47,48,00,00,00,00,00,00,00,00,00,00]

2025-10-14T09:25:34,609 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C628068535535542D3134483234302D474800000000000000000000

2025-10-14T09:25:34,614 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 :Response byte size 24

2025-10-14T09:25:34,616 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 (HEX) =  535535542D3134483234302D474800000000000000000000

2025-10-14T09:25:34,619 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProcessDidResponseValues

2025-10-14T09:25:34,621 INFO class otxcontainer.G2056515.authorLogs - Part number byte 14 IS null

2025-10-14T09:25:34,623 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ProcessDidResponseValues

2025-10-14T09:25:34,626 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 (ASCII) =  SU5T-14H240-GH

2025-10-14T09:25:34,628 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 Type =  Boot Image

2025-10-14T09:25:34,631 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:25:34,633 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422F120

2025-10-14T09:25:34,645 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,F1,20]

2025-10-14T09:25:34,647 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,460,529,973 - [00,00,07,54]

2025-10-14T09:25:34,650 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,460,531,559 - [00,00,07,5C]

2025-10-14T09:25:34,650 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,460,533,430 - [00,00,07,5C,62,F1,20,53,55,35,54,2D,31,34,48,30,39,30,2D,41,47,48,00,00,00,00,00,00,00,00,00]

2025-10-14T09:25:34,650 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62F120535535542D3134483039302D414748000000000000000000

2025-10-14T09:25:34,654 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 :Response byte size 24

2025-10-14T09:25:34,656 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 (HEX) =  535535542D3134483039302D414748000000000000000000

2025-10-14T09:25:34,658 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProcessDidResponseValues

2025-10-14T09:25:34,661 INFO class otxcontainer.G2056515.authorLogs - Part number byte 15 IS null

2025-10-14T09:25:34,662 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ProcessDidResponseValues

2025-10-14T09:25:34,667 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 (ASCII) =  SU5T-14H090-AGH

2025-10-14T09:25:34,669 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 Type =  Strategy

2025-10-14T09:25:34,671 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ReadPartNumDids

2025-10-14T09:25:34,673 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ValidateFlashActionDIDsAgainstModule

2025-10-14T09:25:34,675 INFO class otxcontainer.G2056515.authorLogs - sDidIdentifier = 8068

2025-10-14T09:25:34,677 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 Validation FAIL
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH

2025-10-14T09:25:35,679 INFO class otxcontainer.G2056515.authorLogs - sDidIdentifier = F120

2025-10-14T09:25:35,680 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 Validation FAIL
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH

2025-10-14T09:25:36,684 INFO class otxcontainer.G2056515.authorLogs - here

2025-10-14T09:25:36,684 INFO class otxcontainer.G2056515.authorLogs - 1

2025-10-14T09:25:36,685 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> No Applications in Flash Action List to validate

2025-10-14T09:25:38,695 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Update failed!!

2025-10-14T09:25:38,696 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

	at otxcontainer.G2056515.ValidateFlashActionDIDsAgainstModule(G2056515.java:64126) [G2056515:?]
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64902) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:38,708 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:25:38,710 INFO class otxcontainer.G2056515.authorLogs - Keep bargraph

2025-10-14T09:25:38,710 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ValidateFlashActionDIDsAgainstModule - Exception qualifier =  ValidateFlashActionDIDsAgainstModule - Exception text = Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

2025-10-14T09:25:38,718 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ValidateFlashActionDIDsAgainstModule(G2056515.java:64152) ~[G2056515:?]
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64902) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:38,727 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateSoftwareUpdateProcess text: Validate exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateSoftwareUpdateProcess text: Validate exception
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64932) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:40,238 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateSoftwareUpdateProcess text: USB
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateSoftwareUpdateProcess text: USB
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:65009) ~[G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:25:40,247 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB installation failure, bUSBSuccess = false

2025-10-14T09:25:49,614 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Retry USB process selected

2025-10-14T09:25:57,963 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EstablishCommsProcess

2025-10-14T09:25:58,998 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:26:00,998 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ PingModule

2025-10-14T09:26:01,000 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Pinging node = 754

2025-10-14T09:26:01,002 INFO class otxcontainer.G2056515.authorLogs - g_comChannelSet = false

2025-10-14T09:26:01,004 INFO class otxcontainer.G2056515.authorLogs - Com channel null, need to initialize

2025-10-14T09:26:01,006 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECU does not support CAN FD try CAN Classic for node: 754

2025-10-14T09:26:01,009 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: PingModule text: ECU does not support CAN FD
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: PingModule text: ECU does not support CAN FD
	at otxcontainer.G2056515$20.run(G2056515.java:35948) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:01,519 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:26:01,521 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422D100

2025-10-14T09:26:01,523 INFO impl.core.AbstractServiceFactory - Using pin switched protocol: ISO15765_PS instead of ISO15765

2025-10-14T09:26:01,568 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:26:01,574 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,D1,00]

2025-10-14T09:26:01,576 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,487,457,455 - [00,00,07,54]

2025-10-14T09:26:01,579 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,487,460,697 - [00,00,07,5C,62,D1,00,01]

2025-10-14T09:26:01,579 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62D10001

2025-10-14T09:26:01,581 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Comms ok, protocol = CAN Classic for node: 754

2025-10-14T09:26:01,583 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VCI supports CAN FD =  false

2025-10-14T09:26:01,585 ERROR otxcontainer.G2056515 - Error in application, message was: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
java.lang.ClassCastException: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:22) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.GuardedValue.setValue(GuardedValue.java:147) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:136) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at otxcontainer.G2056515$20.run(G2056515.java:36907) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:01,598 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Exception in StMin NOT overrided

2025-10-14T09:26:01,600 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases

2025-10-14T09:26:01,603 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37

2025-10-14T09:26:01,606 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37

2025-10-14T09:26:01,609 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ PingModule

2025-10-14T09:26:01,611 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EstablishCommsProcess

2025-10-14T09:26:01,613 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EndBargraph

2025-10-14T09:26:01,824 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:26:03,114 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EndBargraph

2025-10-14T09:26:03,116 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61499) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:03,125 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:26:03,127 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:26:03,828 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BargraphDisplayV2

2025-10-14T09:26:04,129 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = UpdateSoftwareOverUSB - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess

2025-10-14T09:26:04,132 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61915) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:04,141 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Update software programming failed, exit process

2025-10-14T09:26:04,143 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:26:04,145 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:26:04,351 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:26:05,147 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ProgramModule - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess

2025-10-14T09:26:05,152 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41872) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:05,161 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:26:05,163 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:26:06,165 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ProgramModule - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess

2025-10-14T09:26:06,174 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:42053) ~[G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) ~[G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:06,189 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EndBargraph

2025-10-14T09:26:07,693 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EndBargraph

2025-10-14T09:26:07,695 ERROR otx.utils.ParallelExecutorOld - [TG] Parallel executor thread Thread[parallel-executor-93-thread-2,5,tg-G2056515] got exception -> com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess

2025-10-14T09:26:07,700 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: UpdateSoftwareOverUSB text: SoftwareUpdateProcess
	at otxcontainer.G2056515$32.run(G2056515.java:57716) ~[?:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:07,709 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:26:07,711 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:26:08,712 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Calling procedure name: SoftwareUpdateProcess ==  Exception text: SoftwareUpdateProcess so retry THIS calling procedure

2025-10-14T09:26:08,715 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ SoftwareUpdateProcess

2025-10-14T09:26:08,718 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BargraphDisplayV2

2025-10-14T09:26:09,718 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProgramModule

2025-10-14T09:26:09,720 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ CheckSoftwareLevel

2025-10-14T09:26:09,721 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> About to check if all the files are already in the module

2025-10-14T09:26:09,724 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH

2025-10-14T09:26:09,728 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: CheckSoftwareLevel text: Handle exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: CheckSoftwareLevel text: Handle exception
	at otxcontainer.G2056515.CheckSoftwareLevel(G2056515.java:9195) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41188) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:09,740 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 SW on module is missing or not at latest level, FLASH!!

2025-10-14T09:26:09,744 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F188 Matches - No need to flash,  part number = SU5T-14H085-HL

2025-10-14T09:26:09,748 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> D027 Matches - No need to flash,  part number = SU5T-14H241-HL

2025-10-14T09:26:09,750 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F121 Matches - No need to flash,  part number = MU5T-14H090-BAZ

2025-10-14T09:26:09,753 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH

2025-10-14T09:26:09,757 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: CheckSoftwareLevel text: Handle exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: CheckSoftwareLevel text: Handle exception
	at otxcontainer.G2056515.CheckSoftwareLevel(G2056515.java:9195) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41188) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:09,772 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 SW on module is missing or not at latest level, FLASH!!

2025-10-14T09:26:09,776 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ CheckSoftwareLevel

2025-10-14T09:26:09,779 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ DownloadSoftwareBinaries

2025-10-14T09:26:09,782 INFO class otxcontainer.G2056515.authorLogs - ListGetLength(listOfFlashActionDIDs) = 5

2025-10-14T09:26:09,785 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bFlashALL = true

2025-10-14T09:26:09,788 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= 8068

2025-10-14T09:26:09,791 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H240-HL

2025-10-14T09:26:09,793 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 = SU5T-14H240-HL Software binary required - get ALL files

2025-10-14T09:26:09,796 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:26:09,797 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:26:09,799 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:09,985 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:26:09,987 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F188

2025-10-14T09:26:09,989 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H085-HL

2025-10-14T09:26:09,992 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F188 = SU5T-14H085-HL Software binary required - get ALL files

2025-10-14T09:26:09,995 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:26:09,997 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:26:09,999 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:10,134 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:26:10,136 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= D027

2025-10-14T09:26:10,138 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H241-HL

2025-10-14T09:26:10,140 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> D027 = SU5T-14H241-HL Software binary required - get ALL files

2025-10-14T09:26:10,144 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:26:10,146 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:26:10,149 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:10,281 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:26:10,283 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F121

2025-10-14T09:26:10,285 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = MU5T-14H090-BAZ

2025-10-14T09:26:10,287 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F121 = MU5T-14H090-BAZ Software binary required - get ALL files

2025-10-14T09:26:10,290 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:26:10,292 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:26:10,294 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:10,440 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:26:10,444 INFO class otxcontainer.G2056515.authorLogs - sDIDNumber= F120

2025-10-14T09:26:10,447 INFO class otxcontainer.G2056515.authorLogs - flashActionPartNumber = SU5T-14H090-AHL

2025-10-14T09:26:10,449 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 = SU5T-14H090-AHL Software binary required - get ALL files

2025-10-14T09:26:10,453 INFO class otxcontainer.G2056515.authorLogs - SBL = 1

2025-10-14T09:26:10,455 INFO class otxcontainer.G2056515.authorLogs - NON APP = 1

2025-10-14T09:26:10,456 ERROR otxcontainer.G2056515 - Error in application, message was: null
java.lang.NullPointerException: null
	at com.ford.otx.vehicle.software.provider.dflt.DiskVehicleSoftwareProvider.addToQueue(DiskVehicleSoftwareProvider.java:151) ~[com.ford.otx.vehicle.software.provider.default-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:32) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.etis.runtime.services.vehicle.software.provider.command.AddVehicleSoftwareToQueue.execute(AddVehicleSoftwareToQueue.java:12) ~[com.ford.otx.vehicle.software.provider-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseLibrary.addSoftwareToQueue(BaseLibrary.java:440) ~[com.ford.otx.apps.otx-72.31.54.jar:?]
	at otxcontainer.G2056515.DownloadSoftwareBinaries(G2056515.java:13314) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41223) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:26:10,580 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software download successful? true

2025-10-14T09:26:10,583 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ DownloadSoftwareBinaries

2025-10-14T09:26:10,585 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ DetermineProgrammingMethod

2025-10-14T09:26:10,587 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 is USB flashed

2025-10-14T09:26:10,591 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bfProgrammingMethod = 02

2025-10-14T09:26:10,600 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 is USB flashed

2025-10-14T09:26:10,603 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bfProgrammingMethod = 02

2025-10-14T09:26:10,605 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> No Applications to install

2025-10-14T09:26:10,607 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ DetermineProgrammingMethod

2025-10-14T09:26:10,611 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BatteryCheck

2025-10-14T09:26:10,646 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:26:11,702 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:26:11,706 DEBUG api.service.Channel - ISO15765 TX         -> 0,000,000,000 - [00,00,07,26,22,40,28]

2025-10-14T09:26:11,708 DEBUG api.service.Channel - ISO15765 TX         -> 0,497,589,003 - [00,00,07,26]

2025-10-14T09:26:11,719 DEBUG api.service.Channel - ISO15765 RX         <- 0,497,599,923 - [00,00,07,2E,62,40,28,64]

2025-10-14T09:26:11,719 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Battery State of Charge SOC (percent) = 100

2025-10-14T09:26:11,722 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Battery voltage = 12.963

2025-10-14T09:26:11,755 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BatteryCheck

2025-10-14T09:26:11,755 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:26:11,757 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Programming method (0-CAN, 1-USB, or 2-BOTH)? = 1

2025-10-14T09:26:11,762 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Programming method: USB

2025-10-14T09:26:11,764 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ UpdateSoftwareOverUSB

2025-10-14T09:26:11,766 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> g_ParsedFlashActionData.removeApplicationsList count =  0

2025-10-14T09:26:11,770 INFO class otxcontainer.G2056515.authorLogs - g_ParsedFlashActionData.removeApplicationsList count = 0

2025-10-14T09:26:11,773 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ SetApplicationState

2025-10-14T09:26:11,776 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Setting ApplicationState = APPLICATION_SKIPPED

2025-10-14T09:26:11,778 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ SetApplicationState

2025-10-14T09:26:11,780 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetFenixUSBPackage

2025-10-14T09:26:11,782 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File to flash over USB =  SU5T-14H240-HL

2025-10-14T09:26:11,785 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File to flash over USB =  SU5T-14H090-AHL

2025-10-14T09:26:11,788 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> addSoftware set to null

2025-10-14T09:26:11,796 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ getFenixData

2025-10-14T09:26:11,798 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> LOG FENIX REQUEST:

2025-10-14T09:26:11,800 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VIN = 1FBAX2YG0PKA54057

2025-10-14T09:26:11,802 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECG ESN = 1EH1BIQJ

2025-10-14T09:26:11,804 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECG Hardware = NU5T-14H026-EB

2025-10-14T09:26:11,806 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Requested node(0) = 754

2025-10-14T09:26:11,808 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Requested software part(0) =

2025-10-14T09:26:11,810 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Remove software part(0) = ""

2025-10-14T09:26:11,812 INFO fdsp.command.RequestFenixData - Requesting GetFenix for 1FBAX2YG0PKA54057

2025-10-14T09:26:14,148 INFO fdsp.command.RequestFenixData - GetFenix received for 1FBAX2YG0PKA54057

2025-10-14T09:26:14,150 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Execute FENIX_SERVICE GET_DATA - SUCCESS

2025-10-14T09:26:14,152 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ getFenixData

2025-10-14T09:26:14,154 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ outputFenixData

2025-10-14T09:26:14,156 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,158 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU CCPU bootchain images"}

2025-10-14T09:26:14,161 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H240-HL

2025-10-14T09:26:14,163 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:26:14,165 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf

2025-10-14T09:26:14,168 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H240-HL.VBF

2025-10-14T09:26:14,170 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: BOOT_IMAGE

2025-10-14T09:26:14,172 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 1994025

2025-10-14T09:26:14,173 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:26:14,175 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: 8068

2025-10-14T09:26:14,184 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,185 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU VMCU load"}

2025-10-14T09:26:14,187 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H085-HL

2025-10-14T09:26:14,189 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:26:14,191 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf

2025-10-14T09:26:14,195 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H085-HL.VBF

2025-10-14T09:26:14,197 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:26:14,199 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 678033

2025-10-14T09:26:14,201 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:26:14,202 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F188

2025-10-14T09:26:14,204 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,206 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU VMCU Bootloader"}

2025-10-14T09:26:14,208 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H241-HL

2025-10-14T09:26:14,211 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:26:14,212 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf

2025-10-14T09:26:14,215 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H241-HL.VBF

2025-10-14T09:26:14,218 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: BOOT_IMAGE

2025-10-14T09:26:14,219 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 50860

2025-10-14T09:26:14,221 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:26:14,223 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: D027

2025-10-14T09:26:14,225 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,227 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU MP images"}

2025-10-14T09:26:14,229 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: MU5T-14H090-BAZ

2025-10-14T09:26:14,231 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:26:14,233 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf

2025-10-14T09:26:14,235 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/MU5T-14H090-BAZ.VBF

2025-10-14T09:26:14,238 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:26:14,239 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 48761810

2025-10-14T09:26:14,241 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:26:14,245 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F121

2025-10-14T09:26:14,246 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,248 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: {"TCU AP images"}

2025-10-14T09:26:14,250 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: SU5T-14H090-AHL

2025-10-14T09:26:14,252 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: CACHED

2025-10-14T09:26:14,254 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf

2025-10-14T09:26:14,257 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: FordSoftwareUpdates/SU5T-14H090-AHL.VBF

2025-10-14T09:26:14,259 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: STRATEGY

2025-10-14T09:26:14,262 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 98168657

2025-10-14T09:26:14,264 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 754

2025-10-14T09:26:14,265 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: F120

2025-10-14T09:26:14,267 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> FENIX response:

2025-10-14T09:26:14,269 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Description: MANIFEST

2025-10-14T09:26:14,271 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Part Number: FordSoftwareManifest

2025-10-14T09:26:14,272 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File Type: SIGNED

2025-10-14T09:26:14,274 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Resource URL: https://www.gsug.vehicleupdates.files.ford.com/M_abba5b6b-c6b7-400d-bdd6-b5739256cf2f

2025-10-14T09:26:14,278 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> File On USB: 1FBAX2YG0PKA54057_FordSoftwareManifest.der

2025-10-14T09:26:14,282 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Software Type: TRANSIENT

2025-10-14T09:26:14,285 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Binary Size: 0

2025-10-14T09:26:14,288 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Node Address: 716

2025-10-14T09:26:14,291 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DID Address: null

2025-10-14T09:26:14,293 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> errorDetails = SUCCESS

2025-10-14T09:26:14,295 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> errorSource = FENIX.

2025-10-14T09:26:14,298 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ outputFenixData

2025-10-14T09:26:14,301 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ParseManifestPresence

2025-10-14T09:26:14,305 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 0

2025-10-14T09:26:14,314 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 1

2025-10-14T09:26:14,317 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 2

2025-10-14T09:26:14,319 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 3

2025-10-14T09:26:14,321 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Manifest not found, keep looping....index = 4

2025-10-14T09:26:14,323 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bManifestFound =true

2025-10-14T09:26:14,325 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ParseManifestPresence

2025-10-14T09:27:22,420 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB drive location = D:\

2025-10-14T09:27:22,424 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ downloadFenixSoftware

2025-10-14T09:27:32,141 INFO resource.util.ResumableFileTransfer - Attempting to download FordSoftwareManifest from https://www.gsug.vehicleupdates.files.ford.com/M_abba5b6b-c6b7-400d-bdd6-b5739256cf2f. Initial size: 0. Expected size: null.

2025-10-14T09:27:32,145 INFO util.download.QueuedFileDownload - Request headers: {Range=bytes=0-}

2025-10-14T09:27:32,400 INFO util.download.QueuedFileDownload - Response headers: {x-guploader-uploadid=AAwnv3LZbjOUDQy55_5YSFsXTqDk59GKoh1Mpac_hyTPRIybjZvTA-4QAiGDsiu_sLpwC6VtuFSqZuY, date=Tue, 14 Oct 2025 13:27:33 GMT, server=UploadServer, expires=Tue, 14 Oct 2025 13:27:33 GMT, x-goog-stored-content-length=4546, Alt-Svc=h3=":443"; ma=2592000,h3-29=":443"; ma=2592000, x-goog-metageneration=1, Connection=close, x-goog-hash=md5=++NDAnlcnoqtXmdo+hP3WQ==, via=1.1 google, last-modified=Tue, 14 Oct 2025 13:26:14 GMT, x-goog-stored-content-encoding=identity, content-range=bytes 0-4545/4546, content-type=application/octet-stream, etag="fbe34302795c9e8aad5e6768fa13f759", x-goog-generation=1760448374575694, cache-control=private, max-age=0, accept-ranges=bytes, Content-Length=4546, x-goog-storage-class=STANDARD}

2025-10-14T09:27:32,414 INFO util.download.QueuedFileDownload - Receiving 4546 of 4546/4546 bytes

2025-10-14T09:27:32,421 INFO util.download.QueuedFileTransfer - Copied 4546 bytes at offset 0 to disk

2025-10-14T09:27:32,424 INFO resource.util.ResumableFileTransfer - Download of FordSoftwareManifest finished

2025-10-14T09:27:32,474 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> executeDownloadFenixSoftware SUCCESS

2025-10-14T09:27:32,478 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ downloadFenixSoftware

2025-10-14T09:27:32,481 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetFenixUSBPackage

2025-10-14T09:27:32,493 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ InstallUSBSoftware

2025-10-14T09:30:32,415 INFO dflt.memory.MemoryMonitor - [MEMORY] Available virtual memory: 497 MB

2025-10-14T09:31:15,678 INFO api.jni.EventHandler - Processing 1 events

2025-10-14T09:31:18,162 ERROR impl.vbatt.BatteryStatusMonitorImpl - Error reading battery voltage
com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 I/O control on channel 2147483649 = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruIoctl(InstalledDeviceImpl.java:696) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.DeviceConnectionImpl.getVehicleBatteryVoltage(DeviceConnectionImpl.java:352) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.services.vehicle.comms.core.api.impl.vbatt.BatteryStatusMonitorImpl.readVoltage(BatteryStatusMonitorImpl.java:593) ~[com.ford.fdt.runtime.comms.core.api.impl-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.services.vehicle.comms.core.api.impl.vbatt.BatteryStatusMonitorImpl.run(BatteryStatusMonitorImpl.java:227) [com.ford.fdt.runtime.comms.core.api.impl-33.13.1-hf.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) [?:1.8.0_171]
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:31:18,165 INFO j2534.win32.InstalledDeviceImpl - VehicleConnectionErrorEventHandler
	java.lang.Thread.getStackTrace(Thread.java:1559)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.logStackTrace(InstalledDeviceImpl.java:1060)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruClose(InstalledDeviceImpl.java:484)
	com.ford.etis.runtime.j2534.win32.DeviceConnectionImpl.closeDeviceConnection(DeviceConnectionImpl.java:431)
	com.ford.etis.runtime.j2534.win32.DeviceConnectionImpl.close(DeviceConnectionImpl.java:399)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.closeConnection(VciConnectionSource.java:190)
	com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.closeAllConnections(DefaultDeviceConnectionProvider.java:160)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.cleanVehicleConnection(DefaultVehicleConnectionManager.java:381)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:281)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:265)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDeviceEventNotification(DefaultVehicleConnectionManager.java:229)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionEventUtil$DeviceErrorCodeListener$1.run(DefaultVehicleConnectionEventUtil.java:126)

2025-10-14T09:31:20,208 INFO deviceselection.vci.VciDeviceSelection - set device list type:VCMII

2025-10-14T09:31:20,210 INFO api.jni.VcmiiApiManager - Cancelling VTX runtime notifications

2025-10-14T09:31:20,213 INFO api.jni.VcmiiApiManager - Shutting down VTX runtime

2025-10-14T09:31:20,213 INFO api.jni.EventHandler - Stop received while waiting for events

2025-10-14T09:31:20,218 INFO deviceselection.vci.VciDeviceSelection - VCI Device Selection started : current context is VCM III...WIRED

2025-10-14T09:31:20,223 INFO vcmii.dflt.VcmiiDeviceManager - connecting VCMIII runtime

2025-10-14T09:31:20,225 INFO vcmii.dflt.VcmiiDeviceManager -  True if 64 bit file exists: true

2025-10-14T09:31:20,227 INFO api.jni.VcmiiApiManager - initializing runtime (log=C:\Program Files (x86)\Ford Motor Company\FDRS\..\VcmiiRuntime.log)

2025-10-14T09:31:20,284 INFO api.jni.EventHandler - Waiting for events - starting

2025-10-14T09:31:20,288 INFO j2534.win32.InstalledDeviceImpl - VehicleConnectionErrorEventHandler
	java.lang.Thread.getStackTrace(Thread.java:1559)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.logStackTrace(InstalledDeviceImpl.java:1060)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:442)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29)
	com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.reconnectVehicleConnection(DefaultVehicleConnectionManager.java:403)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:282)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:265)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDeviceEventNotification(DefaultVehicleConnectionManager.java:229)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionEventUtil$DeviceErrorCodeListener$1.run(DefaultVehicleConnectionEventUtil.java:126)

2025-10-14T09:31:20,419 ERROR dflt.sources.VciConnectionSource - Failed J2534 connection attempt
com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.reconnectVehicleConnection(DefaultVehicleConnectionManager.java:403) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:282) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:265) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDeviceEventNotification(DefaultVehicleConnectionManager.java:229) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionEventUtil$DeviceErrorCodeListener$1.run(DefaultVehicleConnectionEventUtil.java:126) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]

2025-10-14T09:31:20,433 ERROR dflt.sources.VciConnectionSource - Failed to connect to preferred VCI device.
com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.reconnectVehicleConnection(DefaultVehicleConnectionManager.java:403) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:282) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:265) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDeviceEventNotification(DefaultVehicleConnectionManager.java:229) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionEventUtil$DeviceErrorCodeListener$1.run(DefaultVehicleConnectionEventUtil.java:126) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]

2025-10-14T09:31:20,448 WARN deviceconnection.dflt.DefaultDeviceConnectionProvider - Failed to get a device connection for device type : com.ford.etis.runtime.vci.j2534.api.J2534Exception: errorCode=8, message=Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]

2025-10-14T09:31:20,455 ERROR deviceconnection.dflt.DefaultVehicleConnectionManager - Unable to obtain device connection
com.ford.etis.runtime.services.vehicle.comms.core.exception.BootstrapDeviceConnectionException: Unable to get or connect to device, try again.
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:83) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.reconnectVehicleConnection(DefaultVehicleConnectionManager.java:403) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:282) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDisconnectedVehicleConnection(DefaultVehicleConnectionManager.java:265) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.handleDeviceEventNotification(DefaultVehicleConnectionManager.java:229) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionEventUtil$DeviceErrorCodeListener$1.run(DefaultVehicleConnectionEventUtil.java:126) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
Caused by: com.ford.otx.services.deviceconnection.exception.DeviceConnectionException: com.ford.etis.runtime.vci.j2534.api.J2534Exception: errorCode=8, message=Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:92) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	... 7 more
Caused by: com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	... 7 more

2025-10-14T09:31:20,473 WARN deviceconnection.dflt.DefaultVehicleConnectionManager - Unable to reconnect vehicle connection: Unable to obtain device connection

2025-10-14T09:31:20,479 INFO core.comms.CommsServices - VehicleConnectionNotification recieved...DISCONNECTED

2025-10-14T09:34:02,028 INFO deviceselection.vci.VciDeviceSelection - set device list type:VCMII

2025-10-14T09:34:02,030 INFO api.jni.VcmiiApiManager - Cancelling VTX runtime notifications

2025-10-14T09:34:02,032 INFO api.jni.EventHandler - Stop received while waiting for events

2025-10-14T09:34:02,032 INFO api.jni.VcmiiApiManager - Shutting down VTX runtime

2025-10-14T09:34:02,041 INFO deviceselection.vci.VciDeviceSelection - VCI Device Selection started : current context is VCM III...WIRED

2025-10-14T09:34:02,045 INFO vcmii.dflt.VcmiiDeviceManager - connecting VCMIII runtime

2025-10-14T09:34:02,047 INFO vcmii.dflt.VcmiiDeviceManager -  True if 64 bit file exists: true

2025-10-14T09:34:02,049 INFO api.jni.VcmiiApiManager - initializing runtime (log=C:\Program Files (x86)\Ford Motor Company\FDRS\..\VcmiiRuntime.log)

2025-10-14T09:34:02,111 INFO api.jni.EventHandler - Waiting for events - starting

2025-10-14T09:34:02,122 INFO j2534.win32.InstalledDeviceImpl - pool-5-thread-1
	java.lang.Thread.getStackTrace(Thread.java:1559)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.logStackTrace(InstalledDeviceImpl.java:1060)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:442)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29)
	com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129)
	com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61)
	com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17)
	com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126)
	com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source)
	com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source)
	com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source)
	java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308)
	java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180)
	java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294)
	java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	java.lang.Thread.run(Thread.java:748)

2025-10-14T09:34:02,171 ERROR dflt.sources.VciConnectionSource - Failed J2534 connection attempt
com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) [com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source) [com.ford.fdt.hmi.core-73.13.13.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) [?:1.8.0_171]
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:02,185 ERROR dflt.sources.VciConnectionSource - Failed to connect to preferred VCI device.
com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) [com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source) [com.ford.fdt.hmi.core-73.13.13.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) [?:1.8.0_171]
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:02,198 WARN deviceconnection.dflt.DefaultDeviceConnectionProvider - Failed to get a device connection for device type : com.ford.etis.runtime.vci.j2534.api.J2534Exception: errorCode=8, message=Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]

2025-10-14T09:34:02,204 ERROR deviceconnection.dflt.DefaultVehicleConnectionManager - Unable to obtain device connection
com.ford.etis.runtime.services.vehicle.comms.core.exception.BootstrapDeviceConnectionException: Unable to get or connect to device, try again.
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:83) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) [com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17) [com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) [com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source) [com.ford.fdt.hmi.core-73.13.13.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) [?:1.8.0_171]
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]
Caused by: com.ford.otx.services.deviceconnection.exception.DeviceConnectionException: com.ford.etis.runtime.vci.j2534.api.J2534Exception: errorCode=8, message=Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:92) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	... 15 more
Caused by: com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	... 15 more

2025-10-14T09:34:02,233 ERROR core.vci.J2534StatusMonitor - Unable to obtain vehicle connection 
com.ford.otx.services.deviceconnection.exception.VehicleConnectionException: Unable to obtain device connection
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:146) ~[?:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61) ~[com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17) ~[com.ford.otx.services.deviceconnection-72.31.54.jar:?]
	at com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126) ~[com.ford.otx.command.invoker.osgi-40.21.20.jar:?]
	at com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source) [com.ford.fdt.hmi.core-73.13.13.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source) [com.ford.otx.services.notifier.default-72.31.54.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) [?:1.8.0_171]
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180) [?:1.8.0_171]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]
Caused by: com.ford.etis.runtime.services.vehicle.comms.core.exception.BootstrapDeviceConnectionException: Unable to get or connect to device, try again.
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:83) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) ~[?:?]
	... 13 more
Caused by: com.ford.otx.services.deviceconnection.exception.DeviceConnectionException: com.ford.etis.runtime.vci.j2534.api.J2534Exception: errorCode=8, message=Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:92) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) ~[?:?]
	... 13 more
Caused by: com.ford.etis.runtime.vci.j2534.api.J2534Exception: Error 8 opening device = (28240001:00000000) Unable to communicate with device [J2534_ERROR:ERR_DEVICE_NOT_CONNECTED]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:71) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.vci.j2534.api.J2534Exception.createError(J2534Exception.java:87) ~[com.ford.fdt.runtime.comms.j2534-33.13.1-hf.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:460) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195) ~[com.ford.fdt.runtime.comms.j2534.jni-33.13.2.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29) ~[com.ford.otx.services.deviceconnection.default-72.31.54.jar:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328) ~[?:?]
	at com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129) ~[?:?]
	... 13 more

2025-10-14T09:34:02,510 INFO api.jni.EventHandler - Processing 1 events

2025-10-14T09:34:03,937 WARN deviceselection.vcmii.VcmiiDeviceListItem - exception while trying to access device 88934215 : code Invalid handle

2025-10-14T09:34:07,513 INFO deviceselection.vci.VciDeviceSelection - set device list type:VCMII

2025-10-14T09:34:07,517 INFO api.jni.VcmiiApiManager - Cancelling VTX runtime notifications

2025-10-14T09:34:07,519 INFO api.jni.VcmiiApiManager - Shutting down VTX runtime

2025-10-14T09:34:07,519 INFO api.jni.EventHandler - Stop received while waiting for events

2025-10-14T09:34:07,526 INFO deviceselection.vci.VciDeviceSelection - VCI Device Selection started : current context is VCM III...WIRED

2025-10-14T09:34:07,531 INFO vcmii.dflt.VcmiiDeviceManager - connecting VCMIII runtime

2025-10-14T09:34:07,533 INFO vcmii.dflt.VcmiiDeviceManager -  True if 64 bit file exists: true

2025-10-14T09:34:07,534 INFO api.jni.VcmiiApiManager - initializing runtime (log=C:\Program Files (x86)\Ford Motor Company\FDRS\..\VcmiiRuntime.log)

2025-10-14T09:34:07,586 INFO api.jni.EventHandler - Waiting for events - starting

2025-10-14T09:34:08,056 WARN deviceselection.vcmii.VcmiiDeviceListItem - exception while trying to access device 88934215 : code Invalid handle

2025-10-14T09:34:08,116 INFO api.jni.VcmiiApiManager - Disconnecting VTX runtime

2025-10-14T09:34:08,118 INFO api.jni.EventHandler - Processing 1 events

2025-10-14T09:34:08,125 INFO j2534.win32.InstalledDeviceImpl - pool-5-thread-1
	java.lang.Thread.getStackTrace(Thread.java:1559)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.logStackTrace(InstalledDeviceImpl.java:1060)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.passThruOpen(InstalledDeviceImpl.java:442)
	com.ford.etis.runtime.j2534.win32.InstalledDeviceImpl.open(InstalledDeviceImpl.java:195)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.createVciDeviceConnection(VciConnectionSource.java:270)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.connectToPreferredVci(VciConnectionSource.java:228)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:87)
	com.ford.otx.services.deviceconnection.dflt.sources.VciConnectionSource.getDeviceConnection(VciConnectionSource.java:29)
	com.ford.otx.services.deviceconnection.dflt.DefaultDeviceConnectionProvider.getConnection(DefaultDeviceConnectionProvider.java:77)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.init(DefaultVehicleConnectionManager.java:328)
	com.ford.otx.services.deviceconnection.dflt.DefaultVehicleConnectionManager.getVehicleConnection(DefaultVehicleConnectionManager.java:129)
	com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:61)
	com.ford.otx.services.deviceconnection.command.GetVehicleConnection.execute(GetVehicleConnection.java:17)
	com.ford.otx.command.invoker.osgi.OSGICommandInvoker.invoke(OSGICommandInvoker.java:126)
	com.ford.fdt.hmi.core.vci.J2534StatusMonitor.notify(Unknown Source)
	com.ford.otx.services.notifier.dflt.DefaultNotifier$1.notifyAllListeners(Unknown Source)
	com.ford.otx.services.notifier.dflt.DefaultNotifier$1.run(Unknown Source)
	java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	java.util.concurrent.FutureTask.runAndReset(FutureTask.java:308)
	java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:180)
	java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:294)
	java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	java.lang.Thread.run(Thread.java:748)

2025-10-14T09:34:08,247 INFO apps.readvin.ReadVehicleIdentificationNumber - Attempting to read VIN from vehicle

2025-10-14T09:34:08,295 DEBUG api.service.Channel - ISO15765 TX         -> 0,000,000,000 - [00,00,07,DF,09,02]

2025-10-14T09:34:08,376 DEBUG api.service.Channel - ISO15765 TX         -> 0,000,000,000 - [00,00,07,26,22,F1,90]

2025-10-14T09:34:08,477 DEBUG api.service.Channel - ISO15765 RX         <- 0,974,168,636 - [00,00,07,E8]

2025-10-14T09:34:08,477 DEBUG api.service.Channel - ISO15765 RX         <- 0,974,186,221 - [00,00,07,E8,49,02,01,31,46,42,41,58,32,59,47,30,50,4B,41,35,34,30,35,37]

2025-10-14T09:34:08,477 DEBUG api.service.Channel - ISO15765 RX         <- 0,974,248,557 - [00,00,07,2E]

2025-10-14T09:34:08,477 DEBUG api.service.Channel - ISO15765 RX         <- 0,974,281,788 - [00,00,07,2E,62,F1,90,31,46,42,41,58,32,59,47,30,50,4B,41,35,34,30,35,37,00,00,00,00,00,00,00]

2025-10-14T09:34:08,477 INFO apps.readvin.ReadVehicleIdentificationNumber - Number of read vins is 1

2025-10-14T09:34:08,505 INFO readvin.utils.SubmitReadVinUtils - Number of vins has found 1

2025-10-14T09:34:08,507 INFO deviceconnection.dflt.DefaultVehicleConnectionManager - Successfully obtain vehicle connection.

2025-10-14T09:34:09,499 INFO deviceselection.vcmii.VcmiiDeviceListItem - Connection status for 88934215 is 5

2025-10-14T09:34:09,504 INFO api.jni.EventHandler - Processing 3 events

2025-10-14T09:34:10,909 INFO deviceselection.vcmii.VcmiiDeviceListItem - Connection status for 88934215 is 5

2025-10-14T09:34:12,263 INFO deviceselection.vcmii.VcmiiDeviceListItem - Connection status for 88934215 is 5

2025-10-14T09:34:13,649 INFO deviceselection.vcmii.VcmiiDeviceListItem - Connection status for 88934215 is 5

2025-10-14T09:34:14,036 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB installation success was selected.

2025-10-14T09:34:14,039 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ InstallUSBSoftware

2025-10-14T09:34:15,041 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ValidateSoftwareUpdateProcess

2025-10-14T09:34:15,043 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Validation for flash method (0 = CAN, 1 = USB, 2 = BOTH):  1

2025-10-14T09:34:15,049 INFO class otxcontainer.G2056515.authorLogs - listOfApplicationDIDs = 0

2025-10-14T09:34:15,050 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB flash DID count:  2

2025-10-14T09:34:15,056 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB and CAN DID count (including Apps):  2

2025-10-14T09:34:16,561 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EstablishCommsProcess

2025-10-14T09:34:19,568 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ PingModule

2025-10-14T09:34:19,571 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Pinging node = 754

2025-10-14T09:34:19,573 INFO class otxcontainer.G2056515.authorLogs - g_comChannelSet = false

2025-10-14T09:34:19,574 INFO class otxcontainer.G2056515.authorLogs - Com channel null, need to initialize

2025-10-14T09:34:19,576 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECU does not support CAN FD try CAN Classic for node: 754

2025-10-14T09:34:19,578 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: PingModule text: ECU does not support CAN FD
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: PingModule text: ECU does not support CAN FD
	at otxcontainer.G2056515$20.run(G2056515.java:35948) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:20,086 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:34:20,088 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422D100

2025-10-14T09:34:20,090 INFO impl.core.AbstractServiceFactory - Using pin switched protocol: ISO15765_PS instead of ISO15765

2025-10-14T09:34:20,143 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:34:20,146 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,D1,00]

2025-10-14T09:34:20,148 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,986,009,206 - [00,00,07,54]

2025-10-14T09:34:20,156 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,986,017,538 - [00,00,07,5C,62,D1,00,01]

2025-10-14T09:34:20,156 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62D10001

2025-10-14T09:34:20,158 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Comms ok, protocol = CAN Classic for node: 754

2025-10-14T09:34:20,160 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VCI supports CAN FD =  false

2025-10-14T09:34:20,162 ERROR otxcontainer.G2056515 - Error in application, message was: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
java.lang.ClassCastException: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:22) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.GuardedValue.setValue(GuardedValue.java:147) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:136) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at otxcontainer.G2056515$20.run(G2056515.java:36907) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:20,174 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Exception in StMin NOT overrided

2025-10-14T09:34:20,176 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases

2025-10-14T09:34:20,179 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37

2025-10-14T09:34:20,182 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37

2025-10-14T09:34:20,184 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ PingModule

2025-10-14T09:34:20,186 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EstablishCommsProcess

2025-10-14T09:34:20,188 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ReadPartNumDids

2025-10-14T09:34:20,192 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:34:20,195 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  00000754228068

2025-10-14T09:34:20,206 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,80,68]

2025-10-14T09:34:20,209 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,986,069,220 - [00,00,07,54]

2025-10-14T09:34:20,215 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,986,077,494 - [00,00,07,5C]

2025-10-14T09:34:20,218 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,986,079,399 - [00,00,07,5C,62,80,68,53,55,35,54,2D,31,34,48,32,34,30,2D,47,48,00,00,00,00,00,00,00,00,00,00]

2025-10-14T09:34:20,218 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C628068535535542D3134483234302D474800000000000000000000

2025-10-14T09:34:20,221 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 :Response byte size 24

2025-10-14T09:34:20,223 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 (HEX) =  535535542D3134483234302D474800000000000000000000

2025-10-14T09:34:20,227 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProcessDidResponseValues

2025-10-14T09:34:20,229 INFO class otxcontainer.G2056515.authorLogs - Part number byte 14 IS null

2025-10-14T09:34:20,231 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ProcessDidResponseValues

2025-10-14T09:34:20,235 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 (ASCII) =  SU5T-14H240-GH

2025-10-14T09:34:20,239 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 Type =  Boot Image

2025-10-14T09:34:20,242 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:34:20,245 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422F120

2025-10-14T09:34:20,254 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,F1,20]

2025-10-14T09:34:20,257 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,986,116,913 - [00,00,07,54]

2025-10-14T09:34:20,265 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,986,127,484 - [00,00,07,5C]

2025-10-14T09:34:20,267 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,986,129,369 - [00,00,07,5C,62,F1,20,53,55,35,54,2D,31,34,48,30,39,30,2D,41,47,48,00,00,00,00,00,00,00,00,00]

2025-10-14T09:34:20,267 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62F120535535542D3134483039302D414748000000000000000000

2025-10-14T09:34:20,270 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 :Response byte size 24

2025-10-14T09:34:20,273 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 (HEX) =  535535542D3134483039302D414748000000000000000000

2025-10-14T09:34:20,275 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ProcessDidResponseValues

2025-10-14T09:34:20,278 INFO class otxcontainer.G2056515.authorLogs - Part number byte 15 IS null

2025-10-14T09:34:20,279 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ProcessDidResponseValues

2025-10-14T09:34:20,282 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 (ASCII) =  SU5T-14H090-AGH

2025-10-14T09:34:20,284 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 Type =  Strategy

2025-10-14T09:34:20,285 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ReadPartNumDids

2025-10-14T09:34:20,288 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ValidateFlashActionDIDsAgainstModule

2025-10-14T09:34:20,290 INFO class otxcontainer.G2056515.authorLogs - sDidIdentifier = 8068

2025-10-14T09:34:20,291 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> 8068 Validation FAIL
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH

2025-10-14T09:34:21,294 INFO class otxcontainer.G2056515.authorLogs - sDidIdentifier = F120

2025-10-14T09:34:21,295 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> F120 Validation FAIL
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH

2025-10-14T09:34:22,299 INFO class otxcontainer.G2056515.authorLogs - here

2025-10-14T09:34:22,300 INFO class otxcontainer.G2056515.authorLogs - 1

2025-10-14T09:34:22,301 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> No Applications in Flash Action List to validate

2025-10-14T09:34:24,304 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Update failed!!

2025-10-14T09:34:24,306 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

	at otxcontainer.G2056515.ValidateFlashActionDIDsAgainstModule(G2056515.java:64126) [G2056515:?]
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64902) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:24,317 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:34:24,319 INFO class otxcontainer.G2056515.authorLogs - Keep bargraph

2025-10-14T09:34:24,321 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ValidateFlashActionDIDsAgainstModule - Exception qualifier =  ValidateFlashActionDIDsAgainstModule - Exception text = Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

2025-10-14T09:34:24,327 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateFlashActionDIDsAgainstModule text: Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ValidateFlashActionDIDsAgainstModule(G2056515.java:64152) ~[G2056515:?]
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64902) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:24,343 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateSoftwareUpdateProcess text: Validate exception
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateSoftwareUpdateProcess text: Validate exception
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:64932) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:25,853 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ValidateSoftwareUpdateProcess text: USB
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ValidateSoftwareUpdateProcess text: USB
	at otxcontainer.G2056515.ValidateSoftwareUpdateProcess(G2056515.java:65009) ~[G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61073) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:25,862 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> USB installation failure, bUSBSuccess = false

2025-10-14T09:34:39,240 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> CAN flash selected

2025-10-14T09:34:46,454 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EstablishCommsProcess

2025-10-14T09:34:47,490 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:34:49,490 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ PingModule

2025-10-14T09:34:49,492 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Pinging node = 754

2025-10-14T09:34:49,495 INFO class otxcontainer.G2056515.authorLogs - g_comChannelSet = false

2025-10-14T09:34:49,498 INFO class otxcontainer.G2056515.authorLogs - Com channel null, need to initialize

2025-10-14T09:34:49,501 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> ECU does not support CAN FD try CAN Classic for node: 754

2025-10-14T09:34:49,504 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: PingModule text: ECU does not support CAN FD
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: PingModule text: ECU does not support CAN FD
	at otxcontainer.G2056515$20.run(G2056515.java:35948) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:50,017 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 22

2025-10-14T09:34:50,019 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075422D100

2025-10-14T09:34:50,021 INFO impl.core.AbstractServiceFactory - Using pin switched protocol: ISO15765_PS instead of ISO15765

2025-10-14T09:34:50,070 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:34:50,073 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,22,D1,00]

2025-10-14T09:34:50,076 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,015,934,889 - [00,00,07,54]

2025-10-14T09:34:50,076 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,015,936,777 - [00,00,07,5C,62,D1,00,01]

2025-10-14T09:34:50,077 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C62D10001

2025-10-14T09:34:50,079 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Comms ok, protocol = CAN Classic for node: 754

2025-10-14T09:34:50,082 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> VCI supports CAN FD =  false

2025-10-14T09:34:50,084 ERROR otxcontainer.G2056515 - Error in application, message was: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
java.lang.ClassCastException: com.ford.etis.runtime.apps.otx.utils.types.diagcom.ComplexParameter cannot be cast to java.lang.Long
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:22) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.GuardedValue.setValue(GuardedValue.java:147) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at com.ford.etis.runtime.apps.otx.utils.types.core.IntegerVariable.setValue(IntegerVariable.java:136) ~[com.ford.otx.common.apps.utils-40.21.20.jar:?]
	at otxcontainer.G2056515$20.run(G2056515.java:36907) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:34:50,098 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Exception in StMin NOT overrided

2025-10-14T09:34:50,100 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases

2025-10-14T09:34:50,105 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37

2025-10-14T09:34:50,108 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37

2025-10-14T09:34:50,111 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ PingModule

2025-10-14T09:34:50,113 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EstablishCommsProcess

2025-10-14T09:34:50,115 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ FlashSoftwareOverCAN

2025-10-14T09:34:50,119 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash sequence: DID D027 is number 1

2025-10-14T09:34:50,121 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash sequence: DID F188 is number 2

2025-10-14T09:34:50,123 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash sequence: DID 8068 is number 3

2025-10-14T09:34:50,125 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash sequence: DID F120 is number 4

2025-10-14T09:34:50,128 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash sequence: DID F121 is number 5

2025-10-14T09:34:50,130 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ FlashSoftware

2025-10-14T09:34:50,132 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ControlTesterPresent_Functional

2025-10-14T09:34:50,135 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Turning TP ON

2025-10-14T09:34:50,182 INFO impl.legacy.PhysicalChannelImpl - started

2025-10-14T09:34:50,185 DEBUG api.service.Channel - ISO15765 TX         -> 0,000,000,000 - [00,00,07,DF,3E,80]

2025-10-14T09:34:50,206 INFO impl.core.AbstractServiceFactory - Using pin switched protocol: ISO15765_PS instead of ISO15765

2025-10-14T09:34:50,209 DEBUG api.service.Channel - ISO15765 TX         -> 1,016,068,429 - [00,00,07,DF]

2025-10-14T09:34:50,214 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,DF,3E,80]

2025-10-14T09:34:50,230 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,016,089,735 - [00,00,07,DF]

2025-10-14T09:34:50,227 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ControlTesterPresent_Functional

2025-10-14T09:34:51,230 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 10

2025-10-14T09:34:51,232 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> sub function = 02

2025-10-14T09:34:51,234 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Request parameters =

2025-10-14T09:34:51,236 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  000007541002

2025-10-14T09:34:51,252 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,10,02]

2025-10-14T09:34:51,259 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,017,113,567 - [00,00,07,54]

2025-10-14T09:34:51,259 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,017,116,727 - [00,00,07,5C,50,02,00,19,01,F4]

2025-10-14T09:34:51,259 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C5002001901F4

2025-10-14T09:34:51,261 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service parsed response:  001901F4

2025-10-14T09:34:51,764 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GainSecurityAccess

2025-10-14T09:34:51,773 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> DA01 = DSMU5T-14H074-ABR

2025-10-14T09:34:51,783 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 27

2025-10-14T09:34:51,785 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> sub function = 01

2025-10-14T09:34:51,788 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Request parameters =

2025-10-14T09:34:51,790 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  000007542701

2025-10-14T09:34:51,806 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,27,01]

2025-10-14T09:34:51,811 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,017,668,207 - [00,00,07,54]

2025-10-14T09:34:51,821 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,017,676,711 - [00,00,07,5C]

2025-10-14T09:34:51,821 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,017,678,415 - [00,00,07,5C,67,01,D4,F8,E6,33,8A,89,A4,DC,E9,25,D0,DD,0F,B7,30,CA]

2025-10-14T09:34:51,821 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C6701D4F8E6338A89A4DCE925D0DD0FB730CA

2025-10-14T09:34:51,824 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Seed = D4F8E6338A89A4DCE925D0DD0FB730CA

2025-10-14T09:34:51,826 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Security access level = 01

2025-10-14T09:34:51,828 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Level 1 SEED = D4F8E6338A89A4DCE925D0DD0FB730CA

2025-10-14T09:34:52,207 DEBUG api.service.Channel - ISO15765 TX         -> 1,018,068,060 - [00,00,07,DF]

2025-10-14T09:34:52,230 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,018,089,749 - [00,00,07,DF]

2025-10-14T09:34:54,207 DEBUG api.service.Channel - ISO15765 TX         -> 1,020,067,480 - [00,00,07,DF]

2025-10-14T09:34:54,228 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,020,089,160 - [00,00,07,DF]

2025-10-14T09:34:55,964 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Level 2 KEY = ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF

2025-10-14T09:34:55,967 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 27

2025-10-14T09:34:55,969 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> sub function = 02

2025-10-14T09:34:55,971 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Request parameters = ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF

2025-10-14T09:34:55,973 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  000007542702ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF

2025-10-14T09:34:55,992 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,27,02,AD,BE,2E,EC,DA,15,FA,0D,33,CE,00,DC,BC,9B,59,90,B5,CF]

2025-10-14T09:34:55,997 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,021,853,466 - [00,00,07,54]

2025-10-14T09:34:55,997 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,021,856,706 - [00,00,07,5C,67,02]

2025-10-14T09:34:55,997 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C6702

2025-10-14T09:34:55,999 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Security access level = 02

2025-10-14T09:34:56,002 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GainSecurityAccess

2025-10-14T09:34:56,004 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> bFlashALL set to: true

2025-10-14T09:34:56,006 INFO class otxcontainer.G2056515.authorLogs - SBLfile is null = true

2025-10-14T09:34:56,007 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> About to download: D027 = SU5T-14H241-HL

2025-10-14T09:34:56,011 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ DownloadFiles

2025-10-14T09:34:56,014 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Download file started: SU5T-14H241-HL

2025-10-14T09:34:56,026 INFO parser.vbf.VbfParser - Lazy VBF parser is used. It is configured by vbf.parser.lazy system property

2025-10-14T09:34:56,041 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Completed Erase Routine

2025-10-14T09:34:56,044 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ TransferBlockData

2025-10-14T09:34:56,047 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> service id = 34

2025-10-14T09:34:56,050 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> sub function =

2025-10-14T09:34:56,053 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Request parameters = 004400000001000002F5

2025-10-14T09:34:56,055 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service request :  0000075434004400000001000002F5

2025-10-14T09:34:56,078 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,54,34,00,44,00,00,00,01,00,00,02,F5]

2025-10-14T09:34:56,080 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,021,938,654 - [00,00,07,54]

2025-10-14T09:34:56,098 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,021,956,561 - [00,00,07,5C,7F,34,78]

2025-10-14T09:34:56,211 DEBUG api.service.Channel - ISO15765 TX         -> 1,022,066,952 - [00,00,07,DF]

2025-10-14T09:34:56,232 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,022,088,671 - [00,00,07,DF]

2025-10-14T09:34:58,211 DEBUG api.service.Channel - ISO15765 TX         -> 1,024,066,387 - [00,00,07,DF]

2025-10-14T09:34:58,227 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,024,088,090 - [00,00,07,DF]

2025-10-14T09:35:00,208 DEBUG api.service.Channel - ISO15765 TX         -> 1,026,065,811 - [00,00,07,DF]

2025-10-14T09:35:00,232 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,026,087,504 - [00,00,07,DF]

2025-10-14T09:35:00,799 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,026,656,414 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:02,208 DEBUG api.service.Channel - ISO15765 TX         -> 1,028,065,213 - [00,00,07,DF]

2025-10-14T09:35:02,229 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,028,086,943 - [00,00,07,DF]

2025-10-14T09:35:04,206 DEBUG api.service.Channel - ISO15765 TX         -> 1,030,064,694 - [00,00,07,DF]

2025-10-14T09:35:04,229 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,030,086,404 - [00,00,07,DF]

2025-10-14T09:35:05,501 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,031,356,253 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:06,205 DEBUG api.service.Channel - ISO15765 TX         -> 1,032,064,136 - [00,00,07,DF]

2025-10-14T09:35:06,230 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,032,085,835 - [00,00,07,DF]

2025-10-14T09:35:08,207 DEBUG api.service.Channel - ISO15765 TX         -> 1,034,063,459 - [00,00,07,DF]

2025-10-14T09:35:08,225 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,034,085,006 - [00,00,07,DF]

2025-10-14T09:35:10,199 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,036,056,117 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:10,207 DEBUG api.service.Channel - ISO15765 TX         -> 1,036,062,597 - [00,00,07,DF]

2025-10-14T09:35:10,225 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,036,084,143 - [00,00,07,DF]

2025-10-14T09:35:12,204 DEBUG api.service.Channel - ISO15765 TX         -> 1,038,061,722 - [00,00,07,DF]

2025-10-14T09:35:12,225 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,038,083,319 - [00,00,07,DF]

2025-10-14T09:35:14,204 DEBUG api.service.Channel - ISO15765 TX         -> 1,040,060,902 - [00,00,07,DF]

2025-10-14T09:35:14,224 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,040,082,482 - [00,00,07,DF]

2025-10-14T09:35:14,896 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,040,755,953 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:16,204 DEBUG api.service.Channel - ISO15765 TX         -> 1,042,060,149 - [00,00,07,DF]

2025-10-14T09:35:16,225 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,042,081,843 - [00,00,07,DF]

2025-10-14T09:35:18,200 DEBUG api.service.Channel - ISO15765 TX         -> 1,044,059,544 - [00,00,07,DF]

2025-10-14T09:35:18,226 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,044,081,252 - [00,00,07,DF]

2025-10-14T09:35:19,601 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,045,455,812 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:20,200 DEBUG api.service.Channel - ISO15765 TX         -> 1,046,058,979 - [00,00,07,DF]

2025-10-14T09:35:20,222 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,046,080,699 - [00,00,07,DF]

2025-10-14T09:35:22,199 DEBUG api.service.Channel - ISO15765 TX         -> 1,048,058,420 - [00,00,07,DF]

2025-10-14T09:35:22,224 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,048,080,117 - [00,00,07,DF]

2025-10-14T09:35:24,201 DEBUG api.service.Channel - ISO15765 TX         -> 1,050,057,849 - [00,00,07,DF]

2025-10-14T09:35:24,225 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,050,079,542 - [00,00,07,DF]

2025-10-14T09:35:24,297 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,050,155,651 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:26,198 DEBUG api.service.Channel - ISO15765 TX         -> 1,052,057,272 - [00,00,07,DF]

2025-10-14T09:35:26,220 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,052,078,965 - [00,00,07,DF]

2025-10-14T09:35:28,200 DEBUG api.service.Channel - ISO15765 TX         -> 1,054,056,699 - [00,00,07,DF]

2025-10-14T09:35:28,220 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,054,078,435 - [00,00,07,DF]

2025-10-14T09:35:28,997 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,054,855,508 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:30,198 DEBUG api.service.Channel - ISO15765 TX         -> 1,056,056,186 - [00,00,07,DF]

2025-10-14T09:35:30,219 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,056,077,896 - [00,00,07,DF]

2025-10-14T09:35:32,197 DEBUG api.service.Channel - ISO15765 TX         -> 1,058,055,611 - [00,00,07,DF]

2025-10-14T09:35:32,223 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,058,077,303 - [00,00,07,DF]

2025-10-14T09:35:32,415 INFO dflt.memory.MemoryMonitor - [MEMORY] Available virtual memory: 489 MB

2025-10-14T09:35:33,696 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,059,555,350 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:34,197 DEBUG api.service.Channel - ISO15765 TX         -> 1,060,055,016 - [00,00,07,DF]

2025-10-14T09:35:34,218 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,060,076,725 - [00,00,07,DF]

2025-10-14T09:35:36,200 DEBUG api.service.Channel - ISO15765 TX         -> 1,062,054,445 - [00,00,07,DF]

2025-10-14T09:35:36,221 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,062,076,166 - [00,00,07,DF]

2025-10-14T09:35:38,196 DEBUG api.service.Channel - ISO15765 TX         -> 1,064,053,896 - [00,00,07,DF]

2025-10-14T09:35:38,222 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,064,075,588 - [00,00,07,DF]

2025-10-14T09:35:38,396 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,064,255,201 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:40,197 DEBUG api.service.Channel - ISO15765 TX         -> 1,066,053,315 - [00,00,07,DF]

2025-10-14T09:35:40,219 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,066,075,013 - [00,00,07,DF]

2025-10-14T09:35:42,197 DEBUG api.service.Channel - ISO15765 TX         -> 1,068,052,764 - [00,00,07,DF]

2025-10-14T09:35:42,221 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,068,074,477 - [00,00,07,DF]

2025-10-14T09:35:43,097 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,068,955,043 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:44,196 DEBUG api.service.Channel - ISO15765 TX         -> 1,070,052,221 - [00,00,07,DF]

2025-10-14T09:35:44,219 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,070,073,942 - [00,00,07,DF]

2025-10-14T09:35:46,197 DEBUG api.service.Channel - ISO15765 TX         -> 1,072,051,676 - [00,00,07,DF]

2025-10-14T09:35:46,218 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,072,073,359 - [00,00,07,DF]

2025-10-14T09:35:47,799 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,073,654,898 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:48,193 DEBUG api.service.Channel - ISO15765 TX         -> 1,074,051,087 - [00,00,07,DF]

2025-10-14T09:35:48,214 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,074,072,779 - [00,00,07,DF]

2025-10-14T09:35:50,195 DEBUG api.service.Channel - ISO15765 TX         -> 1,076,050,492 - [00,00,07,DF]

2025-10-14T09:35:50,215 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,076,072,188 - [00,00,07,DF]

2025-10-14T09:35:52,195 DEBUG api.service.Channel - ISO15765 TX         -> 1,078,050,003 - [00,00,07,DF]

2025-10-14T09:35:52,218 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,078,071,760 - [00,00,07,DF]

2025-10-14T09:35:52,500 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,078,354,743 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:54,194 DEBUG api.service.Channel - ISO15765 TX         -> 1,080,049,506 - [00,00,07,DF]

2025-10-14T09:35:54,214 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,080,071,213 - [00,00,07,DF]

2025-10-14T09:35:56,193 DEBUG api.service.Channel - ISO15765 TX         -> 1,082,048,936 - [00,00,07,DF]

2025-10-14T09:35:56,216 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,082,070,633 - [00,00,07,DF]

2025-10-14T09:35:57,200 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,083,054,599 - [00,00,07,5C,7F,34,78]

2025-10-14T09:35:58,194 DEBUG api.service.Channel - ISO15765 TX         -> 1,084,048,355 - [00,00,07,DF]

2025-10-14T09:35:58,214 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,084,070,069 - [00,00,07,DF]

2025-10-14T09:36:00,191 DEBUG api.service.Channel - ISO15765 TX         -> 1,086,047,798 - [00,00,07,DF]

2025-10-14T09:36:00,212 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,086,069,494 - [00,00,07,DF]

2025-10-14T09:36:01,899 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,087,754,445 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:02,189 DEBUG api.service.Channel - ISO15765 TX         -> 1,088,047,221 - [00,00,07,DF]

2025-10-14T09:36:02,215 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,088,068,926 - [00,00,07,DF]

2025-10-14T09:36:04,191 DEBUG api.service.Channel - ISO15765 TX         -> 1,090,046,658 - [00,00,07,DF]

2025-10-14T09:36:04,211 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,090,068,357 - [00,00,07,DF]

2025-10-14T09:36:06,191 DEBUG api.service.Channel - ISO15765 TX         -> 1,092,046,078 - [00,00,07,DF]

2025-10-14T09:36:06,211 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,092,067,781 - [00,00,07,DF]

2025-10-14T09:36:06,599 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,092,454,289 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:08,188 DEBUG api.service.Channel - ISO15765 TX         -> 1,094,045,495 - [00,00,07,DF]

2025-10-14T09:36:08,213 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,094,067,212 - [00,00,07,DF]

2025-10-14T09:36:10,191 DEBUG api.service.Channel - ISO15765 TX         -> 1,096,044,932 - [00,00,07,DF]

2025-10-14T09:36:10,213 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,096,066,642 - [00,00,07,DF]

2025-10-14T09:36:11,297 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,097,154,140 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:12,189 DEBUG api.service.Channel - ISO15765 TX         -> 1,098,044,385 - [00,00,07,DF]

2025-10-14T09:36:12,212 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,098,066,090 - [00,00,07,DF]

2025-10-14T09:36:14,186 DEBUG api.service.Channel - ISO15765 TX         -> 1,100,043,835 - [00,00,07,DF]

2025-10-14T09:36:14,213 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,100,065,557 - [00,00,07,DF]

2025-10-14T09:36:15,999 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,101,853,983 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:16,186 DEBUG api.service.Channel - ISO15765 TX         -> 1,102,043,302 - [00,00,07,DF]

2025-10-14T09:36:16,207 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,102,064,997 - [00,00,07,DF]

2025-10-14T09:36:18,187 DEBUG api.service.Channel - ISO15765 TX         -> 1,104,042,727 - [00,00,07,DF]

2025-10-14T09:36:18,208 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,104,064,484 - [00,00,07,DF]

2025-10-14T09:36:20,188 DEBUG api.service.Channel - ISO15765 TX         -> 1,106,042,228 - [00,00,07,DF]

2025-10-14T09:36:20,211 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,106,063,924 - [00,00,07,DF]

2025-10-14T09:36:20,701 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,106,553,835 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:22,187 DEBUG api.service.Channel - ISO15765 TX         -> 1,108,041,638 - [00,00,07,DF]

2025-10-14T09:36:22,210 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,108,063,358 - [00,00,07,DF]

2025-10-14T09:36:24,188 DEBUG api.service.Channel - ISO15765 TX         -> 1,110,041,097 - [00,00,07,DF]

2025-10-14T09:36:24,208 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,110,062,798 - [00,00,07,DF]

2025-10-14T09:36:25,401 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,111,253,681 - [00,00,07,5C,7F,34,78]

2025-10-14T09:36:26,151 DEBUG api.service.Channel - ISO15765_PS RX      <- 1,112,003,643 - [00,00,07,5C,7F,34,22]

2025-10-14T09:36:26,151 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Diag service response:  0000075C7F3422

2025-10-14T09:36:26,153 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Constant-field byte 4 (hex) : 7F

2025-10-14T09:36:26,156 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> NRC = 22 (conditionsNotCorrect)

2025-10-14T09:36:26,183 DEBUG api.service.Channel - ISO15765 TX         -> 1,112,040,508 - [00,00,07,DF]

2025-10-14T09:36:26,209 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,112,062,205 - [00,00,07,DF]

2025-10-14T09:36:28,184 DEBUG api.service.Channel - ISO15765 TX         -> 1,114,039,992 - [00,00,07,DF]

2025-10-14T09:36:28,207 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,114,061,679 - [00,00,07,DF]

2025-10-14T09:36:30,187 DEBUG api.service.Channel - ISO15765 TX         -> 1,116,039,405 - [00,00,07,DF]

2025-10-14T09:36:30,204 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,116,061,096 - [00,00,07,DF]

2025-10-14T09:36:31,577 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

2025-10-14T09:36:31,580 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
	at otxcontainer.G2056515.ExecuteMdxFreeDiagService(G2056515.java) [G2056515:?]
	at otxcontainer.G2056515.Service_34(G2056515.java:55381) [G2056515:?]
	at otxcontainer.G2056515.TransferBlockData(G2056515.java:58525) [G2056515:?]
	at otxcontainer.G2056515.DownloadFiles(G2056515.java) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftware(G2056515.java:18305) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19353) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:31,589 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:31,592 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:31,801 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:36:32,184 DEBUG api.service.Channel - ISO15765 TX         -> 1,118,038,819 - [00,00,07,DF]

2025-10-14T09:36:32,205 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,118,060,548 - [00,00,07,DF]

2025-10-14T09:36:32,595 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ExecuteMdxFreeDiagService(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.Service_34(G2056515.java:55381) [G2056515:?]
	at otxcontainer.G2056515.TransferBlockData(G2056515.java:58525) [G2056515:?]
	at otxcontainer.G2056515.DownloadFiles(G2056515.java) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftware(G2056515.java:18305) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19353) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:32,603 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:32,605 INFO class otxcontainer.G2056515.authorLogs - Keep bargraph

2025-10-14T09:36:32,606 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = Service_34 - Exception qualifier =  ExecuteMdxFreeDiagService - Exception text = NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.

2025-10-14T09:36:32,611 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: ExecuteMdxFreeDiagService text: NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.Service_34(G2056515.java:55505) ~[G2056515:?]
	at otxcontainer.G2056515.TransferBlockData(G2056515.java:58525) [G2056515:?]
	at otxcontainer.G2056515.DownloadFiles(G2056515.java) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftware(G2056515.java:18305) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19353) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:32,619 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ TransferBlockData

2025-10-14T09:36:32,620 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Download file failed

2025-10-14T09:36:32,622 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ DownloadFiles

2025-10-14T09:36:32,625 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Failed to flash SU5T-14H241-HL

2025-10-14T09:36:32,628 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.FlashSoftware(G2056515.java:18389) [G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19353) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:32,637 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> SW Update Failed

2025-10-14T09:36:32,639 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:32,641 INFO class otxcontainer.G2056515.authorLogs - Keep bargraph

2025-10-14T09:36:32,642 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = FlashSoftware - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:32,645 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.FlashSoftware(G2056515.java:18867) ~[G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19353) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:33,804 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BargraphDisplayV2

2025-10-14T09:36:34,182 DEBUG api.service.Channel - ISO15765 TX         -> 1,120,038,292 - [00,00,07,DF]

2025-10-14T09:36:34,204 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,120,059,982 - [00,00,07,DF]

2025-10-14T09:36:36,165 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Flash programming failed, exit process

2025-10-14T09:36:36,168 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:36,171 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:36,182 DEBUG api.service.Channel - ISO15765 TX         -> 1,122,037,707 - [00,00,07,DF]

2025-10-14T09:36:36,208 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,122,059,400 - [00,00,07,DF]

2025-10-14T09:36:36,377 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:36:37,173 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = FlashSoftwareOverCAN - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:37,177 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19641) [G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:37,187 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:37,188 INFO class otxcontainer.G2056515.authorLogs - Keep bargraph

2025-10-14T09:36:37,190 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = FlashSoftwareOverCAN - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:37,193 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.FlashSoftwareOverCAN(G2056515.java:19684) ~[G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61757) [G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:37,202 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:37,204 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:38,181 DEBUG api.service.Channel - ISO15765 TX         -> 1,124,037,161 - [00,00,07,DF]

2025-10-14T09:36:38,205 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,124,058,876 - [00,00,07,DF]

2025-10-14T09:36:38,206 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = UpdateSoftwareOverUSB - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:38,209 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.UpdateSoftwareOverUSB(G2056515.java:61915) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41610) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:38,219 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Update software programming failed, exit process

2025-10-14T09:36:38,221 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:38,223 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:38,379 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ BargraphDisplayV2

2025-10-14T09:36:39,224 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ProgramModule - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:39,228 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:41872) [G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) [G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:39,237 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:39,239 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:39,445 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ BargraphDisplayV2

2025-10-14T09:36:40,183 DEBUG api.service.Channel - ISO15765 TX         -> 1,126,036,614 - [00,00,07,DF]

2025-10-14T09:36:40,204 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,126,058,320 - [00,00,07,DF]

2025-10-14T09:36:40,240 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = ProgramModule - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:40,243 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.ProgramModule(G2056515.java:42053) ~[G2056515:?]
	at otxcontainer.G2056515.access$5800(G2056515.java:89) ~[G2056515:?]
	at otxcontainer.G2056515$32.run(G2056515.java:57665) [G2056515:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) [?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) [?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:40,254 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ EndBargraph

2025-10-14T09:36:41,756 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ EndBargraph

2025-10-14T09:36:41,759 ERROR otx.utils.ParallelExecutorOld - [TG] Parallel executor thread Thread[parallel-executor-232-thread-2,5,tg-G2056515] got exception -> com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL

2025-10-14T09:36:41,767 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515$32.run(G2056515.java:57716) ~[?:?]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[?:1.8.0_171]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[?:1.8.0_171]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:41,780 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:41,782 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:42,182 DEBUG api.service.Channel - ISO15765 TX         -> 1,128,036,044 - [00,00,07,DF]

2025-10-14T09:36:42,202 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,128,057,770 - [00,00,07,DF]

2025-10-14T09:36:42,785 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = SoftwareUpdateProcess - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:42,788 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.SoftwareUpdateProcess(G2056515.java:57831) ~[G2056515:?]
	at otxcontainer.G2056515.SoftwareUpdateProcess(G2056515.java:57848) ~[G2056515:?]
	at otxcontainer.G2056515.OTXAppFlowControl(G2056515.java:3014) [G2056515:?]
	at otxcontainer.G2056515.main(G2056515.java:2593) [G2056515:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication.startApp(BaseApplication.java:400) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication.access$200(BaseApplication.java:123) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication$1.run(BaseApplication.java:287) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:42,798 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:42,800 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:43,801 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = OTXAppFlowControl - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:43,804 ERROR otxcontainer.G2056515 - Error in application, message was: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
com.ford.etis.runtime.apps.otx.utils.exceptions.UserExceptionLiteral: Qualifier: FlashSoftware text: Failed to flash SU5T-14H241-HL
	at otxcontainer.G2056515.ExceptionHandler(G2056515.java) ~[G2056515:?]
	at otxcontainer.G2056515.OTXAppFlowControl(G2056515.java:3121) ~[G2056515:?]
	at otxcontainer.G2056515.main(G2056515.java:2593) [G2056515:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication.startApp(BaseApplication.java:400) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication.access$200(BaseApplication.java:123) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at com.ford.etis.runtime.apps.otx.core.BaseApplication$1.run(BaseApplication.java:287) [com.ford.otx.apps.otx-72.31.54.jar:?]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_171]

2025-10-14T09:36:43,814 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> >>>EXCEPTIONHANDLER>>>

2025-10-14T09:36:43,815 INFO class otxcontainer.G2056515.authorLogs - End bargraph

2025-10-14T09:36:44,182 DEBUG api.service.Channel - ISO15765 TX         -> 1,130,035,489 - [00,00,07,DF]

2025-10-14T09:36:44,203 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,130,057,246 - [00,00,07,DF]

2025-10-14T09:36:44,818 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure name = main - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

2025-10-14T09:36:44,821 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ ApplicationExitAndCleanUp

2025-10-14T09:36:44,823 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> BEGIN ~~ GetApplicationState

2025-10-14T09:36:44,825 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Getting ApplicationState = APPLICATION_SKIPPED

2025-10-14T09:36:44,827 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ GetApplicationState

2025-10-14T09:36:46,180 DEBUG api.service.Channel - ISO15765 TX         -> 1,132,034,990 - [00,00,07,DF]

2025-10-14T09:36:46,206 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,132,056,694 - [00,00,07,DF]

2025-10-14T09:36:48,182 DEBUG api.service.Channel - ISO15765 TX         -> 1,134,034,420 - [00,00,07,DF]

2025-10-14T09:36:48,205 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,134,056,118 - [00,00,07,DF]

2025-10-14T09:36:50,178 DEBUG api.service.Channel - ISO15765 TX         -> 1,136,033,833 - [00,00,07,DF]

2025-10-14T09:36:50,204 DEBUG api.service.Channel - ISO15765_PS TX      -> 1,136,055,536 - [00,00,07,DF]

2025-10-14T09:36:50,931 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:36:50,961 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> Procedure exit reason: Failed to flash SU5T-14H241-HL

2025-10-14T09:36:50,961 INFO impl.legacy.PhysicalChannelImpl - Thread complete

2025-10-14T09:36:50,963 INFO class otxcontainer.G2056515.authorLogs - 

LOG>> END ~~ ApplicationExitAndCleanUp

2025-10-14T09:36:50,969 INFO class otxcontainer.G2056515.authorLogs - 

***** DEBUG LOG RESULTS *****
TCU SoftwareUpdate
Based on template version: MDX_FREE_TEMPLATE_VER_14.0
OTX_APP_VERSION: 3.1

BEGIN ~~ InitAppInfo

BEGIN ~~ SetApplicationState
Setting ApplicationState = FINISHED
END ~~ SetApplicationState
END ~~ InitAppInfo

BEGIN ~~ OTXAppFlowControl

BEGIN ~~ GetVehicleNodeInfoProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ GetVehicleNodeInfo
Node address:    754
VIN:    1FBAX2YG0PKA54057
ECU acronym:    TCU
GVMS CDL DID  DE10 = 001B1067 (null) - Configuration
GVMS CDL DID  F16C = MU5T-14H100-AAJ (null) - ECU Configuration
GVMS CDL DID  DE00 = 1802000000 (null) - Configuration
GVMS CDL DID  DE0A = AA (null) - Configuration
GVMS CDL DID  41AE = 89011703272237429515 (null) - 
GVMS CDL DID  DE03 = 006496012C006402580A007800050A003C003C00140C (null) - Configuration
GVMS CDL DID  EEFA = 31633761313335320000000000000000 (null) - 
GVMS CDL DID  DE0D = 4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B3C3C3C3C3C3C3C323C3C3C32 (null) - Configuration
GVMS CDL DID  D027 = SU5T-14H241-GH (null) - Boot Image
GVMS CDL DID  F121 = MU5T-14H090-BAZ (null) - Strategy
GVMS CDL DID  DE11 = 626F6F7473747261702E7362312E6175746F6E6F6D69632E61693A38303930000000000000000000 (null) - Configuration
GVMS CDL DID  F17F = 1TA1QBTT (null) - Serial Number
GVMS CDL DID  DE04 = 70726F6430346E6177696669666F7264000000000000000000000000000000000000000000000000 (null) - Configuration
GVMS CDL DID  DE0B = 00 (null) - Configuration
GVMS CDL DID  F120 = SU5T-14H090-AGH (null) - Strategy
GVMS CDL DID  F166 = 23041103 (null) - 
GVMS CDL DID  EEFB = 3337333835333332333033303331333732363330303130393230323231313135 (null) - 
GVMS CDL DID  F188 = SU5T-14H085-GH (null) - Strategy
GVMS CDL DID  DE07 = 1D00596F (null) - Configuration
GVMS CDL DID  DE0E = 31304544050701 (null) - Configuration
GVMS CDL DID  DEFF = 0507 (null) - Configuration
GVMS CDL DID  DE0C = 000102050202020502020205000102050303030A0303030A0002030A0404040F0404040F (null) - Configuration
GVMS CDL DID  DE05 = 00000000000000000000000000000000000000000000000000000000000000000000000000000000 (null) - Configuration
GVMS CDL DID  F15F = 0805113D030000000000 (null) - 
GVMS CDL DID  DE0F = 00 (null) - Configuration
GVMS CDL DID  DE01 = 1D00000010 (null) - Configuration
GVMS CDL DID  F110 = DSMU5T-14H074-ABR (null) - Part II Specification
GVMS CDL DID  8068 = SU5T-14H240-GH (null) - Boot Image
GVMS CDL DID  F18C = FUBCH23006110995 (null) - Serial Number
GVMS CDL DID  DE08 = 0000000000000000000000000000000000000000 (null) - Configuration
GVMS CDL DID  DE06 = 0203596F (null) - Configuration
GVMS CDL DID  F163 = 05 (null) - ECU Diagnostic Spec
GVMS CDL DID  D040 = 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (null) - 
GVMS CDL DID  F111 = NU5T-14H089-FDA (null) - Core Assembly
GVMS CDL DID  F113 = NU5T-14H074-FLA (null) - Assembly
GVMS CDL DID  DE09 = 5553 (null) - Configuration
GVMS CDL DID  DE02 = 0A00F13530CD523C1E2D005A000F05096050500010002A887D03C0BFFCA01C4044 (null) - Configuration
DE00 is a DExx DID
DE01 is a DExx DID
DE02 is a DExx DID
DE03 is a DExx DID
DE04 is a DExx DID
DE05 is a DExx DID
DE06 is a DExx DID
DE07 is a DExx DID
DE08 is a DExx DID
DE09 is a DExx DID
DE0A is a DExx DID
DE0B is a DExx DID
DE0C is a DExx DID
DE0D is a DExx DID
DE0E is a DExx DID
DE0F is a DExx DID
DE10 is a DExx DID
DE11 is a DExx DID
DEFF is a DExx DID
Number of DExx config DIDs =    19
Config range start = DE00  Config range end = DEFF
END ~~ GetVehicleNodeInfo
Network = HS2
Transmit address:    00000754
Response address:    0000075C

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ GetVehicleNodeInfoProcess

BEGIN ~~ InitialSetupInformation
Application type - Software Update

BEGIN ~~ EstablishCommsProcess

BEGIN ~~ BargraphDisplayV2
Closing comms exception for g_ComChannel

BEGIN ~~ PingModule

Pinging node = 754
ECU does not support CAN FD try CAN Classic for node: 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok, protocol = CAN Classic for node: 754
VCI supports CAN FD =  false
Exception in StMin NOT overrided
Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases
Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37 
Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37 
END ~~ PingModule

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ EstablishCommsProcess

BEGIN ~~ ReadDirectConfigProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ PingModule

Pinging node = 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok for node: 754
END ~~ PingModule

BEGIN ~~ ReadConfigDids

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE10
Diag service response:  0000075C62DE10001B1067
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE10 = 001B1067

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE00
Diag service response:  0000075C62DE001802000000
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE00 = 1802000000

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0A
Diag service response:  0000075C62DE0AAA
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0A = AA

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE03
Diag service response:  0000075C62DE03006496012C006402580A007800050A003C003C00140C
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE03 = 006496012C006402580A007800050A003C003C00140C

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0D
Diag service response:  0000075C62DE0D4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B3C3C3C3C3C3C3C323C3C3C32
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0D = 4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B4B3C3C3C3C3C3C3C323C3C3C32

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE13
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
>>>EXCEPTIONHANDLER>>>
Cannot read DID: DE13

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DEFE
Diag service response:  0000075C62DEFE00006E
END ~~ ReadDid
(HEX) Read from module BEFORE config write DEFE = 00006E

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE11
Diag service response:  0000075C62DE11626F6F7473747261702E7362312E6175746F6E6F6D69632E61693A38303930000000000000000000
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE11 = 626F6F7473747261702E7362312E6175746F6E6F6D69632E61693A38303930000000000000000000

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE04
Diag service response:  0000075C62DE0470726F6430346E6177696669666F7264000000000000000000000000000000000000000000000000
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE04 = 70726F6430346E6177696669666F7264000000000000000000000000000000000000000000000000

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0B
Diag service response:  0000075C62DE0B00
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0B = 00

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE14
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
>>>EXCEPTIONHANDLER>>>
Cannot read DID: DE14

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE07
Diag service response:  0000075C62DE071D00596F
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE07 = 1D00596F

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0E
Diag service response:  0000075C62DE0E31304544050701
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0E = 31304544050701

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DEFF
Diag service response:  0000075C62DEFF0507
END ~~ ReadDid
(HEX) Read from module BEFORE config write DEFF = 0507

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0C
Diag service response:  0000075C62DE0C000102050202020502020205000102050303030A0303030A0002030A0404040F0404040F
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0C = 000102050202020502020205000102050303030A0303030A0002030A0404040F0404040F

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE15
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
>>>EXCEPTIONHANDLER>>>
Cannot read DID: DE15

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE05
Diag service response:  0000075C62DE0500000000000000000000000000000000000000000000000000000000000000000000000000000000
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE05 = 00000000000000000000000000000000000000000000000000000000000000000000000000000000

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE0F
Diag service response:  0000075C62DE0F00
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE0F = 00

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE01
Diag service response:  0000075C62DE011D00000010
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE01 = 1D00000010

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE08
Diag service response:  0000075C62DE080000000000000000000000000000000000000000
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE08 = 0000000000000000000000000000000000000000

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE06
Diag service response:  0000075C62DE060203596F
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE06 = 0203596F

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE16
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
>>>EXCEPTIONHANDLER>>>
Cannot read DID: DE16

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE09
Diag service response:  0000075C62DE095553
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE09 = 5553

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE12
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
>>>EXCEPTIONHANDLER>>>
Cannot read DID: DE12

BEGIN ~~ ReadDid

service id = 22
Diag service request :  0000075422DE02
Diag service response:  0000075C62DE020A00F13530CD523C1E2D005A000F05096050500010002A887D03C0BFFCA01C4044
END ~~ ReadDid
(HEX) Read from module BEFORE config write DE02 = 0A00F13530CD523C1E2D005A000F05096050500010002A887D03C0BFFCA01C4044
END ~~ ReadConfigDids

BEGIN ~~ DTC_Check
service id = 19
Diag service request :  0000075419028F
Diag service response:  0000075C5902CBDA010949F0004949

BEGIN ~~ DtcParserService
Input DTC byte field: 0000075C5902CBDA010949F0004949
Parsed DTC byte field: DA010949F0004949

DTC #1
DTC raw hex value: DA010949
DTC number (hex):  DA01
DTC fault byte:  09
DTC fault status:  49
DTC number (display):  U1A01
DTC description = Communication Link


DTC #2
DTC raw hex value: F0004949
DTC number (hex):  F000
DTC fault byte:  49
DTC fault status:  49
DTC number (display):  U3000
DTC description = Control Module

END ~~ DtcParserService
END ~~ DTC_Check

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ ReadDirectConfigProcess
END ~~ InitialSetupInformation

BEGIN ~~ GetFlashActionsProcess

BEGIN ~~ GetFlashActions

BEGIN ~~ BargraphDisplayV2
END ~~ GetFlashActions

BEGIN ~~ ParseFlashActionData

in_FlashActionList size = 1

flashAction.id = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539-1.0.0
flashAction.parser = MR
flashAction.targetNode = 1876




flashActionAssembly number 1 of 1
flashActionAssembly.currentAssembly = NU5T-14H089-FDA
flashActionAssembly.availableAssembly = NU5T-14H089-FDA
flashActionAssembly.directivesFileDownloadId = FENIX
flashActionAssembly.hasActionID.value = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539
flashActionAssembly.hasActionID.revision = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539
targetNodeAddress = 0754

null pointer =  java.lang.NullPointerException
firstCondition is null, there are no HasAction conditions for this node


Flash Action DID = 8068
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H240-HL
assemblySoftware.softwareSize = 1994025
assemblySoftware.didValue (Decimal) = 32872
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F188
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H085-HL
assemblySoftware.softwareSize = 678033
assemblySoftware.didValue (Decimal) = 61832
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = D027
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H241-HL
assemblySoftware.softwareSize = 50860
assemblySoftware.didValue (Decimal) = 53287
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F121
assemblySoftware.type = STRATEGY
assemblySoftware.id = MU5T-14H090-BAZ
assemblySoftware.softwareSize = 48761810
assemblySoftware.didValue (Decimal) = 61729
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F120
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H090-AHL
assemblySoftware.softwareSize = 98168657
assemblySoftware.didValue (Decimal) = 61728
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


END ~~ ParseFlashActionData

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ GetFlashActionsProcess

BEGIN ~~ ReadPartNumDIDsProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ PingModule

Pinging node = 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok for node: 754
END ~~ PingModule

BEGIN ~~ ReadPartNumDids

service id = 22
Diag service request :  0000075422F16C
Diag service response:  0000075C62F16C4D5535542D3134483130302D41414A000000000000000000
F16C (HEX) =  4D5535542D3134483130302D41414A000000000000000000
F16C (ASCII) =  MU5T-14H100-AAJ
F16C Type =  ECU Configuration

service id = 22
Diag service request :  0000075422A014
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: A014

service id = 22
Diag service request :  000007542241AE
Diag service response:  0000075C6241AE3839303131373033323732323337343239353135
41AE (HEX) =  3839303131373033323732323337343239353135
41AE (ASCII) =  89011703272237429515
41AE Type =  

service id = 22
Diag service request :  0000075422A017
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: A017

service id = 22
Diag service request :  0000075422EEFA
Diag service response:  0000075C62EEFA31633761313335320000000000000000
EEFA (HEX) =  31633761313335320000000000000000
EEFA (HEX) =  31633761313335320000000000000000
EEFA Type =  

service id = 22
Diag service request :  0000075422D027
Diag service response:  0000075C62D027535535542D3134483234312D484C00000000000000000000
D027 (HEX) =  535535542D3134483234312D484C00000000000000000000
D027 (ASCII) =  SU5T-14H241-HL
D027 Type =  Boot Image

service id = 22
Diag service request :  0000075422F121
Diag service response:  0000075C62F1214D5535542D3134483039302D42415A000000000000000000
F121 (HEX) =  4D5535542D3134483039302D42415A000000000000000000
F121 (ASCII) =  MU5T-14H090-BAZ
F121 Type =  Strategy

service id = 22
Diag service request :  0000075422F16B
Diag service response:  0000075C62F16B000000000000000000000000000000000000000000000000
F16B (HEX) =  000000000000000000000000000000000000000000000000
F16B (ASCII) =  \u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000
F16B Type =  ECU Configuration

service id = 22
Diag service request :  0000075422F17F
Diag service response:  0000075C62F17F3154413151425454
F17F (HEX) =  3154413151425454
F17F (ASCII) =  1TA1QBTT
F17F Type =  Serial Number

service id = 22
Diag service request :  0000075422A015
Diag service response:  0000075C62A0156174742E636F6D2F6C696E636F6C6E0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F410000000000000000000000000000000000000000006174742E636F6D2F666F72640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F41000000000000000000000000000000000000000000
A015 (HEX) =  6174742E636F6D2F6C696E636F6C6E0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F410000000000000000000000000000000000000000006174742E636F6D2F666F72640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F41000000000000000000000000000000000000000000
A015 (HEX) =  6174742E636F6D2F6C696E636F6C6E0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F410000000000000000000000000000000000000000006174742E636F6D2F666F72640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004E2F41000000000000000000000000000000000000000000
A015 Type =  

service id = 22
Diag service request :  0000075422F120
Diag service response:  0000075C62F120535535542D3134483039302D414748000000000000000000
F120 (HEX) =  535535542D3134483039302D414748000000000000000000
F120 (ASCII) =  SU5T-14H090-AGH
F120 Type =  Strategy

service id = 22
Diag service request :  0000075422F166
Diag service response:  0000075C62F16623081709
F166 (HEX) =  23081709
F166 (HEX) =  23081709
F166 Type =  

service id = 22
Diag service request :  0000075422F10A
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: F10A

service id = 22
Diag service request :  0000075422EEFB
Diag service response:  0000075C62EEFB3337333835333332333033303331333732363330303130393230323231313135
EEFB (HEX) =  3337333835333332333033303331333732363330303130393230323231313135
EEFB (HEX) =  3337333835333332333033303331333732363330303130393230323231313135
EEFB Type =  

service id = 22
Diag service request :  0000075422A011
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: A011

service id = 22
Diag service request :  0000075422F188
Diag service response:  0000075C62F188535535542D3134483038352D484C00000000000000000000
F188 (HEX) =  535535542D3134483038352D484C00000000000000000000
F188 (ASCII) =  SU5T-14H085-HL
F188 Type =  Strategy

service id = 22
Diag service request :  0000075422F15F
Diag service response:  0000075C62F15F0805113D030000000000
F15F (HEX) =  0805113D030000000000
F15F (HEX) =  0805113D030000000000
F15F Type =  

service id = 22
Diag service request :  0000075422F110
Diag service response:  0000075C62F11044534D5535542D3134483037342D41425300000000000000
F110 (HEX) =  44534D5535542D3134483037342D41425300000000000000
F110 (ASCII) =  DSMU5T-14H074-ABS
F110 Type =  Part II Specification

service id = 22
Diag service request :  00000754228068
Diag service response:  0000075C628068535535542D3134483234302D474800000000000000000000
8068 (HEX) =  535535542D3134483234302D474800000000000000000000
8068 (ASCII) =  SU5T-14H240-GH
8068 Type =  Boot Image

service id = 22
Diag service request :  0000075422A012
Diag service response:  0000075C62A012011E130F00078B0001
A012 (HEX) =  011E130F00078B0001
A012 (HEX) =  011E130F00078B0001
A012 Type =  

service id = 22
Diag service request :  0000075422F18C
Diag service response:  0000075C62F18C46554243483233303036313130393935
F18C (HEX) =  46554243483233303036313130393935
F18C (ASCII) =  FUBCH23006110995
F18C Type =  Serial Number

service id = 22
Diag service request :  0000075422F163
Diag service response:  0000075C62F16305
F163 (HEX) =  05
F163 (HEX) =  05
F163 Type =  ECU Diagnostic Spec

service id = 22
Diag service request :  0000075422D040
Diag service response:  0000075C62D040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
D040 (HEX) =  000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
D040 (ASCII) =  \u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000
D040 Type =  

service id = 22
Diag service request :  0000075422F111
Diag service response:  0000075C62F1114E5535542D3134483038392D464441000000000000000000
F111 (HEX) =  4E5535542D3134483038392D464441000000000000000000
F111 (ASCII) =  NU5T-14H089-FDA
F111 Type =  Core Assembly

service id = 22
Diag service request :  0000075422F113
Diag service response:  0000075C62F1134E5535542D3134483037342D464C41000000000000000000
F113 (HEX) =  4E5535542D3134483037342D464C41000000000000000000
F113 (ASCII) =  NU5T-14H074-FLA
F113 Type =  Assembly

service id = 22
Diag service request :  0000075422F162
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: F162

service id = 22
Diag service request :  0000075422A016
Diag service response:  0000075C7F2231
Constant-field byte 4 (hex) : 7F
NRC = 31 (requestOutOfRange)
Diag service response:  0000075C7F2231
>>>EXCEPTIONHANDLER>>>
Cannot read DID: A016
END ~~ ReadPartNumDids

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ ReadPartNumDIDsProcess

BEGIN ~~ GetFlashActionContentProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ GetFlashActionContent
File Mode = MR parser Used

BEGIN ~~ SerialNumberCheck
strCDL_F17F = 1TA1QBTT    strModule_F17F = 1TA1QBTT
strCDL_F18C = FUBCH23006110995    strModule_F18C = FUBCH23006110995
Serial number check PASS
END ~~ SerialNumberCheck

BEGIN ~~ GetGIVISWarnings
Warnings from topology: GIVIS_AVAILABLE
Number of GIVIS warnings = 0
END ~~ GetGIVISWarnings

BEGIN ~~ GetConfigDataFromGIVIS
Config data pulled from AVAILABLE_TOPOLOGY
Config data source is MODIFIED_CONFIG, number of DIDs =    19
bRemoveNonDExxDIDs = true

BEGIN ~~ RemoveNonDExxDIDs
Total number of direct config DIDs  19
Config DID NOT in exclusion List DE00 = 1802000000
Config DID NOT in exclusion List DE01 = 1d00000010
Config DID NOT in exclusion List DE02 = 0a00f13530cd523c1e2d005a000f05096050500010002a887d03c0bffca01c4044
Config DID NOT in exclusion List DE03 = 006496012c006402580a007800050a003c003c00140c
Config DID NOT in exclusion List DE04 = 70726f6430346e6177696669666f7264000000000000000000000000000000000000000000000000
Config DID NOT in exclusion List DE05 = 00000000000000000000000000000000000000000000000000000000000000000000000000000000
Config DID NOT in exclusion List DE06 = 0203596f
Config DID NOT in exclusion List DE07 = 1d00596f
Config DID NOT in exclusion List DE08 = 0000000000000000000000000000000000000000
Config DID NOT in exclusion List DE09 = 5553
Config DID NOT in exclusion List DE0A = aa
Config DID NOT in exclusion List DE0B = 00
Config DID NOT in exclusion List DE0C = 000102050202020502020205000102050303030a0303030a0002030a0404040f0404040f
Config DID NOT in exclusion List DE0D = 4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b3c3c3c3c3c3c3c323c3c3c32
Config DID NOT in exclusion List DE0E = 31304544050701
Config DID NOT in exclusion List DE0F = 00
Config DID NOT in exclusion List DE10 = 001b1067
Config DID NOT in exclusion List DE11 = 626f6f7473747261702e7362312e6175746f6e6f6d69632e61693a38303930000000000000000000
Config DID NOT in exclusion List DEFF = 0507
Number of DExx Config DIDs  19
END ~~ RemoveNonDExxDIDs

BEGIN ~~ PrintToLogVehicldDidList
Number of DIDs in: MasterListOfDirectConfigData : 19
MasterListOfDirectConfigData[0]: DE00 = 1802000000
MasterListOfDirectConfigData[1]: DE01 = 1d00000010
MasterListOfDirectConfigData[2]: DE02 = 0a00f13530cd523c1e2d005a000f05096050500010002a887d03c0bffca01c4044
MasterListOfDirectConfigData[3]: DE03 = 006496012c006402580a007800050a003c003c00140c
MasterListOfDirectConfigData[4]: DE04 = 70726f6430346e6177696669666f7264000000000000000000000000000000000000000000000000
MasterListOfDirectConfigData[5]: DE05 = 00000000000000000000000000000000000000000000000000000000000000000000000000000000
MasterListOfDirectConfigData[6]: DE06 = 0203596f
MasterListOfDirectConfigData[7]: DE07 = 1d00596f
MasterListOfDirectConfigData[8]: DE08 = 0000000000000000000000000000000000000000
MasterListOfDirectConfigData[9]: DE09 = 5553
MasterListOfDirectConfigData[10]: DE0A = aa
MasterListOfDirectConfigData[11]: DE0B = 00
MasterListOfDirectConfigData[12]: DE0C = 000102050202020502020205000102050303030a0303030a0002030a0404040f0404040f
MasterListOfDirectConfigData[13]: DE0D = 4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b3c3c3c3c3c3c3c323c3c3c32
MasterListOfDirectConfigData[14]: DE0E = 31304544050701
MasterListOfDirectConfigData[15]: DE0F = 00
MasterListOfDirectConfigData[16]: DE10 = 001b1067
MasterListOfDirectConfigData[17]: DE11 = 626f6f7473747261702e7362312e6175746f6e6f6d69632e61693a38303930000000000000000000
MasterListOfDirectConfigData[18]: DEFF = 0507
END ~~ PrintToLogVehicldDidList
GIVIS DE0x Ok

BEGIN ~~ GetFlashActionsProcess

BEGIN ~~ GetFlashActions
END ~~ GetFlashActions

BEGIN ~~ ParseFlashActionData

in_FlashActionList size = 1

flashAction.id = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539-1.0.0
flashAction.parser = MR
flashAction.targetNode = 1876




flashActionAssembly number 1 of 1
flashActionAssembly.currentAssembly = NU5T-14H089-FDA
flashActionAssembly.availableAssembly = NU5T-14H089-FDA
flashActionAssembly.directivesFileDownloadId = FENIX
flashActionAssembly.hasActionID.value = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539
flashActionAssembly.hasActionID.revision = V363N_2023_68658a4d2d9d560573bfd1c3_1751552398539
targetNodeAddress = 0754

null pointer =  java.lang.NullPointerException
firstCondition is null, there are no HasAction conditions for this node


Flash Action DID = 8068
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H240-HL
assemblySoftware.softwareSize = 1994025
assemblySoftware.didValue (Decimal) = 32872
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F188
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H085-HL
assemblySoftware.softwareSize = 678033
assemblySoftware.didValue (Decimal) = 61832
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = D027
assemblySoftware.type = BOOT_IMAGE
assemblySoftware.id = SU5T-14H241-HL
assemblySoftware.softwareSize = 50860
assemblySoftware.didValue (Decimal) = 53287
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F121
assemblySoftware.type = STRATEGY
assemblySoftware.id = MU5T-14H090-BAZ
assemblySoftware.softwareSize = 48761810
assemblySoftware.didValue (Decimal) = 61729
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


Flash Action DID = F120
assemblySoftware.type = STRATEGY
assemblySoftware.id = SU5T-14H090-AHL
assemblySoftware.softwareSize = 98168657
assemblySoftware.didValue (Decimal) = 61728
assemblySoftware.flashSequence (Decimal) = 0
assemblySoftware.programmingNetworkInterface.networkProtocol = USB
assemblySoftware.url = https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf
supportingSoftware.id = 
supportingSoftware.url = 
supportingSoftware.type = 


END ~~ ParseFlashActionData
END ~~ GetFlashActionsProcess

BEGIN ~~ ReMapFlashActionDataStructure

BEGIN ~~ GetProgrammingNetworkInterface
DID: 8068
PNI = USB
PNI = USB for DID = 8068
END ~~ GetProgrammingNetworkInterface

BEGIN ~~ GetProgrammingNetworkInterface
DID: F188
PNI = USB
PNI = USB for DID = F188
END ~~ GetProgrammingNetworkInterface

BEGIN ~~ GetProgrammingNetworkInterface
DID: D027
PNI = USB
PNI = USB for DID = D027
END ~~ GetProgrammingNetworkInterface

BEGIN ~~ GetProgrammingNetworkInterface
DID: F121
PNI = USB
PNI = USB for DID = F121
END ~~ GetProgrammingNetworkInterface

BEGIN ~~ GetProgrammingNetworkInterface
DID: F120
PNI = USB
PNI = USB for DID = F120
END ~~ GetProgrammingNetworkInterface
Number of flash action parts= 5
END ~~ ReMapFlashActionDataStructure

BEGIN ~~ ParseAndCompareFlashActionApplications
Flash Action Applications count  = 0
There are no Applications in the Flash Action List!
END ~~ ParseAndCompareFlashActionApplications
END ~~ GetFlashActionContent

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
END ~~ GetFlashActionContentProcess

BEGIN ~~ SoftwareUpdateProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ ProgramModule

BEGIN ~~ CheckSoftwareLevel
8068 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH
F188 Matches - No need to flash,  part number = SU5T-14H085-HL
D027 Matches - No need to flash,  part number = SU5T-14H241-HL
F121 Matches - No need to flash,  part number = MU5T-14H090-BAZ
F120 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH
END ~~ CheckSoftwareLevel

BEGIN ~~ DownloadSoftwareBinaries
bFlashALL = true
8068 = SU5T-14H240-HL Software binary required - get ALL files
Software download successful? true
F188 = SU5T-14H085-HL Software binary required - get ALL files
Software download successful? true
D027 = SU5T-14H241-HL Software binary required - get ALL files
Software download successful? true
F121 = MU5T-14H090-BAZ Software binary required - get ALL files
Software download successful? true
F120 = SU5T-14H090-AHL Software binary required - get ALL files
Software download successful? true
END ~~ DownloadSoftwareBinaries

BEGIN ~~ DetermineProgrammingMethod
8068 is USB flashed
bfProgrammingMethod = 02
F120 is USB flashed
bfProgrammingMethod = 02
No Applications to install
END ~~ DetermineProgrammingMethod

BEGIN ~~ BatteryCheck
Battery State of Charge SOC (percent) = 100
Battery voltage = 12.933
END ~~ BatteryCheck
Programming method (0-CAN, 1-USB, or 2-BOTH)? = 1
Programming method: USB

BEGIN ~~ UpdateSoftwareOverUSB

g_ParsedFlashActionData.removeApplicationsList count =  0

BEGIN ~~ SetApplicationState
Setting ApplicationState = APPLICATION_SKIPPED
END ~~ SetApplicationState

BEGIN ~~ GetFenixUSBPackage

File to flash over USB =  SU5T-14H240-HL

File to flash over USB =  SU5T-14H090-AHL
addSoftware set to null

BEGIN ~~ getFenixData
LOG FENIX REQUEST:
VIN = 1FBAX2YG0PKA54057
ECG ESN = 1EH1BIQJ
ECG Hardware = NU5T-14H026-EB
Requested node(0) = 754
Requested software part(0) = 
Remove software part(0) = ""
Execute FENIX_SERVICE GET_DATA - SUCCESS
END ~~ getFenixData

BEGIN ~~ outputFenixData
FENIX response:
Description: {"TCU CCPU bootchain images"}
Part Number: SU5T-14H240-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H240-HL.VBF
Software Type: BOOT_IMAGE
Binary Size: 1994025
Node Address: 754
DID Address: 8068
FENIX response:
Description: {"TCU VMCU load"}
Part Number: SU5T-14H085-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H085-HL.VBF
Software Type: STRATEGY
Binary Size: 678033
Node Address: 754
DID Address: F188
FENIX response:
Description: {"TCU VMCU Bootloader"}
Part Number: SU5T-14H241-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H241-HL.VBF
Software Type: BOOT_IMAGE
Binary Size: 50860
Node Address: 754
DID Address: D027
FENIX response:
Description: {"TCU MP images"}
Part Number: MU5T-14H090-BAZ
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf
File On USB: FordSoftwareUpdates/MU5T-14H090-BAZ.VBF
Software Type: STRATEGY
Binary Size: 48761810
Node Address: 754
DID Address: F121
FENIX response:
Description: {"TCU AP images"}
Part Number: SU5T-14H090-AHL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H090-AHL.VBF
Software Type: STRATEGY
Binary Size: 98168657
Node Address: 754
DID Address: F120
FENIX response:
Description: MANIFEST
Part Number: FordSoftwareManifest
File Type: SIGNED
Resource URL: https://www.gsug.vehicleupdates.files.ford.com/M_7057e5f9-8c36-47c9-b1cc-72799b626f06
File On USB: 1FBAX2YG0PKA54057_FordSoftwareManifest.der
Software Type: TRANSIENT
Binary Size: 0
Node Address: 716
DID Address: null
errorDetails = SUCCESS
errorSource = FENIX. 
END ~~ outputFenixData

BEGIN ~~ ParseManifestPresence
Manifest not found, keep looping....index = 0
Manifest not found, keep looping....index = 1
Manifest not found, keep looping....index = 2
Manifest not found, keep looping....index = 3
Manifest not found, keep looping....index = 4
bManifestFound =true
END ~~ ParseManifestPresence
USB drive location = D:\

BEGIN ~~ downloadFenixSoftware
executeDownloadFenixSoftware SUCCESS
END ~~ downloadFenixSoftware
END ~~ GetFenixUSBPackage

BEGIN ~~ InstallUSBSoftware
USB installation success was selected.
END ~~ InstallUSBSoftware

BEGIN ~~ ValidateSoftwareUpdateProcess

Validation for flash method (0 = CAN, 1 = USB, 2 = BOTH):  1

USB flash DID count:  2

USB and CAN DID count (including Apps):  2

BEGIN ~~ EstablishCommsProcess

BEGIN ~~ PingModule

Pinging node = 754
ECU does not support CAN FD try CAN Classic for node: 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok, protocol = CAN Classic for node: 754
VCI supports CAN FD =  false
Exception in StMin NOT overrided
Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases
Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37 
Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37 
END ~~ PingModule
END ~~ EstablishCommsProcess

BEGIN ~~ ReadPartNumDids

service id = 22
Diag service request :  00000754228068
Diag service response:  0000075C628068535535542D3134483234302D474800000000000000000000
8068 (HEX) =  535535542D3134483234302D474800000000000000000000
8068 (ASCII) =  SU5T-14H240-GH
8068 Type =  Boot Image

service id = 22
Diag service request :  0000075422F120
Diag service response:  0000075C62F120535535542D3134483039302D414748000000000000000000
F120 (HEX) =  535535542D3134483039302D414748000000000000000000
F120 (ASCII) =  SU5T-14H090-AGH
F120 Type =  Strategy
END ~~ ReadPartNumDids

BEGIN ~~ ValidateFlashActionDIDsAgainstModule
8068 Validation FAIL
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH
F120 Validation FAIL
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH
No Applications in Flash Action List to validate
Update failed!!
>>>EXCEPTIONHANDLER>>>
Procedure name = ValidateFlashActionDIDsAgainstModule - Exception qualifier =  ValidateFlashActionDIDsAgainstModule - Exception text = Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

USB installation failure, bUSBSuccess = false
Retry USB process selected

BEGIN ~~ EstablishCommsProcess

BEGIN ~~ PingModule

Pinging node = 754
ECU does not support CAN FD try CAN Classic for node: 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok, protocol = CAN Classic for node: 754
VCI supports CAN FD =  false
Exception in StMin NOT overrided
Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases
Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37 
Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37 
END ~~ PingModule
END ~~ EstablishCommsProcess

BEGIN ~~ EndBargraph
END ~~ BargraphDisplayV2
END ~~ EndBargraph
>>>EXCEPTIONHANDLER>>>

BEGIN ~~ BargraphDisplayV2
Procedure name = UpdateSoftwareOverUSB - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess
Update software programming failed, exit process
>>>EXCEPTIONHANDLER>>>
END ~~ BargraphDisplayV2
Procedure name = ProgramModule - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess
>>>EXCEPTIONHANDLER>>>
Procedure name = ProgramModule - Exception qualifier =  UpdateSoftwareOverUSB - Exception text = SoftwareUpdateProcess

BEGIN ~~ EndBargraph
END ~~ EndBargraph
>>>EXCEPTIONHANDLER>>>
Calling procedure name: SoftwareUpdateProcess ==  Exception text: SoftwareUpdateProcess so retry THIS calling procedure

BEGIN ~~ SoftwareUpdateProcess

BEGIN ~~ BargraphDisplayV2

BEGIN ~~ ProgramModule

BEGIN ~~ CheckSoftwareLevel
8068 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH
F188 Matches - No need to flash,  part number = SU5T-14H085-HL
D027 Matches - No need to flash,  part number = SU5T-14H241-HL
F121 Matches - No need to flash,  part number = MU5T-14H090-BAZ
F120 SW Not at latest level, FLASH
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH
END ~~ CheckSoftwareLevel

BEGIN ~~ DownloadSoftwareBinaries
bFlashALL = true
8068 = SU5T-14H240-HL Software binary required - get ALL files
Software download successful? true
F188 = SU5T-14H085-HL Software binary required - get ALL files
Software download successful? true
D027 = SU5T-14H241-HL Software binary required - get ALL files
Software download successful? true
F121 = MU5T-14H090-BAZ Software binary required - get ALL files
Software download successful? true
F120 = SU5T-14H090-AHL Software binary required - get ALL files
Software download successful? true
END ~~ DownloadSoftwareBinaries

BEGIN ~~ DetermineProgrammingMethod
8068 is USB flashed
bfProgrammingMethod = 02
F120 is USB flashed
bfProgrammingMethod = 02
No Applications to install
END ~~ DetermineProgrammingMethod

BEGIN ~~ BatteryCheck
Battery State of Charge SOC (percent) = 100
Battery voltage = 12.963
END ~~ BatteryCheck
Programming method (0-CAN, 1-USB, or 2-BOTH)? = 1
Programming method: USB

BEGIN ~~ UpdateSoftwareOverUSB

g_ParsedFlashActionData.removeApplicationsList count =  0

BEGIN ~~ SetApplicationState
Setting ApplicationState = APPLICATION_SKIPPED
END ~~ SetApplicationState

BEGIN ~~ GetFenixUSBPackage

File to flash over USB =  SU5T-14H240-HL

File to flash over USB =  SU5T-14H090-AHL
addSoftware set to null

BEGIN ~~ getFenixData
LOG FENIX REQUEST:
VIN = 1FBAX2YG0PKA54057
ECG ESN = 1EH1BIQJ
ECG Hardware = NU5T-14H026-EB
Requested node(0) = 754
Requested software part(0) = 
Remove software part(0) = ""
Execute FENIX_SERVICE GET_DATA - SUCCESS
END ~~ getFenixData

BEGIN ~~ outputFenixData
FENIX response:
Description: {"TCU CCPU bootchain images"}
Part Number: SU5T-14H240-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/a59d9588-dc42-43eb-a94c-71b7073984d8_SU5T-14H240-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H240-HL.VBF
Software Type: BOOT_IMAGE
Binary Size: 1994025
Node Address: 754
DID Address: 8068
FENIX response:
Description: {"TCU VMCU load"}
Part Number: SU5T-14H085-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/4bf71316-d16d-4c67-ab89-edef8d16d73c_SU5T-14H085-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H085-HL.VBF
Software Type: STRATEGY
Binary Size: 678033
Node Address: 754
DID Address: F188
FENIX response:
Description: {"TCU VMCU Bootloader"}
Part Number: SU5T-14H241-HL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/d78cc5da-2ab3-4459-bee2-a1cedfa5bca2_SU5T-14H241-HL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H241-HL.VBF
Software Type: BOOT_IMAGE
Binary Size: 50860
Node Address: 754
DID Address: D027
FENIX response:
Description: {"TCU MP images"}
Part Number: MU5T-14H090-BAZ
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/df5430fe-8776-4b99-9018-7655c7bc8a73_MU5T-14H090-BAZ.vbf
File On USB: FordSoftwareUpdates/MU5T-14H090-BAZ.VBF
Software Type: STRATEGY
Binary Size: 48761810
Node Address: 754
DID Address: F121
FENIX response:
Description: {"TCU AP images"}
Part Number: SU5T-14H090-AHL
File Type: CACHED
Resource URL: https://vehiclesoftware.ford.com/02169ae6-3175-4468-be22-2471dd6513df_SU5T-14H090-AHL.vbf
File On USB: FordSoftwareUpdates/SU5T-14H090-AHL.VBF
Software Type: STRATEGY
Binary Size: 98168657
Node Address: 754
DID Address: F120
FENIX response:
Description: MANIFEST
Part Number: FordSoftwareManifest
File Type: SIGNED
Resource URL: https://www.gsug.vehicleupdates.files.ford.com/M_abba5b6b-c6b7-400d-bdd6-b5739256cf2f
File On USB: 1FBAX2YG0PKA54057_FordSoftwareManifest.der
Software Type: TRANSIENT
Binary Size: 0
Node Address: 716
DID Address: null
errorDetails = SUCCESS
errorSource = FENIX. 
END ~~ outputFenixData

BEGIN ~~ ParseManifestPresence
Manifest not found, keep looping....index = 0
Manifest not found, keep looping....index = 1
Manifest not found, keep looping....index = 2
Manifest not found, keep looping....index = 3
Manifest not found, keep looping....index = 4
bManifestFound =true
END ~~ ParseManifestPresence
USB drive location = D:\

BEGIN ~~ downloadFenixSoftware
executeDownloadFenixSoftware SUCCESS
END ~~ downloadFenixSoftware
END ~~ GetFenixUSBPackage

BEGIN ~~ InstallUSBSoftware
USB installation success was selected.
END ~~ InstallUSBSoftware

BEGIN ~~ ValidateSoftwareUpdateProcess

Validation for flash method (0 = CAN, 1 = USB, 2 = BOTH):  1

USB flash DID count:  2

USB and CAN DID count (including Apps):  2

BEGIN ~~ EstablishCommsProcess

BEGIN ~~ PingModule

Pinging node = 754
ECU does not support CAN FD try CAN Classic for node: 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok, protocol = CAN Classic for node: 754
VCI supports CAN FD =  false
Exception in StMin NOT overrided
Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases
Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37 
Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37 
END ~~ PingModule
END ~~ EstablishCommsProcess

BEGIN ~~ ReadPartNumDids

service id = 22
Diag service request :  00000754228068
Diag service response:  0000075C628068535535542D3134483234302D474800000000000000000000
8068 (HEX) =  535535542D3134483234302D474800000000000000000000
8068 (ASCII) =  SU5T-14H240-GH
8068 Type =  Boot Image

service id = 22
Diag service request :  0000075422F120
Diag service response:  0000075C62F120535535542D3134483039302D414748000000000000000000
F120 (HEX) =  535535542D3134483039302D414748000000000000000000
F120 (ASCII) =  SU5T-14H090-AGH
F120 Type =  Strategy
END ~~ ReadPartNumDids

BEGIN ~~ ValidateFlashActionDIDsAgainstModule
8068 Validation FAIL
Flash Action part number = SU5T-14H240-HL
Module part number = SU5T-14H240-GH
F120 Validation FAIL
Flash Action part number = SU5T-14H090-AHL
Module part number = SU5T-14H090-AGH
No Applications in Flash Action List to validate
Update failed!!
>>>EXCEPTIONHANDLER>>>
Procedure name = ValidateFlashActionDIDsAgainstModule - Exception qualifier =  ValidateFlashActionDIDsAgainstModule - Exception text = Update was not successful!

FAIL - 8068 = SU5T-14H240-GH >>> SHOULD = SU5T-14H240-HL
FAIL - F120 = SU5T-14H090-AGH >>> SHOULD = SU5T-14H090-AHL

USB installation failure, bUSBSuccess = false
CAN flash selected

BEGIN ~~ EstablishCommsProcess

BEGIN ~~ PingModule

Pinging node = 754
ECU does not support CAN FD try CAN Classic for node: 754

service id = 22
Diag service request :  0000075422D100
Diag service response:  0000075C62D10001
Comms ok, protocol = CAN Classic for node: 754
VCI supports CAN FD =  false
Exception in StMin NOT overrided
Here after setting CP_DoIPLogicalGatewayAddress which means FDRS >R37 since DoIP is not supported on prior releases
Here after setting CP_P4_MaxPendingTimeout which means FDRS >R37 
Here after setting CP_P2_Star_PendingTimeout which means FDRS >R37 
END ~~ PingModule
END ~~ EstablishCommsProcess

BEGIN ~~ FlashSoftwareOverCAN
Flash sequence: DID D027 is number 1
Flash sequence: DID F188 is number 2
Flash sequence: DID 8068 is number 3
Flash sequence: DID F120 is number 4
Flash sequence: DID F121 is number 5

BEGIN ~~ FlashSoftware

BEGIN ~~ ControlTesterPresent_Functional

Turning TP ON
END ~~ ControlTesterPresent_Functional
service id = 10
sub function = 02
Request parameters = 
Diag service request :  000007541002
Diag service response:  0000075C5002001901F4
Diag service parsed response:  001901F4

BEGIN ~~ GainSecurityAccess

DA01 = DSMU5T-14H074-ABR
service id = 27
sub function = 01
Request parameters = 
Diag service request :  000007542701
Diag service response:  0000075C6701D4F8E6338A89A4DCE925D0DD0FB730CA
Seed = D4F8E6338A89A4DCE925D0DD0FB730CA
Security access level = 01
Level 1 SEED = D4F8E6338A89A4DCE925D0DD0FB730CA
Level 2 KEY = ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF

service id = 27
sub function = 02
Request parameters = ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF
Diag service request :  000007542702ADBE2EECDA15FA0D33CE00DCBC9B5990B5CF
Diag service response:  0000075C6702
Security access level = 02
END ~~ GainSecurityAccess
bFlashALL set to: true
About to download: D027 = SU5T-14H241-HL

BEGIN ~~ DownloadFiles
Download file started: SU5T-14H241-HL

BEGIN ~~ TransferBlockData
service id = 34
sub function = 
Request parameters = 004400000001000002F5
Diag service request :  0000075434004400000001000002F5
Diag service response:  0000075C7F3422
Constant-field byte 4 (hex) : 7F
NRC = 22 (conditionsNotCorrect)
NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34
>>>EXCEPTIONHANDLER>>>
END ~~ BargraphDisplayV2
>>>EXCEPTIONHANDLER>>>
Procedure name = Service_34 - Exception qualifier =  ExecuteMdxFreeDiagService - Exception text = NRC 22(conditionsNotCorrect)

Unable to execute diagnostic service  0x34

Fix fault and retest.
END ~~ TransferBlockData

Download file failed
END ~~ DownloadFiles
Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
Procedure name = FlashSoftware - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

BEGIN ~~ BargraphDisplayV2
Flash programming failed, exit process
>>>EXCEPTIONHANDLER>>>
END ~~ BargraphDisplayV2
Procedure name = FlashSoftwareOverCAN - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
Procedure name = FlashSoftwareOverCAN - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
Procedure name = UpdateSoftwareOverUSB - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
Update software programming failed, exit process
>>>EXCEPTIONHANDLER>>>

BEGIN ~~ BargraphDisplayV2
Procedure name = ProgramModule - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
END ~~ BargraphDisplayV2
Procedure name = ProgramModule - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

BEGIN ~~ EndBargraph
END ~~ EndBargraph
>>>EXCEPTIONHANDLER>>>
Procedure name = SoftwareUpdateProcess - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
Procedure name = OTXAppFlowControl - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL
>>>EXCEPTIONHANDLER>>>
Procedure name = main - Exception qualifier =  FlashSoftware - Exception text = Failed to flash SU5T-14H241-HL

BEGIN ~~ ApplicationExitAndCleanUp

BEGIN ~~ GetApplicationState
Getting ApplicationState = APPLICATION_SKIPPED
END ~~ GetApplicationState
Procedure exit reason: Failed to flash SU5T-14H241-HL
END ~~ ApplicationExitAndCleanUp

2025-10-14T09:36:51,805 INFO class otxcontainer.G2056515.authorLogs - 
Total elapsed time: 1050sec

2025-10-14T09:36:52,831 INFO otx.core.BaseApplication - Application finished with state APPLICATION_SKIPPED - indictedComponentId: null, inditingAppId: null

2025-10-14T09:36:52,835 INFO otx.core.BaseApplication - [APPLICATION]{type=STOPPED, id=G2056515, version=44.0} Application stopped

2025-10-14T09:36:52,837 INFO otx.core.BaseApplication - Removing runtime logs appender from COMMS channel logger

