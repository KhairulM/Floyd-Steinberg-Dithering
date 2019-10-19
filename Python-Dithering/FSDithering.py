import numpy as np
import cv2



def main():
        imgName = input("Image Name : ")
        img = cv2.imread(imgName, cv2.IMREAD_COLOR)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        factor = 3

        height, width = imgGray.shape[:2]
        for y in range(0, height-1):
                for x in range(1, width-1):
                        oldPixel = imgGray[y][x]
                        newPixel = round(round(factor*oldPixel/255) * (255/factor))
                        imgGray[y][x] = newPixel
                        quantErr = oldPixel - newPixel
                
                        imgGray[y][x+1] += (quantErr*7/16.0)
                
                        imgGray[y+1][x-1] += (quantErr*3/16.0)
                
                        imgGray[y+1][x] += (quantErr*5/16.0)
                
                        imgGray[y+1][x+1] += (quantErr/16.0)

                        """
                        pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error * 7 / 16 kanan
                        pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error * 3 / 16 kiri bawah
                        pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error * 5 / 16 bawah
                        pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error * 1 / 16 kanan bawah
                        """
                        

        rez = cv2.resize(imgGray, ((width*300) // height, 300), cv2.INTER_AREA)
        cv2.imshow("Result", rez) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

           

main()