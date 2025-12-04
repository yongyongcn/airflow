def add(a, b):
    """
    The function we want the PythonOperator to execute.
    In a real-world scenario, this function would contain complex ETL logic, 
    data processing, or API calls.
    """
    result = a + b + 10
    print(f"The result of {a} + {b} is: {result}")
    
    # In Airflow, if you need to pass data to the next task, 
    # you would use the 'return' value for XCom (Cross-Communication).
    return result