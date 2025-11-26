"""
ECU Node Reference Database
Contains information about specific ECU nodes and their DIDs for automotive diagnostics
Updated with complete 75+ module list from vehicle specification
"""

# ECU Node Database - Complete list of all ECU modules
ECU_NODES = {
    # Audio & Entertainment
    "7A4": {"acronym": "AAM", "name": "Audio Amplifier Module", "protocol": "CAN", "category": "audio"},
    "727": {"acronym": "ACM", "name": "Audio Front Control Module", "protocol": "CAN", "category": "audio"},
    "774": {"acronym": "RACM", "name": "Rear Audio Control Module", "protocol": "CAN", "category": "audio"},
    "783": {"acronym": "DSP", "name": "Audio Digital Signal Processing Module", "protocol": "CAN", "category": "audio"},
    
    # Braking Systems (CRITICAL)
    "760": {"acronym": "ABS", "name": "Anti-Lock Brake System (ABS) Control Module", "protocol": "CAN", "critical": True, "category": "safety"},
    "7F2": {"acronym": "ABSB", "name": "Anti-Lock Brake System (ABS) Control Module B", "protocol": "CAN", "critical": True, "category": "safety"},
    
    # Climate Control
    "7C7": {"acronym": "ACCM", "name": "Air Conditioning Control Module", "protocol": "CAN", "category": "climate"},
    "6E0": {"acronym": "ACCMB", "name": "Air Conditioning Control Module B", "protocol": "CAN", "category": "climate"},
    "733": {"acronym": "HVAC", "name": "Heating, Ventilation, and Air Conditioning Module", "protocol": "CAN", "category": "climate"},
    "776": {"acronym": "SCME", "name": "Front Seat Climate Control Module", "protocol": "CAN", "category": "climate"},
    "777": {"acronym": "SCMF", "name": "Rear Seat Climate Control Module", "protocol": "CAN", "category": "climate"},
    
    # Infotainment & Display (CRITICAL)
    "7D0": {"acronym": "APIM", "name": "Accessory Protocol Interface Module", "protocol": "CAN", "critical": True, "category": "infotainment"},
    "720": {"acronym": "IPC", "name": "Instrument Panel Cluster", "protocol": "CAN", "critical": True, "category": "display"},
    "7B2": {"acronym": "HUD", "name": "Heads Up Display Module", "protocol": "CAN", "category": "display"},
    
    # Drivetrain & Performance
    "792": {"acronym": "ATCM", "name": "All Terrain Control Module", "protocol": "CAN", "category": "drivetrain"},
    "703": {"acronym": "AWD", "name": "All Wheel Drive", "protocol": "CAN", "category": "drivetrain"},
    "795": {"acronym": "DCMR", "name": "Differential Control Module Rear", "protocol": "CAN", "category": "drivetrain"},
    "761": {"acronym": "TCCM", "name": "Transfer Case Control Module", "protocol": "CAN", "category": "drivetrain"},
    "7E9": {"acronym": "TCM", "name": "Transmission Control Module", "protocol": "CAN", "critical": True, "category": "drivetrain"},
    
    # Body Control (CRITICAL)
    "726": {"acronym": "BCM", "name": "Body Control Module", "protocol": "CAN", "critical": True, "category": "body"},
    "6F0": {"acronym": "BCMC", "name": "Body Control Module C / Battery Junction Box", "protocol": "CAN", "category": "body"},
    
    # Battery & Power Management (CRITICAL)
    "7E4": {"acronym": "BECM", "name": "Battery Energy Control Module", "protocol": "CAN", "critical": True, "category": "power"},
    "723": {"acronym": "BECMB", "name": "Battery Energy Control Module B", "protocol": "CAN", "critical": True, "category": "power"},
    "746": {"acronym": "DCDC", "name": "Direct Current / Direct Current Convertor Control Module", "protocol": "CAN", "category": "power"},
    "6F1": {"acronym": "DCACA", "name": "Direct Current / Alternating Current Convertor Module A", "protocol": "CAN", "category": "power"},
    "6F5": {"acronym": "OBCC", "name": "Off-Board Charger Controller", "protocol": "CAN", "category": "power"},
    
    # Camera & Vision Systems
    "764": {"acronym": "CCM", "name": "Cruise Control Module", "protocol": "CAN", "category": "camera"},
    "7C1": {"acronym": "CMR", "name": "Camera Module Rear (Driver Status Monitor Camera Module)", "protocol": "CAN", "category": "camera"},
    "706": {"acronym": "IPMA", "name": "Image Processing Module A", "protocol": "CAN", "category": "camera"},
    "7B1": {"acronym": "IPMB", "name": "Image Processing Module B", "protocol": "CAN", "category": "camera"},
    "6F2": {"acronym": "SODCMC", "name": "Side Obstacle Detection Control Module C", "protocol": "CAN", "category": "camera"},
    "6F3": {"acronym": "SODCMD", "name": "Side Obstacle Detection Control Module D", "protocol": "CAN", "category": "camera"},
    "7C4": {"acronym": "SODL", "name": "Side Obstacle Detection Control Module LH", "protocol": "CAN", "category": "camera"},
    "7C6": {"acronym": "SODR", "name": "Side Obstacle Detection Control Module RH", "protocol": "CAN", "category": "camera"},
    
    # Door Control Modules
    "7A2": {"acronym": "DCME", "name": "Door Control Module E", "protocol": "CAN", "category": "doors"},
    "762": {"acronym": "DCMF", "name": "Door Control Module F", "protocol": "CAN", "category": "doors"},
    "7B3": {"acronym": "DCMG", "name": "Door Control Module G", "protocol": "CAN", "category": "doors"},
    "7B4": {"acronym": "DCMH", "name": "Door Control Module H", "protocol": "CAN", "category": "doors"},
    "740": {"acronym": "DDM", "name": "Driver Door Module", "protocol": "CAN", "category": "doors"},
    "741": {"acronym": "PDM", "name": "Passenger Door Module", "protocol": "CAN", "category": "doors"},
    
    # Seat Control Modules
    "744": {"acronym": "DSM", "name": "Driver Front Seat Module / Running Board Control Module", "protocol": "CAN", "category": "seats"},
    "7A3": {"acronym": "SCMB", "name": "Passenger Front Seat Module", "protocol": "CAN", "category": "seats"},
    "702": {"acronym": "SCMC", "name": "Seat Control Module C", "protocol": "CAN", "category": "seats"},
    "763": {"acronym": "SCMD", "name": "Seat Control Module D", "protocol": "CAN", "category": "seats"},
    "712": {"acronym": "SCMG", "name": "Driver Multi-Contour Seat Module", "protocol": "CAN", "category": "seats"},
    "713": {"acronym": "SCMH", "name": "Passenger Multi-Contour Seat Module", "protocol": "CAN", "category": "seats"},
    "787": {"acronym": "SCMJ", "name": "Seat Control Module J", "protocol": "CAN", "category": "seats"},
    
    # Lighting Control
    "734": {"acronym": "HCM", "name": "Headlamp Control Module", "protocol": "CAN", "category": "lighting"},
    "6F6": {"acronym": "LDCMA", "name": "Lighting Driver Control Module A", "protocol": "CAN", "category": "lighting"},
    "6F7": {"acronym": "LDCMB", "name": "Lighting Driver Control Module B", "protocol": "CAN", "category": "lighting"},
    
    # Safety & Occupant Protection (CRITICAL)
    "765": {"acronym": "OCS", "name": "Occupant Classification System Module", "protocol": "CAN", "critical": True, "category": "safety"},
    "737": {"acronym": "RCM", "name": "Restraints Control Module", "protocol": "CAN", "critical": True, "category": "safety"},
    
    # Driver Assistance & Parking
    "750": {"acronym": "PACM", "name": "Pedestrian Alert Control Module", "protocol": "CAN", "category": "assist"},
    "736": {"acronym": "PAM", "name": "Parking Assist Control Module", "protocol": "CAN", "category": "assist"},
    
    # Powertrain (CRITICAL)
    "7E0": {"acronym": "PCM", "name": "Powertrain Control Module", "protocol": "CAN", "critical": True, "category": "powertrain"},
    
    # Steering Systems (CRITICAL)
    "730": {"acronym": "PSCM", "name": "Power Steering Control Module", "protocol": "CAN", "critical": True, "category": "steering"},
    "797": {"acronym": "SASM", "name": "Steering Angle Sensor Module", "protocol": "CAN", "category": "steering"},
    "724": {"acronym": "SCCM", "name": "Steering Column Control Module", "protocol": "CAN", "category": "steering"},
    "7C5": {"acronym": "SECM", "name": "Steering Effort Control Module", "protocol": "CAN", "category": "steering"},
    
    # Diagnostics & Communication
    "7E2": {"acronym": "SOBDM", "name": "Secondary On-Board Diagnostic Control Module A", "protocol": "CAN", "category": "diagnostics"},
    "7E7": {"acronym": "SOBDMB", "name": "Secondary On-Board Diagnostic Control Module B", "protocol": "CAN", "category": "diagnostics"},
    "7E6": {"acronym": "SOBDMC", "name": "Secondary On-Board Diagnostic Control Module C", "protocol": "CAN", "category": "diagnostics"},
    "732": {"acronym": "GSM", "name": "Gear Shift Module", "protocol": "CAN", "category": "drivetrain"},
    "716": {"acronym": "GWM", "name": "Gateway Module A", "protocol": "CAN", "category": "diagnostics"},
    
    # Access & Security
    "7A7": {"acronym": "FCIM", "name": "Front Control Interface Module", "protocol": "CAN", "category": "access"},
    "7A1": {"acronym": "GFM", "name": "Generic Function Module (Front Trunk Release Module)", "protocol": "CAN", "category": "access"},
    "731": {"acronym": "RFA", "name": "Remote Function Actuator", "protocol": "CAN", "category": "access"},
    "775": {"acronym": "RGTM", "name": "Rear Gate Trunk Module", "protocol": "CAN", "category": "access"},
    "766": {"acronym": "RBM", "name": "Running Board Control Module", "protocol": "CAN", "category": "access"},
    
    # Connectivity & Telemetry
    "751": {"acronym": "RTM", "name": "Radio Transceiver Module", "protocol": "CAN", "category": "connectivity"},
    "754": {"acronym": "TCU", "name": "Telematic Control Unit Module", "protocol": "CAN", "category": "connectivity"},
    "725": {"acronym": "WACM", "name": "Wireless Accessory Charging Module", "protocol": "CAN", "category": "connectivity"},
    
    # Trailer & Towing
    "791": {"acronym": "TRM", "name": "Trailer Relay Module / Trailer Brake Control Module", "protocol": "CAN", "category": "trailer"},
    
    # Vehicle Dynamics (CRITICAL)
    "721": {"acronym": "VDM", "name": "Vehicle Dynamics Control Module", "protocol": "CAN", "critical": True, "category": "dynamics"},
}

