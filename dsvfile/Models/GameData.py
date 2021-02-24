from ..Fields import Int64Field, BoolField, ModelField, StringField, ArrayField, ConditionalField
from ..Func import ge
from . import Model, Int32Field
from .GameDesc import GameDesc
from .GamePrefsData import GamePrefsData
from .GameHistoryData import GameHistoryData
from .GameStatData import GameStatData
from .Player import Player
from .GalacticTransport import GalacticTransport
from .Planets import PlanetFactory
from .DysonSphere import DysonSphereSwitch


class GameData(Model):
    version = Int32Field()
    gameName = StringField()
    gameDesc = ModelField(GameDesc)
    gameTick = Int64Field()
    gamePrefsData = ConditionalField(lambda: ModelField(GamePrefsData), arg_fields='version', condition_func=ge(1))
    gameHistoryData = ModelField(GameHistoryData)
    hidePlayerModel = ConditionalField(BoolField, arg_fields='version', condition_func=ge(2))
    disableController = ConditionalField(BoolField, arg_fields='version', condition_func=ge(2))
    gameStatData = ModelField(GameStatData)
    planetId = Int32Field()
    mainPlayer = ModelField(Player)
    factoryCount = Int32Field()
    galacticTransport = ModelField(GalacticTransport)
    planetFactory = ArrayField(lambda: ModelField(PlanetFactory), length_field='factoryCount')
    galaxyStarCount = Int32Field()
    dysonSpheres = ArrayField(lambda: ModelField(DysonSphereSwitch), length_field='galaxyStarCount')
