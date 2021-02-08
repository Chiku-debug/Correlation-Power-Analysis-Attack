import csv
import time
import os
import math
import json

class CPA(object):

    cipherTextCol = 1
    plainTextCol = 0
    extraColFront = 2
    extraColRear = 0
    cipher = 'AES128'
    keysize = 16

    def __init__(self,traceFile = 'waveform.csv'):

        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        inputDirectory = os.path.join(currentDirectory, 'input')
        self.traceFile = os.path.join(inputDirectory, traceFile)

        self.key = []
        self.numberOfTraces = 0
        self.numberOfTracesPoint = 0
        self.plainText = []
        self.cipherText = []
        self.traceMatrix = []
        self.hypothesis = []
        self.correlation = []
        self.assignment31 = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "10": [],
            "11": [],
            "12": [],
            "13": [],
            "14": [],
            "15": [],
            "16": [],
        }
        self.assignment32 = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "10": [],
            "11": [],
            "12": [],
            "13": [],
            "14": [],
            "15": [],
            "16": [],
        }

    def initTraceMatrix(self):

        print("initTraceMatrix")

        plainTextCol = CPA.plainTextCol
        cipherTextCol = CPA.cipherTextCol
        extraColFront = CPA.extraColFront
        extraColRear = CPA.extraColRear

        self.plainText = []
        self.cipherText = []
        self.traceMatrix = []
        self.numberOfTraces = 0
        self.numberOfTracesPoint = 0

        traceFile = self.traceFile

        with open(traceFile, newline='') as csvfile:
            waveformReader = csv.reader(csvfile)

            for row in waveformReader:


                if(self.numberOfTraces is 0):
                    self.numberOfTracesPoint = (len(row) - 1) - (extraColRear + extraColFront)

                self.plainText.append(row[plainTextCol])
                self.cipherText.append(row[cipherTextCol])

                self.numberOfTraces = self.numberOfTraces + 1

                traceRow = []
                
                for col in range(0 + extraColFront,(len(row) - 1) - extraColRear):
                    traceRow.append(float(row[col]))

                self.traceMatrix.append(traceRow)

        # this.br = new BufferedReader(new FileReader(this.traceFile));
        # this.traceMatrix = new double[this.self.numberOfTraces][this.numberOfTracePoints];
        # this.plainText = new String[this.self.numberOfTraces];
        # this.cipherText = new String[this.self.numberOfTraces];

        # for (int count = 0; count < this.self.numberOfTraces; ++count) {
        #     String[] t = this.br.readLine().split(","); 

        #     this.plainText[count] = t[thisplaintextCol]; = CPA.plainTextCol
        #     this.cipherText[count] = t[1];
        #     for (int j = this.extraColFront; j < this.numberOfTracePoints - this.extraColRear; ++j) {
        #         this.traceMatrix[count][j - this.extraColFront] = Double.parseDouble(t[j]);
        #     }
        # }

    def HW(self,n): 
        count = 0
        while (n): 
            count += n & 1
            n >>= 1
        return count 

    # public int HW(int n) {
    #      return Integer.bitCount(n);
    #  }

    def SBOX(self,a):
        s = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
        return s[a]

    # public int SBOX(int a) {
    #      int[] s = new int[]{99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22};
    #      return s[a];
    #  }

    def Correlation(self,xs,ys):
        sx = 0.0
        sy = 0.0
        sxx = 0.0
        syy = 0.0
        sxy = 0.0

        n = len(xs)

        for i in range(0,n):
            x = xs[i]
            y = ys[i]

            sx = sx + x
            sy = sy + y

            sxx = sxx + (x * x)
            syy = syy + (y * y)
            sxy = sxy + (x * y)

        cov = sxy / n - sx * sy / n / n
        sigmax = math.sqrt(sxx / n - sx * sx / n / n)
        sigmay = math.sqrt(syy / n - sy * sy / n / n)

        return cov / sigmax / sigmay



        # public double Correlation(double[] xs, double[] ys) {
        #      double sx = 0.0;
        #      double sy = 0.0;
        #      double sxx = 0.0;
        #      double syy = 0.0;
        #      double sxy = 0.0;
        #      int n = xs.length;
        #      for (int i = 0; i < n; ++i) {
        #          double x = xs[i];
        #          double y = ys[i];
        #          sx += x;
        #          sy += y;
        #          sxx += x * x;
        #          syy += y * y;
        #          sxy += x * y;
        #      }
        #      double cov = sxy / (double)n - sx * sy / (double)n / (double)n;
        #      double sigmax = Math.sqrt(sxx / (double)n - sx * sx / (double)n / (double)n);
        #      double sigmay = Math.sqrt(syy / (double)n - sy * sy / (double)n / (double)n);
        #      return cov / sigmax / sigmay;
        #  }



    def findCorrelation(self):

        x = []
        y = []
        self.correlation = [[None for i in range(self.numberOfTracesPoint)] for j in range(256)]
        temp = 0

        for count in range(0,256):
            y = []
            rowCorrelation = []
            for j in range(0,self.numberOfTraces):
                y.append(self.hypothesis[j][count] / 256.0)
            for i in range(0,self.numberOfTracesPoint):
                x = []
                for j in range(0,self.numberOfTraces):
                    x.append(self.traceMatrix[j][i])
                

                self.correlation[count][i] = self.Correlation(x, y)
                # rowCorrelation.append(self.Correlation(x,y))
            # self.correlation.append(rowCorrelation)

    def findCorrelation32(self,result,traceCount):# = self.numberOfTraces

        x = []
        y = []
        self.correlation = [[None for i in range(self.numberOfTracesPoint)] for j in range(256)]
        temp = 0

        count = result
        y = []
        rowCorrelation = []
        for j in range(0,traceCount):
            y.append(self.hypothesis[j][count] / 256.0)
        for i in range(0,self.numberOfTracesPoint):
            x = []
            for j in range(0,traceCount):
                x.append(self.traceMatrix[j][i])
            

            self.correlation[count][i] = self.Correlation(x, y)
        

    def findKey32(self,result):
        max = self.correlation[result][0]
        loc = 0
        i = result
        for j in range(0,self.numberOfTracesPoint):
            if not (self.correlation[i][j] > max):
                continue
            max = self.correlation[i][j]
            loc = i
        return max



    # public void findCorrelation() {
        #     this.cor = new double[256][this.numberOfTracePoints];
        #     double[] x = new double[this.self.numberOfTraces];
        #     double[] y = new double[this.self.numberOfTraces];
        #     for (int count = 0; count <= 255; ++count) {
        #         for (int j = 0; j < this.self.numberOfTraces; ++j) {
        #             y[j] = (double)this.hypothesis[j][count] / 256.0;
        #         }
        #         for (int i = 0; i < this.numberOfTracePoints; ++i) {
        #             for (int j = 0; j < this.self.numberOfTraces; ++j) {
        #                 x[j] = this.traceMatrix[j][i];
        #             }
        #             this.cor[count][i] = this.Correlation(x, y);
        #         }
        #     }
        # }

    def hex2int(self,hexString):
        hexmap = {}
        hexmap["0"] = 0
        hexmap["1"] = 1
        hexmap["2"] = 2
        hexmap["3"] = 3
        hexmap["4"] = 4
        hexmap["5"] = 5
        hexmap["6"] = 6
        hexmap["7"] = 7
        hexmap["8"] = 8
        hexmap["9"] = 9
        hexmap["A"] = 10
        hexmap["B"] = 11
        hexmap["C"] = 12
        hexmap["D"] = 13
        hexmap["E"] = 14
        hexmap["F"] = 15
        return hexmap[hexString[0] + ""] << 4 ^ hexmap[hexString[1] + ""]

    # public int hex2int(String hex) {
    #      HashMap<String, Integer> hexmap = new HashMap<String, Integer>();
    #      hexmap.put("0", 0);
    #      hexmap.put("1", 1);
    #      hexmap.put("2", 2);
    #      hexmap.put("3", 3);
    #      hexmap.put("4", 4);
    #      hexmap.put("5", 5);
    #      hexmap.put("6", 6);
    #      hexmap.put("7", 7);
    #      hexmap.put("8", 8);
    #      hexmap.put("9", 9);
    #      hexmap.put("A", 10);
    #      hexmap.put("B", 11);
    #      hexmap.put("C", 12);
    #      hexmap.put("D", 13);
    #      hexmap.put("E", 14);
    #      hexmap.put("F", 15);
    #      return (Integer)hexmap.get(hex.charAt(0) + "") << 4 ^ (Integer)hexmap.get(hex.charAt(1) + "");
    #  }

    def initHypothesis_MCU8_AES128(self,byteNumber):

        keyHyp = []
        for i in range(0,256):
            keyHyp.append(i)

        keyHyp[255] = 0

        self.hypothesis = []

        for i in range(0,len(self.plainText)):
            rowHypothesis = []
            P = self.plainText[i][2 * (byteNumber - 1): 2 * byteNumber]
            for j in range(0,len(keyHyp)):
                temp1 = self.hex2int(P) ^ keyHyp[j]
                temp2 = self.SBOX(temp1)
                temp = self.HW(temp2)
                rowHypothesis.append(temp)
            self.hypothesis.append(rowHypothesis)


        # int i;
        # int[] keyHyp = new int[256];
        # for (i = 0; i < 255; ++i) {
        #     keyHyp[i] = i;
        # }
        # this.hypothesis = new int[this.plainText.length][keyHyp.length];
        # for (i = 0; i < this.plainText.length; ++i) {
        #     String P = this.plainText[i].substring(2 * (byteNumber - 1), 2 * byteNumber);
        #     for (int j = 0; j < keyHyp.length; ++j) {
        #         this.hypothesis[i][j] = this.HW(this.SBOX(this.hex2int(P) ^ keyHyp[j]));
        #     }
        # }


    def findKey(self):
        max = self.correlation[0][0]
        loc = 0
        for i in range(0,256):
            for j in range(0,self.numberOfTracesPoint):
                if not (self.correlation[i][j] > max):
                    continue
                max = self.correlation[i][j]
                loc = i
        return loc
    
    def findKey31(self,keySet):
        max = self.correlation[0][0]
        loc = 0
        for i in range(0,256):
            localMaximum = self.correlation[i][0]
            for j in range(0,self.numberOfTracesPoint):
                if (self.correlation[i][j] >= localMaximum):
                    localMaximum = self.correlation[i][j]

                if not (self.correlation[i][j] > max):
                    continue
                max = self.correlation[i][j]
                loc = i
            self.assignment31[str(keySet)].append({str(i): localMaximum})
        return loc


        # public int findKey() {
        #      double max = this.cor[0][0];
        #      int loc = 0;
        #      for (int i = 0; i < 256; ++i) {
        #          for (int j = 0; j < this.numberOfTracePoints; ++j) {
        #              if (!(this.cor[i][j] > max)) continue;
        #              max = this.cor[i][j];
        #              loc = i;
        #          }
        #      }
        #      return loc;
        #  }


    def CPA31(self):

        keysize = CPA.keysize

        self.key = [None] * keysize
        print("Running Analysis...")
        self.initTraceMatrix()
        start = time.process_time()
        # for i in range(1,2):
        for i in range(1,keysize + 1):
            self.initHypothesis_MCU8_AES128(i)
            self.findCorrelation()
            self.key[i - 1] = self.findKey31(i)
            print(self.key)
            print(i)

        end = time.process_time()
        print("Analysis Complete.")
        timetaken = end - start
        strkey = ""
        t = ""
        for i in range(0,keysize):
            t = ('{:x}'.format(self.key[i]).upper() + " ")
            if len(t) < 3:
                strkey = strkey + "0" + t
            else:
                strkey = strkey + t
            print("t = " + t + " \t strkey = " + strkey)
        print(strkey.strip())
        print("Total Time: " + str(timetaken) + " seconds")
        retVal = {"key": self.key, "time": timetaken, "assignment": self.assignment31}
        print(self.assignment31)
        return retVal

    def CPA32(self,results):

        keysize = CPA.keysize

        self.key = [None] * keysize
        print("Running Analysis...")
        self.initTraceMatrix()
        start = time.process_time()
        # for i in range(1,2):
        self.assignment32 = []
        
        for i in range(1,keysize + 1):
            self.initHypothesis_MCU8_AES128(i)
            print("Key " + str(i) + " of 16")
            tempassignment = []
            for traceCount in range(10,101,10):
                
                self.findCorrelation32(results[i - 1],traceCount)
                maxcorrelation = str(self.findKey32(results[i - 1]))
                print("Trace " + str(traceCount) + ", Max Correlation: "+ maxcorrelation)
                tempassignment = tempassignment + [maxcorrelation]
            self.assignment32.append(tempassignment)
        end = time.process_time()
        print("Analysis Complete.")
        # print(self.assignment32)
        timetaken = end - start
        strkey = ""
        t = ""
        print(strkey.strip())
        print("Total Time: " + str(timetaken) + " seconds")
        retVal = {"key": strkey, "time": timetaken, "assignment": self.assignment32}
        return retVal


    def CPA(self):

        keysize = CPA.keysize

        self.key = [None] * keysize
        print("Running Analysis...")
        self.initTraceMatrix()
        start = time.process_time()
        # for i in range(1,2):
        for i in range(1,keysize + 1):
            print(i)
            self.initHypothesis_MCU8_AES128(i)
            self.findCorrelation()
            self.key[i - 1] = self.findKey()
            print(self.key)

        end = time.process_time()
        print("Analysis Complete.")
        timetaken = end - start
        strkey = ""
        t = ""
        for i in range(0,keysize):
            t = ('{:x}'.format(self.key[i]).upper() + " ")
            if len(t) < 3:
                strkey = strkey + "0" + t
            else:
                strkey = strkey + t
            print("t = " + t + " \t strkey = " + strkey)
        print(strkey.strip())
        print("Total Time: " + str(timetaken) + " seconds")
        retVal = {"key": strkey.strip(), "time": timetaken}
        return retVal

    # public HashMap<Object, Object> CPA(int keysize) throws IOException {
    #     this.key = new int[keysize];
    #     LOGGER.info("Running Analysis...");
    #     this.initTraceMatrix();
    #     long start = System.currentTimeMillis();
    #     for (int i = 1; i <= keysize; ++i) {
    #         this.initHypothesis_MCU8_AES128(i);
    #         this.findCorrelation();
    #         this.key[i - 1] = this.findKey();
    #     }
    #     long end = System.currentTimeMillis();
    #     LOGGER.info("Analysis Complete.");
    #     double timetaken = (end - start) / 1000L;
    #     String strkey = "";
    #     String t = "";
    #     for (int i = 0; i < keysize; ++i) {
    #         strkey = strkey + ((t = Integer.toHexString(this.key[i]).toUpperCase() + " ").length() < 3 ? "0" + t : t);
    #         System.out.println("t = " + t + " \t strkey = " + strkey);
    #     }
    #     System.out.println(strkey.trim());
    #     System.out.println("Total Time: " + timetaken + " seconds");
    #     HashMap<Object, Object> retVal = new HashMap<Object, Object>();
    #     retVal.put("key", strkey);
    #     retVal.put("time", timetaken);
    #     return retVal;
    # }

