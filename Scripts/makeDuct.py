from formatExl import Pyxl

class DuctSizes():
    def __init__(self, smDimension, lgDimension):
        self.smDimension = int(smDimension)
        self.lgDimension = int(lgDimension)
        self.exl = Pyxl('Templates/sampleData.xlsx')
        self.exl.createNewSpreadsheet()
        self.wrapList = ['Bare', '2" Insulation', '1" Lined']

    def makeType(self, ductType):
        #choose duct type and generate all items in size range.
        if ductType == 'Spiral':
            self.makeSpiral(self.smDimension, self.lgDimension)
        elif ductType == 'Rectangular':
            self.wrapList.append('Mastic')
            self.makeRectangular(self.smDimension, self.lgDimension)

    def makeSpiral(self, smDiameter, lgDiameter, ductType='Spiral'):
        while self.smDimension <= self.lgDimension:
            self.defineDimensions(ductType)
            self.smDimension += 2

    def makeRectangular(self, smWidth, lgWidth):
        while self.smDimension <= self.lgDimension:
            self.addDepth(self.smDimension)
            self.smDimension += 2

    def addDepth(self, width, ductType='Rectangular'):
        #create depth dimension for rectangular ductwork e.g. 50"x30".
        self.depth = 6
        while self.depth <= width:
            self.defineDimensions(ductType)
            self.depth += 2

    def defineDimensions(self, ductType):
        if ductType == 'Rectangular':
            self.dimensions = str(self.smDimension) + '"x' + str(self.depth) + '"'
        elif ductType == 'Spiral':
            self.dimensions = str(self.smDimension) + '"'
        self.iterWrap(ductType)

    def iterWrap(self, ductType):
        #index to track which wrap type is applied. used when creating itemCode.
        self.wrapIndex = 1
        for wrap in self.wrapList:
            self.addWrap(wrap, ductType)
            self.wrapIndex += 1

    def addWrap(self, wrap, ductType):
        self.wrapped = self.dimensions + ' - ' + wrap
        self.describeDuct(ductType)
    
    def describeDuct(self, ductType):
        self.itemDescription = self.wrapped
        self.subdivisionDescription = (str(self.smDimension) +
                                           '" ' + ductType + ' Duct')
        self.divisionDescription = 'HVAC'
        self.generateCodes(self.smDimension, ductType)

    def generateCodes(self, width, ductType, dbPatch=True):
        if ductType == 'Rectangular':
            self.itemCode = (str(self.smDimension) + str(self.depth) +
                             str(self.wrapIndex))
        elif ductType == 'Spiral':
            self.itemCode = (str(self.smDimension) + str(self.wrapIndex))
        #formatting subdivisionCode for use with existing database. Not normally necessary.
        if dbPatch == True:
            self.subdivisionCode = (str(int(480+((self.smDimension-48)/2))))
        else:
            self.subdivisionCode = str(self.smDimension*10)
        self.divisionCode = '12'
        self.code = (self.divisionCode + '.' + self.subdivisionCode +
                     '.' + self.itemCode)
        self.writeToSpreadsheet(ductType)

    def writeToSpreadsheet(self, ductType):
        #overwrites activeColumns in formatExl.py and adds new data to excel sheet.
        self.exl.activeColumns['Code'][1] = self.code
        self.exl.activeColumns['DivisionCode'][1] = self.divisionCode
        self.exl.activeColumns['SubDivisionCode'][1] = self.subdivisionCode
        self.exl.activeColumns['DivisionDescription'][1] = self.divisionDescription
        self.exl.activeColumns['SubDivisionDescription'][1] = self.subdivisionDescription
        self.exl.activeColumns['ItemDescription'][1] = self.itemDescription
        self.exl.writeData()
        self.exl.row += 1
    
    def saveDuct(self):
        self.exl.saveSpreadsheet()
