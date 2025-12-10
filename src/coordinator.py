"""
Coordinator Agent
-----------------
Orquesta el pipeline completo:
- Planificación simulada (como si fuera un LLM Planner)
- Scraper Agent
- NLP Agent (NER)
- Fact Checker Agent
"""

import json
from workers.scraper import simple_scrape
from workers.ner import simple_ner
from workers.fact_checker import simple_fact_check


def plan_query_to_tasks(query: str):
    """
    Planificador simulando un LLM.
    Retorna un plan estructurado de subtareas.
    """
    return {
        "query": query,
        "plan": [
            {
                "task_id": 1,
                "type": "scrape",
                "targets": [
                    "https://example.com",
                    "https://example.org"
                ]
            },
            {
                "task_id": 2,
                "type": "ner",
                "target": "scraped_texts"
            },
            {
                "task_id": 3,
                "type": "fact_check",
                "target": "query"
            }
        ]
    }


def run_pipeline(query: str):
    """
    Ejecuta el pipeline completo basado en el plan.
    """

    # 1. Obtener plan de “LLM”
    plan = plan_query_to_tasks(query)

    # 2. Scraping
    scrape_targets = plan["plan"][0]["targets"]
    scraped = []

    for url in scrape_targets:
        scraped.append(simple_scrape(url))

    # Extraer solo texto
    texts = [s.get("text", "") for s in scraped]

    # 3. NER Agent
    ner_results = [simple_ner(t) for t in texts]

    # 4. Fact Checking
    fact_result = simple_fact_check(query, texts)

    # 5. Resultado final combinado
    result = {
        "plan": plan,
        "scraped_results": scraped,
        "ner_output": ner_results,
        "fact_check": fact_result
    }

    return result


if __name__ == "__main__":
    q = "La inflación fue 2% en 2025"
    output = run_pipeline(q)
    print(json.dumps(output, indent=2, ensure_ascii=False))
