-- Task 3
CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    sex CHAR(1),
    age INT,
    phone VARCHAR(15)
);

INSERT INTO user (id, name, sex, age, phone) VALUES
(1, '张三', 'M', 25, '1234567890'),
(2, '李四', 'F', 22, '0987654321'),
(3, '王五', 'M', 35, '1122334455');

-- Task 4
SELECT * FROM user WHERE age BETWEEN 20 AND 30;

-- Task 5
DELETE FROM user WHERE name LIKE '%张%';

-- Task 6
SELECT AVG(age) AS average_age FROM user;

-- Task 7
SELECT * FROM user WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%' ORDER BY age DESC;

-- Task 8
CREATE TABLE team (
    id INT PRIMARY KEY,
    teamName VARCHAR(50)
);

CREATE TABLE score (
    id INT PRIMARY KEY,
    teamid INT,
    userid INT,
    score INT,
    FOREIGN KEY (teamid) REFERENCES team(id),
    FOREIGN KEY (userid) REFERENCES user(id)
);

-- Task 9
SELECT u.* FROM user u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;

-- Task 10
SELECT COALESCE(SUM(s.score), 0) AS total_score FROM score s
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU';
