import sys
import json
import itertools

def exhausive_search(input_file):

    # Read input file 
    json_open = open(input_file, 'r')
    problem_info = json.load(json_open)

    max_weight = problem_info['max_weight']
    weight_and_value_list = problem_info['weight_and_value_list']

    print('Max Weight', max_weight)
    print('Weight and Value List', weight_and_value_list)
    print()


    # Perform exhaustive Search
    candidate_solution_i = 0
    candidate_solutions = []
    max_value = 0
    for nb_objects in range(len(weight_and_value_list)):
        for wvi in itertools.combinations(weight_and_value_list,nb_objects):

            total_weight = 0
            total_value = 0
            for wv in wvi:
                total_weight += wv[0]
                total_value += wv[1]

            if total_weight <= max_weight:
                candidate_solutions.append([[total_weight, total_value], wvi])
                candidate_solution_i  += 1

                if max_value <= total_value:
                    max_value = total_value


    candidate_solution_under_max_weight = []
    for candidate_solution in candidate_solutions:
        if candidate_solution[0][0] <= max_weight and candidate_solution[0][1] == max_value:
            candidate_solution_under_max_weight.append(candidate_solution)

    # Display solutions
    print('Solution and Total weight and Total value')
    sol_i = 1
    for csumw in candidate_solution_under_max_weight:
        print('No.'+ str(sol_i), csumw[1], csumw[0][0], csumw[0][1])
        sol_i += 1


if __name__ == "__main__":


    input_file = sys.argv[1]
    exhausive_search(input_file)
