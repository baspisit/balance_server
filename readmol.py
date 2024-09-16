import re
from collections import defaultdict, deque


def parse_molecule(formula):
    # Regular expression to match elements, numbers, parentheses, and nested structures
    element_regex = r'([A-Z][a-z]*)(\d*)'
    group_regex = r'([A-Z][a-z]*|\()(\d*)'
    
    def parse_group(formula):
        stack = deque()
        element_counts = defaultdict(int)
        
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                # Start of a new group
                stack.append(element_counts)
                element_counts = defaultdict(int)
                i += 1
            elif formula[i] == ')':
                # End of a group
                i += 1
                # Read the multiplier after the closing parenthesis
                multiplier_match = re.match(r'(\d+)', formula[i:])
                multiplier = int(multiplier_match.group(1)) if multiplier_match else 1
                i += len(multiplier_match.group(0)) if multiplier_match else 0
                
                # Multiply the counts in the current group
                for key, value in element_counts.items():
                    element_counts[key] *= multiplier
                
                # Merge with the previous level
                prev_counts = stack.pop()
                for key, value in element_counts.items():
                    prev_counts[key] += value
                element_counts = prev_counts
            else:
                # Match element or group with multiplier
                match = re.match(group_regex, formula[i:])
                if match:
                    element = match.group(1)
                    count = int(match.group(2)) if match.group(2) else 1
                    if '(' in element or ')' in element:
                        # Skip parentheses in match
                        i += len(match.group(0))
                        continue
                    element_counts[element] += count
                    i += len(match.group(0))
        
        return dict(element_counts)
    
    # Remove all spaces from formula
    formula = formula.replace(' ', '')
    return parse_group(formula)

def summarize_elements_keys(dict_list):
    # Initialize a set to store unique elements
    unique_elements = set()
    
    # Iterate over each dictionary in the list
    for element_dict in dict_list:
        # Add the keys (elements) to the set
        unique_elements.update(element_dict.keys())
    
    # Convert the set to a sorted list and return it as a tuple
    return list(sorted(unique_elements))

# Example usage
# dict_list = [
#     {'C': 6, 'H': 12, 'O': 6},
#     {'Na': 1, 'Cl': 1},
#     {'O': 2},
#     {'C': 1, 'Xe': 2}
# ]

# result = summarize_elements_keys(dict_list)
# print(result)

# formula = "Al2(CO3)3"
# result = parse_molecule(formula)
# print(result)  # Should output: {'Al': 2, 'C': 3, 'O': 9}

