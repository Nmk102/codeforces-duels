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

def check_problem_solved(handle, contest_id, problem_index):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        if data.get("status") != "OK":
            print(f"Ошибка API Codeforces: {data.get('comment')}")
            return False
        
        submissions = data.get("result", [])
        
        for sub in submissions:
            problem = sub.get("problem", {})
            if (problem.get("contestId") == int(contest_id) and problem.get("index").upper() == str(problem_index).upper()):
                if sub.get("verdict") == "OK":
                    return True
                    
        return False

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сети: {e}")
        return False

handle = input()
ci = int(input())
pi = input()

print(check_problem_solved(handle, ci, pi))