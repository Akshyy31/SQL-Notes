# What are SQL Clauses?

# A clause is a part of an SQL statement that tells the database what to do with the data.


# | Clause       | Purpose                            | Example                                                                             |
# | ------------ | ---------------------------------- | ----------------------------------------------------------------------------------- |
# | **SELECT**   | Choose columns to show             | `SELECT name, email FROM students;`                                                 |
# | **FROM**     | Choose table to get data from      | `SELECT * FROM students;`                                                           |
# | **WHERE**    | Filter rows based on condition     | `SELECT * FROM students WHERE student_id = 1;`                                      |
# | **ORDER BY** | Sort rows (ASC/DESC)               | `SELECT * FROM students ORDER BY name ASC;`                                         |
# | **GROUP BY** | Group rows for aggregation         | `SELECT student_id, COUNT(*) FROM courses GROUP BY student_id;`                     |
# | **HAVING**   | Filter groups (used with GROUP BY) | `SELECT student_id, COUNT(*) FROM courses GROUP BY student_id HAVING COUNT(*) > 1;` |
# | **LIMIT**    | Limit number of rows               | `SELECT * FROM students LIMIT 2;`                                                   |
# | **OFFSET**   | Skip rows before returning results | `SELECT * FROM students OFFSET 2;`                                                  |
# | **DISTINCT** | Remove duplicates                  | `SELECT DISTINCT course_name FROM courses;`                                         |
