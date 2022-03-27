from Fibonacci_Class import Fibonacci

fibonacci_of = Fibonacci()
fibonacci_tuple = [fibonacci_of(i) for i in range(10)]
second_value = fibonacci_of(2)

print('\nFibonacci Sequence:\n',fibonacci_tuple, '\nSecond element value:\n', second_value)