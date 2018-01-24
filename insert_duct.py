from formatxl import Pyxl

class DuctSizes():
    def __init__(self, smDimension, lgDimension):
        self.smDimension = int(smDimension)
        self.lgDimension = int(lgDimension)
        self.xl = Pyxl('Book1.xlsx')
        self.xl.createNewSpreadsheet()
        self.wrapList = ['Bare', '2" Insulation', '1" Lined']

    def makeType(self, ductType):
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
        self.wrapIndex = 0
        for wrap in self.wrapList:
            self.wrapIndex += 1
            self.addWrap(wrap, ductType)

    def addWrap(self, wrap, ductType):
        self.wrapped = self.dimensions + ' - ' + wrap
        self.describeDuct(ductType)
    
    def describeDuct(self, ductType):
        self.itemDescription = self.wrapped
        self.subdivisionDescription = (str(self.smDimension) +
                                           '" ' + ductType + ' Duct')
        self.divisionDescription = 'HVAC'
        self.classifyType(ductType)

    def classifyType(self, ductType):
        if ductType == 'Rectangular':
            self.generateCodes(self.smDimension, self.depth)
        elif ductType == 'Spiral':
            self.generateCodes(self.smDimension)

    def generateCodes(self, width, depth=None, dbPatch=True):
        if depth is not None:
            self.itemCode = (str(self.smDimension) + str(self.depth) +
                             str(self.wrapIndex))
        else:
            self.itemCode = (str(self.smDimension) + str(self.wrapIndex))
        if dbPatch == True:
            self.subdivisionCode = (str(int(480+((self.smDimension-48)/2))))
        else:
            self.subdivisionCode = str(self.smDimension*10)
        self.divisionCode = '12'
        self.code = (self.divisionCode + '.' + self.subdivisionCode +
                     '.' + self.itemCode)
        self.writeToSpreadsheet()

    def writeToSpreadsheet(self):
        self.xl.activeColumns['Code'][1] = (self.code)
        self.xl.activeColumns['DivisionCode'][1] = self.divisionCode
        self.xl.activeColumns['SubDivisionCode'][1] = self.subdivisionCode
        self.xl.activeColumns['DivisionDescription'][1] = self.divisionDescription
        self.xl.activeColumns['SubDivisionDescription'][1] = self.subdivisionDescription
        self.xl.activeColumns['ItemDescription'][1] = self.itemDescription
        self.xl.writeData()
        self.xl.row += 1

duct = DuctSizes(50, 52)
duct.makeType('Rectangular')
