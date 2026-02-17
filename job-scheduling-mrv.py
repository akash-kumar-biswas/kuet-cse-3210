tasks = ["A", "B", "C"]

duration = {
    "A": 2,
    "B": 2,
    "C": 1
}

domain = range(0, 6)

precedence = {
    "B": ["A"],
    "C": ["B"]
}


def is_valid(task, start_time, assignment):
    if task in precedence:
        for prev_task in precedence[task]:
            if prev_task in assignment:
                prev_end = assignment[prev_task] + duration[prev_task]
                if start_time < prev_end:
                    return False
    return True

def select_mrv_task(assignment):
    unassigned = [t for t in tasks if t not in assignment]
    
    min_task = None
    min_domain_size = float('inf')
    
    for task in unassigned:
        valid_times = [
            time for time in domain
            if is_valid(task, time, assignment)
        ]
        
        if len(valid_times) < min_domain_size:
            min_domain_size = len(valid_times)
            min_task = task
            
    return min_task


def backtrack(assignment):
    if len(assignment) == len(tasks):
        return assignment

    task = select_mrv_task(assignment)

    for time in domain:
        if is_valid(task, time, assignment):
            assignment[task] = time
            
            result = backtrack(assignment)
            if result:
                return result

            del assignment[task]

    return None

solution = backtrack({})
print("Schedule:", solution)
