CID_ALIVE_REQ = 0x101
CID_ALIVE_RES = 0x102
CID_ALIVE_REP = 0x104
CID_GET_BDINFO_REQ = 0x201
CID_GET_BDINFO_RES = 0x202
CID_SET_BDINFO_REQ = 0x401
CID_SET_BDINFO_RES = 0x402
CID_GET_PROFILE_REQ = 0x801
CID_GET_PROFILE_RES = 0x802
CID_SET_PROFILE_REQ = 0x1001
CID_SET_PROFILE_RES = 0x1002
CID_ACQ_DATA_REP = 0x1104
CID_ALARM_REP = 0x1204
CID_RESET_REQ = 0x1401
CID_RESET_RES = 0x1402
CID_FW_DL_REQ = 0x2001
CID_FW_DL_RES = 0x2002
CID_FW_DL_REP = 0x2004
CID_FW_DATA_REQ = 0x2101
CID_FW_DATA_RES = 0x2102
CID_SIG_DATA_REQ = 0x4001
CID_SIG_DATA_RES = 0x4002
CID_SIG_DATA_REP = 0x4004
CID_LOG_START_REQ = 0x8001
CID_LOG_START_RES = 0x8002
CID_LOG_DATA_REP = 0x8004
CID_LOG_END_REP = 0x8008
CID_MAKE_MAP_REQ = 0xA001
CID_MAKE_MAP_RES = 0xA002
CID_MAKE_MAP_REP = 0xA004
CID_MAP_REQ = 0xB001
CID_MAP_RES = 0xB002
CID_GET_FAREA_REQ = 0xC001
CID_GET_FAREA_RES = 0xC002
CID_SET_FAREA_REQ = 0xD001
CID_SET_FAREA_RES = 0xD002
CID_GET_WIFIINFO_REQ = 0xE001
CID_GET_WIFIINFO_RES = 0xE002
CID_SET_WIFIINFO_REQ = 0xE101
CID_SET_WIFIINFO_RES = 0xE102
CID_IRDATA_REP = 0xFA04

STRUCT_CID_ALIVE_REQ = "HH12sBBBBI"
STRUCT_CID_ALIVE_RES = "HH12sBBBBI"
STRUCT_CID_ALIVE_REP = "HH12sBBBBI"
STRUCT_CID_GET_BDINFO_REQ = "HH12sII"
STRUCT_CID_GET_BDINFO_RES = "HH12s16s4s16s16s32s16s16s16sB3BI"
STRUCT_CID_SET_BDINFO_REQ = "HH12s16s4s16s16s32s16s16s16sB3BI"
STRUCT_CID_SET_BDINFO_RES = "HH12s3BBI"
STRUCT_CID_GET_PROFILE_REQ = "HH12s4BI"
STRUCT_CID_GET_PROFILE_RES = "HH12s32sHHHHHHHHHHHHfffIIIff8BI"
STRUCT_CID_SET_PROFILE_REQ = "HH12s32sHHHHHHHHHHHHfffIIIff8BI"
STRUCT_CID_SET_PROFILE_RES = "HH12s3BBI"
STRUCT_CID_ACQ_DATA_REP = "HH12sBBBB3BBBBHHHBBHHHBBHHHHHHH36BI"
STRUCT_CID_ALARM_REP = "HH12sHH8BI"
STRUCT_CID_RESET_REQ = "HH12sB3BI"
STRUCT_CID_RESET_RES = "HH12sBHBI"
STRUCT_CID_FW_DL_REQ = "HH12s32s16sB3BI"
STRUCT_CID_FW_DL_RES = "HH12sBHBI"
STRUCT_CID_FW_DL_REP = "HH12sB2BBI"
STRUCT_CID_FW_DATA_REQ = "HH12sB3BHHII100BI"
STRUCT_CID_FW_DATA_RES = "HH12sI3BHHIII"
STRUCT_CID_SIG_DATA_REQ = "HH12sBBBBI"
STRUCT_CID_SIG_DATA_RES = "HH12sBBBBI"
STRUCT_CID_SIG_DATA_REP = "HH12sII1600BIIBBIIIII"
STRUCT_CID_LOG_START_REQ = "HH12sII"
STRUCT_CID_LOG_START_RES = "HH12s3BBI"
STRUCT_CID_LOG_DATA_REQ = "HH12sII1600BIIHHIIIII"
STRUCT_CID_LOG_END_REP = "HH12s3BBI"
STRUCT_CID_MAKE_MAP_REQ = "HH12sHHI"
STRUCT_CID_MAKE_MAP_RES = "HH12s3sBI"
STRUCT_CID_MAKE_MAP_REP = "HH12sHBBI"
STRUCT_CID_GET_WIFIINFO_REQ = "HH12sB3BI"
STRUCT_CID_GET_WIFIINFO_RES = "HH12sBB6B16s128s128s128s128s16s16s16s32s16sI36BBB2B4"
STRUCT_CID_SET_WIFIINFO_REQ = "HH12sBB6B16s128s128s128s128s16s16s16s32s16sI36BBB2B4"
STRUCT_CID_SET_WIFIINFO_RES = "HH12sB2BBI"
STRUCT_CID_IRDATA_REP = "HH12sHHHH28BI"

LENGTH = 0
ID = "0"
MainSys = 0
MainRadar = 0
SubSys = 0
SubRadar = 0
CRC32 = 0
