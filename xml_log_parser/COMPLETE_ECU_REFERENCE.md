# 🚗 COMPLETE ECU REFERENCE - ALL 75+ MODULES

## 📊 Database Statistics

- **Total ECU Modules:** 75+
- **Critical Modules:** 13
- **Categories:** 15
- **All modules auto-detected in logs**

---

## 🚨 CRITICAL MODULES (13) - Always Flagged with ⚠️

These modules are safety-critical or essential for vehicle operation:

| Address | Module | Full Name | Why Critical |
|---------|--------|-----------|--------------|
| **7D0** | APIM | Accessory Protocol Interface Module | Infotainment/SYNC control |
| **760** | ABS | Anti-Lock Brake System | Prevents wheel lockup (SAFETY) |
| **7F2** | ABSB | Anti-Lock Brake System B | Secondary ABS (SAFETY) |
| **720** | IPC | Instrument Panel Cluster | Driver information display |
| **726** | BCM | Body Control Module | Central body control |
| **7E0** | PCM | Powertrain Control Module | Engine/transmission control |
| **7E4** | BECM | Battery Energy Control Module | Battery management |
| **723** | BECMB | Battery Energy Control Module B | Secondary power management |
| **7E9** | TCM | Transmission Control Module | Transmission shifting |
| **737** | RCM | Restraints Control Module | Airbags (SAFETY) |
| **765** | OCS | Occupant Classification System | Airbag deployment logic (SAFETY) |
| **730** | PSCM | Power Steering Control Module | Steering assist (SAFETY) |
| **721** | VDM | Vehicle Dynamics Control Module | Stability control (SAFETY) |

---

## 📂 ALL MODULES BY CATEGORY

### 🔊 Audio & Entertainment (4 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 7A4 | AAM | Audio Amplifier Module |
| 727 | ACM | Audio Front Control Module |
| 774 | RACM | Rear Audio Control Module |
| 783 | DSP | Audio Digital Signal Processing Module |

### 🛡️ Braking Systems (2 modules) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 760 | ABS | Anti-Lock Brake System Control Module ⚠️ |
| 7F2 | ABSB | Anti-Lock Brake System Control Module B ⚠️ |

### ❄️ Climate Control (5 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 7C7 | ACCM | Air Conditioning Control Module |
| 6E0 | ACCMB | Air Conditioning Control Module B |
| 733 | HVAC | Heating, Ventilation, and Air Conditioning Module |
| 776 | SCME | Front Seat Climate Control Module |
| 777 | SCMF | Rear Seat Climate Control Module |

### 📺 Infotainment & Display (3 modules) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 7D0 | APIM | Accessory Protocol Interface Module ⚠️ |
| 720 | IPC | Instrument Panel Cluster ⚠️ |
| 7B2 | HUD | Heads Up Display Module |

### ⚙️ Drivetrain & Performance (5 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 792 | ATCM | All Terrain Control Module |
| 703 | AWD | All Wheel Drive |
| 795 | DCMR | Differential Control Module Rear |
| 761 | TCCM | Transfer Case Control Module |
| 7E9 | TCM | Transmission Control Module ⚠️ |
| 732 | GSM | Gear Shift Module |

### 🏗️ Body Control (2 modules) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 726 | BCM | Body Control Module ⚠️ |
| 6F0 | BCMC | Body Control Module C / Battery Junction Box |

### 🔋 Battery & Power Management (5 modules) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 7E4 | BECM | Battery Energy Control Module ⚠️ |
| 723 | BECMB | Battery Energy Control Module B ⚠️ |
| 746 | DCDC | Direct Current / Direct Current Convertor |
| 6F1 | DCACA | Direct Current / Alternating Current Convertor |
| 6F5 | OBCC | Off-Board Charger Controller |

### 📷 Camera & Vision Systems (8 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 764 | CCM | Cruise Control Module |
| 7C1 | CMR | Camera Module Rear (Driver Status Monitor) |
| 706 | IPMA | Image Processing Module A |
| 7B1 | IPMB | Image Processing Module B |
| 6F2 | SODCMC | Side Obstacle Detection Control Module C |
| 6F3 | SODCMD | Side Obstacle Detection Control Module D |
| 7C4 | SODL | Side Obstacle Detection Control Module LH |
| 7C6 | SODR | Side Obstacle Detection Control Module RH |

