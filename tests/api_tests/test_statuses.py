import pytest
from api.statuses import Statuses
import data.test_lists as test_data

class TestStatuses:
    """Проверки получения статусов"""
    def test_get_statuses(self,access_token):
        """Проверка  получения статусов"""
        statuses = Statuses(access_token).get_statuses()
        assert statuses[0].status_code == 200
        assert statuses[1]== test_data.status_list
        print(statuses[1])
    def test_get_statuses_recruit_requirement(self,access_token):
        """Проверка получения статусов кандидатов"""
        response = Statuses(access_token).get_statuses_recruit_requirement()
        assert response[0].status_code == 200
        assert response[1] == test_data.status_recruit_list
        print(response[1])

    def test_get_statuses_recruit_requirement_for_candidates(self,access_token):
        """Проверка получение статусов для кандидатов от заказчика"""
        response = Statuses(access_token).get_status_recruit_requirement_for_candidates()
        assert response[0].status_code == 200
        assert response[1] == test_data.status_recruit_requriments_for_candidates
        print(response[1])