### Z-test of proportions for hypothesis testing when only summary statistics are provided

## DEPENDANCIES:
## import numpy as np
## import scipy.stats as ss



def Test_of_Proportion(p_hat, p_null, n, alt, alpha):
    z = (p_hat - p_null)/(np.sqrt(p_null*(1-p_null)/n))
    print("Z-score: %f" % z)
    if alt == '=/=':
        pval = 2*(ss.norm.cdf(z))
    elif alt == '>':
        pval = ss.norm.cdf(z)
    elif alt == '<':
        pval = 1-ss.norm.cdf(z)
    print("P-value: %f" % pval)
    if pval > alpha:
        print("As %f is greater than %f, there is insufficent evidence to reject the null hypothesis." % (pval, alpha))
    else:
        print("As %f is less than %f, there is sufficent evidence to reject the null hypothesis, and accept the alternative." % (pval, alpha))


### March 17, 2018 ###
## MEAK ##
