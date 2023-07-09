import subprocess

def get_process_tree():
    # Execute the wmic command and capture the output
    output = subprocess.check_output('wmic process get Caption,ParentProcessId,ProcessId', shell=True).decode()

    # Split the output into lines and remove the header
    lines = output.strip().split('\n')[1:]
    # Create a dictionary to store process information
    process_dict = {}
    PIDs = []
    # Process each line and populate the dictionary
    for line in lines:
        caption, parent_pid, process_id = line.strip().split(None, 2)
        PIDs.append(process_id)
        process_dict[process_id] = {'caption': caption, 'parent_pid': parent_pid}
    # print(process_dict)
    # Function to recursively print process tree
    def print_process_tree(pid, indent=''):
        PIDs.remove(pid)
        process = process_dict.get(pid)
        if process:
            print(indent + '└─', process['caption'], '(', pid, ')')
            children = [child for child, info in process_dict.items() if info['parent_pid'] == pid]
            for child in children:
                print(indent + '   ', end='')
                print_process_tree(child, indent + '   ')
    
    
    sorted(PIDs)
    for root_pid in PIDs:
        print_process_tree(root_pid)

# Call the function to generate and print the process tree
get_process_tree()
