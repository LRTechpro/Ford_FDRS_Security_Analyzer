# NRC (Negative Response Code) Quick Reference Guide

## What Are NRC Codes?

NRC (Negative Response Code) are standardized diagnostic error codes used in vehicle communication protocols (UDS/ISO 14229). When you send a diagnostic request to a vehicle module and it **cannot** complete the request, it responds with a negative response containing an NRC code that explains **why** it failed.

---

## 🔍 How to Identify NRC Codes in Your Logs

### Pattern Recognition
NRC codes appear in diagnostic responses with this structure:

```
[00, 00, 07, 5C, 7F, 34, 78]
                 │   │   └─ NRC Code (0x78)
                 │   └───── Service ID (0x34 = RequestDownload)
                 └───────── Negative Response Indicator (0x7F)
```

**Key Components:**
- **0x7F** = Negative Response Service Identifier (always present in NRC responses)
- **Service ID** = The diagnostic service that was requested (e.g., 0x34, 0x27, 0x31)
- **NRC Code** = The specific reason for rejection (e.g., 0x78, 0x33, 0x35)

---

## 📋 Common NRC Codes You'll See

### 🟢 INFORMATIONAL (Not Actually Errors)

#### NRC 0x78 - RequestCorrectlyReceived-ResponsePending ⏳
**What it looks like:** `7F 34 78`
**What it means:** "I got your request, I'm working on it, please wait"
**When you see it:** During programming, long calculations, flash operations
**Action:** **WAIT** - This is normal. The module is busy processing.
**Frequency in your log:** 20+ times (normal for programming)

---

### 🟡 SECURITY/ACCESS ISSUES

#### NRC 0x33 - SecurityAccessDenied 🔒
**What it looks like:** `7F 27 33`
**What it means:** Security challenge failed, wrong key/seed
**When you see it:** Service 0x27 (SecurityAccess)
**Action:** 
- Verify security algorithm is correct
- Check seed-to-key calculation
- Ensure using correct security level

#### NRC 0x35 - InvalidKey 🔑
**What it looks like:** `7F 27 35`
**What it means:** Security key is incorrect
**When you see it:** Service 0x27 after sending security key
**Action:**
- Recalculate security key from seed
- Verify key calculation algorithm
- Check for byte order issues (endianness)

#### NRC 0x36 - ExceedNumberOfAttempts 🚫
**What it looks like:** `7F 27 36`
**What it means:** Too many wrong security attempts, locked out
**When you see it:** After multiple failed 0x27 attempts
**Action:**
- **STOP sending security requests**
- May need power cycle
- Wait for lockout timer (varies by module)

---

### 🔴 OPERATIONAL ERRORS

#### NRC 0x13 - IncorrectMessageLengthOrInvalidFormat 📏
**What it looks like:** `7F 34 13` or `7F 36 13`
**What it means:** Request has wrong number of bytes or format
**When you see it:** Any service with incorrect parameters
**Action:**
- Check service parameter count
- Verify byte order
- Confirm data format matches spec

#### NRC 0x31 - RequestOutOfRange 📍
**What it looks like:** `7F 2E 31`
**What it means:** Parameter value is outside valid range
**When you see it:** Writing DIDs, memory operations
**Action:**
- Check min/max values for the parameter
- Verify address ranges for memory operations
- Confirm DID supports the value being written

#### NRC 0x22 - ConditionsNotCorrect ⚙️
**What it looks like:** `7F 10 22` or `7F 34 22`
**What it means:** Preconditions not met (ignition, speed, gear, etc.)
**When you see it:** Programming, diagnostic session changes
**Action:**
- Check preconditions: ignition, park, doors, speed = 0
- Verify no DTCs preventing operation
- Ensure correct diagnostic session active

---

### 🟠 RESOURCE/TIMING ISSUES

#### NRC 0x14 - ResponseTooLong 📦
**What it looks like:** `7F 22 14`
**What it means:** Response data is too large to send
**When you see it:** Reading large DIDs, memory reads
**Action:**
- Request smaller data chunks
- Use paging/segmented reads
- Increase buffer size if possible

#### NRC 0x24 - RequestSequenceError 🔄
**What it looks like:** `7F 36 24`
**What it means:** Services sent in wrong order
**When you see it:** Multi-step operations (programming, download)
**Action:**
- Follow correct sequence: 0x10→0x27→0x34→0x36→0x37
- Don't skip required steps
- Wait for previous service to complete

#### NRC 0x93 - VoltageToolow / 0x94 - VoltageTooHigh 🔋
**What it looks like:** `7F 34 93` or `7F 34 94`
**What it means:** Battery voltage outside safe range
**When you see it:** Programming operations
**Action:**
- **STOP** - voltage issue could brick the module
- Connect battery charger
- Verify voltage: 12.5V - 14.5V recommended

---

## 🔧 Programming-Specific NRC Codes

### Service 0x34 (RequestDownload) Issues
```
7F 34 70  → Upload/Download Not Accepted
7F 34 22  → Conditions Not Correct (preconditions failed)
7F 34 13  → Incorrect Length (address/size wrong format)
7F 34 31  → Request Out of Range (invalid memory address)
```

### Service 0x36 (TransferData) Issues
```
7F 36 24  → Request Sequence Error (missing 0x34 first)
7F 36 13  → Wrong Block Length
7F 36 71  → Transfer Data Suspended (interrupted)
```

### Service 0x37 (RequestTransferExit) Issues
```
7F 37 24  → Sequence Error (transfer not complete)
7F 37 72  → General Programming Failure
```

---

## 📊 NRC Severity Levels

### ✅ IGNORE (Normal Operation)
- **0x78** - Response Pending (just wait)

