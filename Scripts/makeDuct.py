from formatExl import Pyxl

class DuctSizes():
    def __init__(self, ductType, smDimension, lgDimension, fittingType):
        self.ductType = ductType
        self.smDimension = int(smDimension)
        self.lgDimension = int(lgDimension)
        self.fittingType = fittingType
        self.exl = Pyxl('Templates/sampleData.xlsx')
        self.wrapList = ['Bare', '2" Insulation', '1" Lined']
        
        #dictionary of fitting types used in generating unique item codes.
        #note: ProExl does not yet support reducers. all other listed fittings are supported.
        self.fittingIndex = {
            'Duct': 0,
            'Start Collars': 1,
            'Couplings': 2,
            '90 Elbows': 3,
            '45 Elbows': 4,
            'Horizontal Elbows': 5,
            'Vertical Elbows': 6,
            'Reducers': 7,
            'Tees': 8,
            'Saddle Taps': 9,
            'Dampers': 10}

    def makeType(self):
        self.exl.createNewSpreadsheet()
        #choose duct type and generate all items in size range.
        if self.ductType == 'Spiral':
            self.makeSpiral(self.smDimension, self.lgDimension)
        elif self.ductType == 'Rectangular':
            self.wrapList.append('Mastic')
            self.makeRectangular(self.smDimension, self.lgDimension)

    def makeSpiral(self, smDiameter, lgDiameter):
        while self.smDimension <= self.lgDimension:
            self.defineDimensions()
            self.smDimension += 2

    def makeRectangular(self, smWidth, lgWidth):
        while self.smDimension <= self.lgDimension:
            self.addDepth(self.smDimension)
            self.smDimension += 2
            
    def addDepth(self, width):
        #create depth dimension for rectangular ductwork e.g. 50"x30".
        self.depth = 6
        while self.depth <= width:
            self.defineDimensions()
            self.depth += 2

    def defineDimensions(self):
        if self.ductType == 'Rectangular':
            self.dimensions = str(self.smDimension) + '"x' + str(self.depth) + '"'
        elif self.ductType == 'Spiral':
            self.dimensions = str(self.smDimension) + '"'
        self.addWrap()

    def addWrap(self):
        #index to track which wrap type is applied. used when creating itemCode.
        self.wrapIndex = 1
        for wrap in self.wrapList:
            self.wrapped = self.dimensions + ' ' + self.fittingType + ' - ' + wrap
            self.describeDuct()
            self.wrapIndex += 1
    
    def describeDuct(self):
        self.itemDescription = self.wrapped
        self.subdivisionDescription = (str(self.smDimension) +
                                           '" ' + self.ductType + ' ' + self.fittingType)
        self.divisionDescription = 'HVAC'
        self.generateCodes(self.smDimension)

    def generateCodes(self, width):
        #assigns unique itemCode & subdivisionCode to each fititng & size.
        if self.ductType == 'Rectangular':
            self.itemCode = (10*self.wrapIndex) + (20*(self.depth-6))
            self.subdivisionCode = (self.smDimension*10) + (self.fittingIndex[self.fittingType]*1000)
        elif self.ductType == 'Spiral':
            self.itemCode = (str(self.smDimension) + str(self.wrapIndex))
            self.subdivisionCode = 12000 + (self.smDimension*10) + (self.fittingIndex[self.fittingType]*1000)
        self.divisionCode = 12
        self.code = (str(self.divisionCode) + '.' + str(self.subdivisionCode) +
                     '.' + str(self.itemCode))
        self.writeToSpreadsheet()

    def writeToSpreadsheet(self):
        #overwrites activeColumns in formatExl.py and adds new data to excel sheet.
        self.exl.activeColumns['Code'][1] = self.code
        self.exl.activeColumns['DivisionCode'][1] = int(self.divisionCode)
        self.exl.activeColumns['SubDivisionCode'][1] = int(self.subdivisionCode)
        self.exl.activeColumns['ItemCode'][1] = int(self.itemCode)
        self.exl.activeColumns['DivisionDescription'][1] = self.divisionDescription
        self.exl.activeColumns['SubDivisionDescription'][1] = self.subdivisionDescription
        self.exl.activeColumns['ItemDescription'][1] = self.itemDescription
        self.exl.writeData()
        self.exl.row += 1
    
    def saveDuct(self):
        self.exl.saveSpreadsheet()
