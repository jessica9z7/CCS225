# Jessica Kusmierz
# 11/14/2025
# Problem 6
def check_tasks(character_items, character_debuffs):
    """
    Check if the character can perform various tasks based on:
    - Items they have collected
    - Status debuffs affecting them
    
    Parameters:
    character_items (list): List of items the character has
    character_debuffs (list): List of debuffs affecting the character
    """
    
    # Define the requirements for each task
    tasks = {
        'Climb a mountain': {
            'required_items': ['rope', 'coat', 'first aid kit'],
            'blocking_debuffs': ['slow']
        },
        'Cook a meal': {
            'required_items': ['pan', 'groceries'],
            'blocking_debuffs': ['small']  # Assuming 'small' means they're too small to cook
        },
        'Write a book': {
            'required_items': ['pen', 'paper', 'idea'],
            'blocking_debuffs': ['confusion']
        }
    }
    
    print("=== TASK CHECKER ===")
    print(f"Character Items: {character_items}")
    print(f"Character Debuffs: {character_debuffs}")
    print("=" * 40)
    
    # Check each task
    for task_name, requirements in tasks.items():
        print(f"\nChecking: {task_name}")
        
        # Check if character has ALL required items
        missing_items = []
        for required_item in requirements['required_items']:
            if required_item not in character_items:
                missing_items.append(required_item)
        
        # Check if character has ANY blocking debuffs
        blocking_debuffs = []
        for blocking_debuff in requirements['blocking_debuffs']:
            if blocking_debuff in character_debuffs:
                blocking_debuffs.append(blocking_debuff)
        
        # Determine if task can be performed
        can_perform = len(missing_items) == 0 and len(blocking_debuffs) == 0
        
        # Print detailed results
        if can_perform:
            print("CAN perform this task!")
        else:
            print(" CANNOT perform this task")
            
        if missing_items:
            print(f"   Missing items: {missing_items}")
        else:
            print(f"   ✓ Has all required items")
            
        if blocking_debuffs:
            print(f"   Blocking debuffs: {blocking_debuffs}")
        else:
            print(f"   ✓ No blocking debuffs")
    
    return tasks

# Test with the given character data
def main():
    """Test the task checker with the provided character data"""
    
    # Character data from the problem
    character_items = ['pan', 'paper', 'idea', 'rope', 'groceries']
    character_debuffs = ['slow']
    
    print("Testing with provided character data:")
    check_tasks(character_items, character_debuffs)
    
    # Additional test cases to demonstrate different scenarios
    print("\n" + "="*50)
    print("ADDITIONAL TEST CASES")
    print("="*50)
    
    # Test Case 1: Character with all items and no debuffs
    print("\n--- TEST CASE 1: Perfect Character ---")
    perfect_items = ['rope', 'coat', 'first aid kit', 'pan', 'groceries', 'pen', 'paper', 'idea']
    perfect_debuffs = []
    check_tasks(perfect_items, perfect_debuffs)
    
    # Test Case 2: Character missing some items
    print("\n--- TEST CASE 2: Missing Some Items ---")
    missing_items = ['pan', 'paper', 'idea', 'rope', 'groceries']  # Missing coat, first aid kit, pen
    some_debuffs = []
    check_tasks(missing_items, some_debuffs)
    
    # Test Case 3: Character with blocking debuffs
    print("\n--- TEST CASE 3: Has Blocking Debuffs ---")
    all_items = ['rope', 'coat', 'first aid kit', 'pan', 'groceries', 'pen', 'paper', 'idea']
    bad_debuffs = ['slow', 'small', 'confusion']  # Has all blocking debuffs
    check_tasks(all_items, bad_debuffs)

# Enhanced version with more detailed analysis
def detailed_task_analysis(character_items, character_debuffs):
    """
    Provides a more detailed analysis of what the character can/cannot do
    and suggestions for improvement
    """
    tasks = {
        'Climb a mountain': {
            'required_items': ['rope', 'coat', 'first aid kit'],
            'blocking_debuffs': ['slow'],
            'description': 'Scale the treacherous mountain peak'
        },
        'Cook a meal': {
            'required_items': ['pan', 'groceries'],
            'blocking_debuffs': ['small'],
            'description': 'Prepare a nutritious meal'
        },
        'Write a book': {
            'required_items': ['pen', 'paper', 'idea'],
            'blocking_debuffs': ['confusion'],
            'description': 'Author a great literary work'
        }
    }
    
    print("\n" + "="*50)
    print("DETAILED TASK ANALYSIS")
    print("="*50)
    print(f"Current Inventory: {character_items}")
    print(f"Current Status: {character_debuffs}")
    print()
    
    available_tasks = []
    unavailable_tasks = []
    
    for task_name, requirements in tasks.items():
        missing_items = [item for item in requirements['required_items'] if item not in character_items]
        blocking_debuffs = [debuff for debuff in requirements['blocking_debuffs'] if debuff in character_debuffs]
        
        if not missing_items and not blocking_debuffs:
            available_tasks.append(task_name)
        else:
            unavailable_tasks.append({
                'task': task_name,
                'missing_items': missing_items,
                'blocking_debuffs': blocking_debuffs,
                'description': requirements['description']
            })
    
    # Print available tasks
    if available_tasks:
        print(" TASKS YOU CAN PERFORM:")
        for task in available_tasks:
            print(f"    {task}")
    else:
        print(" No tasks can be performed currently")
    
    # Print unavailable tasks with reasons
    if unavailable_tasks:
        print("\n TASKS YOU CANNOT PERFORM:")
        for task_info in unavailable_tasks:
            print(f"\n    {task_info['task']}")
            print(f"      Description: {task_info['description']}")
            if task_info['missing_items']:
                print(f"      Missing: {', '.join(task_info['missing_items'])}")
            if task_info['blocking_debuffs']:
                print(f"      Blocked by: {', '.join(task_info['blocking_debuffs'])}")
    
    # Provide suggestions
    print("\n💡 SUGGESTIONS:")
    all_required_items = set()
    all_blocking_debuffs = set()
    
    for task_info in tasks.values():
        all_required_items.update(task_info['required_items'])
        all_blocking_debuffs.update(task_info['blocking_debuffs'])
    
    missing_from_all = [item for item in all_required_items if item not in character_items]
    current_blocking = [debuff for debuff in character_debuffs if debuff in all_blocking_debuffs]
    
    if missing_from_all:
        print(f"   Find these items: {', '.join(missing_from_all)}")
    if current_blocking:
        print(f"   Remove these debuffs: {', '.join(current_blocking)}")
    
    return available_tasks, unavailable_tasks

# Run the tests
if __name__ == "__main__":
    # Test with original character data
    character_items = ['pan', 'paper', 'idea', 'rope', 'groceries']
    character_debuffs = ['slow']
    
    main()
    
    # Run detailed analysis
    detailed_task_analysis(character_items, character_debuffs)