### ⚠️ WARNING (Retry May Work)
- **0x22** - Conditions Not Correct (fix preconditions)
- **0x31** - Request Out of Range (adjust parameters)
- **0x13** - Incorrect Format (fix message)

### 🔴 ERROR (Requires Action)
- **0x33** - Security Access Denied (wrong algorithm)
- **0x35** - Invalid Key (recalculate)
- **0x24** - Sequence Error (restart procedure)

### 🚨 CRITICAL (Stop Immediately)
- **0x36** - Exceed Attempts (locked out)
- **0x93/0x94** - Voltage Issue (risk of brick)
- **0x72** - Programming Failure (module may be damaged)

---

## 🎯 Troubleshooting by Service

### 0x10 (DiagnosticSessionControl)
- **0x12** - Sub-Function Not Supported
- **0x13** - Incorrect Message Length
- **0x22** - Conditions Not Correct

### 0x27 (SecurityAccess)
- **0x33** - Security Access Denied ← Most common
- **0x35** - Invalid Key
- **0x36** - Exceed Number of Attempts ← STOP!
- **0x37** - Required Time Delay Not Expired

### 0x34/0x36/0x37 (Programming Sequence)
- **0x22** - Conditions Not Correct (check preconditions)
- **0x24** - Sequence Error (wrong order)
- **0x31** - Request Out of Range (bad address)
- **0x70** - Upload/Download Not Accepted
- **0x71** - Transfer Suspended
- **0x72** - Programming Failure ← CRITICAL

### 0x22 (ReadDataByIdentifier)
- **0x14** - Response Too Long
- **0x31** - Request Out of Range (invalid DID)
- **0x33** - Security Access Denied (DID protected)

### 0x2E (WriteDataByIdentifier)
- **0x22** - Conditions Not Correct
- **0x31** - Request Out of Range (bad value)
- **0x33** - Security Access Denied
- **0x72** - General Programming Failure

---

## 💡 Quick Decision Tree

```
Got an NRC Code?
│
├─ Is it 0x78? 
│  └─ YES → ✅ WAIT (normal, module is busy)
│
├─ Is it 0x33, 0x35, or 0x36?
│  └─ YES → 🔒 SECURITY ISSUE
│     ├─ 0x33 → Check security algorithm
│     ├─ 0x35 → Recalculate key
│     └─ 0x36 → STOP! Locked out, power cycle needed
│
├─ Is it 0x22?
│  └─ YES → ⚙️ CHECK PRECONDITIONS
│     ├─ Ignition ON?
│     ├─ Vehicle in Park?
│     ├─ Speed = 0?
│     ├─ Doors closed?
│     └─ Correct diagnostic session?
│
├─ Is it 0x93 or 0x94?
│  └─ YES → 🔋 VOLTAGE ISSUE - STOP IMMEDIATELY
│     └─ Connect battery charger, verify 12.5-14.5V
│
├─ Is it 0x24?
│  └─ YES → 🔄 SEQUENCE ERROR
│     └─ Restart from beginning (0x10 → 0x27 → 0x34...)
│
└─ Other codes?
   └─ Check specific service requirements above
```

---

## 🧪 How to Use This in Your Parser

The parser now **automatically emphasizes NRC codes** in Simple Mode:

### What You'll See:

```
⚠️  NRC ERROR #1 ⚠️
========================================
🚨 NEGATIVE RESPONSE CODE (NRC) DETECTED:
🔍 Error Code: 78 (0x78)
💡 Technical: Request correctly received, response pending
📖 In Simple Terms:
   The module received your request and is working on it.
   Just wait - the module will respond when ready.
```

### NRC Summary Section:

```
🚨 NEGATIVE RESPONSE CODES (NRC) - CRITICAL DIAGNOSTIC INFO
────────────────────────────────────────────────────────────
🔍 NRC Code: 0x78 (78)
   Technical: Request correctly received, response pending
   Occurrences: 20 time(s) ⚠️⚠️⚠️
   
   📖 What This Means in Plain English:
      The module is processing your request...
```

---

## 📚 Additional Resources

### ISO 14229 (UDS) Standard
- Defines all NRC codes
- Specifies service requirements
- Details diagnostic protocols

### Ford-Specific Notes
- Some NRCs may have manufacturer-specific meanings
- Check FDRS/IDS documentation for module-specific NRC handling
- Programming operations often generate many 0x78 codes (normal)

---

## 🎓 Pro Tips

1. **NRC 0x78 is your friend** - It means the module is working, not failing
2. **Always check voltage first** - 0x93/0x94 can brick modules
3. **Security lockouts are serious** - 0x36 may require dealer intervention
4. **Sequence matters** - 0x24 means you skipped a step
5. **Read the full response** - Context tells you which service failed

---

## 🔍 Decoding Practice

### Example 1:
```
[00,00,07,54,7F,27,35]
           │   │  │  └─ NRC: 0x35 (Invalid Key)
           │   │  └──── Service: 0x27 (Security Access)
           │   └─────── Negative Response: 0x7F
           └─────────── Target ECU: 0x754 (TCU)
```
**Diagnosis:** Security key calculation is wrong for TCU

### Example 2:
```
[00,00,07,5C,7F,34,78]
           │   │  │  └─ NRC: 0x78 (Response Pending)
           │   │  └──── Service: 0x34 (Request Download)
           │   └─────── Negative Response: 0x7F
           └─────────── Target ECU: 0x75C (TCU response address)
```
**Diagnosis:** TCU is processing download request, wait for completion

---

*This guide covers the most common NRC codes you'll encounter. For a complete list, refer to ISO 14229-1 Annex A.1*
