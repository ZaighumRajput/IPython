

import numpy as np
from math import *


def CND(X):
    (a1,a2,a3,a4,a5) = (0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429)
    L = abs(X)
    K = 1.0 / (1.0 + 0.2316419 * L)
    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +
    a4*pow(K,4) + a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w
def BlackScholes(CallPutFlag,S,X,T,r,v):
    d1 = (log(S/X)+(r+v*v/2.)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*CND(d1)-X*exp(-r*T)*CND(d2)

    else:
        return X*exp(-r*T)*CND(-d2)-S*CND(-d1)


def MJDCall(jumpIntensity, jumpMean, jumpVol, sigma, r, q, T, S, K):
    lambdaPrime = jumpIntensity*(1+jumpMean)
    call = 0;
    for k in range(50):
        sigma_n = sqrt(sigma**2 + (k/T)*jumpVol**2)
        r_n = r - jumpIntensity*jumpMean + k*log(1 + jumpMean)/T
        call =+  ( exp(-lambdaPrime*T) * (lambdaPrime*T)**K * BlackScholes(S, K, T, r_n, q, sigma_n) * (1/factorial(k)))
    return call


#if __name__=='__main__':
	


class TestCasesforMJDCall:
	
	t1 = 1.0
	t10 = 10.0
	r1 = 0.03
	r10 = 0.05
        
	y1 = 0.03
	y10 = 0.05
        
	vol1 = 0.03
	vol10 = 0.03
        
	spotPriceA = 100
	moneynessA = 1
	maturityA = 1
                    
	spotPriceB = 100
	moneynessB = 0.8
	maturityB = 10
	
	def functionTests(self, parameters):
		jumpIntensity = parameters[0]
		jumpMean = parameters[1]
		jumpVol = parameters[2]
		vol = parameters[3]
		
		callPutFlag = 1
		
		assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
					self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
					BlackScholes(callPutFlag,self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,vol)
	
		assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
					self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
					BlackScholes(callPutFlag,self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,vol)
	
		assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
					self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
					BlackScholes(callPutFlag,self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,vol)
		
		
	
	
	def test_NoJumpProcess(self):
		a = TestCasesforMJDCall()
		a.functionTests(np.array([0,0,0,0.25]))
			
	#def test_NoJumpProcess(self):
	#	parameters = np.array([0,0,0,0.25])
	#	assert MJDCall(0,0,0,0.25,0.03,0,1,1,1) == 0
	#	assert parameters[self.t1] == 0
	#	jumpIntensity = parameters[0]
	#	jumpMean = parameters[1]
	#	jumpVol = parameters[2]
	#	vol = parameters[3]
		#assert MJDCall(0,0,0,0.25, self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == 5
		
    	#assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol,
        #           r1,y1,t1,spotPriceA, SpotPriceA/moneynessA) == \
        #   BlackScholes(1,spotPriceA,spotPriceA/moneynessA,t1,r1,vol)
    	#assert MJDCall(parameters[0], parameters[1], parameters[2], parameters[3],
    	#			r2,y1, t1, spotPriceB, spotPriceB/moneynessB) == \
    	#			BlackScholes(1,spotPriceA,spotPriceA/moneynessA,t1,r1,parameters[3])
    #               Intensity	mean	jumpVol	VOL		Matlab				
#.AEX-Index Curve	0.20198608	-0.254267161	0.046407838	0.096676606			0.2047	-0.2523	0.0495	0.0964
#.IBEX-Index Curve	0.441440266	-0.204915812	0.091882019	0.126625648			0.4377	-0.2062	0.09	0.1265
#.TOPX-Index Curve	0.187498301	-0.057665506	0.3019463	0.147861008			0.2041	-0.0545	0.29	0.1466
#.FTSE-Index Curve	0.200665135	-0.240872983	0.075736307	0.084150369			0.2046	-0.2384	0.0777	0.0838