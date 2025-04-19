def inheritance(k, m, n):
    t = k+m+n
    
    prob_AA_AA = k/t * (k-1)/(t-1) 
    prob_AA_Aa = k/t * ((m)/(t-1)) * 2 
    prob_AA_aa = k/t * ((n)/(t-1)) * 2
    prob_Aa_Aa = m/t * ((m-1)/(t-1)) * 0.75
    prob_Aa_aa = m/t * ((n)/(t-1)) * 2 * 0.5
    #prob_aa_aa = n/t * (n-1)/(t-1) * 0.0
    
    return (prob_AA_AA+prob_AA_Aa+prob_AA_aa+prob_Aa_Aa+prob_Aa_aa)

print(inheritance(21,29,23))