DROP TABLE IF EXISTS userTable;
CREATE TABLE userTable(
	id BIGINT UNSIGNED,
	username varchar(100) not null,
	email varchar(100) not null,
	pw varchar(256) not null,
	hp INT,
	userRight INT,
	numDonatedItem INT not null,
	numRedeemedItem INT,
	imageURL varchar(1024),
	userRating FLOAT,
	jointDate DATE,
	currentPoints INT,
	PRIMARY KEY (id));

DROP TABLE IF EXISTS categoryList;
CREATE TABLE categoryList(
	id BIGINT UNSIGNED,
	name varchar(1024),
	description text,
	PRIMARY KEY (id));

DROP TABLE IF EXISTS donatedList;
CREATE TABLE donatedList(
	id BIGINT UNSIGNED PRIMARY KEY,
	donatedUserID BIGINT unsigned,
	categoryID BIGINT unsigned,
	itemName varchar(1024),
	description text,
	imageURL varchar(1024),
	equivalentPoints INT, status varchar(3),
	donateDate timeStamp,
	FOREIGN KEY (donatedUserID) REFERENCES userTable(id),
	FOREIGN KEY (categoryID) REFERENCES categoryList(id));

DROP TABLE IF EXISTS inProgressList;
CREATE TABLE inProgressList(
    id BIGINT PRIMARY KEY,
    userID BIGINT unsigned not null,
    itemID BIGINT unsigned not null,
    itemStatus varchar(3) not null,
	FOREIGN KEY (userID) REFERENCES userTable(id),
	FOREIGN KEY (itemID) REFERENCES donatedList(id));

DROP TABLE IF EXISTS transactionList;
CREATE TABLE transactionList(
    id BIGINT PRIMARY KEY,
    itemID BIGINT unsigned not null,
    postedUserID BIGINT unsigned not null,
	purchasedUserID BIGINT unsigned not null,
    ptsSpent int not null,
	FOREIGN KEY (itemID) REFERENCES donatedList(id),
	FOREIGN KEY (postedUserID) REFERENCES userTable(id),
    FOREIGN KEY (purchasedUserID) REFERENCES userTable(id));