# Critical ECUs that should be highlighted (expanded list)
CRITICAL_ECUS = [
    "APIM",   # Infotainment system
    "ABS",    # Anti-lock braking (safety)
    "ABSB",   # Secondary ABS (safety)
    "IPC",    # Instrument cluster
    "BCM",    # Body control
    "PCM",    # Powertrain control
    "BECM",   # Battery energy control
    "BECMB",  # Secondary battery control
    "TCM",    # Transmission control
    "RCM",    # Restraints/airbags (safety)
    "OCS",    # Occupant classification (safety)
    "PSCM",   # Power steering (safety)
    "VDM",    # Vehicle dynamics (safety)
]

# Common DIDs (Data Identifiers) for diagnostics
COMMON_DIDS = {
    "F190": "VIN (Vehicle Identification Number)",
    "F187": "Vehicle Manufacturer Spare Part Number",
    "F18A": "System Supplier Identifier",
    "F18C": "ECU Serial Number",
    "F191": "Vehicle Manufacturer ECU Hardware Number",
    "F192": "System Supplier ECU Hardware Number",
    "F193": "System Supplier ECU Hardware Version Number",
    "F194": "System Supplier ECU Software Number",
    "F195": "System Supplier ECU Software Version Number",
    "F197": "System Name or Engine Type",
    "F198": "Vehicle Manufacturer ECU Software Number",
    "F199": "Vehicle Manufacturer ECU Software Version Number",
    "F19D": "Vehicle Manufacturer ECU Software Assembly Part Number",
    "F19E": "Vehicle Manufacturer ECU Software Assembly Part Number",
}


