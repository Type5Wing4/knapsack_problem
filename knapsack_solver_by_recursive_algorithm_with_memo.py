import sys
import json
import itertools

def knapsack_problem_solver_by_recursive_algorithm_with_memo(input_file):

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

    def total_value(i, max_weight):

        if memo[i][max_weight] != -1:
            pass

        else:

            if i <= nb_candidate_objects-1:

                weight_i = weight_and_value_list[i][0] 
                value_i  = weight_and_value_list[i][1] 

                if weight_i <= max_weight:
                    # select i+1 th object or not.
                    tval = max(value_i + total_value(i+1, max_weight - weight_i),
                                         total_value(i+1, max_weight))
                else:
                    # not select i+1 th object.
                    tval = total_value(i+1, max_weight)

            elif i == nb_candidate_objects:
                # total value is zero if there are no more candidate objects.
                tval = 0

            memo[i][max_weight] = tval

        print(memo)

        return memo[i][max_weight] 

    tval = total_value(0, max_weight)

    print(tval)

#    # Display solutions
#    print('Solution and Total weight and Total value')


if __name__ == "__main__":

    input_file = sys.argv[1]
    knapsack_problem_solver_by_recursive_algorithm_with_memo(input_file)