### 🚪 Door Control Modules (6 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 7A2 | DCME | Door Control Module E |
| 762 | DCMF | Door Control Module F |
| 7B3 | DCMG | Door Control Module G |
| 7B4 | DCMH | Door Control Module H |
| 740 | DDM | Driver Door Module |
| 741 | PDM | Passenger Door Module |

### 💺 Seat Control Modules (7 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 744 | DSM | Driver Front Seat Module |
| 7A3 | SCMB | Passenger Front Seat Module |
| 702 | SCMC | Seat Control Module C |
| 763 | SCMD | Seat Control Module D |
| 712 | SCMG | Driver Multi-Contour Seat Module |
| 713 | SCMH | Passenger Multi-Contour Seat Module |
| 787 | SCMJ | Seat Control Module J |

### 💡 Lighting Control (3 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 734 | HCM | Headlamp Control Module |
| 6F6 | LDCMA | Lighting Driver Control Module A |
| 6F7 | LDCMB | Lighting Driver Control Module B |

### 🛡️ Safety & Occupant Protection (2 modules) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 765 | OCS | Occupant Classification System Module ⚠️ |
| 737 | RCM | Restraints Control Module ⚠️ |

### 🅿️ Driver Assistance & Parking (2 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 750 | PACM | Pedestrian Alert Control Module |
| 736 | PAM | Parking Assist Control Module |

### 🚗 Powertrain (1 module) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 7E0 | PCM | Powertrain Control Module ⚠️ |

### 🎯 Steering Systems (4 modules) - 1 CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 730 | PSCM | Power Steering Control Module ⚠️ |
| 797 | SASM | Steering Angle Sensor Module |
| 724 | SCCM | Steering Column Control Module |
| 7C5 | SECM | Steering Effort Control Module |

### 🔍 Diagnostics & Communication (4 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 7E2 | SOBDM | Secondary On-Board Diagnostic Control Module A |
| 7E7 | SOBDMB | Secondary On-Board Diagnostic Control Module B |
| 7E6 | SOBDMC | Secondary On-Board Diagnostic Control Module C |
| 716 | GWM | Gateway Module A |

### 🔐 Access & Security (5 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 7A7 | FCIM | Front Control Interface Module |
| 7A1 | GFM | Generic Function Module (Front Trunk Release) |
| 731 | RFA | Remote Function Actuator |
| 775 | RGTM | Rear Gate Trunk Module |
| 766 | RBM | Running Board Control Module |

### 📡 Connectivity & Telemetry (3 modules)

| Address | Module | What It Does |
|---------|--------|--------------|
| 751 | RTM | Radio Transceiver Module |
| 754 | TCU | Telematic Control Unit Module |
| 725 | WACM | Wireless Accessory Charging Module |

### 🚛 Trailer & Towing (1 module)

| Address | Module | What It Does |
|---------|--------|--------------|
| 791 | TRM | Trailer Relay Module / Trailer Brake Control |

### 🏎️ Vehicle Dynamics (1 module) - CRITICAL

| Address | Module | What It Does |
|---------|--------|--------------|
| 721 | VDM | Vehicle Dynamics Control Module ⚠️ |

---

## 📋 Common DIDs (Data Identifiers)

These are automatically recognized when they appear in logs:

| DID | What It Contains |
|-----|------------------|
| F190 | VIN (Vehicle Identification Number) |
| F187 | Vehicle Manufacturer Spare Part Number |
| F18A | System Supplier Identifier |
| F18C | ECU Serial Number |
| F191 | Vehicle Manufacturer ECU Hardware Number |
| F192 | System Supplier ECU Hardware Number |
| F193 | System Supplier ECU Hardware Version Number |
| F194 | System Supplier ECU Software Number |
| F195 | System Supplier ECU Software Version Number |
| F197 | System Name or Engine Type |
| F198 | Vehicle Manufacturer ECU Software Number |
| F199 | Vehicle Manufacturer ECU Software Version Number |
| F19D | Vehicle Manufacturer ECU Software Assembly Part Number |
| F19E | Vehicle Manufacturer ECU Software Assembly Part Number |

