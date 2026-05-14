def z_score(x, mu, sigma):
    # Group Members: Matt Hammer, Mei Tate, Cohen Flanagan

    if sigma == 0:
        raise ValueError("Standard deviation cannot be zero.")

    result = (x - mu) / sigma

    return result