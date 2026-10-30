# Original practice examples: lists, functions and dictionaries
transactions = [120, -45, 90, -15, 210]
def summarize(values):
    return {"count": len(values), "net": sum(values), "positive": sum(x for x in values if x > 0)}
print(summarize(transactions))
