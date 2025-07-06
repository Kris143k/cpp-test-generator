def main():
    # Step 1: Generate initial tests
    generate_initial_tests('src', 'tests')
    
    # Step 2: Refine tests
    refine_tests('tests')
    
    # Step 3: Build and handle errors
    if build_and_debug():
        # Step 4: Analyze coverage and improve
        coverage = run_tests_and_coverage()
        send_coverage_for_improvement(coverage)
        
        # Final build check
        if build_and_debug():
            print("Success! Tests generated and passing with good coverage.")
            generate_report(coverage)

if __name__ == "__main__":
    main()