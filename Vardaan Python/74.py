#WAP to return list through function

def get_squares(numbers):
    squares = [n**2 for n in numbers]
    return squares
nums = [1,2,3,4]
squares_list = get_squares(nums)
print(squares_list)
print("written by Vardaan Valecha 0221BCA068")