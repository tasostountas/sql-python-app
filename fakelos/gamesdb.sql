CREATE TABLE games
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    YEAR INT,
    genre VARCHAR(255),
    creator VARCHAR(255),
    patch VARCHAR(255)
);