def get_ecu_info(node_address: str) -> dict:
    """Get ECU information by node address"""
    # Clean up the node address (remove 0x prefix if present, convert to uppercase)
    clean_address = node_address.replace("0x", "").replace("0X", "").upper()
    
    return ECU_NODES.get(clean_address, None)


def get_did_info(did: str) -> str:
    """Get DID (Data Identifier) information"""
    # Clean up the DID (remove 0x prefix if present, convert to uppercase)
    clean_did = did.replace("0x", "").replace("0X", "").upper()
    
    return COMMON_DIDS.get(clean_did, None)


def is_critical_ecu(node_address: str) -> bool:
    """Check if ECU is critical"""
    ecu_info = get_ecu_info(node_address)
    if ecu_info:
        return ecu_info.get("critical", False)
    return False


def format_ecu_info(node_address: str) -> str:
    """Format ECU information for display"""
    ecu_info = get_ecu_info(node_address)
    if not ecu_info:
        return f"Unknown ECU at address {node_address}"
    
    critical_flag = " ⚠️ CRITICAL" if ecu_info.get("critical") else ""
    network = f" on {ecu_info.get('network', 'N/A')}" if ecu_info.get('network') else ""
    
    return f"{ecu_info['acronym']}{critical_flag} - {ecu_info['name']}{network}"


