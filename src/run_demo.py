"""
Run Demo
--------
Este script permite ejecutar el pipeline desde consola.
"""

from coordinator import run_pipeline
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agente para Text & Web Analytics")
    parser.add_argument("--query", "-q", required=True, type=str, help="Consulta a procesar")
    args = parser.parse_args()

    result = run_pipeline(args.query)

    print("\n===== RESULTADO DEL PIPELINE =====\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("\n==================================\n")
