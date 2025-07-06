def run_tests_and_coverage():
    # Run tests
    subprocess.run(['./test_runner'], check=True)
    
    # Generate coverage data
    subprocess.run(['lcov', '--capture', '--directory', '.', '--output-file', 'coverage.info'])
    subprocess.run(['genhtml', 'coverage.info', '--output-directory', 'coverage_report'])
    
    # Parse coverage for LLM feedback
    coverage = parse_coverage('coverage.info')
    return coverage