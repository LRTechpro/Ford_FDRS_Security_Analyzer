# FSA 26588 - Wrong Target Part Numbers After OTA Interruption

**VIN:** 1FTEW2LP5SKD68013 | **FSA:** 26588 (IPC Update) | **Date:** November 19, 2025  
**Module:** IPC (0x0720) | **FDRS:** 46.5.5 | **Technician:** HWATKI16

---

## THE REAL PROBLEM

FSA 26588 SVF shows "Not Complete" because **the vehicle is not at the FSA target part numbers**. The November 19 FDRS update was interrupted by OTA and left the vehicle one revision behind on F188.

### FSA 26588 Target Part Numbers:
- F188: **SL3T-14C026-AF** ← Required for FSA completion
- F120: **SL3T-14C026-BC** ✓
- F110: **DS-SL3T-1A292-AD** ✓

### Current Vehicle Part Numbers (After Nov 19 Update):
- F188: **SL3T-14C026-AE** ← One revision behind (should be -AF)
- F120: **SL3T-14C026-BC** ✓ Correct
- F110: **DS-SL3T-1A292-AD** ✓ Correct

### What Happened on November 19:
1. FDRS started programming with correct target (-AF for F188)
2. OTA system interrupted the FDRS session during update
3. FDRS completed but **stopped at -AE instead of -AF**
4. F120 and F110 updated correctly
5. FDRS reported "SUCCESS" because it validated what it flashed
6. FSA SVF checks for -AF, finds -AE, shows "Not Complete"

**The issue:** Vehicle needs F188 updated from -AE to -AF to satisfy FSA requirements.

---

## WHY OTA INTERRUPTED AND WHAT TO DO

### OTA Interruption Issue:
PTS shows an IPC update is still available for this VIN. When FDRS tried to program on 11/19, the **OTA system interrupted** the FDRS session, preventing it from completing the full update to -AF.

However, the OTA update **will send the vehicle to the correct FSA target part numbers** (-AF for F188), so no GVMS changes or manual intervention needed.

### Lead Tech Recommendation:

**Allow the OTA update to complete naturally** - it will update F188 from -AE to -AF and satisfy the FSA requirements.

### Steps to Complete FSA 26588:

1. **Do not reprogram via FDRS** - this may conflict with OTA again
2. **Ensure vehicle has connectivity:**
   - WiFi or cellular connection active
   - Vehicle in Park with ignition on for OTA processing
   - Allow sufficient time for download/install
3. **Monitor PTS for OTA completion status**
4. **Verify final part numbers after OTA:**
   - F188 should show **SL3T-14C026-AF**
   - F120 should remain **SL3T-14C026-BC**
   - F110 should remain **DS-SL3T-1A292-AD**
5. **Check FSA SVF after OTA completes** - should show "Complete"

---

## ANALYSIS OF NOVEMBER 19 FDRS SESSION

### Why FDRS Showed SUCCESS:

Looking at the logs, FDRS successfully flashed what it downloaded:
- Downloaded: SL3T-14C026-AE (not -AF as intended)
- Flashed: SL3T-14C026-AE to vehicle ✓
- Validated: SL3T-14C026-AE in module ✓
- Result: SUCCESS (because it matched what was flashed)

### The Flash Action Analysis:

From the logs at 14:06:07:
```
Flash Action DID = F188
assemblySoftware.id = SL3T-14C026-AE  ← Downloaded -AE, not -AF
assemblySoftware.url = https://vehiclesoftware.ford.com/8d11bd2c-2649-4b43-9e1e-cec6b66d8b63_SL3T-14C026-AE.vbf
```

**FDRS received the wrong software package** from FDSP/GIVIS:
- FSA target: -AF
- FDRS downloaded: -AE
- OTA likely updated GIVIS after FDRS pulled packages
- FDRS completed successfully with old package

This explains why:
1. FDRS reported SUCCESS (flashed what it downloaded correctly)
2. FSA shows Not Complete (vehicle doesn't have -AF)
3. PTS shows update available (OTA has newer -AF package)
4. OTA interruption mentioned (OTA tried to update during FDRS session)

---

## ROOT CAUSE

**Timing issue between FDRS package retrieval and OTA system updates:**

1. FDRS queried GIVIS for software packages
2. GIVIS provided -AE package (latest at that moment)
3. OTA system updated to -AF while FDRS was running
4. OTA detected outdated flash in progress and interrupted
5. FDRS completed with -AE anyway
6. Vehicle now one revision behind FSA target

---

## RECOMMENDATION

**From Lead Tech:** Let OTA handle this naturally. Don't fight the OTA system with manual FDRS programming. The OTA update is queued and will complete when the vehicle is in the right conditions.

**No GVMS changes needed** - OTA already has the correct configuration.
