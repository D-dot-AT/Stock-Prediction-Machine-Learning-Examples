from scipy.stats import fisher_exact


def print_statistics(tp: int, fp: int, fn: int, tn: int):
    # Step 5: Statistical Analysis
    # Using the counts obtained from Step 4, perform Fisher's exact test to determine the p-value.
    contingency_table = [[tp, tp + fp], [fn + tp, tp + fp + tn + fn]]
    _, p_value = fisher_exact(contingency_table)
    precision = float(tp) / (tp + fp)
    accuracy = float(tp + tn) / (tp + fp + tn + fn)

    # Step 6: Output
    # Print the following information:
    print(f'TN: {tn}')
    print(f'TP: {tp}')
    print(f'FN: {fn}')
    print(f'FP: {fp}')
    print(f'Precision: {precision}')
    print(f'Accuracy: {accuracy}')
    print(f'P-value of precision: {p_value}')