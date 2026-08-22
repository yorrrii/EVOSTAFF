import requests
import data.candidate_data as data

class Candidate:
    def __init__(self, access_token):
        self.stand = access_token.stand
        self.token = access_token.token
        self.headers = access_token.headers

    def get_candidates(self,get_current_user_id):
        """Получение списка кандидатов"""
        body = data.get_users
        candidates = requests.post(f'{self.stand}/api/v1/candidate/no-cache/by-user/{get_current_user_id}/?page=0&size=30', headers=self.headers, json = body)
        candidates_list = []
        count = 0
        for i in range(len(candidates.json()["content"])):
            candidates_list.append(candidates.json()["content"][i]["person"]["lastname"])
            count += 1
        return candidates, candidates_list, count

    def create_candidate(self):
        """Создание карточки кандидата"""
        body = data.create_valid_candidate
        response = requests.post(f'{self.stand}/api/v1/candidate',headers=self.headers,json=body)
        return response

    def edit_candidate(self, get_candidate):
        body = get_candidate
        response = requests.post(f"{self.stand}/api/v1/candidate/no-cache/edite",headers=self.headers, json=body)