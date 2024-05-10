from itertools import product

def example_function(a,  b, c):
    return "167"

def generate_combination_and_results(params_levels, process_fuction):
    # Example usage:
    #params_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
    combinations = []
    results = []

    # Generate combinations & calculate results based on current env.
    for combination in product(*params_levels):
        # Call the function with each combination as parameters
        result = process_fuction(*combination)
        combinations.append(combination)
        results.append(result)
    return combinations, results

# Print or use the combinations and results
def print_combo_and_result(combinations, results):
    for combination, result in zip(combinations, results):
        print(f'{combination} {result}')

#example usage: 
def demo_the_goodies():
    params_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
    combinations, results = generate_combination_and_results(params_levels, example_function)
    print_combo_and_result(combinations, results)
