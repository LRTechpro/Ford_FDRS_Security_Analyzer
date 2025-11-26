# NRC (Negative Response Code) Quick Reference

## Overview
Negative Response Codes (NRC) are used in automotive diagnostics (UDS - Unified Diagnostic Services) to indicate why a service request failed.

## Complete NRC Code List

| Code  | Hex  | Description | Common Causes |
|-------|------|-------------|---------------|
| 16    | 0x10 | General Reject | Service not supported |
| 17    | 0x11 | Service Not Supported | ECU doesn't implement this service |
| 18    | 0x12 | Sub-Function Not Supported | Service exists, but not this sub-function |
| 19    | 0x13 | Incorrect Message Length Or Invalid Format | Message structure error |
| 20    | 0x14 | Response Too Long | Response exceeds buffer size |
| 33    | 0x21 | Busy Repeat Request | ECU is busy, try again later |
| 34    | 0x22 | Conditions Not Correct | Prerequisites not met |
| 36    | 0x24 | Request Sequence Error | Commands must be in specific order |
| 37    | 0x25 | No Response From Subnet Component | Sub-component not responding |
| 38    | 0x26 | Failure Prevents Execution Of Requested Action | Hardware/software failure |
| 49    | 0x31 | Request Out Of Range | Parameter value invalid |
| 51    | 0x33 | Security Access Denied | Authentication/authorization failed |
| 53    | 0x35 | Invalid Key | Wrong security key provided |
| 54    | 0x36 | Exceed Number Of Attempts | Too many failed security attempts |
| 55    | 0x37 | Required Time Delay Not Expired | Must wait before retrying |
| 112   | 0x70 | Upload Download Not Accepted | Transfer rejected |
| 113   | 0x71 | Transfer Data Suspended | Transfer paused |
| 114   | 0x72 | General Programming Failure | Flash programming error |
| 115   | 0x73 | Wrong Block Sequence Counter | Block counter mismatch |
| 120   | 0x78 | Request Correctly Received - Response Pending | ECU needs more time |
| 126   | 0x7E | Sub-Function Not Supported In Active Session | Wrong diagnostic session |
| 127   | 0x7F | Service Not Supported In Active Session | Service needs different session |

## Most Common Codes

### 0x22 - Conditions Not Correct
**When you see this:**
- ECU is in wrong state (e.g., engine running when it should be off)
- Voltage out of range
- Temperature not in acceptable range

**Solution:**
- Check prerequisites for the service
- Verify ECU state
- Check vehicle conditions

### 0x35 - Invalid Key
**When you see this:**
- Wrong security key sent
- Key calculation error
- Security algorithm mismatch

**Solution:**
- Verify key calculation algorithm
- Check seed-key authentication process
- Ensure correct security level

### 0x78 - Response Pending
**When you see this:**
- ECU acknowledges request but needs time
- Normal for long-running operations
- Should be followed by actual response

**Solution:**
- Wait for final response
- This is not an error, just acknowledgment
- Timeout if final response never comes

### 0x31 - Request Out Of Range
**When you see this:**
- Parameter value exceeds limits
- Address out of valid range
- Invalid data identifier

**Solution:**
- Check parameter ranges
- Verify memory addresses
- Confirm data identifier values

### 0x73 - Wrong Block Sequence Counter
**When you see this:**
- Flash programming sequence error
- Blocks sent out of order
- Block counter increment error

**Solution:**
- Reset programming sequence
- Track block counter carefully
- Resend from last successful block

## Response Code Categories

### General (0x10 - 0x3F)
Basic protocol and service-level errors

### Security (0x33 - 0x37)
Authentication and authorization issues

### Data Transfer (0x70 - 0x73)
Upload/download and programming errors

### Session (0x7E - 0x7F)
Diagnostic session-related issues

## Diagnostic Services Reference

### Common UDS Services

| Service | Hex  | Description |
|---------|------|-------------|
| DiagnosticSessionControl | 0x10 | Change diagnostic session |
| ECUReset | 0x11 | Reset ECU |
| SecurityAccess | 0x27 | Unlock protected services |
| CommunicationControl | 0x28 | Enable/disable communication |
| TesterPresent | 0x3E | Keep session active |
| ReadDataByIdentifier | 0x22 | Read specific data |
| ReadMemoryByAddress | 0x23 | Read memory directly |
| WriteDataByIdentifier | 0x2E | Write specific data |
| WriteMemoryByAddress | 0x3D | Write memory directly |
| ClearDiagnosticInformation | 0x14 | Clear DTCs |
| ReadDTCInformation | 0x19 | Read diagnostic trouble codes |
| InputOutputControlByIdentifier | 0x2F | Control actuators |
| RoutineControl | 0x31 | Start/stop routines |
| RequestDownload | 0x34 | Initiate download |
| RequestUpload | 0x35 | Initiate upload |
| TransferData | 0x36 | Transfer data block |
| RequestTransferExit | 0x37 | End transfer |

## Troubleshooting Guide

### Security Access Failed (0x33, 0x35, 0x36)
1. Verify seed-key algorithm
2. Check security level (odd numbers for request, even for key)
3. Ensure correct session (usually extended)
4. Wait for time delays after failures (0x37)

### Programming Errors (0x70 - 0x73)
1. Check memory ranges
2. Verify block sequence
3. Ensure correct programming session
4. Validate data integrity
5. Check voltage stability

### Session Issues (0x7E, 0x7F)
1. Switch to correct diagnostic session first
2. Use 0x10 service to change session
3. Keep session alive with TesterPresent (0x3E)
4. Check session timeout settings

### Timing Issues (0x21, 0x78)
1. Implement proper response pending handling
2. Add delays between requests
3. Don't flood ECU with rapid requests
4. Respect timing parameters

## Best Practices

### 1. Always Handle 0x78
```
If response == 0x78:
    Wait for final response
    Implement timeout (typically 5-10 seconds)
```

### 2. Security Access Pattern
```
1. Request seed (0x27 0x01)
2. Calculate key from seed
3. Send key (0x27 0x02)
4. Verify positive response
```

### 3. Programming Sequence
```
1. Enter programming session (0x10 0x02)
2. Unlock security (0x27)
3. Request download (0x34)
4. Transfer data blocks (0x36)
5. Request transfer exit (0x37)
6. Check dependencies (0x31)
7. Reset ECU (0x11)
```

### 4. Error Recovery
```
On any NRC:
    1. Log the error
    2. Check prerequisites
    3. Wait appropriate delay
    4. Retry with corrections
    5. Escalate if persistent
```

## Additional Resources

- ISO 14229 (UDS Standard)
- ISO 15765 (Diagnostic Communication)
- Vehicle-specific diagnostic specifications
- ECU documentation

---

**Quick Lookup:**
- Security problems? → Check 0x33, 0x35, 0x36
- Timing issues? → Look for 0x21, 0x78
- Programming fails? → Check 0x70-0x73
- Wrong session? → See 0x7E, 0x7F
- Invalid request? → Review 0x11-0x13, 0x31
