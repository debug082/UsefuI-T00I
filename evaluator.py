def evaluate(text):

    score = 0

    if "FLAG_LOW" in text:
        score = max(score,3)

    if "FLAG_MEDIUM" in text:
        score = max(score,4)

    if "FLAG_HIGH" in text:
        score = max(score,5)

    return score