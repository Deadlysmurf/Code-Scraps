### For t-test hypothesis testing when only summary statistics are provided

## DEPENDANCIES:
## import numpy as np
## import scipy.stats as ss

def t_test(sample_mean, mu, sd, n, alpha, tails):

    if tails == 1:
        t_critical = (sample_mean-mu)/(sd/(np.sqrt(n)))
        pval = ss.t.sf(np.abs(t_critical), n-1)
        print("T-critical value: %f" % t_critical)
        print("P-value: %f" % pval)
        if pval > alpha:
            print("As %f is greater than %f, there is insufficent evidence to reject the null hypothesis." % (pval, alpha))
        else:
            print("As %f is less than %f, there is sufficent evidence to reject the null hypothesis, and accept the alternative." % (pval, alpha))

    elif tails == 2:
        t_critical = (sample_mean-mu)/(sd/(np.sqrt(n)))
        pval = ss.t.sf(np.abs(t_critical), n-1)*2
        print("T-critical value: %f" % t_critical)
        print("P-value: %f" % pval)
        if pval > alpha:
            print("As %f is greater than %f, there is insufficent evidence to reject the null hypothesis." % (pval, alpha))
        else:
            print("As %f is less than %f, there is sufficent evidence to reject the null hypothesis, and accept the alternative." % (pval, alpha))

### March 17, 2018 ###
## MEAK ##
