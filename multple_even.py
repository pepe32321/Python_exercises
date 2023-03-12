def multiply_even_numbers(numbers):
    even_numbers=[num for num in numbers if num%2==0]
    if not even_numbers:
        return
    result=1
    for i in range(0,len(even_numbers)):
        result=result*even_numbers[i]
    return print(result)

multiply_even_numbers([2,3,4,5,6]) # 48