---

## 🎮 How Recognition Works

### Automatic Detection:
The application scans every line in your logs for:
- **ECU addresses** (3-character hex like `7D0`, `726`, `760`)
- **DIDs** (4-character hex starting with F like `F190`, `F187`)
- **Formats recognized:**
  - `7D0` (plain hex)
  - `0x7D0` (with prefix)
  - `APIM (7D0)` (with acronym)
  - `726 BCM` (address with acronym)

### What You'll See:
- ⚠️ icon for CRITICAL modules
- 🔧 icon for regular modules
- 📋 icon for DID identifications
- Plain English explanations
- Context about why it matters

---

## 💡 Example Output

When the parser finds an ECU in a log:

```
Error #1
----------------------------------------
📍 Line: 45
❌ What: ERROR: RCM (737) - Fault code detected

⚠️ ECU: RCM ⚠️ CRITICAL - Restraints Control Module
   → Controls airbags and safety restraints. Critical 
      safety system. ⚠️ CRITICAL MODULE - Issues here 
      need immediate attention!
```

When it finds a DID:

```
Success #3
----------------------------------------
📍 Line: 18
✓ What: SUCCESS: Reading DID F190 from APIM

🔧 ECU: APIM ⚠️ CRITICAL - Accessory Protocol Interface Module
   → Controls the infotainment system (SYNC). Critical 
      for media, navigation, and vehicle settings. 
      ⚠️ CRITICAL MODULE - Issues here need immediate attention!
      
📋 DID F190: VIN (Vehicle Identification Number)
```

---

## 🚀 Testing the Feature

1. **Open the application** (should still be running)
2. **Load any log file** that mentions ECU addresses or acronyms
3. **Sample files available:**
   - `sample_ecu_session.txt` - Full diagnostic session
   - `sample_log.txt` - Original sample
   - Your own logs!

---

## 📊 Quick Stats Summary

| Category | Count | Critical |
|----------|-------|----------|
| Total Modules | 75+ | 13 |
| Audio & Entertainment | 4 | 0 |
| Braking Systems | 2 | 2 |
| Climate Control | 5 | 0 |
| Infotainment & Display | 3 | 2 |
| Drivetrain | 6 | 1 |
| Body Control | 2 | 1 |
| Power Management | 5 | 3 |
| Camera & Vision | 8 | 0 |
| Door Control | 6 | 0 |
| Seat Control | 7 | 0 |
| Lighting | 3 | 0 |
| Safety & Occupant | 2 | 2 |
| Driver Assistance | 2 | 0 |
| Powertrain | 1 | 1 |
| Steering | 4 | 1 |
| Diagnostics | 4 | 0 |
| Access & Security | 5 | 0 |
| Connectivity | 3 | 0 |
| Trailer | 1 | 0 |
| Vehicle Dynamics | 1 | 1 |

---

## 🆘 Need Help?

**Q: Why are some modules flagged as CRITICAL?**  
A: These modules handle safety-critical functions (airbags, braking, steering) or core vehicle operations. Errors here require immediate attention.

**Q: Can I see all modules in my vehicle?**  
A: Parse a comprehensive diagnostic log, and the app will detect all ECUs present in that log.

**Q: What if my ECU isn't recognized?**  
A: The database has 75+ modules. If yours isn't there, the address will still show, just without detailed context.

**Q: Does this work in Expert Mode?**  
A: Yes! ECU context works in both Simple and Expert modes.

---

## 📚 Related Files

- `ecu_reference.py` - Complete 75+ module database
- `simplified_report.py` - Detection engine
- `sample_ecu_session.txt` - Test file
- `NEW_FEATURE_ECU_RECOGNITION.md` - Feature overview

---

**Your vehicle's complete ECU map is now built into the application!** 🎉
