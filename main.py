import csv
import time
from typing import List, Tuple

import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"


def send_prompt(prompt: str) -> str:
    """
    Отправляет один запрос на сервер Ollama
    и возвращает сгенерированный ответ модели.

    Args:
        prompt (str): Входной запрос для LLM.

    Returns:
        str: Ответ, сгенерированный моделью.

    Raises:
        requests.RequestException:
            Возникает при ошибке HTTP-запроса.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    result = response.json()
    return result.get("response", "").strip()


def run_inference(prompts: List[str]) -> List[Tuple[str, str]]:
    """
    Запускает инференс для списка запросов.

    Args:
        prompts (List[str]): Список входных запросов.

    Returns:
        List[Tuple[str, str]]:
            Список пар (запрос, ответ).
    """
    results = []

    for i, prompt in enumerate(prompts, start=1):
        print(f"[{i}/{len(prompts)}] Отправка запроса: {prompt}")

        start_time = time.time()

        try:
            answer = send_prompt(prompt)
        except requests.RequestException as e:
            answer = f"ОШИБКА: {str(e)}"

        elapsed = time.time() - start_time
        print(f"Выполнено за {elapsed:.2f} сек.\n")

        results.append((prompt, answer))

    return results


def save_report(results: List[Tuple[str, str]], filename: str = "report.csv") -> None:
    """
    Сохраняет результаты инференса в CSV-файл.

    Args:
        results (List[Tuple[str, str]]):
            Список пар запрос-ответ.
        filename (str):
            Имя выходного CSV-файла.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["запрос", "ответ"])

        for prompt, response in results:
            writer.writerow([prompt, response])

    print(f"Отчет сохранен в файл {filename}")


def main() -> None:
    """
    Основная функция запуска программы.
    Содержит 10 заранее подготовленных запросов.
    """
    prompts = [
        "Что такое язык программирования Python?",
        "Объясни простыми словами, что такое REST API.",
        "Напиши программу Hello World на Go.",
        "Что такое Docker?",
        "Объясни, что такое Kubernetes.",
        "Кто такой Альберт Эйнштейн?",
        "Что такое машинное обучение?",
        "Напиши пример SQL JOIN.",
        "Что такое рекурсия в программировании?",
        "Объясни разницу между TCP и UDP."
    ]

    results = run_inference(prompts)
    save_report(results)


if __name__ == "__main__":
    main()
