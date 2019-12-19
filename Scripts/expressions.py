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
            'Bushings': size + 'bushing+',
            'Return Bends': size + 'ret(urn)? bend+',
            'Nipples': size + 'nipple+',
            'Sleeves': size + 'sleeves+',
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
            'schedule\-40|schedule\-80|90|45|street|black|iron|' +
            'galv|victaulic|thread|plain|bevel|seamless|base|' +
            'cast|weld|slip|blind|red|concentric|eccentric|' +
            'male|female|ball|solid|cored|square|hex|round|companion|' +
            'compression|floor|short|long|neck|lap|weldolet|sockolet|' +
            'thrdolet|pipoweld|line|nozzle|check|butterfly|mechanical|' +
            'gasket|pxp|pxf|pxm|pxpxp|pxpxf|g/j|bolt set|11.25|' +
            '22.5|125|150|180|300|2000|3000|6000'
        )
        
        subtypes = {}
        for d in self.divisions['6']:
            subtypes[d] = possible_6
            
        return self.compile_division(subtypes)
    
    
    def revisions_6(self):
        return {
            'Welds': 'SIZE0xSIZE1 WELD_SUBTYPES',
            'Gaskets': 'SIZE0 GASKET_SUBTYPES',
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
            'thread': 'THREADED',
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
        size_x_size = '[0-9]+[0-9]*"?[ ]?x[ ]?[0-9]+[0-9]*"?'
        
        return self.compile_division({
            'Straight Collar': '^straight collar',
            'Reducers': '^' + size_x_size + '([ ]*to[ ]*|[ ]*-[ ]*)' + size_x_size + '[ ]*-[ ]*reducer',
            'End Caps': '^' + size_x_size + ' - end cap',
            'Rectangular Duct': '^' + size_x_size + '( rectangular)? - (?!fire|bottom|side)',
            'Rectangular Tees': '^' + size_x_size + 'x[ ]?[0-9]+[0-9]*"? - rectangular tee',
            'Vertical Elbows': 'vertical duct elbow',
            'Horizontal Elbows': 'horizontal duct elbow',
        })
        
        
    def subtypes_12(self):
        return self.compile_division({
            'Straight Collar': '(bare|1" [w|l|i]*|2" [w|l|i]*)+',
            'Rectangular Duct': '(bare|1" [w|l|i]*|2" [w|l|i]*|mastic)+',
            'Vertical Elbows': '(bare|wrapped|lined)+',
            'Horizontal Elbows': '(bare|wrapped|lined)+',
        })
        
        
    def revisions_12(self):
        return {
            'Straight Collar': 'SIZE0xSIZE1 COLLAR_SUBTYPES',
            'Reducers': 'SIZE0xSIZE1 TO SIZE0xSIZE1 REDUCER_SUBTYPES',
            'End Caps': 'SIZE0xSIZE1 END CAP_SUBTYPES',
            'Rectangular Duct': 'SIZE0xSIZE1 RECT_SUBTYPES',
            'Rectangular Tees': 'SIZE0xSIZE1xSIZE2 RECT TEE_SUBTYPES',
            'Vertical Elbows': 'SIZE0xSIZE1 STACK ELBOW_SUBTYPES',
            'Horizontal Elbows': 'SIZE0xSIZE1 SWEEP ELBOW_SUBTYPES',
        }
        
    
    def subtype_revisions_12(self):
        return {
            '2"': '2" WRAP',
            '1"': '1" LINED',
            'mastic': 'MASTIC',
            'bare': 'BARE',
            'wrapped': 'WRAPPED',
            'lined': 'LINED',
        }
        
    
    def compile_division(self, division_data):
        for d in division_data:
            division_data[d] = re.compile(division_data[d], re.IGNORECASE)
        
        return division_data
    

if __name__ == '__main__':
    exp = Expressions()
    for div_num in exp.divisions:
        print('Division ' + div_num + ':\n' + str(exp.divisions[div_num]) + '\n')