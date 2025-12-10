"""
Fact Checker Agent
------------------
Verifica si la afirmación del usuario aparece en algún texto obtenido por scraping.
"""

def simple_fact_check(claim: str, contexts: list):
    """
    Fact-checking básico:
    - Verifica si el claim aparece en los textos del scraper
    - Retorna veredicto, confianza y evidencia
    """

    evidence = []
    for ctx in contexts:
        if claim.lower() in ctx.lower():
            evidence.append(ctx[:400])

    if evidence:
        verdict = "Supported"
        confidence = min(0.9, 0.5 + 0.15 * len(evidence))
    else:
        verdict = "Not supported"
        confidence = 0.05

    return {
        "claim": claim,
        "verdict": verdict,
        "confidence": round(confidence, 2),
        "evidence": evidence
    }
