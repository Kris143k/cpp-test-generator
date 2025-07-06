# report_generator.py
def generate_report(coverage_data):
    report = f"""
    Unit Test Generation Report
    ==========================
    
    Test Coverage Summary:
    - Line Coverage: {coverage_data['line_coverage']}%
    - Function Coverage: {coverage_data['function_coverage']}%
    - Branch Coverage: {coverage_data['branch_coverage']}%
    
    Generated Tests:
    - Total test files: {len(os.listdir('tests'))}
    - Total test cases: {count_test_cases()}
    
    Build Status:
    - Final build: {'Successful' if check_build() else 'Failed'}
    """
    
    with open('test_report.txt', 'w') as f:
        f.write(report)