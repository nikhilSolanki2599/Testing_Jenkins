
def fibonacci(n, intermediate_results={}):
    if n <= 1:
        return n
    if n not in intermediate_results:
        intermediate_results[n] = fibonacci(n - 1, intermediate_results) + fibonacci(n - 2, intermediate_results)
        # print(intermediate_results,"\n")
    return intermediate_results[n]

no_of_terms = 50

if no_of_terms<=0:
  print("Please enter a positive integer")
else:
  print("Fibonacci series:")
  for i in range(no_of_terms):
    print("Term",i+1,"\t",fibonacci(i))