def get_all_ecu_addresses() -> list:
    """Get list of all known ECU addresses"""
    return list(ECU_NODES.keys())


def get_critical_ecu_addresses() -> list:
    """Get list of critical ECU addresses"""
    return [addr for addr, info in ECU_NODES.items() if info.get("critical", False)]


def explain_ecu_context(node_address: str) -> str:
    """Provide context explanation for an ECU"""
    ecu_info = get_ecu_info(node_address)
    if not ecu_info:
        return "This is an ECU (Electronic Control Unit) in the vehicle's network."
    
    acronym = ecu_info['acronym']
    name = ecu_info['name']
    category = ecu_info.get('category', 'general')
    
    # Provide simple explanations by category and specific module
    explanations = {
        # Critical Systems
        "APIM": "Controls the infotainment system (SYNC). Critical for media, navigation, and vehicle settings.",
        "ABS": "Prevents wheel lockup during braking. Critical safety system.",
        "ABSB": "Secondary anti-lock braking system. Critical safety system.",
        "IPC": "The dashboard display showing speed, fuel, warnings, etc. Critical for driver information.",
        "BCM": "Controls body functions like lights, locks, wipers. Central to vehicle operation.",
        "BCMC": "Secondary body control functions and battery junction box.",
        "PCM": "Controls the engine and transmission. Critical for vehicle performance.",
        "BECM": "Manages battery and electrical systems. Critical for electric/hybrid vehicles.",
        "BECMB": "Secondary battery energy control. Critical for power management.",
        "TCM": "Controls transmission shifting. Critical for vehicle drivability.",
        "TCU": "Handles telematics, connectivity, and remote services.",
        "RCM": "Controls airbags and safety restraints. Critical safety system.",
        "OCS": "Detects seat occupancy for airbag deployment. Critical safety system.",
        "PSCM": "Controls power steering assist. Critical for vehicle handling.",
        "VDM": "Manages vehicle stability and dynamics. Critical safety system.",
        
        # Audio & Entertainment
        "ACM": "Controls the front audio system and speakers.",
        "AAM": "Amplifies audio signals for the sound system.",
        "RACM": "Controls rear audio system and speakers.",
        "DSP": "Processes and enhances audio signals.",
        
        # Climate Control
        "HVAC": "Controls heating, ventilation, and air conditioning.",
        "ACCM": "Manages air conditioning functions.",
        "ACCMB": "Secondary air conditioning control.",
        "SCME": "Controls front seat heating and cooling.",
        "SCMF": "Controls rear seat heating and cooling.",
        
        # Camera & Vision
        "CMR": "Rear-view camera for parking assistance.",
        "CCM": "Manages cruise control functions.",
        "IPMA": "Processes images from front cameras.",
        "IPMB": "Processes images from secondary cameras.",
        "SODCMC": "Side obstacle detection camera C.",
        "SODCMD": "Side obstacle detection camera D.",
        "SODL": "Left side obstacle detection.",
        "SODR": "Right side obstacle detection.",
        
        # Doors & Access
        "DDM": "Controls driver door locks, windows, and switches.",
        "PDM": "Controls passenger door locks, windows, and switches.",
        "DCME": "Door control module E functions.",
        "DCMF": "Door control module F functions.",
        "DCMG": "Door control module G functions.",
        "DCMH": "Door control module H functions.",
        
        # Seats
        "DSM": "Controls driver seat positioning and memory.",
        "SCMB": "Controls passenger seat functions.",
        "SCMC": "Seat control module C.",
        "SCMD": "Seat control module D.",
        "SCMG": "Driver multi-contour seat adjustments.",
        "SCMH": "Passenger multi-contour seat adjustments.",
        "SCMJ": "Seat control module J.",
        
        # Lighting
        "HCM": "Controls headlamp functions and automatic lighting.",
        "LDCMA": "Lighting driver control module A.",
        "LDCMB": "Lighting driver control module B.",
        
        # Steering
        "SASM": "Measures steering wheel angle for stability control.",
        "SCCM": "Controls steering column adjustments and functions.",
        "SECM": "Manages steering effort and feel.",
        
        # Power Management
        "DCDC": "Converts DC voltage levels for electrical systems.",
        "DCACA": "Converts DC to AC for electric motor systems.",
        "OBCC": "Controls off-board charging for electric vehicles.",
        
        # Drivetrain
        "ATCM": "Controls all-terrain and off-road driving modes.",
        "AWD": "Manages all-wheel drive system.",
        "DCMR": "Controls rear differential functions.",
        "TCCM": "Controls transfer case for 4WD systems.",
        "GSM": "Manages gear shift functions and modes.",
        
        # Driver Assistance
        "PACM": "Pedestrian alert system for electric vehicles.",
        "PAM": "Parking assist with sensors and guidance.",
        
        # Diagnostics & Gateway
        "SOBDM": "Secondary on-board diagnostics module.",
        "SOBDMB": "Secondary on-board diagnostics module B.",
        "SOBDMC": "Secondary on-board diagnostics module C.",
        "GWM": "Gateway for network communication between modules.",
        
        # Access & Remote
        "FCIM": "Front control interface for vehicle access.",
        "GFM": "Generic functions including front trunk release.",
        "RFA": "Remote keyless entry and remote start.",
        "RGTM": "Rear gate and trunk functions.",
        "RBM": "Running board deployment and control.",
        
        # Connectivity
        "RTM": "Radio transceiver for wireless communication.",
        "WACM": "Wireless charging pad for mobile devices.",
        
        # Trailer
        "TRM": "Trailer brake and lighting control.",
    }
    
    simple_explanation = explanations.get(acronym, f"Manages {name.lower()} functions.")
    
    if ecu_info.get("critical"):
        simple_explanation += " ⚠️ CRITICAL MODULE - Issues here need immediate attention!"
    
    return simple_explanation


# Export for use in other modules
__all__ = [
    'ECU_NODES',
    'CRITICAL_ECUS',
    'COMMON_DIDS',
    'get_ecu_info',
    'get_did_info',
    'is_critical_ecu',
    'format_ecu_info',
    'get_all_ecu_addresses',
    'get_critical_ecu_addresses',
    'explain_ecu_context',
]
