import unittest
from two_sum import Solution
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service('C:\Development\chromedriver.exe')


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    """ The following test below are for the equivalence partitioning """
    # Test input with two numbers that add up to the target
    def test_with_any_integer(self):
        arr = [2, 7, 11, 15]
        target = 9

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        assert self.solution.twoSum(arr, target) == [1, 2], 'Not equal'

        # print(check_result == [1, 2])

    '''Test input with negative number and same goes with the target'''
    def test_with_negative_number(self):
        arr = [-5, -4, -3, -2, -1]
        target = -6

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        assert self.solution.twoSum(arr, target) == [1, 5], 'Not equal'
        # self.assertEqual(self.solution.twoSum(arr, target), [1, 5])

        # print(check_result == [1, 3])

    ''' Test input with two numbers where one number is zero and the other is the target'''
    def test_with_zero_target(self):
        arr = [-1, 0, 1]
        target = 1

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        self.assertEqual(self.solution.twoSum(arr, target), [2, 3])
        # print(check_result == [2, 3])

    '''Test input with two numbers where both numbers are the target'''
    def test_input_same_target(self):
        arr = [2, 2]
        target = 4

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        # self.assertEqual(self.solution.twoSum(arr, target), [1, 2])
        self.assertEqual(self.solution.twoSum(arr, target), [1, 2])

        print(self.solution.twoSum(arr, target) == [1, 2])

    '''Here the target can't meet the requirement when added to any integer in the array'''
    def test_input_no_solution(self):
        arr = [2, 7, 11, 15]
        target = 10

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        if num_str2 == "":
            send_answer.send_keys('Empty, No Solution')
        else:
            send_answer.send_keys(num_str2)

        # print(self.assertEqual(self.solution.twoSum(arr, target), [1, 2]))
        self.assertEqual(self.solution.twoSum(arr, target), [])

        print(self.solution.twoSum(arr, target) == [])

    def test_with_mixed_number(self):
        arr = [-5, -4, 0, 2, 4]
        target = -3

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        self.assertEqual(check_result, [1, 4])

        # print(check_result == [1, 4])

    """The below are test of boundary value analysis """

    def test_with_empty_list(self):
        arr = []
        target = 0
        lst = []

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        self.assertEqual(self.solution.twoSum(arr, target), lst)  # []

        print(self.solution.twoSum(arr, target) == lst)

    # in this function nothing should be in the list(lst) because the expected result for a single element
    # should be null if anything is inputted in the test fails
    def test_with_single_length(self):
        arr = [1]
        target = 1
        lst = []

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        self.assertEqual(self.solution.twoSum(arr, target), lst)

        print(self.solution.twoSum(arr, target) == lst)

    def test_with_arrayEqual_target(self):
        arr = [1, 2]
        target = 3
        lst = [1, 2]

        arr_string = ' '.join(str(num) for num in arr)
        target_str = str(target)

        input_arr = self.driver.find_element(by=By.ID, value='numbers')
        input_tar = self.driver.find_element(by=By.ID, value='target')

        input_arr.send_keys(arr_string)
        input_tar.send_keys(target_str)

        submit_button = self.driver.find_element(by=By.ID, value='submit')
        submit_button.click()

        check_result = self.solution.twoSum(arr, target)

        num_str2 = ' and '.join(str(num) for num in check_result)
        # print(type(num_str2))

        js = "let upperDiv = document.createElement('div');" \
             "upperDiv.innerText = 'Answer(Array Index): ';" \
             "var elemDiv = document.createElement('input');" \
             "elemDiv.setAttribute('class', 'check_answer');" \
             "upperDiv.appendChild(elemDiv);" \
             "document.body.appendChild(upperDiv);"

        self.driver.execute_script(js)

        send_answer = self.driver.find_element(by=By.CLASS_NAME, value='check_answer')

        send_answer.send_keys(num_str2)

        assert self.solution.twoSum(arr, target) == lst, 'Not equal'
        # self.assertEqual(self.solution.twoSum(arr, target), [1, 2])

        print(self.solution.twoSum(arr, target) == lst)

    """ Test with a list of length 2 where the sum is smaller or larger than target
        NB this two will be a bug as it is a failed test  """


if __name__ == '__main__':
    unittest.main()
