def refine_tests(test_dir):
    for test_file in os.listdir(test_dir):
        with open(os.path.join(test_dir, test_file), 'r') as f:
            test_code = f.read()
        
        with open('instructions/test_refinement.yaml', 'r') as f:
            instructions = f.read()
        
        prompt = f"Improve these existing unit tests:\n\n{test_code}\n\nFollow these instructions:\n{instructions}"
        refined_code = query_llm(prompt)
        
        with open(os.path.join(test_dir, test_file), 'w') as f:
            f.write(refined_code)