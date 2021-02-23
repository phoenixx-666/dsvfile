from Fields import FixedHeaderField, Int32Field, Int64Field, ByteStringField, ModelField
from Models import Model
from Models.GameData import GameData


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
