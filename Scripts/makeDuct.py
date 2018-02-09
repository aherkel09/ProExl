from formatExl import Pyxl

class DuctSizes():
    def __init__(self, ductType, smDimension, lgDimension, fittingType):
        self.ductType = ductType
        self.smDimension = int(smDimension)
        self.lgDimension = int(lgDimension)
        self.fittingType = fittingType
        self.exl = Pyxl('Templates/sampleData.xlsx')
        self.wrapList = ['Bare', '2" Insulation', '1" Lined']
        self.wrapIndex = 1 #index to assign unique itemCodes to ductwork.
        self.reducerIndex = 0 #index to assign unique itemCode to reducers.

        #dictionary of fitting types used in generating unique item codes.
        self.fittingIndex = {
            'Duct': 0,
            'Start Collars': 1,
            'Couplings': 2,
            '90 Elbows': 3,
            '45 Elbows': 4,
            'Horizontal Elbows': 5,
            'Vertical Elbows': 6,
            'Tees': 7,
            'Saddle Taps': 8,
            'End Caps': 9,
            'Volume Dampers': 10,
            'Reducers': 11
            }

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
            if self.fittingType == 'Reducers':
                self.defineReducerDimensions()
            else:
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
            if self.fittingType == 'Reducers':
                self.defineReducerDimensions()
            else:
                self.defineDimensions()
            self.depth += 2
    
    def defineReducerDimensions(self):
        self.reduceTo = 6
        while self.reduceTo < self.smDimension:
            self.reducerType()
            self.reduceTo += 2

    def reducerType(self):
        if self.ductType == 'Spiral':
            self.dimensions = (str(self.smDimension) + '" x ' + str(self.reduceTo) +
                                   '" ' + self.ductType + ' ' + self.fittingType)
            self.reducerIndex += 1
            self.describeItem(self.dimensions)
        elif self.ductType == 'Rectangular':
            self.addReducerDepth()

    def addReducerDepth(self):
        self.reducerDepth = 6
        while self.reducerDepth <= self.depth:
            self.dimensions = (str(self.smDimension) + '"x' + str(self.depth) + '" x ' +
                                str(self.reduceTo) + '"x' + str(self.reducerDepth) + '" ' +
                                self.fittingType)
            self.reducerIndex += 1
            self.describeItem(self.dimensions)
            self.reducerDepth += 2

    def defineDimensions(self):
        if self.ductType == 'Rectangular':
            self.dimensions = (str(self.smDimension) + '"x' + str(self.depth) + '" ' +
                               self.fittingType)
        elif self.ductType == 'Spiral':
            self.dimensions = (str(self.smDimension) + '" ' + self.fittingType)

        if self.fittingType == 'Duct':
            self.addWrap()
        else:
            self.describeItem(self.dimensions)

    def addWrap(self):
        self.wrapIndex = 1
        for wrap in self.wrapList:
            self.ductDimensions = self.dimensions + ' ' + ' - ' + wrap
            self.describeItem(self.ductDimensions)
            self.wrapIndex += 1
    
    def describeItem(self, dimensions):
        self.itemDescription = dimensions
        self.subdivisionDescription = (str(self.smDimension) +
                                       '" ' + self.ductType + ' ' + self.fittingType)
        self.divisionDescription = 'HVAC'
        self.generateCodes(self.smDimension)

    def generateCodes(self, width):
        #assigns unique itemCode & subdivisionCode to each fititng & size.
        if self.ductType == 'Rectangular':
            self.itemCode = (10*self.wrapIndex) + (20*(self.depth-6)) + self.reducerIndex
            self.subdivisionCode = (self.smDimension*10) + (self.fittingIndex[self.fittingType]*1000)
        elif self.ductType == 'Spiral':
            self.itemCode = 10*self.wrapIndex + self.reducerIndex
            self.subdivisionCode = 13000 + (self.smDimension*10) + (self.fittingIndex[self.fittingType]*1000)
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
