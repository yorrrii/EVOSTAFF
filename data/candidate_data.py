from faker import Faker

fake = Faker("ru_RU")

create_valid_candidate = {"asap":False,"comment":"ясчм","contacts":{"email":fake.email(),"mainContact":{"id":"58da469c-feda-41a3-aa0f-aac382681153","label":"Телефон","value":"phone1"},"phone":fake.phone_number(),"phone2":"","social":"","social2":"","telegram":fake.password(length=10)},"name":{},"person":{"age":"","country":{"id":"92895e68-428a-4c4c-bcf5-bfb64741e907","label":"Россия","value":"russia"},"lastname":fake.last_name(),"name":fake.first_name(),"photo":"","readyToMove":False,"secondname":""},"resume":{"habr":"","hhru":""},"salary":{"current":{"currency":{"id":"8906678e-604c-497d-850a-0bbbf4fb123b","label":"руб","orderId":1,"value":"rub"},"value":""},"desired":{"currency":{"id":"8906678e-604c-497d-850a-0bbbf4fb123b","label":"руб","orderId":1,"value":"rub"},"value":""}},"statuses":[{"status":{"color":"#439B38","id":"1e47ce74-d161-4fcb-9c1b-aa33d2d26626","isManager":False,"label":"Новый кандидат","results":[],"showCalendar":False,"showClarifying":False,"showCustomer":False,"showResult":False,"value":"new_candidate"}}]}

get_users = {"query":"","specialization":[],"status":[],"regions":[],"typeEmployment":[],"country":[],"result":[],"clarifying":[],"education":[],"competitions":[],"languages":[],"showCase":False}
