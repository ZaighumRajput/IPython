import numpy as np
from math import *


def CND(X):
    '''Cumulative Distribution Function
    '''
    (a1,a2,a3,a4,a5) = (0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429)
    L = abs(X)
    K = 1.0 / (1.0 + 0.2316419 * L)
    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +
    a4*pow(K,4) + a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w
def BlackScholes(S,X,T,r,q,v):
    '''Simple BlackScholes; only calls
    '''
    d1 = (log(S/X)+(r-q+v*v/2.0)*T)/(v*np.sqrt(T))
    d2 = d1-v*np.sqrt(T)
    return (S*np.exp(-q*T)*CND(d1)-X*np.exp(-r*T)*CND(d2))
    
def MJDCall(jumpIntensity, jumpMean, jumpVol, sigma, r, q, T, S, K):
    '''Call option price under Merton Jump Diffusion
    '''
    lambdaPrime = jumpIntensity*(1+jumpMean)
    call = 0;
    #print lambdaPrime
    for i in range(0,50):
        sigma_n = np.sqrt(sigma**2 + (i/T)*jumpVol**2);
        
        r_n = r - jumpIntensity*jumpMean + i*np.log(1 + jumpMean)/T;
        #if(Debug):
          #  print "k is % sigma_n is % and r_n is %", i,sigma_n, r_n
          #  print "exp %", exp(-lambdaPrime*T)
          #  print "lam to i %",(lambdaPrime*T)**i
          #  print "fac %",(factorial(i))
          #  print BlackScholes(S,K,T,r_n,q,sigma_n)
        
        call += (((lambdaPrime*T)**i)/(factorial(i)))*np.exp(-lambdaPrime*T)*BlackScholes(S,K,T,r_n,q,sigma_n)
        #print call
    return call

class TestCasesforMJDCall:
    
    t1 = 1.0
    t10 = 10.0
    r1 = 0.03
    r10 = 0.05
        
    q1 = 0.03
    q10 = 0.05
        
    vol1 = 0.03
    vol10 = 0.03
        
    spotPriceA = 100
    moneynessA = 1
    maturityA = 1
                    
    spotPriceB = 100
    moneynessB = 0.8
    maturityB = 10
    
    def functionTests(self, parameters):
        jumpIntensity = parameters[0];
        jumpMean = parameters[1];
        jumpVol = parameters[2];
        vol = parameters[3];
        
        print MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
                        self.r1, self.q1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA)
        
        print BlackScholes(self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,self.q1,vol)
        

       # assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
        #    self.r1, self.q1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
        #    BlackScholes(self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,self.q1,vol)
	
		#assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
		#			self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
		#			BlackScholes(callPutFlag,self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,vol)
	
		#assert MJDCall(jumpIntensity, jumpMean, jumpVol, vol, \
		#			self.r1, self.y1, self.t1, self.spotPriceA, self.spotPriceA/self.moneynessA) == \
		#			BlackScholes(callPutFlag,self.spotPriceA,self.spotPriceA/self.moneynessA,self.t1,self.r1,vol)

        
    #def test_NoJumpProcess(self):
    #    a = TestCasesforMJDCall()
    #    a.functionTests(np.array([0,0,0,0.25]))

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

a = TestCasesforMJDCall()
a.functionTests(np.array([0,0,0,0.25]))