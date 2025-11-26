"""
Remove duplicate function definitions from professional_diagnostic_analyzer.py
"""

def remove_duplicate_functions(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Track function definitions
    function_starts = {}
    function_ends = {}
    current_function = None
    indent_stack = []
    
    for i, line in enumerate(lines):
        # Check for function definition
        if line.strip().startswith('def '):
            func_name = line.strip().split('(')[0].replace('def ', '')
            indent = len(line) - len(line.lstrip())
            
            if func_name not in function_starts:
                function_starts[func_name] = []
            function_starts[func_name].append((i, indent))
            current_function = (func_name, indent)
        
        # Track end of function (next def or class at same/lower indent, or end of file)
        elif current_function and line.strip() and not line.strip().startswith('#'):
            indent = len(line) - len(line.lstrip())
            func_name, func_indent = current_function
            
            if line.strip().startswith(('def ', 'class ')) and indent <= func_indent:
                # End of current function
                if func_name not in function_ends:
                    function_ends[func_name] = []
                function_ends[func_name].append(i - 1)
                current_function = None
    
    # Mark the last function
    if current_function:
        func_name, _ = current_function
        if func_name not in function_ends:
            function_ends[func_name] = []
        function_ends[func_name].append(len(lines) - 1)
    
    # Find duplicates to remove (keep only first occurrence)
    lines_to_remove = set()
    
    for func_name, starts in function_starts.items():
        if len(starts) > 1:
            print(f"Found {len(starts)} copies of function '{func_name}'")
            # Keep first, remove rest
            for start_idx, indent in starts[1:]:
                # Find the end of this duplicate
                end_idx = start_idx + 1
                # Simple heuristic: find next function or class at same/lower indent
                for j in range(start_idx + 1, len(lines)):
                    line = lines[j]
                    if line.strip() and not line.strip().startswith('#'):
                        curr_indent = len(line) - len(line.lstrip())
                        if line.strip().startswith(('def ', 'class ')) and curr_indent <= indent:
                            end_idx = j
                            break
                else:
                    end_idx = len(lines)
                
                print(f"  Removing duplicate at lines {start_idx+1}-{end_idx}")
                for k in range(start_idx, end_idx):
                    lines_to_remove.add(k)
    
    # Create cleaned version
    cleaned_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
    
    # Write backup
    import shutil
    backup_path = filepath + '.backup'
    shutil.copy(filepath, backup_path)
    print(f"\nBackup created: {backup_path}")
    
    # Write cleaned file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print(f"\nRemoved {len(lines_to_remove)} lines")
    print(f"Original: {len(lines)} lines")
    print(f"Cleaned: {len(cleaned_lines)} lines")

if __name__ == '__main__':
    filepath = r'c:\Users\HWATKI16\Downloads\xml_log_parser\professional_diagnostic_analyzer.py'
    remove_duplicate_functions(filepath)
    print("\nDone! Duplicates removed.")
