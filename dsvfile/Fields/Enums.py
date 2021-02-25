from . import EnumField, Int16Field


__all__ = ['EInserterStage', 'EItem', 'ELogisticStorage', 'EMinerType', 'EMonsterState', 'EMovementState', 'ENaviStage',
           'ERecipe', 'ERecipeType', 'EStorageType', 'EWorkState', 'EVeinType', 'EVeinType16']


class EInserterStage(EnumField):
    enum_values = ('Picking', 'Sending', 'Inserting', 'Returning')


class EItem(EnumField):
    enum_values = {
        -1: 'Lava', 0: 'None', 1001: 'Iron ore', 1002: 'Copper ore', 1003: 'Silicon ore', 1004: 'Titanium ore',
        1005: 'Stone', 1006: 'Coal', 1030: 'Log', 1031: 'Plant fuel', 1011: 'Fire ice', 1012: 'Kimberlite ore',
        1013: 'Fractal silicon', 1014: 'Optical grating crystal', 1015: 'Spiniform stalagmite crystal',
        1016: 'Unipolar magnet', 1101: 'Iron ingot', 1104: 'Copper ingot', 1105: 'High-purity silicon',
        1106: 'Titanium ingot', 1108: 'Stone brick', 1109: 'Energetic graphite', 1103: 'Steel', 1107: 'Titanium alloy',
        1110: 'Glass', 1119: 'Titanium glass', 1111: 'Prism', 1112: 'Diamond', 1113: 'Crystal silicon', 1201: 'Gear',
        1102: 'Magnet', 1202: 'Magnetic coil', 1203: 'Electric motor', 1204: 'Electromagnetic turbine',
        1205: 'Super-magnetic ring', 1206: 'Particle container', 1127: 'Strange matter', 1301: 'Circuit board',
        1303: 'Processor', 1305: 'Quantum chip', 1302: 'Microcrystalline component', 1304: 'Plane filter',
        1402: 'Particle broadband', 1401: 'Plasma exciter', 1404: 'Photon combiner', 1501: 'Solar sail', 1000: 'Water',
        1007: 'Crude oil', 1114: 'Refined oil', 1116: 'Sulfuric acid', 1120: 'Hydrogen', 1121: 'Deuterium',
        1122: 'Antimatter', 1208: 'Critical photon', 1801: 'Hydrogen fuel rod', 1802: 'Deuteron fuel rod',
        1803: 'Antimatter fuel rod', 1115: 'Plastic', 1123: 'Graphene', 1124: 'Carbon nanotube',
        1117: 'Organic crystal', 1118: 'Titanium crystal', 1126: 'Casimir crystal', 1209: 'Graviton lens',
        1210: 'Space warper', 1403: 'Annihilation constraint sphere', 1405: 'Thruster', 1406: 'Reinforced thruster',
        5001: 'Logistics drone', 5002: 'Logistics vessel', 1125: 'Frame material', 1502: 'Dyson sphere component',
        1503: 'Small carrier rocket', 1131: 'Foundation', 1141: 'Accelerant Mk.I', 1142: 'Accelerant Mk.II',
        1143: 'Accelerant Mk.III', 2001: 'Conveyor belt MK.I', 2002: 'Conveyor belt MK.II',
        2003: 'Conveyor belt MK.III', 2011: 'Sorter MK.I', 2012: 'Sorter MK.II', 2013: 'Sorter MK.III',
        2020: 'Splitter(4-direction)', 2101: 'Storage MK.I', 2102: 'Storage MK.II', 2106: 'Storage tank',
        2303: 'Assembling machine Mk.I', 2304: 'Assembling machine Mk.II', 2305: 'Assembling machine Mk.III',
        2201: 'Tesla tower', 2202: 'Wireless power tower', 2212: 'Satellite substation', 2203: 'Wind turbine',
        2204: 'Thermal power station', 2211: 'Mini fusion power station', 2301: 'Mining machine', 2302: 'Smelter',
        2307: 'Oil extractor', 2308: 'Oil refinery', 2306: 'Water pump', 2309: 'Chemical plant', 2314: 'Fractionator',
        2313: 'Spray coater', 2205: 'Solar panel', 2206: 'Accumulator', 2207: 'Accumulator(full)',
        2311: 'EM-Rail Ejector', 2208: 'Ray receiver', 2312: 'Vertical launching silo', 2209: 'Energy exchanger',
        2310: 'Miniature particle collider', 2210: 'Artificial star', 2103: 'Planetary Logistics Station',
        2104: 'Interstellar Logistics Station', 2105: 'Orbital Collector', 2901: 'Matrix lab',
        6001: 'Electromagnetic matrix', 6002: 'Energy matrix', 6003: 'Structure matrix', 6004: 'Information matrix',
        6005: 'Gravity matrix', 6006: 'Universe matrix'}


class ELogisticStorage(EnumField):
    enum_values = ('None', 'Supply', 'Demand')


class EMinerType(EnumField):
    enum_values = ('None', 'Water', 'Vein', 'Oil')


class EMonsterState(EnumField):
    enum_values = ('Null', 'Stopped', 'Wandering')


