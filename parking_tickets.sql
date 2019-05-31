
USE parking_db;
DROP TABLE parking_tickets;
CREATE TABLE parking_tickets(
	id INT PRIMARY KEY,
    date_of_infraction  INT,
    infraction_code INT,
    infraction_description VARCHAR(1000),
    set_fine_amount FLOAT,
    time_of_infraction INT
    location2 VARCHAR(100)
    );
SELECT*FROM parking_tickets;




