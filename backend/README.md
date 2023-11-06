### Project Summary:

This project aims to thoroughly test an innovative approach to a possible substitute for database-driven analytics. It involves creating a containerized layer that utilizes *read-only* [Pandas](https://pandas.pydata.org/) dataframes for selected tables in front of the database. The primary purpose of this setup is *to gauge its advantages and disadvantages in real-world scenarios*.

##### Key Objectives:

1. **Performance Evaluation**: One of the primary goals is to rigorously test and measure the performance improvements achieved by using Pandas dataframes for analytics. This includes comparing the time required to generate analytical results against the traditional database-driven approach.

2. **Database Load Reduction Assessment**: Evaluate the extent of the reduction in the database's load. This involves monitoring the number of database queries, assessing their response times, and determining any noticeable enhancements in overall database performance.

3. **Custom Analytics Testing**: Examine the capability to create and execute custom analytical queries, and assess whether this approach allows for more flexible and tailored data analysis, catering to specific user needs.

4. **Data Integrity Analysis**: Ensure that the read-only dataframes maintain data integrity and test for any unexpected side effects on the original database data.

5. **Isolation and Scalability Testing**: Evaluate the ease of managing, updating, and scaling the analytical components within the containerized environment. Determine if this setup provides the desired flexibility and isolation for analytics processes.

6. **Challenges and Limitations**: Test for any disadvantages or challenges associated with this approach, such as data consistency, resource utilization, complexity, scalability, costs, and security considerations.

The project aims to provide empirical evidence to support decisions about whether this approach is suitable for your specific use case. Through a comprehensive testing phase, you will gain a deep understanding of the benefits and drawbacks, enabling informed decisions regarding its adoption and potential optimizations.
