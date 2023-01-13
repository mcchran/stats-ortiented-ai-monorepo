import scipy.stats as stats

def likelihood_binomial(n,p,k):
    return stats.binom.pmf(k,n,p)