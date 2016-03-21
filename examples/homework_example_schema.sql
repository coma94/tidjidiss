-- Target tables
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Grant;

CREATE TABLE Company (
	Id TEXT,
	Name TEXT,
	Symbol TEXT
);

CREATE TABLE Grant(
	Amount INTEGER, 
	Company TEXT
);

-- Source tables
DROP TABLE IF EXISTS NYSE;
DROP TABLE IF EXISTS PublicCompany;
DROP TABLE IF EXISTS PublicGrant;
DROP TABLE IF EXISTS NSFGrantee;
DROP TABLE IF EXISTS NSFGrant;

CREATE TABLE NYSE(
	Name TEXT,
	Symbol TEXT
);

CREATE TABLE PublicCompany(
	Name TEXT, 
	City TEXT
);

CREATE TABLE PublicGrant(
	Amount INTEGER, 
	Investigator TEXT, 
	Company TEXT
);

CREATE TABLE NSFGrantee(
	Id TEXT,
	Name TEXT,
	Symbol TEXT
);

CREATE TABLE NSFGrant(
	Amount INTEGER,
	Company TEXT
);

-- DB prepopulation
INSERT INTO NYSE(Name, Symbol) VALUES ('Google', 'GOOG');
INSERT INTO NYSE(Name, Symbol) VALUES ('Yahoo!', 'YHOO');

INSERT INTO PublicCompany(Name, City) VALUES ('Apple', 'Cup');
INSERT INTO PublicCompany(Name, City) VALUES ('Adobe', 'SJ');

INSERT INTO PublicGrant(Amount, Investigator, Company) 
VALUES (25000, 'Mike B.', 'Apple');
INSERT INTO PublicGrant(Amount, Investigator, Company)
VALUES (50000, 'Anne C.', 'Adobe');

INSERT INTO NSFGrantee(Id, Name, Symbol) VALUES ('23', 'YAHOO', 'YHOO');
INSERT INTO NSFGrantee(Id, Name, Symbol) VALUES ('25', 'ADOBE', 'ADBE');

INSERT INTO NSFGrant(Amount, Company) VALUES ('23', 18000);
INSERT INTO NSFGrant(Amount, Company) VALUES ('25', 50000);

