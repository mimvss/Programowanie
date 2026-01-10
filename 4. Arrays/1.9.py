# 1.7 - Test results statistics
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]
num_questions = len(test_results)
correct_answers = sum(1 for x in test_results if x)
incorrect_answers = num_questions - correct_answers
percentage = correct_answers/num_questions*100

print('TEST STATISTICS')
print('Number of questions:', num_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', percentage)
