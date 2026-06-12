def calculate_score(
    amount,
    is_foreign,
    high_risk_country,
    failed_attempts,
    new_device
):
    score = 0

    if amount > 50000:
        score += 25

    if is_foreign:
        score += 25

    if high_risk_country:
        score += 20

    if failed_attempts >= 3:
        score += 20

    if new_device:
        score += 10

    return min(score, 100)