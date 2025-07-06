def build_and_debug():
    # Build the tests
    build_process = subprocess.run(['g++', '-std=c++17', '-I.', '-lgtest', '-lgtest_main', '-pthread', 
                                  'tests/*.cpp', '-o', 'test_runner'], 
                                 capture_output=True, text=True)
    
    if build_process.returncode != 0:
        # Build failed - send to LLM for fixes
        with open('instructions/build_fix.yaml', 'r') as f:
            instructions = f.read()
        
        prompt = f"Fix these test compilation errors:\n\n{build_process.stderr}\n\nOriginal tests:\n\n{get_all_tests()}\n\nFollow these instructions:\n{instructions}"
        fixed_code = query_llm(prompt)
        
        # Save fixed tests and try building again
        save_fixed_tests(fixed_code)
        return build_and_debug()
    else:
        # Build succeeded - run tests and get coverage
        run_tests_and_coverage()
        return True