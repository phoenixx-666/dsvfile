from Field import FixedHeaderField, Int32Field, Int64Field, ByteStringField, ReaderField
from Reader import Reader
from Readers.GameData import GameData


class GameSave(Reader):
    header = FixedHeaderField('VFSAVE')
    fileStreamLength = Int64Field()
    saveFileFormatNumber = Int32Field()
    majorGameVersion = Int32Field()
    minorGameVersion = Int32Field()
    releaseGameVersion = Int32Field()
    gameTick = Int64Field()
    nowTicks = Int64Field()
    screenShotPngFile = ByteStringField()
    gameData = ReaderField(GameData)
