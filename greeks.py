from scipy.stats import norm
import numpy as np
from bs_call_putt import BS_CALL, BS_PUT

class greeks(): 
    def d1(S, K, T, r, sigma):
        return (np.log(S/K) + (r + sigma**2/2)*T) / sigma*np.sqrt(T)

    def d2(S, K, T, r, sigma):
        return d1(S, K, T, r, sigma) - sigma* np.sqrt(T)

    def delta_call(S, K, T, r, sigma):
        N = norm.cdf
        return N(d1(S, K, T, r, sigma))
    
    def delta_fdm_call(S, K, T, r, sigma, ds = 1e-5, method='central'):
        method = method.lower() 
        if method =='central':
            return (BS_CALL(S+ds, K, T, r, sigma) -BS_CALL(S-ds, K, T, r, sigma))/\
                            (2*ds)
        elif method == 'forward':
            return (BS_CALL(S+ds, K, T, r, sigma) - BS_CALL(S, K, T, r, sigma))/ds
        elif method == 'backward':
            return (BS_CALL(S, K, T, r, sigma) - BS_CALL(S-ds, K, T, r, sigma))/ds
    
    
    def delta_put(S, K, T, r, sigma):
        return - N(-d1(S, K, T, r, sigma))

    def delta_fdm_put(S, K, T, r, sigma, ds = 1e-5, method='central'):
        method = method.lower() 
        if method =='central':
            return (BS_PUT(S+ds, K, T, r, sigma) -BS_PUT(S-ds, K, T, r, sigma))/(2*ds)
        elif method == 'forward':
            return (BS_PUT(S+ds, K, T, r, sigma) - BS_PUT(S, K, T, r, sigma))/ds
        elif method == 'backward':
            return (BS_PUT(S, K, T, r, sigma) - BS_PUT(S-ds, K, T, r, sigma))/ds    


    def gamma(S, K, T, r, sigma):
        N_prime = norm.pdf
        return N_prime(d1(S,K, T, r, sigma))/(S*sigma*np.sqrt(T))

    def vega(S, K, T, r, sigma):
        N_prime = norm.pdf
        return S*np.sqrt(T)*N_prime(d1(S,K,T,r,sigma)) 

    def vega_fdm(S, K, T, r, sigma, dv=1e-4, method='central'):
        method = method.lower() 
        if method =='central':
            return (BS_CALL(S, K, T, r, sigma+dv) -BS_CALL(S, K, T, r, sigma-dv))/\
                            (2*dv)
        elif method == 'forward':
            return (BS_CALL(S, K, T, r, sigma+dv) - BS_CALL(S, K, T, r, sigma))/dv
        elif method == 'backward':
            return (BS_CALL(S, K, T, r, sigma) - BS_CALL(S, K, T, r, sigma-dv))/dv


    def gamma_fdm(S, K, T, r, sigma , ds = 1e-5, method='central'):
        method = method.lower() 
        if method =='central':
            return (BS_CALL(S+ds , K, T, r, sigma) -2*BS_CALL(S, K, T, r, sigma) +  BS_CALL(S-ds , K, T, r, sigma) )/(ds)**2
        elif method == 'forward':
            return (BS_CALL(S+2*ds, K, T, r, sigma) - 2*BS_CALL(S+ds, K, T, r, sigma)+ BS_CALL(S, K, T, r, sigma) )/(ds**2)
        elif method == 'backward':
            return (BS_CALL(S, K, T, r, sigma) - 2* BS_CALL(S-ds, K, T, r, sigma) + BS_CALL(S-2*ds, K, T, r, sigma)) /(ds**2) 