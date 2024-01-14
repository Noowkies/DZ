-- SQLite
-- CREATE TABLE Departments (
--     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     NAME TEXT
-- );

-- CREATE TABLE Employee (
--     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     NAME TEXT,
--     DEPARTMENT_ID INTEGER,
--     ROLE TEXT,
--     MANAGER_ID INTEGER,
--     FOREIGN KEY (DEPARTMENT_ID) REFERENCES Departments(ID)
-- );

-- INSERT INTO departments VALUES(1,'managment');
-- INSERT INTO departments VALUES(2,'HRs');
-- INSERT INTO departments VALUES(3,'sales');
-- INSERT INTO departments VALUES(4,'Software Development');
-- INSERT INTO departments VALUES(5,'support');
-- INSERT INTO departments VALUES(6,'RND');

-- INSERT INTO employee(id,name,department_id,role) VALUES(1,'James Smith',1,'CEO');
-- INSERT INTO employee VALUES(2,'Sara Goldman',1,'CFO',1);
-- INSERT INTO employee VALUES(3,'Wayne Albet',1,'CIO',1);
-- INSERT INTO employee VALUES(4,'Michelle Carey',2,'HR manager',1);
-- INSERT INTO employee VALUES(5,'Chris Matthews',3,'sales manager',2);
-- INSERT INTO employee VALUES(6,'Andrew Judy',4,'Development manager',3);
-- INSERT INTO employee VALUES(7,'Daniele McLeon',5,'support manager',3);
-- INSERT INTO employee VALUES(8,'Matthew Swan',2,'HR representative',4);
-- INSERT INTO employee VALUES(9,'Stephanie Richardson',2,'salesperson',5);
-- INSERT INTO employee VALUES(10,'Tony Stark',3,'salesperson',5);
-- INSERT INTO employee VALUES(11,'Jenna Lockett',4,'Front-end Developer',6);
-- INSERT INTO employee VALUES(12,'Michael Dunstall',4,'Back-end Developer',6);
-- INSERT INTO employee VALUES(13,'Jane Voss',4,'Back-End Developer',6);
-- INSERT INTO employee(id, name,role,manager_id) VALUES(14,'Anthony Hird','support',7);
-- INSERT INTO employee VALUES(15,'Natali Rocca',5,'support',7);

-- SELECT Employee.NAME, Employee.ROLE, Departments.NAME
-- FROM Employee LEFT JOIN Departments ON Employee.DEPARTMENT_ID = Departments.ID;

-- SELECT NAME FROM Employee WHERE ID = (
--     SELECT MANAGER_ID FROM Employee WHERE NAME = 'Tony Stark');

-- SELECT Departments.NAME, Employee.NAME
-- FROM Departments OUTER LEFT JOIN Employee ON Departments.ID = Employee.DEPARTMENT_ID;