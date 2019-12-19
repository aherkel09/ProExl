import re

class Expressions:
    def __init__(self):
        self.divisions = {
            '3': self.division_3(),
            '6': self.division_6(),
            '12': self.division_12(),
        }
        
        self.subtypes = {
            '3': self.subtypes_3(),
            '6': self.subtypes_6(),
            '12': self.subtypes_12(),
        }
        
        self.revisions = {
            '3': self.revisions_3(),
            '6': self.revisions_6(),
            '12': self.revisions_12(),
        }
        
        self.subtype_revisions = {
            '3': self.subtype_revisions_3(),
            '6': self.subtype_revisions_6(),
            '12': self.subtype_revisions_12(),
        }
        
    
    def division_3(self):
        size = '^[0-9]+(-[0-9]+/[0-9]*)?"?.*'
        return self.compile_division({
            'Inserts': size + 'insert+',
            'Unions': size + 'union+',
            'Laterals': size + 'lateral+',
            'Tees': size + 'tee+',
            'Couplings': size + 'coupling+',
            'Elbows': size + 'elbow+',
            'Pipe': size + 'pipe+',
            'Saddle Taps': size + 'saddle tap+',
            'Flanges': size + 'flange+',
            'Valves': size + 'valve+',
            'Caps': size + 'cap+',
            'Plugs': size + 'plug+',
            'Wyes': size + 'wye+',
            'Crosses': size + 'cross+',
            'Cleanouts': size + 'cleanout+',
            'P-Traps': size + 'p-trap+',
            'Locknuts': size + 'locknut+',
            'Nuts': size + 'nut+',
            'Sleeves': size + 'sleeve+',
            'Bushings': size + 'bushing+',
            'Return Bends': size + 'ret(urn)? bend+',
            'Nipples': size + 'nipple+',
            'Sleeves': size + 'sleeve+',
            'Adapters': size + 'adapter+',
            'Reducers': size + 'red+',
        })
        
    
    def subtypes_3(self):
        possible_3 = str(
            'oxygen|service|coil|60\'|dwv|dmv|refr|90|45|22\-1/2|' +
            'wrot|long|short|red|crossover|cast|sanitary|' +
            'double|male|female|brass|type|threaded|125|150|250|flush|' +
            'copper|floor|companion|hex|flared|adapter|compression|' +
            'cxc|cxm|cxf|cxftg|cxnh|cxcxc|cxcxf|cxcxcxc|ftgxc|ftgxm|' +
            'hard|soft|k|l|m'
        )
        
        subtypes = {}
        for d in self.divisions['3']:
            subtypes[d] = possible_3
            
        return self.compile_division(subtypes)
    
    
    def subtype_revisions_3(self):
        return {
            'galv': 'GALV',
            'dmv': 'DWV',
            'red': 'REDUC',
            'g/j': 'GR JOINT',
            'cxc': 'CxC',
            'cxm': 'CxM',
            'cxf': 'CxF',
            'cxftg': 'CxFTG',
            'cxnh': 'CxNH',
            'cxcxc': 'CxCxC',
            'cxcxf': 'CxCxF',
            'cxcxcxc': 'CxCxCxC',
            'ftgxc': 'FTGxC',
            'ftgxm': 'FTGxM',
        }
        
    
    def revisions_3(self):
        return {
            'Adapters': 'SIZE0 ADAPTER_SUBTYPES',
            'Inserts': 'SIZE0 INSERT_SUBTYPES',
            'Laterals': 'SIZE0 LATERAL_SUBTYPES',
            'Tees': 'SIZE0xSIZE1xSIZE2 TEE_SUBTYPES',
            'Couplings': 'SIZE0xSIZE1 COUPLING_SUBTYPES',
            'Elbows': 'SIZE0xSIZE1 ELBOW_SUBTYPES',
            'Pipe': 'SIZE0 PIPE_SUBTYPES',
            'Saddle Taps': 'SIZE0 SADDLE TAP_SUBTYPES',
            'Flanges': 'SIZE0xSIZE1 FLANGE_SUBTYPES',
            'Valves': 'SIZE0xSIZE1 VALVE_SUBTYPES',
            'Unions': 'SIZE0xSIZE1 UNION_SUBTYPES',
            'Caps': 'SIZE0 CAP_SUBTYPES',
            'Plugs': 'SIZE0xSIZE1 PLUG_SUBTYPES',
            'Wyes': 'SIZE0xSIZE1xSIZE2 WYE_SUBTYPES',
            'Crosses': 'SIZE0xSIZE1 CROSS_SUBTYPES',
            'Cleanouts': 'SIZE0 CLEANOUT_SUBTYPES',
            'P-Traps': 'SIZE0 P-TRAP_SUBTYPES',
            'Locknuts': 'SIZE0 LOCKNUT_SUBTYPES',
            'Nuts': 'SIZE0 NUT_SUBTYPES',
            'Sleeves': 'SIZE0 SLEEVE_SUBTYPES',
            'Bushings': 'SIZE0xSIZE1 BUSHING_SUBTYPES',
            'Return Bends': 'SIZE0 RETURN BEND_SUBTYPES',
            'Nipples': 'SIZE0xSIZE1 NIPPLE_SUBTYPES',
            'Reducers': 'SIZE0xSIZE1 REDUCER_SUBTYPES',
        }
        
    
    def division_6(self):
        size = '^[0-9]+(-[0-9]+/[0-9]*)?"?.*'
        
        return self.compile_division({
            'Welds': size + 'weld+',
            'Gaskets': size + 'gasket+',
            'Regulators': 'regulator+',
            'Inserts': size + 'insert+',
            'Adapters': size + 'adapter+',
            'Laterals': size + 'lateral+',
            'Tees': size + 'tee+',
            'Couplings': size + 'coupling+',
            'Elbows': size + 'elbow+',
            'Pipe': size + 'pipe+',
            'Saddle Taps': size + 'saddle tap+',
            'Flanges': size + 'flange+',
            'Valves': size + 'valve+',
            'Unions': size + 'union+',
            'Caps': size + 'cap+',
            'Plugs': size + 'plug+',
            'Wyes': size + 'wye+',
            'Crosses': size + 'cross+',
            'Bushings': size + 'bushing+',
            'Return Bends': size + 'ret(urn)? bend+',
            'Nipples': size + 'nipple+',
            'Reducers': size + 'red+',
        })
        
    
    def subtypes_6(self):
        possible_6 = str(
            'schedule\-40|schedule\-80|90|45|street|black|iron|tee|straight|' +
            'galv|victaulic|plain|bevel|seamless|base|cap|exh|elbow|' +
            'cast|weld|slip|blind|red|concentric|eccentric|gas|flange|' +
            'male|female|ball|solid|cored|square|hex|round|companion|' +
            'compression|floor|short|long|neck|lap-joint|weldolet|sockolet|' +
            'thrdolet|threadolet|pipoweld|line|nozzle|check|butterfly|mechanical|' +
            'gasket|pxp|pxf|pxm|pxpxp|pxpxf|fs s/w|fs scr|fs soc|g/j|bolt set|' +
            'thread|11.25|22.5|125|150|180|300|2000|3000|6000'
        )
        
        subtypes = {}
        for d in self.divisions['6']:
            subtypes[d] = possible_6
            
        return self.compile_division(subtypes)
    
    
    def revisions_6(self):
        return {
            'Welds': 'SIZE0xSIZE1 WELD_SUBTYPES',
            'Gaskets': 'SIZE0 GASKET_SUBTYPES',
            'Regulators': 'SIZE0 REGULATOR_SUBTYPES',
            'Adapters': 'SIZE0 ADAPTER_SUBTYPES',
            'Inserts': 'SIZE0 INSERT_SUBTYPES',
            'Laterals': 'SIZE0 LATERAL_SUBTYPES',
            'Tees': 'SIZE0xSIZE1xSIZE2 TEE_SUBTYPES',
            'Couplings': 'SIZE0xSIZE1 COUPLING_SUBTYPES',
            'Elbows': 'SIZE0xSIZE1 ELBOW_SUBTYPES',
            'Pipe': 'SIZE0 PIPE_SUBTYPES',
            'Saddle Taps': 'SIZE0 SADDLE TAP_SUBTYPES',
            'Flanges': 'SIZE0xSIZE1 FLANGE_SUBTYPES',
            'Valves': 'SIZE0xSIZE1 VALVE_SUBTYPES',
            'Unions': 'SIZE0xSIZE1 UNION_SUBTYPES',
            'Caps': 'SIZE0 CAP_SUBTYPES',
            'Plugs': 'SIZE0xSIZE1 PLUG_SUBTYPES',
            'Wyes': 'SIZE0xSIZE1xSIZE2 WYE_SUBTYPES',
            'Crosses': 'SIZE0xSIZE1 CROSS_SUBTYPES',
            'Bushings': 'SIZE0xSIZE1 BUSHING_SUBTYPES',
            'Return Bends': 'SIZE0 RETURN BEND_SUBTYPES',
            'Nipples': 'SIZE0xSIZE1 NIPPLE_SUBTYPES',
            'Reducers': 'SIZE0xSIZE1 REDUCER_SUBTYPES',
        }
        
    
    def subtype_revisions_6(self):
        return {
            'schedule-40': 'SCHED 40',
            'schedule-80': 'SCHED 80',
            'galv': 'GALV',
            'plain': 'PLAIN END',
            'bevel': 'BEVELED',
            'red': 'REDUC',
            'short': 'SHORT RAD',
            'long': 'LONG RAD',
            'g/j': 'GR JOINT',
            'pxp': 'PxP',
            'pxf': 'PxF',
            'pxm': 'PxM',
            'pxpxp': 'PxPxP',
            'pxpxf': 'PxPxF',
        }
        
    
    def division_12(self):
        size = '[0-9]+(-[0-9]+/[0-9]*)?"?[ ]?x?[ ]?[0-9]?(-[0-9]+/[0-9]*)?"?.*'
        
        return self.compile_division({
            'Straight Collar': '^straight collar.*' + size,
            'End Caps': '^' + size + 'end cap',
            'Rectangular Tees': '^' + size + 'x[ ]?[0-9]+[0-9]*"? - rectangular tee',
            'Vertical Elbows': 'vertical duct elbow',
            'Horizontal Elbows': 'horizontal duct elbow',
            'Reducers': '^' + size + '([ ]*to[ ]*|[ ]*-[ ]*)' + size + '[ ]*-[ ]*reducer',
            'AES Dropbox': '^aes drop',
            'Grilles': size + 'grill',
            'Registers': size + 'register',
            'Lay-Ins': size + '(lay-in)',
            'Linears': size + 'linear',
            'Diffusers': size + 'diffuser',
            'Louvers': size + 'louver',
            'Dampers': size + 'damper',
            'Sheet Metal': size + 'sheet metal',
            'Collars': size + 'collar',
            'Round Reducers': size + 'reducer',
            'Round Tees': size + 'tee',
            'Ys': size + ' - y',
            'Saddle Taps': size + '[ ]*on[ ]*' + size + 'saddle',
            'Flex': size + 'flex',
            'VAVs': size + 'vav ',
            'Chimney Vents': size + 'chimney',
            'Caps': size + 'cap',
            'Roof Flashings': size + 'roof flashing',
            'Intakes': size + 'intake',
            'Access Doors': size + 'access door',
            'PVC': size + 'pvc',
            'Grease Duct': size + 'grease',
            'Clean Out Doors': size + 'clean out door',
            'Couplings': size + 'coupling',
            'Fire Wrap': size + 'fire wrap',
            'Risers': size + 'riser',
            'Offsets': size + 'offset',
            'Elbows': size + 'elbow',
            'Side Angles': size + 'side angle',
            '3-Ways': size + '3-way',
            'Rd Pipe': size + 'rd\. s',
            'Spiral Duct': size + 'spiral duct',
            'Rectangular Duct': '^' + size + '( rectangular)? - [1|2|b|m]+',
        })
        
        
    def subtypes_12(self):
        possible_12 = str(
            'bare|mastic|wrap|lined|spiral|floor|elbow|gas connector|duct|' +
            'exhaust|return|supply|round|baseboard|rect|linear|soffit|45|90|' +
            'drum|12\" x 12\"|24\" x 24\"|lay\-in|provide|install|volume|fire|' +
            'bellmouth|start|flex|ungasketed|gasketed|manual|butterfly|cable|edge|2 hour|' +
            'r\-4\.2|r\-6\.0|non-insulated|pvc|motorized|stack|sweep|rd\.|' +
            'sweep|3-way|28 ga|26 ga|30 ga|24 ga|22 ga|24\" long|48\" long|72\" long|' +
            'bypass|damper|\(4\) grilles|\(6\) grilles|concentric|door|connector|' +
            'flange|braid|thread|weld|rain|storm|vent|sleeve|revolving|galvanized|' +
            'stainless|dryer|fresh air|1\" [w|l|i]{1}|2\" [w|l|i]{1}'
        )
        
        subtypes = {}
        for d in self.divisions['12']:
            subtypes[d] = possible_12
            
        return self.compile_division(subtypes)
        
        
    def revisions_12(self):
        return {
            'Straight Collar': 'SIZE0xSIZE1 RECT COLLAR_SUBTYPES',
            'End Caps': 'SIZE0xSIZE1 END CAP_SUBTYPES',
            'Rectangular Tees': 'SIZE0xSIZE1xSIZE2 RECT TEE_SUBTYPES',
            'Vertical Elbows': 'SIZE0xSIZE1 VERT DUCT ELBOW_SUBTYPES',
            'Horizontal Elbows': 'SIZE0xSIZE1 HORIZ DUCT ELBOW_SUBTYPES',
            'Reducers': 'SIZE0xSIZE1 TO SIZE2xSIZE3 REDUCER_SUBTYPES',
            'Grilles': 'SIZE0xSIZE1 GRILLE_SUBTYPES',
            'Registers': 'SIZE0xSIZE1 REGISTER_SUBTYPES',
            'Linears': 'SIZE0 DIFFUSER_SUBTYPES',
            'Lay-Ins': 'SIZE0 DIFFUSER_SUBTYPES',
            'Diffusers': 'SIZE0xSIZE1 DIFFUSER_SUBTYPES',
            'Louvers': 'SIZE0xSIZE1 LOUVER_SUBTYPES',
            'Dampers': 'SIZE0xSIZE1 DAMPER_SUBTYPES',
            'Sheet Metal': 'SIZE0 SHEET METAL PIPE_SUBTYPES',
            'Collars': 'SIZE0xSIZE1 COLLAR_SUBTYPES',
            'Round Reducers': 'SIZE0xSIZE1 REDUCER_SUBTYPES',
            'Round Tees': 'SIZE0xSIZE1xSIZE2 TEE_SUBTYPES',
            'Ys': 'SIZE0xSIZE1xSIZE2 Y_SUBTYPES',
            'Saddle Taps': 'SIZE0 ON SIZE1xSIZE2xSIZE3 SADDLE TAP_SUBTYPES',
            'Flex': 'SIZE0 FLEX_SUBTYPES',
            'AES Dropbox': 'AES DROPBOX_SUBTYPES',
            'VAVs': 'SIZE0 VAV_SUBTYPES',
            'Chimney Vents': 'SIZE0 CHIMNEY_SUBTYPES',
            'Caps': 'SIZE0xSIZE1 CAP_SUBTYPES',
            'Roof Flashings': 'SIZE0 ROOF FLASHING_SUBTYPES',
            'Intakes': 'SIZE0 INTAKE_SUBTYPES',
            'Access Doors': 'SIZE0xSIZE1 ACCESS DOOR_SUBTYPES',
            'PVC': 'SIZE0 PVC_SUBTYPES',
            'Grease Duct': 'SIZE0XSIZE1 GREASE_SUBTYPES',
            'Clean Out Doors': 'SIZE0xSIZE1 CLEAN OUT DOOR_SUBTYPES',
            'Couplings': 'SIZE0 COUPLING_SUBTYPES',
            'Fire Wrap': 'SIZE0xSIZE1 FIRE WRAP_SUBTYPES',
            'Risers': 'SIZE0xSIZE1 RISER_SUBTYPES',
            'Offsets': 'SIZE0xSIZE1 OFFSET_SUBTYPES',
            'Elbows': 'SIZE0 ELBOW_SUBTYPES',
            'Side Angles': 'SIZE0xSIZE1 SIDE ANGLE_SUBTYPES',
            '3-Ways': 'SIZE0xSIZE1 3-WAY_SUBTYPES',
            'Rd Pipe': 'SIZE0 PIPE_SUBTYPES',
            'Spiral Duct': 'SIZE0 SPIRAL DUCT_SUBTYPES',
            'Rectangular Duct': 'SIZE0xSIZE1 RECT_SUBTYPES',
        }
        
    
    def subtype_revisions_12(self):
        return {
            '2" w': '2" WRAP',
            '2" i': '2" WRAP',
            '2" l': '',
            '1" l': '1" LINED',
            '1" i': '1" LINED',
            '2 hour': '2 HR',
            'rd.': 'ROUND',
            '24" x 24"': '24x24',
            '12" x 12"': '12x12',
        }
        
    
    def compile_division(self, division_data):
        for d in division_data:
            division_data[d] = re.compile(division_data[d], re.IGNORECASE)
        
        return division_data
    

if __name__ == '__main__':
    exp = Expressions()
    for div_num in exp.divisions:
        print('Division ' + div_num + ':\n' + str(exp.divisions[div_num]) + '\n')