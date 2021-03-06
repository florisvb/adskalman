# Make a point move in the 2D plane
# State = (x y xdot ydot). We only observe (x y).

# This code was ported from "tracking_demo.m"
import numpy
import adskalman

ss = 4 # state size
os = 2 # observation size
F = numpy.array([[1,0,1,0], # process update
                 [0,1,0,1],
                 [0,0,1,0],
                 [0,0,0,1]],
                dtype=numpy.float)
H = numpy.array([[1,0,0,0], # observation matrix
                 [0,1,0,0]],
                dtype=numpy.float)
Q = 0.1*numpy.eye(ss) # process noise
R = 1.0*numpy.eye(os) # observation noise
initx = numpy.array([10,10,1,0],dtype=numpy.float)
initV = 10*numpy.eye(ss)

T = 15

# This is the data that is generated by Murphy's demo.
#seed = 9
#numpy.random.seed(seed)
#x,y = adskalman.sample_lds(F,H,Q,R,initx,T)

x = numpy.array([[ 10.        ,  10.78562922,  12.14884733,  13.37768744, 14.70391646,  15.0972105 ,  15.27100392,  16.02603256, 16.77868535,  17.35367989,  17.60693265,  17.90492854, 18.8527745 ,  19.0826357 ,  19.50682031],
                 [ 10.        ,  10.2018565 ,  10.37289444,  10.24726726, 9.41747009,   9.23049962,   8.25498444,   7.93055042, 7.74377694,   6.57500322,   6.09083901,   6.04183098, 6.25299483,   5.86752675,   5.63880611],
                 [  1.        ,   1.32750793,   0.89718228,   1.04323621, 0.6012368 ,   0.38607908,   0.10314957,   0.58612548, 0.64803301,   0.31990456,   0.51884579,   1.12411301, 0.9584339 ,   0.89764825,   0.99435954],
                 [  0.        ,  -0.13645972,  -0.41671164,  -0.91084177, -0.29670515,  -0.80974329,  -0.75982391,  -0.28591924,  -0.76442545,  -0.16191313,   0.32366389,   0.19091798, -0.11169736,  -0.20569391,   0.08488225]]).T
y = numpy.array([[ 11.49746646,   8.34917862,  12.2345992 ,  13.01971219, 12.93696592,  14.91080222,  17.03870584,  14.63065253, 18.12204124,  16.81571886,  18.08187941,  17.91986286, 20.4956051 ,  18.90627217,  19.40367059],
                 [ 10.37519837,  11.74461097,  10.10072462,   9.07503471, 9.47889654,   9.65741996,   9.11313015,   7.58503774, 6.4678298 ,   5.02218694,   5.79485744,   4.45538921, 6.42789419,   6.45878971,   2.74446057]]).T

xsmooth,Vsmooth = adskalman.kalman_smoother(y,F,H,Q,R,initx,initV)

print 'xsmooth',xsmooth
print 'Vsmooth',Vsmooth
