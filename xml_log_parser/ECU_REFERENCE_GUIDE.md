# ECU Node Quick Reference Guide

## 🎯 What's New?

The application now **automatically recognizes and explains** the ECU nodes and DIDs you work with! When parsing logs, it will:

✅ Identify ECU nodes by their addresses (like 7D0, 760, 726)  
✅ Show the ECU name and what it controls  
✅ Flag CRITICAL modules that need special attention  
✅ Explain DIDs (Data Identifiers) like F190, F187, etc.  

---

## 🚨 Critical ECUs (Pay Special Attention!)

These modules are flagged with ⚠️ because issues here affect safety or core functions:

| Address | Acronym | Full Name | Why It's Critical |
|---------|---------|-----------|-------------------|
| **7D0** | APIM | Accessory Protocol Interface Module | Controls SYNC4 infotainment system |
| **760** | ABS | Anti-lock Braking System | Prevents wheel lockup - safety critical |
| **720** | IPC | Instrument Panel Cluster | Driver information display |
| **726** | BCM | Body Control Module | Central control for lights, locks, wipers |
| **7E0** | PCM | Powertrain Control Module | Engine and transmission control |
| **7E4** | BECM | Battery Energy Control Module | Battery/electrical management |
| **754** | TCU | Transmission Control Unit | Controls transmission shifting |
| **737** | RCM | Restraint Control Module | Airbag and safety systems |

---

## 🔧 Other ECUs You'll See

### Camera & Vision Systems
- **7C1** - CMR (Rear Camera)
- **6F2** - SODCMC (Side Camera MC)
- **6F3** - SODCMD (Side Camera MD)
- **706** - IPMA (Image Processing Module)
- **764** - CCM (Camera Control Module)

### Door Control Modules
- **740** - DDM (Driver Door)
- **741** - PDM (Passenger Door)
- **7B3** - DCMG (Door Control G)
- **7B4** - DCMH (Door Control H)
- **7A2** - DCME (Door Control E)
- **762** - DCMF (Door Control F)

### Driver Assistance
- **7C7** - ACCM (Adaptive Cruise Control)
- **750** - PACM (Park Assist)
- **731** - BLEM (Blind Spot Left)
- **7C4** - SODL (Side Obstacle Detection Left)
- **7C6** - SODR (Side Obstacle Detection Right)

### Comfort & Convenience
- **727** - ACM (Audio Control Module)
- **733** - HVAC (Climate Control)
- **730** - PSCM (Power Steering)
- **725** - WCM (Wireless Connectivity)
- **724** - SCCM (Steering Column Control)

### Other Important Modules
- **732** - GSM (Gateway Support Module)
- **716** - ECG2 (Electric Control Gateway 2)
- **765** - OCS (Occupant Classification)
- **7A1** - FTRM (Front Thermal Management)
- **746** - DCDC (DC-DC Converter)
- **6F5** - DCGM (Door Control GM)
- **6F0** - BCMC (Body Control Module C)

### Diagnostic Modules
- **7E2** - SOBDM (Side OBD Module)
- **7E6** - SOBDMC (Side OBD Module C)

---

## 📋 Common DIDs (Data Identifiers)

These are data points you can read from ECUs:

| DID | What It Gives You |
|-----|-------------------|
| **F190** | VIN (Vehicle Identification Number) |
| **F187** | Vehicle Manufacturer Part Number |
| **F18A** | System Supplier Identifier |
| **F18C** | ECU Serial Number |
| **F191** | ECU Hardware Number |
| **F194** | System Software Number |
| **F195** | System Software Version |
| **F197** | System Name or Engine Type |
| **F198** | Manufacturer ECU Software Number |
| **F199** | Manufacturer ECU Software Version |

---

## 🎮 How to Use This Feature

### Step 1: Parse Your Log
Just load any log file that mentions ECU addresses (like "7D0", "PCM", "726 BCM", etc.)

### Step 2: Review the Enhanced Report
The application will automatically:
- 🔍 Detect ECU addresses in error/success messages
- ⚠️ Flag critical modules with special icons
- 📝 Explain what each module does in plain English
- 💡 Provide context about why an error matters

### Step 3: Test with Sample File
Try the new **sample_ecu_session.txt** file to see it in action!

---

## 💡 Examples of What You'll See

### When an error involves a critical ECU:
```
Error #1
----------------------------------------
📍 Line: 32
❌ What: ERROR: BCM (726) - Communication timeout
⚠️ ECU: BCM ⚠️ CRITICAL - Body Control Module on HS2
   → Controls body functions like lights, locks, wipers. 
      Central to vehicle operation. This is a CRITICAL 
      module - issues here need immediate attention.
```

### When reading DIDs:
```
Success #1
----------------------------------------
📍 Line: 18
✓ What: SUCCESS: VIN retrieved: 3FMCR9B60PRA12345
🔧 ECU: APIM ⚠️ CRITICAL - Accessory Protocol Interface 
        Module (SYNC4) on HS2
   → Controls the infotainment system (SYNC). Critical 
      for media, navigation, and vehicle settings.
📋 DID F190: VIN (Vehicle Identification Number)
```

---

## 🚀 Quick Start Testing

1. **Open the application** (should still be running from earlier)
2. **Click "Browse..."**
3. **Select "sample_ecu_session.txt"** (new file with your ECUs!)
4. **Make sure "Simple Mode" is checked** ✅
5. **Click "Parse Log"**
6. **See the magic!** The report will identify all the ECUs and explain them

---

## 📝 Notes

- The ECU database contains **38 modules** from your vehicle
- **8 critical modules** are specially flagged
- **10 common DIDs** are automatically explained
- Works in both Simple Mode and Expert Mode
- All ECU info is shown in plain English for beginners

---

## 🆘 Troubleshooting

**Q: I don't see ECU context in my reports**  
A: Make sure your log mentions ECU addresses in one of these formats:
- 3-character hex: `7D0`, `726`, `760`
- With acronym: `APIM (7D0)`, `726 BCM`
- In hex format: `0x7D0`, `0x726`

**Q: My ECU isn't recognized**  
A: The database has 38 ECUs loaded. If yours isn't there, you'll still see the address, just without the detailed explanation.

---

## 📚 Related Files

- `ecu_reference.py` - ECU database with all 38 modules
- `simplified_report.py` - Enhanced to detect and explain ECUs
- `sample_ecu_session.txt` - Test file with your actual ECU nodes

Enjoy the enhanced diagnostic experience! 🎉
