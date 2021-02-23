from ..Fields import FixedHeaderField, Int64Field, ByteStringField, ModelField
from . import Model, Int32Field
from .GameData import GameData


class GameSave(Model):
    header = FixedHeaderField('VFSAVE')
    fileStreamLength = Int64Field()
    saveFileFormatNumber = Int32Field()
    majorGameVersion = Int32Field()
    minorGameVersion = Int32Field()
    releaseGameVersion = Int32Field()
    gameTick = Int64Field()
    nowTicks = Int64Field()
    screenShotPngFile = ByteStringField(format='PNG')
    gameData = ModelField(GameData)
