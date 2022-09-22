###ALGORITHMS SECTION

def selection_sort(arr):
    array_length = len(arr)
    for i in range(array_length):

        lowest_value_index = i

        for j in range(i + 1, array_length):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j

        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]

    return arr
###########



###TASKS SECTION###



class Solution():

    def quadratic_equation_coefficients(self, x, y):
        ###Шукаємо за оберненою теоремою Вієта

        b = -(x + y)
        a = int(b / (-x - y))
        c = x * y

        return f"First coefficient - {a}\nSecond coefficient - {b}\nThird coefficient - {c}\n"

    def is_triangle(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        else:
            sides = [a, b, c]
            greatest_side = (selection_sort(sides)[-1]) ###LAST NUM OF ARRAY(BIGGEST SIDE OF TRIANGLE)

            sum_of_other_sides = sides[0] + sides[1]
            sum_of_other_sides_square = sides[0] ** 2 + sides[1] ** 2

            if greatest_side >= sum_of_other_sides:
                return False

            else:
                ### If c^2 = b^2 + a^2 - right triangle   If c^2 > b^2 + a^2 - obtuse triangle  If c^2 < b^2 + a^2 - acute triangle
                if greatest_side ** 2 == sum_of_other_sides_square:
                    return "Прямокутний трикутник."
                elif greatest_side ** 2 < sum_of_other_sides_square:
                    return "Гострокутний трикутник."
                else:
                    return "Тупокутний трикутник."

    def is_sum_equals(self, number):

        if len(str(number)) != 4:
            return False

        cur_number = number
        second_sum = 0
        first_sum = 0

        while cur_number != 0:

            if len(str(cur_number)) > 2:
                second_sum += cur_number % 10
                cur_number = cur_number // 10

            else:
                first_sum += cur_number % 10
                cur_number = cur_number // 10

        if second_sum == first_sum:
            return True
        else:
            return False

    def fibonacci(self, n):
        if n < 0 :
            return False
        elif n in {0, 1}:
            return n

        return self.fibonacci(n - 1) + self.fibonacci(n - 2) #### this function will show n-1 element

    def find_in_arr(self, element, arr):
        for i in arr:
            if i == element:
                return True
        return False

    def prime_numbers(self, length):
        prime_numbers_arr = []
        for number in range(2, length + 1):
            for divider in range(2, number):
                if number % divider == 0:
                    break
            else:
                prime_numbers_arr.append(number)

        return prime_numbers_arr

    def lcm(self, m, n):
        if m < n:
            bigger = n
        else:
            bigger = m

        while True:
            if bigger % n == 0 and bigger % m == 0:
                return bigger
            else:
                bigger+= 1


    def different_numbers(self, arr):
        cache = {}

        for number in arr:
            number_key = str(number)
            if number_key in cache:
                cache[number_key] += 1
            else:
                cache[number_key] = 1

        return cache





class_instance = Solution()

# print(class_instance.quadratic_equation_coefficients(3, -1))
# print(class_instance.is_triangle(7, 2, 8))
# print(class_instance.is_sum_equals(7281))
# print(class_instance.fibonacci(3))
# print(class_instance.find_in_arr(5, [3,2,1]))
# print(class_instance.prime_numbers(100))
# print(class_instance.lcm(100, 1000))
# print(class_instance.different_numbers([1, 3, 3, 8, 12, 15, 15]))

######

