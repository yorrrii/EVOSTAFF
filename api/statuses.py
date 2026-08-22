import requests
import pytest

class Statuses:
    def __init__(self, access_token):
        self.stand = access_token.stand
        self.token = access_token.token
        self.headers = access_token.headers

    def get_statuses(self):
        """Получение списка статусов отпуска"""
        response = requests.get(f"{self.stand}/api/v1/user/vacation/statuses", headers=self.headers)
        assert response.status_code == 200
        statuses_list = []
        for i in range(len(response.json())):
            statuses_list.append(response.json()[i]["value"])
        return response,statuses_list

    def get_statuses_recruit_requirement(self):
        response = requests.get(f"{self.stand}/api/v1/statuses_recruit_requirement", headers=self.headers)
        statuses_recruit_requirement_list = []
        for i in range(len(response.json())):
            statuses_recruit_requirement_list.append(response.json()[i]["label"])
        return response,statuses_recruit_requirement_list

    def get_status_recruit_requirement_for_candidates(self):
        """Получение статусов кандидата"""
        response = requests.get(f"{self.stand}/api/v1/recruitment/status-recruit-requirement-for-candidates", headers=self.headers)
        recruit_requirement_for_candidates_list = []
        for i in range(len(response.json())):
            recruit_requirement_for_candidates_list.append(response.json()[i]["label"])
        return response,recruit_requirement_for_candidates_list

    def get_status_config(self):
        response = requests.get(f"{self.stand}/api/v1/status-config", headers=self.headers)
        return response
