# from application.app.folder.file import func_name
from src.modelReport import averageUsersImprovement


def test_answer():
    Test_area = "tech"
    Test_attr = "forward"
    Test_user_id = [8, 9]

    assert averageUsersImprovement(Test_user_id, Test_area, Test_attr) == 2.0
