## Database
1. [ruan yi feng Tutorial](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
2. sudo su - postgres
3. psql
4. ¥d *(to check what tables you have)*
5. create table: Student information
    ```sql
    CREATE TABLE student_information(
    id INT PRIMARY KEY     NOT NULL,
    name           TEXT    NOT NULL,
    vector         TEXT     NOT NULL,
    image_address        CHAR(50)
    );
    ```
    change vector into string
6. create table: passing record
    ```sql
    CREATE TABLE passing_record(
    id INT PRIMARY KEY      NOT NULL,
    datetime       varchar(40) DEFAULT (now()),
    image_address  CHAR(50),
    cemeraID       CHAR(50) NOT NULL,
    inORout        CHAR(10)
    ); 
    ```
7. insert some information to test
8. find the fast way to compare one vector with the whole vectors in database
9. consider develop a app or website

