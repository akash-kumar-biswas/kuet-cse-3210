variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
colors = ["Red", "Green", "Blue"]

graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}


def is_valid(variable, color, assignment):
    for neighbor in graph[variable]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def select_mrv_variable(assignment):
    unassigned = [v for v in variables if v not in assignment]
    
    min_var = None
    min_domain_size = float('inf')
    
    for var in unassigned:
        valid_colors = 0
        for color in colors:
            if is_valid(var, color, assignment):
                valid_colors += 1
        
        if valid_colors < min_domain_size:
            min_domain_size = valid_colors
            min_var = var
            
    return min_var


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = select_mrv_variable(assignment)

    for color in colors:
        if is_valid(var, color, assignment):
            assignment[var] = color
            
            result = backtrack(assignment)
            if result:
                return result

            del assignment[var]

    return None


solution = backtrack({})
print("Solution:")
print(solution)
