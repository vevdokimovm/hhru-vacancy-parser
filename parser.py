import requests


def get_vacancies_from_api():
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "python",  # Поисковый запрос
        "area": 1,  # ID региона (1 - Москва)
        "per_page": 10  # Количество вакансий на странице
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        vacancies = []
        for item in data.get("items", []):
            vacancies.append({
                "Вакансия": item.get("name"),
                "Компания": item.get("employer", {}).get("name"),
                "Зарплата": (
                    f"{item['salary']['from']} - {item['salary']['to']} {item['salary']['currency']}"
                    if item.get("salary") else "Не указана"
                ),
                "Ссылка": item.get("alternate_url"),
            })
        return vacancies
    else:
        print(f"Ошибка: {response.status_code}")
        return []


if __name__ == "__main__":
    vacancies = get_vacancies_from_api()
    for vacancy in vacancies:
        print(vacancy, '\n')



