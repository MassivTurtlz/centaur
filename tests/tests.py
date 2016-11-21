from config import JSON_TEST_NAME
from config import TEST_JSON
from config import TEST_SAVE_FILE
from controller.readWrite import get_json
from controller.readWrite import update_json


# This tests the get_json() function, and the update_json() function.
def test_update_json():

    array_length_start = len(get_json(TEST_SAVE_FILE))
    update_json(TEST_JSON, TEST_SAVE_FILE)
    array_length_finish = len(get_json(TEST_SAVE_FILE))
    if array_length_start < array_length_finish:
        print(JSON_TEST_NAME + " success")
    elif array_length_start == array_length_finish:
        print(JSON_TEST_NAME + " fail")

test_update_json()
