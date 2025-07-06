def send_coverage_for_improvement(coverage):
    with open('instructions/test_refinement.yaml', 'r') as f:
        instructions = f.read()
    
    prompt = f"Analyze this test coverage data:\n\n{coverage}\n\nAnd improve tests to increase coverage. Follow these instructions:\n{instructions}"
    improved_tests = query_llm(prompt)
    save_improved_tests(improved_tests)