def dominant_allele_probability(k, m, n):
    # Total number of organisms
    total = k + m + n
    
    # Calculate the probability of picking each pair type
    prob_AA_AA = (k / total) * ((k - 1) / (total - 1))
    prob_AA_Aa = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    prob_AA_aa = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1))
    prob_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1))
    
    # Calculate probability of offspring with dominant allele from each pairing
    dominant_prob = (
        prob_AA_AA * 1.0 +   # AA x AA produces all dominant
        prob_AA_Aa * 1.0 +   # AA x Aa produces all dominant
        prob_AA_aa * 1.0 +   # AA x aa produces all dominant
        prob_Aa_Aa * 0.75 +  # Aa x Aa produces 75% dominant
        prob_Aa_aa * 0.5     # Aa x aa produces 50% dominant
        # No need to add prob_aa_aa, as it produces 0% dominant
    )
    
    return dominant_prob

prob = dominant_allele_probability(19 , 27 ,22)
print(prob)  # Should output approximately 0.78333