
## What is DBMS?


Database Management System (DBMS) is software for storing and retrieving users’ data while considering appropriate security measures. It consists of a group of programs that manipulate the database. The DBMS accepts the request for data from an application and instructs the operating system to provide the specific data. In large systems, a DBMS helps users and other third-party software store and retrieve data.

DBMS allows users to create their own databases as per their requirements. The term “DBMS” includes the user of the database and other application programs. It provides an interface between the data and the software application. 

---

- DBMS definition: A database is a collection of related data which represents some aspect of the real world.
- The full form of DBMS is Database Management System. DBMS stands for Database Management System. It is software for storing and retrieving users’ data by considering appropriate security measures.
- DBMS Provides security and removes redundancy
- DBMS has many advantages over traditional Flat File management system
- Some Characteristics of DBMS are Security, Self-describing nature, Insulation between programs and data abstraction, Support of multiple views of the data, etc.
- End-Users, Application Programmers, and Database Administrators are the type of users who access a DBMS
- DBMS is widely used in Banking, Airlines, Telecommunication, Finance, and other industries
- The four main DBMS types are 1) Hierarchical, 2) Network, 3) Relational, 4) Object-Oriented DBMS.
- DBMS serves as an efficient handler to balance the needs of multiple applications using the same data
- The cost of Hardware and Software of a DBMS is quite high, which increases the budget of your organization.

---

**Relational Model Concepts in DBMS**

- Attribute: Each column in a Table. Attributes are the properties which define a relation. e.g., Student_Rollno, NAME,etc.
- Tables – In the Relational model the, relations are saved in the table format. It is stored along with its entities. A table has two properties rows and columns. Rows represent records and columns represent attributes.
- Tuple – It is nothing but a single row of a table, which contains a single record.
- Relation Schema: A relation schema represents the name of the relation with its attributes.
- Degree: The total number of attributes which in the relation is called the degree of the relation.
- Cardinality: Total number of rows present in the Table.
- Column: The column represents the set of values for a specific attribute.
- Relation instance – Relation instance is a finite set of tuples in the RDBMS system. Relation instances never have duplicate tuples.
- Relation key – Every row has one, two or multiple attributes, which is called relation key.
- Attribute domain – Every attribute has some pre-defined value and scope which is known as attribute domain.

---

## Keys in SQL

- Super Key – A super key is a group of single or multiple keys which identifies rows in a table.
- Primary Key – is a column or group of columns in a table that uniquely identify every row in that table.
- Candidate Key – is a set of attributes that uniquely identify tuples in a table. Candidate Key is a super key with no repeated attributes.
- Alternate Key – is a column or group of columns in a table that uniquely identify every row in that table.
- Foreign Key – is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain data integrity and allow navigation between two different instances of an entity.
- Compound Key – has two or more attributes that allow you to uniquely recognize a specific record. It is possible that each column may not be unique by itself within the database.
- Composite Key – is a combination of two or more columns that uniquely identify rows in a table. The combination of columns guarantees uniqueness, though individual uniqueness is not guaranteed.

---

![Ref_link](https://www.guru99.com/dbms-keys.html)

**ER MODEL**

 ![Ref](https://gdevtest.geeksforgeeks.org/introduction-of-er-model/)
 (https://www.geeksforgeeks.org/generalization-specialization-and-aggregation-in-er-model/)
 ![Integrity constraints](https://www.javatpoint.com/dbms-integrity-constraints)

 ---

 **ACID**

 
ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee the reliability and integrity of transactions in a database system. Let's explore each of these properties:

*Atomicity*: Atomicity ensures that a transaction is treated as a single, indivisible unit of work. It means that either all the operations within a transaction are successfully completed, or none of them are. If any part of a transaction fails, the entire transaction is rolled back, and the database is left unchanged. Atomicity helps maintain data consistency and prevents partial updates that could lead to data inconsistencies.

*Consistency*: Consistency ensures that a transaction brings the database from one valid state to another valid state. It enforces integrity constraints and rules defined for the database. The database must be in a consistent state both before and after the execution of a transaction. If a transaction violates any integrity constraints, it is rolled back, and the database remains unchanged.

*Isolation*: Isolation ensures that concurrent transactions do not interfere with each other. Each transaction should appear as if it is executed in isolation, regardless of the presence of other concurrent transactions. Isolation prevents concurrency-related issues such as dirty reads, non-repeatable reads, and phantom reads. It ensures that the concurrent execution of transactions does not lead to data inconsistencies.

*Durability*: Durability guarantees that once a transaction is committed, its effects are permanent and survive any subsequent failures, such as system crashes or power outages. The committed data is stored in a durable storage medium (such as disk) and can be recovered in case of failures. Durability ensures that the data remains consistent and intact even in the face of system failures.

---

**Normalization**

Normalization is a process in database design that helps organize data into well-structured and efficient relational database tables. It involves breaking down a database schema into smaller, more manageable parts, while reducing redundancy and improving data integrity. The objective of normalization is to eliminate data anomalies and maintain data consistency.

The process of normalization typically follows a set of rules or normal forms, which are guidelines for structuring the database tables. The most commonly used normal forms are:

`First Normal Form (1NF)`: In 1NF, data is organized into tables where each column contains atomic values (indivisible values). There should be no repeating groups or arrays within a table. Each table should have a primary key to uniquely identify each row.

`Second Normal Form (2NF)`: In 2NF, a table is in 1NF, and all non-key attributes (columns) are fully dependent on the entire primary key. If any attribute depends on only a portion of the primary key, it should be moved to a separate table with a foreign key relationship.

`Third Normal Form (3NF)`: In 3NF, a table is in 2NF, and no non-key attribute depends on another non-key attribute. If such dependencies exist, the dependent attribute should be moved to a separate table.

`Boyce-Codd Normal Form (BCNF)`: BCNF is an extension of 3NF that further refines the concept of functional dependencies. It states that every determinant (the attribute that determines another attribute's value) in a table must be a candidate key. In other words, there should be no non-trivial dependencies of non-prime attributes on any candidate key. BCNF eliminates certain types of anomalies and ensures that a table is free from redundancy based on functional dependencies.

`Fourth Normal Form (4NF)`: 4NF addresses multi-valued dependencies that can occur when a table has multiple independent multi-valued attributes. It requires that a table be in BCNF and that there are no non-trivial multi-valued dependencies between non-key attributes. To resolve such dependencies, the table may need to be split into multiple tables, each containing a single multi-valued attribute.

`Fifth Normal Form (5NF) or Project-Join Normal Form (PJNF)`: 5NF deals with join dependencies and is also known as PJNF. It aims to eliminate redundancy and anomalies caused by join operations. It requires that a table be in 4NF and that all join dependencies are logically implied by the candidate keys. Join dependencies occur when information from multiple tables is combined into a single table. 5NF helps ensure that the database schema is free from redundancies caused by these join operations.

---

