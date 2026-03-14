import pytest

class TestAuthorization:
    """Проверки авторизации"""
    @pytest.mark.parametrize(
        "login, password, status",
        [
            ("yura.ulyanov.1997@mail.ru","YU#2SVhoxU!I",200),
            ("yura.ulyinov.1997@mail.ru","YU#2SVhoxU!I",404),
            ("yura.ulyanov.1997@mail.ru","YUU#2SVhoxU!I",500)
        ]
    )
    def test_authorization(self,authorization_api,login,password,status):
        authorization = authorization_api
        print(authorization)
        assert authorization.status_code == status
        if authorization.status_code == 200:
            response_success = authorization.json()["success"]
            assert response_success == True
        elif authorization.status_code == 404:
            assert authorization.json()["message"] == f"Пользователь с таким E-mail не найден в базе данных: {login}"
        else:
            assert authorization.json()["message"] == "Bad credentials"