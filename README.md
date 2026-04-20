# Parser-hhru-vacancies

A Python script that fetches Python-related job vacancies from the [hh.ru API](https://api.hh.ru/) and prints them to stdout.

## Features

- Fetches vacancies by keyword and region via the public hh.ru API
- Displays job title, company, salary range, and direct URL
- No authentication required — uses the public hh.ru API

## Tech Stack

- Python 3.10+
- [requests](https://docs.python-requests.org/) — HTTP client

## Getting Started

### Installation

```bash
git clone https://github.com/vevdokimovm/Parser-hhru-vacancies.git
cd Parser-hhru-vacancies
pip install -r requirements.txt
```

### Run

```bash
python parser.py
```

### Configuration

Edit the parameters inside `parser.py` to change the search:

```python
params = {
    "text": "python",   # search keyword
    "area": 1,          # region ID (1 = Moscow)
    "per_page": 10      # results per page
}
```

Region IDs can be found in the [hh.ru areas reference](https://api.hh.ru/areas).

## Example Output

```
{'Вакансия': 'Python Developer', 'Компания': 'Some Company', 'Зарплата': '150000 - 250000 RUR', 'Ссылка': 'https://hh.ru/vacancy/...'}
```

## License

MIT
