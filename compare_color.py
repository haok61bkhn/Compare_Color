from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color 
from colormath.color_diff import delta_e_cie2000,delta_e_cie1976,delta_e_cie1994
import time

from math import sqrt
class Compare_color:
    def __init__(self):
        pass

    def rgb_to_cielab(self,a):
        """
        a is a pixel with RGB coloring
        """
        a1,a2,a3 = a[0]/255,a[1]/255,a[2]/255

        color1_rgb = sRGBColor(a1, a2, a3)

        color1_lab = convert_color(color1_rgb, LabColor)
        # print()
        return color1_lab

    def distance2percent(self,dis,first=0,last=100):
        if(dis<first):return 1
        if(dis>last) : return 0
        return int(100*(last-dis)/(last-first))
    
    def compare(self,rgb1,rbg2,percent):
        return self.distance2percent(delta_e_cie1994(self.rgb_to_cielab(rgb1),self.rgb_to_cielab(rgb1)))>percent

if __name__=="__main__":
    x=Compare_color()
    rgb1=(163,60,60)
    rgb2=(247,23,23)
    t1=time.time()
    # print(x.distance2percent(delta_e_cie1994(x.rgb_to_cielab(rgb1),x.rgb_to_cielab(rgb2))))
    # print("time ",time.time()-t1)
    print(x.compare(rgb1,rgb2,70))