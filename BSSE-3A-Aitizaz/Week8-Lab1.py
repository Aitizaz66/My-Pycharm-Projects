def gps(initial_states, goal_states, operators):
    prefix = 'EXECUTING '
    for operator in operators:
        operator['action'] = operator['action'].upper()
        operator['add'].append(prefix + operator['action'])
        operator['preconds'] = [pre.upper() for pre in operator['preconds']]
        operator['delete'] = [dlst.upper() for dlst in operator['delete']]
        operator['add'] = [add.upper() for add in operator['add']]
    initial_states = [state.upper() for state in initial_states]
    goal_states = [goal.upper() for goal in goal_states]
    final_states = achieve_all(initial_states, operators, goal_states, [])
    if not final_states:
        return None
    actions = [state for state in final_states if state.startswith(prefix)]
    for a in actions:
        print(a)
    return actions


def achieve_all(states, ops, goals, goal_stack):
    for goal in goals:
        states = achieve(states, ops, goal, goal_stack)
        if not states:
            return None
    for goal in goals:
        if goal not in states:
            return None
    return states


def achieve(states, operators, goal, goal_stack):
    print(len(goal_stack), 'Achieving: %s' % goal)
    if goal in states:
        print(len(goal_stack), 'Achieved: %s' % goal)
        return states
    if goal in goal_stack:
        return None
    for op in operators:
        if goal not in op['add']:
            continue
        result = apply_operator(op, states, operators, goal, goal_stack)
        if result:
            return result


def apply_operator(operator, states, ops, goal, goal_stack):
    print(len(goal_stack), 'Consider: %s' % operator['action'])
    result = achieve_all(states, ops, operator['preconds'], [goal] + goal_stack)
    if not result:
        return None
    print(len(goal_stack), 'Action: %s' % operator['action'], '  Achieved: %s' % goal)
    add_list, delete_list = operator['add'], operator['delete']
    return [state for state in result if state not in delete_list] + add_list


# Robot_ops=[
#    {
#       "action": "open the door",
#       "preconds": ["door close"],
#       "add": ["door open"],
#       "delete": ["door close"]
#    },
#    {
#       "action": "move robot inside",
#       "preconds": ["robot standing outside","door open"],
#       "add": ["robot inside"],
#       "delete": ["robot standing outside"]
#    },
#    {
#       "action": "Turn on lights",
#       "preconds": ["robot inside","lights off"],
#       "add": ["lights on"],
#       "delete": ["lights off"]
#    }
# ]
# gps(["robot standing outside","lights off","door close"],
#     ["lights on"],Robot_ops)
block_ops = [
    {"action": "Move block C on table",
     "preconds": ["Block C on A", "C-free"],
     "add": ["Block C on table", "A-free"],
     "delete": ["Block C on A"]},
    {"action": "Move block A on table",
     "preconds": ["Block A on B", "A-free"],
     "add": ["Block A on table", "B-free"],
     "delete": ["Block A on B"]},
    {"action": "Move block B on C",
     "preconds": ["Block B on table", "B-free", "C-free"],
     "add": ["Block B on C"],
     "delete": ["Block B on table", "C-free"]},
    {"action": "Move block A on B",
     "preconds": ["Block A on table", "A-free", "B-free"],
     "add": ["Block A on B"],
     "delete": ["Block A on table", "B-free"]}
]
gps(["Block B on table", "Block A on B", "Block C on A", "C-free"],
    ["Block C on table", "Block B on C", "Block A on B", "A-free"]
    , block_ops)
