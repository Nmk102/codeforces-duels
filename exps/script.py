import requests

def get_last_submissions(handle: str, count: int = 5):
    url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count={count}"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") == "OK":
        print(f"Последние {count} посылок пользователя {handle}:\n")
        for sub in data["result"]:
            sub_id = sub["id"]
            problem = sub["problem"]
            prob_code = f"{problem.get('contestId', '')}{problem.get('index', '')}"
            prob_name = problem.get("name", "Unknown")
            verdict = sub.get("verdict", "TESTING")
            lang = sub.get("programmingLanguage")
            
            print(f"• ID посылки: {sub_id}")
            print(f"  Задача: {prob_code} — {prob_name}")
            print(f"  Вердикт: {verdict}")
            print(f"  Язык: {lang}\n")
    else:
        print(f"Ошибка: {data.get('comment', 'Не удалось получить данные')}")

handle = input()

get_last_submissions(handle, 5)