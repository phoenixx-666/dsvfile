from Fields import EnumField, Int16Field


class EInserterStage(EnumField):
    enum_values = ('Picking', 'Sending', 'Inserting', 'Returning')


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
