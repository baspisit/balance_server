from gauss import gauss_elimination
from readmol import parse_molecule, summarize_elements_keys
import numpy as np
import math

def scale_to_integer(numbers):
    scale = 1
    rounded_numbers = []

    # Iterate until all numbers can be rounded to an integer
    while True:
        rounded_numbers = [round(num * scale) for num in numbers]
        # Check if all numbers are rounded to integers
        if all(math.isclose(num * scale, round(num * scale)) for num in numbers):
            break
        scale += 1
    
    return rounded_numbers

def balancing(reagent,product):
    # reagent = ('CH4','O2')
    # product = ('CO2','H2O')
    for index, item in enumerate(reagent):
        var_name = f're{index}'
        globals()[var_name] = parse_molecule(item)

    for index, item in enumerate(product):
        var_name = f'pr{index}'
        globals()[var_name] = parse_molecule(item)

    re_dist=[]
    for i in range(len(reagent)):
        re_dist.append(eval(f're{i}'))

    pr_dist=[]
    for i in range(len(product)):
        pr_dist.append(eval(f'pr{i}'))

    dict_list=[]
    for i in range(len(reagent)):
        dict_list.append(eval(f're{i}'))

    for i in range(len(product)):
        dict_list.append(eval(f'pr{i}'))

    element_list = summarize_elements_keys(dict_list)
    # print(element_list)
    # print(re_dist)
    # print(pr_dist)
    # print(dict_list)

    if((len(reagent)+len(product))-len(element_list) < 2):
        newelement = element_list[:(len(reagent)+len(product))-1]
        matrix = [
            [
                *[re.get(el, 0) for re in re_dist[1:]],  # Append values from all `re` dictionaries
                *[-pr.get(el, 0) for pr in pr_dist]  # Append negative values from all `pr` dictionaries
            ]
        for el in newelement
        ]
        vector = [-re0.get(el, 0) for el in newelement]
        A = np.array(matrix, dtype=float)
        # Right-hand side vector (adjusted for a = 1, c = 1, d = 2)
        b = np.array(vector, dtype=float)


        # Perform Gauss elimination
        coefficients = gauss_elimination(A, b)
        coefficients = np.insert(coefficients, 0, 1)  # a = 1
        rounded = scale_to_integer(coefficients)
        roundedcoff = np.round(rounded).astype(int)
        compounds = reagent + product
        # print(compounds)
        # print(coefficients)

        # For reagents
        reagent_str = " + ".join(f"{roundedcoff[i]}{reagent[i]}" for i in range(len(reagent)))

        # For products
        product_str = " + ".join(f"{roundedcoff[i+len(reagent)]}{product[i]}" for i in range(len(product)))

        # Combine both parts into the final balanced equation
        balanced_equation = f"{reagent_str} ---> {product_str}"
        return f"Balanced Equation: {balanced_equation}"
    else:
        print((len(reagent)+len(product))-len(element_list))
        return ("this reaction has more than 1 solution")

    