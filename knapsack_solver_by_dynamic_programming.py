import sys
import json
import itertools

def knapsack_problem_solver_by_dynamic_programming(input_file):

    # Read input file 
    json_open = open(input_file, 'r')
    problem_info = json.load(json_open)

    max_weight = problem_info['max_weight']
    weight_and_value_list = problem_info['weight_and_value_list']
    nb_candidate_objects = len(weight_and_value_list)

    print('Max Weight', max_weight)
    print('Weight and Value List', weight_and_value_list)
    print()

    memo = [[-1 for j in range(max_weight+1)] for i in range(nb_candidate_objects+1)]

    for j in range(max_weight+1):
        memo[nb_candidate_objects][j] = 0

    for i in range(nb_candidate_objects)[::-1]:

        weight_i = weight_and_value_list[i][0]
        value_i = weight_and_value_list[i][1]

        for w in range(max_weight+1):

            if w >= weight_i:
                memo[i][w] = max(memo[i+1][w], value_i + memo[i+1][w - weight_i])
            else:
                memo[i][w] = memo[i+1][w]

    print(memo)

#    # Display solutions
#    print('Solution and Total weight and Total value')


if __name__ == "__main__":

    input_file = sys.argv[1]
    knapsack_problem_solver_by_dynamic_programming(input_file)