if __name__ == '__main__':
    CPAObject = CPA()
    # results = CPAObject.CPA31()
    # with open('assignment31.json', 'w') as outfile:
    #     json.dump(results, outfile)
    # json.dumps(result) #["assignment"]
    # key = results["key"]
    key = [120, 164, 48, 71, 149, 125, 76, 33, 129, 93, 230, 114, 14, 173, 111, 65]
    results = CPAObject.CPA32(key)

    with open('assignment32.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

        csvwriter.writerow(["Keypart","10","20","30","40","50","60","70","80","90","100"])
        print(results)
        csvwriter.writerow(["1"] + results["assignment"][0])
        csvwriter.writerow(["2"] + results["assignment"][1])
        csvwriter.writerow(["3"] + results["assignment"][2])
        csvwriter.writerow(["4"] + results["assignment"][3])
        csvwriter.writerow(["5"] + results["assignment"][4])
        csvwriter.writerow(["6"] + results["assignment"][5])
        csvwriter.writerow(["7"] + results["assignment"][6])
        csvwriter.writerow(["8"] + results["assignment"][7])
        csvwriter.writerow(["9"] + results["assignment"][8])
        csvwriter.writerow(["10"] + results["assignment"][9])
        csvwriter.writerow(["11"] + results["assignment"][10])
        csvwriter.writerow(["12"] + results["assignment"][11])
        csvwriter.writerow(["13"] + results["assignment"][12])
        csvwriter.writerow(["14"] + results["assignment"][13])
        csvwriter.writerow(["15"] + results["assignment"][14])
        csvwriter.writerow(["16"] + results["assignment"][15])



