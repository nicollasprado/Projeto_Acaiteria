CREATE TABLE IF NOT EXIST users (
    id INT unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(256) NOT NULL,
    password VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXIST products (
    id INT unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category INT unsigned NOT NULL,
    name VARCHAR(100) NOT NULL,
    price INT unsigned NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXIST categories (
    id INT unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

ALTER TABLE products ADD FOREIGN KEY (category) REFERENCES categories(id);

CREATE TABLE IF NOT EXIST purchases (
    id INT unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT
    user_id INT unsigned NOT NULL,
    product_id INT unsigned NOT NULL
);

ALTER TABLE purchases ADD FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE purchases ADD FOREIGN KEY (product_id) REFERENCES products(id);