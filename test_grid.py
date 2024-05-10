from generate_result import * 

def run_ut(function_under_test, combinations, results):
    for combination, result in zip(combinations, results):
        assert result == function_under_test(*combination)
        print("TRUE")

def test_general_uts():
    param_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
    combinations, results = generate_combination_and_results(param_levels, example_function)
    run_ut(example_function, combinations, results)