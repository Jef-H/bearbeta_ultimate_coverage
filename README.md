# bearbeta_ut_grid


This is based on a full factorial design from a Design of Experiments class. 

Given a data structure with the valid parameter levels, generate a unit test grid, and what the results should be if the code is executing correctly. 

Double check this grid behaves as expected!! then in future UTs if anything changes you will have full coverage. 


#example usage: 
def demo_the_goodies():
    params_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
    combinations, results = generate_combination_and_results(params_levels, example_function)
    print_combo_and_result(combinations, results)
