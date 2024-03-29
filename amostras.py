import numpy as np
from scipy.stats import f
import statsmodels.stats.power as smp
from statsmodels.stats.power import TTestIndPower, tt_ind_solve_power


def teste_t(effect_size= 0.8,alpha=None,power=None):
# parameters for the analysis 
    #effect_size = 0.8
    #alpha = 0.05 # significance level
    #power = 0.8

    alpha = float(alpha)
    power = float(power)
    
    
    sample_size = tt_ind_solve_power(effect_size = effect_size, alpha=alpha, power=power, ratio=1, alternative='two-sided')

    #power_analysis = TTestIndPower()
    #sample_size = power_analysis.solve_power(effect_size = effect_size, 
                                            #power = power, 
                                            #alpha = alpha)
    
    return round(sample_size)
    

def anova_sample_size(effect_size, alpha, power, num_groups):
    
    analysis = smp.FTestAnovaPower()
    sample_size = analysis.solve_power(
        effect_size=effect_size, alpha=alpha, power=power, k_groups=num_groups)
    return round(sample_size)


# def anova_sample_size(k, alpha, poder,f1=0.8):


#     poder = float(poder)
#     alpha = float(alpha)
#     beta = 1-poder

#     power = 0
#     for i in range(100):
#         ni = (i+1)+1
#         N = ni*k
#         lambd = N*f1**2

      

#         q = f.ppf(1-alpha,k - 1, (ni - 1) * k, loc=0, scale=1)
#         power_new = f.cdf(q,  k - 1, (ni - 1) * k, loc=lambd, scale=1)
#         power_new = 1 - power_new
#         power = np.r_[power,power_new]

#         if power[i]>= 1-beta:
#             break

#     return len(power+1)*k







