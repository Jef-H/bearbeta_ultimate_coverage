from itertools import product


def process_combination(param1, param2, param3):
    # Example operation: Concatenate the parameters and return the result
    result = f"{param1}-{param2}-{param3}"  # Example operation
    return result


def example_function(a, b, c):
    return "167"


def generate_combination_and_results(params_levels, process_fuction):
    # Example usage:
    # params_levels = [['A', 'B', 'C'], [1, 2], ['X', 'Y']]
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
        print(f"{combination} {result}")


def pretty_print_combo_and_result_together(combinations, results):
    for combination, result in zip(combinations, results):
        print(f"[Combo: {combination}, {result}]")


def write_log_file(example_function, combinations, results):
    log_file_name = example_function.__name__ + "_log.txt"
    with open(log_file_name, "w") as log_file:
        log_file.write("Combinations=")
        log_file.write("[")
        for combo in combinations:
            log_file.write(str(combo))
            log_file.write(",")
        log_file.write("]")
        log_file.write("\n")
        log_file.write("Results=")
        log_file.write("[")
        for res in results:
            log_file.write(res)
            log_file.write(",")
        log_file.write("]")


# example usage:
def demo_the_goodies():
    params_levels = [["A", "B", "C"], [1, 2], ["X", "Y"]]
    combinations, results = generate_combination_and_results(
        params_levels, example_function
    )
    pretty_print_combo_and_result_together(combinations, results)
    write_log_file(example_function, combinations, results)


demo_the_goodies()
