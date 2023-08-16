import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass

def generate_folder_structure():
    # Create main project directories
    create_directory('emulator')
    create_directory('emulator/game_files')
    
    create_directory('src')
    create_directory('src/ai')
    create_directory('src/game')
    create_directory('src/utils')
    
    create_directory('data')
    create_directory('data/training_data')
    create_directory('data/checkpoints')
	
    create_directory('tests')
    create_directory('tests/ai')
    create_directory('tests/game')
    create_directory('tests/utils')
    
    create_directory('docs')
    
    # Create empty template files
    create_file('src/main.py')
    create_file('src/ai/evolution_algorithm.py')
    create_file('src/ai/neural_network.py')
    create_file('src/game/game_interface.py')
    create_file('src/game/game_state.py')
    create_file('src/utils/logging.py')
    create_file('src/utils/config.py'))
	
    create_file('tests/test_utils.py')
    
    create_file('docs/folder_structure.md')
    create_file('docs/naming_conventions.md')
	
    create_file('docs/chatgpt_branch_relevant_logs.md')
    create_file('docs/chatgpt_commit_relevant_logs.md')
    
    with open('README.md', 'w') as readme_file:
        readme_file.write("# Your Project's README\n\nThis is where you can introduce your project.")
    
    print("Folder structure and template files generated successfully.")

if __name__ == "__main__":
    generate_folder_structure()