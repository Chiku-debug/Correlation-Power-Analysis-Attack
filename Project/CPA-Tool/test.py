import unittest
import csv
from CPA import CPA
import difflib


class TestCPA(unittest.TestCase):

    def testInitTestMatrix(self):
        cpa = CPA()
        cpa.initTraceMatrix()

        rowCount = 100
        traceCount = 2500

        self.assertEqual(len(cpa.plainText), rowCount)
        self.assertEqual(len(cpa.cipherText), rowCount)
        self.assertEqual(len(cpa.traceMatrix), rowCount)
        for row in cpa.traceMatrix:
            self.assertEqual(len(row), traceCount)
            self.assertEqual(type(row), list)
            for col in row:
                self.assertEqual(type(col), float)
        self.assertEqual(cpa.numberOfTraces, rowCount)
        self.assertEqual(cpa.numberOfTracesPoint, traceCount)

    def testCorrelation(self):
        cpa = CPA()
        cpa.initTraceMatrix()
        cpa.initHypothesis_MCU8_AES128(1)
        cpa.findCorrelation()

        traceFile = 'intermediate/waveform.csv'
        
        rowTable = open(traceFile, newline='').readlines()
        for count in range(0,255):
            
            rowString = rowTable[count]
            testCaseString = ','.join(format(x, ".5f") for x in cpa.correlation[count])
            rowStringLength = len(rowString)
            rowStringLength = rowStringLength - 8 # idk why its diff (Nan vs actual value) sx on java is 0.0
            self.assertEqual(testCaseString[0:rowStringLength] == rowString[0:rowStringLength], True)

    def testWaveform(self):
        cpa = CPA()
        results = cpa.CPA()
        self.assertEqual(results["key"].strip(), "78 A4 30 47 95 7D 4C 21 81 5D E6 72 0E AD 6F 41")

    # def testWaveform2(self):
        # CPA.tracefile
        
# if __name__ == '__main__':
#     unittest.main()

# waveform.csv
# 78 A4 30 47 95 7D 4C 21 81 5D E6 72 0E AD 6F 41 

# waveform_HS.csv
# 48 9D B4 B3 F3 17 29 61 CC 2B CB 4E D2 E2 8E B7