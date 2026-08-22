from api.candidate import Candidate


class TestCandidate:

    def test_get_candidates(self, access_token, get_current_user_id):
        """Проверка получения списка карточек кандидатов"""
        response = Candidate(access_token).get_candidates(get_current_user_id)
        assert response[0].status_code == 200
        print(f'общее количество {response[2]} {response[1]}')

    def test_create_new_candidate(self, access_token):
        """Проверка создания карточки кандидата"""
        candidate = Candidate(access_token)
        response = candidate.create_candidate()
        assert response.status_code == 201
        print(response.json())
