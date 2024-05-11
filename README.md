# bearbeta_ultimate_coverage


This is based on a full factorial design from a Design of Experiments class. 

Given a data structure with the valid parameter levels, generate a unit test grid, and what the results should be if the code is executing correctly. 

Double check this grid behaves as expected!! then in future UTs if anything changes you will have full coverage. 

#example usage: 
this would deal with 3 parameters, and pass them in order to the fuction named "example_function"

def demo_the_goodies():
    params_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
    combinations, results = generate_combination_and_results(params_levels, example_function)
    print_combo_and_result(combinations, results)


Output for the pretty print
[Combo: ('A', 1, 'X'), 167]

[Combo: ('A', 1, 'Y'), 167]

[Combo: ('A', 2, 'X'), 167]

[Combo: ('A', 2, 'Y'), 167]

[Combo: ('B', 1, 'X'), 167]

[Combo: ('B', 1, 'Y'), 167]

[Combo: ('B', 2, 'X'), 167]

[Combo: ('B', 2, 'Y'), 167]

[Combo: ('C', 1, 'X'), 167]

[Combo: ('C', 1, 'Y'), 167]

[Combo: ('C', 2, 'X'), 167]

[Combo: ('C', 2, 'Y'), 167]

    
