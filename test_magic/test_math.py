# import pytest
#
# @pytest.fixture(scope="function")
# def base_url():
#     return "http://94.156.115.228"
#
# @pytest.mark.smoke
# def test_base_url_looks_valid(base_url):
#     print(f"Использум API по адресу: {base_url}")
#
# @pytest.mark.smoke
# def test_sum():
#     result = 2 + 3
#     expected_result = 5
#
#     assert result == expected_result, f"Ожидалось {expected_result}, но питон не умеет считать и получили {result}"
#
# @pytest.mark.smoke
# def test_string_concat():
#     result = "Qa" + "Mentor"
#     expected_result = "QaMentor"
#     assert result == expected_result, f"Ожидалось {expected_result}, но питон не умеет складывать слова и получили {result}"
#
# @pytest.mark.smoke
# def test_search_clowns():
#     result = "GOMO" + "GEY"
#     expected_result = "IvanZelenov"
#     assert result == expected_result, f"Ожидалось {expected_result}, но питон не знает, что из гомогеев существует только Ванюшка {result}"