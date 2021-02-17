from Field import Int32Field, Int64Field, BoolField, ReaderField, StringField, ArrayField, ConditionalField
from Func import ge
from Reader import Reader
from Readers.GameDesc import GameDesc
from Readers.GamePrefsData import GamePrefsData
from Readers.GameHistoryData import GameHistoryData
from Readers.GameStatData import GameStatData
from Readers.Player import Player
from Readers.GalacticTransport import GalacticTransport
from Readers.Planets import PlanetFactory


"""
GameData
{
    int32 version = 2
    string gameName
    GameDesc
    int64 gameTick
    GamePrefsData preferences (version >= 1)
    GameHistoryData
    uint8_bool hidePlayerModel (version >= 2)
    uint8_bool disableController (version >= 2)
    GameStatData statistics
    int32 planetId
    Player mainPlayer
    int32 factoryCount
    GalacticTransport
    PlanetFactory[factoryCount]
    int32 galaxyStarCount: Must equal GameDesc::starCount or the game will crash.
    int32 numDysonSpheres
    [numDysonSpheres] {
        int32 dysonSphereDataIsAvailableFlag: Must be 0 or 1 or the game will crash.
        DysonSphere (dysonSphereDataIsAvailableFlag == 1)
    }
}
"""


class GameData(Reader):
    version = Int32Field()
    gameName = StringField()
    gameDesc = ReaderField(GameDesc)
    gameTick = Int64Field()
    gamePrefsData = ConditionalField(lambda: ReaderField(GamePrefsData), arg_fields='version', condition_func=ge(1))
    gameHistoryData = ReaderField(GameHistoryData)
    hidePlayerModel = ConditionalField(BoolField, arg_fields='version', condition_func=ge(2))
    disableController = ConditionalField(BoolField, arg_fields='version', condition_func=ge(2))
    gameStatData = ReaderField(GameStatData)
    planetId = Int32Field()
    mainPlayer = ReaderField(Player)
    factoryCount = Int32Field()
    galacticTransport = ReaderField(GalacticTransport)
    planetFactory = ArrayField(lambda: ReaderField(PlanetFactory), length_field='factoryCount')
    galaxyStarCount = Int32Field()
