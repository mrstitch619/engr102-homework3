def z_score(x, mu, sigma):
    if sigma == 0:
        raise
    return (x - mu) / sigma