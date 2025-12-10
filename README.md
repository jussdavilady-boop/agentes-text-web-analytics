cat > README.md <<'EOF'
# Arquitectura Agéntica para Text & Web Analytics  
Análisis de Mercado, Scraping, NER y Fact-Checking con un Orquestador Inteligente

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Activo-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## Descripción General

Este proyecto implementa una Arquitectura Agéntica para resolver problemas reales de  
Text & Web Analytics, integrando:

- Scraping web automático  
- Procesamiento de lenguaje natural (NER)  
- Fact-checking básico  
- Coordinación mediante un Agente Orquestador  
- Integración de herramientas determinísticas (Python + Requests + BeautifulSoup)  
- Planificador simulado estilo LLM Planner

El sistema está diseñado para aplicaciones como:

- Inteligencia de mercados  
- Automatización de resúmenes  
- Análisis de sentimiento  
- Monitoreo de tendencias  
- Verificación de afirmaciones  
- Análisis de texto desde fuentes web  

---

## Arquitectura General

El sistema sigue el patrón:

Orchestrator → Tool Agents (Scraper / NLP / Fact-Checker)

Flujo general:

1. El usuario envía una consulta.  
2. El Agente Orquestador genera un plan compuesto por subtareas.  
3. El Orquestador coordina la ejecución:  
   - Scraper Agent  
   - NER Agent  
   - Fact-Checker Agent  
4. El sistema retorna un resultado estructurado.

---

## Diagrama de Arquitectura (Mermaid)

```mermaid
graph TD
    A[Usuario] --> B[Agente Orquestador]
    B --> C[Planificación<br>(LLM simulado)]
    B --> D[Scraper Agent]
    B --> E[NER Agent]
    B --> F[Fact Checker Agent]

    D --> B
    E --> B
    F --> B

    B --> G[Respuesta JSON estructurada]
