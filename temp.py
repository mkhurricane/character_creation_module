def remove_rep(current_rep: float), 
               (rep_points: int), 
               (debuf_effect: bool) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return float(current_rep)