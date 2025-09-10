













# PostgreSQL 
# PostgreSQL is one of the most advanced Relational database management systems (RDBMS). 
# It is open-source software, which means the source code is available under the PostgreSQL license. 

# It supports both relational as well as Non-Relational JSON Queries.


# | Aspect                | **Table** (Practical Term) 🗄️                                            | **Relation** (Theoretical Term) 📘                                                                                     |
# | --------------------- | ------------------------------------------------------------------------| ---------------------------------------------------------------------------------------------------------------------- |
# | Definition            | A physical structure in a database that stores data in rows & columns.  | A mathematical concept in relational theory that represents a set of tuples (rows) with the same attributes (columns). |
# | Usage                 | Used in **SQL & DBMS** (like PostgreSQL, MySQL).                        | Used in **Database Theory** (Relational Model by E.F. Codd).                                                           |
# | Structure             | Rows = Records, Columns = Fields.                                       | Tuples = Rows, Attributes = Columns.                                                                                   |
# | Example (Students)    | A table you create in PostgreSQL:
#                           <br> `CREATE TABLE students(id INT, name VARCHAR(50), age INT);`        | The abstract relation **Student(id, name, age)** which defines the set of all possible rows.                           |
# | Visibility            | You can **see and use** it in pgAdmin/psql.                             | You **can’t see** it physically — it’s a **concept**.                                                                  |
# | Relation Between Data | A table can be linked to other tables using **keys**.                   | A relation can be linked to other relations (mathematically).                                                          |