class EMovementState(EnumField):
    enum_values = ('Walk', 'Drift', 'Fly', 'Sail')


class ENaviStage(EnumField):
    enum_values = ('None', 'Departure', 'OriginOrbit', 'AccOrbit', 'Space', 'DestOrbit', 'Approaching')


class ERecipe(EnumField):
    enum_values = {
        0: 'None', 1: 'Iron ingot', 2: 'Magnet', 3: 'Copper ingot', 4: 'Stone brick', 5: 'Gear', 6: 'Magnetic coil',
        7: 'Wind turbine', 8: 'Tesla tower', 9: 'Electromagnetic matrix', 10: 'Matrix lab', 11: 'Prism',
        12: 'Plasma exciter', 13: 'Wireless power tower', 14: 'Oil extractor', 15: 'Oil refinery',
        16: 'Plasma refining', 17: 'Energetic graphite', 18: 'Energy matrix', 19: 'Hydrogen fuel rod', 20: 'Thruster',
        21: 'Reinforced thruster', 22: 'Chemical plant', 23: 'Plastic', 24: 'Sulfuric acid', 25: 'Organic crystal',
        26: 'Titanium crystal', 27: 'Structure matrix', 28: 'Casimir crystal', 29: 'Casimir crystal (advanced)',
        30: 'Titanium glass', 31: 'Graphene', 32: 'Graphene (advanced)', 33: 'Carbon nanotube', 34: 'Silicon ore',
        35: 'Carbon nanotube (advanced)', 36: 'Particle broadband', 37: 'Crystal silicon', 38: 'Plane filter',
        39: 'Miniature particle collider', 40: 'Deuterium', 41: 'Deuteron fuel rod',
        42: 'Annihilation constraint sphere', 43: 'Artificial star', 44: 'Antimatter fuel rod',
        45: 'Assembling machine Mk.I', 46: 'Assembling machine Mk.II', 47: 'Assembling machine Mk.III',
        48: 'Mining machine', 49: 'Water pump', 50: 'Circuit board', 51: 'Processor', 52: 'Quantum chip',
        53: 'Microcrystalline component', 54: 'Organic crystal (original)', 55: 'Information matrix', 56: 'Smelter',
        57: 'Glass', 58: 'X-ray cracking', 59: 'High-purity silicon', 60: 'Diamond', 61: 'Diamond (advanced)',
        62: 'Crystal silicon (advanced)', 63: 'Steel', 64: 'Thermal power station', 65: 'Titanium ingot',
        66: 'Titanium alloy', 67: 'Solar panel', 68: 'Photon combiner', 69: 'Photon combiner (advanced)',
        70: 'Solar sail', 71: 'EM-Rail Ejector', 72: 'Ray receiver', 73: 'Satellite substation',
        74: 'Mass-energy storage', 75: 'Universe matrix', 76: 'Accumulator', 77: 'Energy exchanger', 78: 'Space warper',
        79: 'Space warper (advanced)', 80: 'Frame material', 81: 'Dyson sphere component',
        82: 'Vertical launching silo', 83: 'Small carrier rocket', 84: 'Conveyor belt MK.I', 85: 'Sorter MK.I',
        86: 'Storage MK.I', 87: 'Splitter(4-direction)', 88: 'Sorter MK.II', 89: 'Conveyor belt MK.II',
        90: 'Sorter MK.III', 91: 'Storage MK.II', 92: 'Conveyor belt MK.III', 93: 'Planetary Logistics Station',
        94: 'Logistics drone', 95: 'Interstellar Logistics Station', 96: 'Logistics vessel', 97: 'Electric motor',
        98: 'Electromagnetic turbine', 99: 'Particle container', 100: 'Particle container (advanced)',
        101: 'Graviton lens', 102: 'Gravity matrix', 103: 'Super-magnetic ring', 104: 'Strange matter',
        106: 'Accelerant Mk.I', 107: 'Accelerant Mk.II', 108: 'Accelerant Mk.III', 109: 'Spray coater',
        110: 'Fractionator', 111: 'Orbital Collector', 112: 'Foundation', 113: 'Mini fusion power station',
        114: 'Storage tank', 115: 'Deuterium fractionation', }


class ERecipeType(EnumField):
    enum_values = {0: 'None', 1: 'Smelt', 2: 'Chemical',  3: 'Refine',  4: 'Assemble',
                   5: 'Particle', 6: 'Exchange', 7: 'PhotonStore', 8: 'Fractionate', 15: 'Research'}


class EStorageType(EnumField):
    enum_values = {0: 'Default', 1: 'Fuel', 9: 'Filtered'}


class EWorkState(EnumField):
    enum_values = ('Idle', 'Running', 'Outputing', 'Lack', 'Full')


class EVeinType(EnumField):
    enum_values = ('None', 'Iron', 'Copper', 'Silicium',
                   'Titanium', 'Stone', 'Coal', 'Oil',
                   'Fireice', 'Diamond', 'Fractal', 'Crysrub',
                   'Grat', 'Bamboo', 'Mag')


class EVeinType16(EVeinType):
    base_type = Int16Field
