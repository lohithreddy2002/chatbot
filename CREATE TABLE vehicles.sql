CREATE TABLE vehicles(
   ID INT PRIMARY KEY,
   type           TEXT    NOT NULL,
   licence_plate   CHAR(50)   NOT NULL,
   color        CHAR(50)
);

DROP TABLE vehicles

INSERT INTO vehicles(ID,type,licence_plate,color)
VALUES (1,"bike","KA19EQ1316","black"),(2,"car","TN37EF4902","white"),
    (3,"truck","MP15NC9738","blue"),(5,"bike","HR26DQ5551","green"),
    (4,"car","KL35JE1626","yellow"),(6,"truck","UP67AA3601","grey");


CREATE TABLE test1(
ID Int,
entry Date;
)

DROP TABLE vehicle_entries

CREATE TABLE vehicle_entries(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   entry_time DATETIME  NOT NULL,
   exit_time DATETIME  NOT NULL,
   number_plate VARCHAR(20) NOT NULL,
   vehicle_type VARCHAR(10) NOT NULL,
   vehicle_color VARCHAR(20) NOT NULL,
   parked_level INT
);


INSERT INTO GATES (id, name) VALUES
    (1, 'Entrance 1'),
    (2, 'Entrance 2'),
    (3, 'Exit 1'),
    (4, 'Exit 2');



SELECT DATABASE test

DROP TABLE vehicle_entries

INSERT INTO vehicle_entries(entry_time,exit_time,vehicle_type,number_plate, vehicle_color,parked_level)
VALUES ('2023-04-14 07:05:26.544444','2023-09-10 07:05:52.379154',"bike","KA19EQ1316","black",1),
('2023-05-11 05:33:29.201179','2023-05-13 05:21:50.770382',"car","TN37EF4902","white" ,2),
('2023-05-13 00:38:59.942387','2023-05-14 17:14:40.138048',"bike","HR26DQ5551","green",2),
('2023-05-12 10:11:18.499962','2023-05-13 13:42:55.371987',"truck","UP67AA3601","grey",1),
('2023-05-11 12:33:58.458641','2023-05-12 14:07:20.224968',"truck","MP15NC9738","blue",3),
('2023-05-12 11:43:48.174757','2023-05-11 20:22:04.026222',"bike","HR26DQ5551","green",4),
('2023-05-10 19:15:42.751271','2023-05-14 03:10:44.719043',"car","TN37EF4902","white" ,4),
('2023-05-11 02:17:52.354760','2023-05-13 02:38:21.599464',"bike","HR26DQ5551","green",3),
('2023-05-12 14:46:19.159885','2023-05-11 03:48:22.101270',"truck","UP67AA3601","grey",1),
('2023-05-10 14:48:25.566428','2023-05-14 09:26:25.125642',"truck","MP15NC9738","blue",2),
('2023-05-12 09:20:30.071038','2023-05-10 03:29:29.629166',"car","TN37EF4902","white" ,3),
('2023-05-14 09:13:46.029864','2023-05-10 20:03:24.438290',"bike","KA19EQ1316","black",4),
('2023-05-12 00:53:58.217145','2023-05-11 11:47:15.811852',"bike","HR26DQ5551","green",4),
('2023-05-14 17:28:15.340677','2023-05-12 18:20:35.333001',"car","TN37EF4902","white" ,1),
('2023-05-13 17:22:18.551320','2023-05-14 11:18:47.052495',"bike","HR26DQ5551","green",3);

DROP TABLE entries

#test1
CREATE TABLE VEHICLES (
    id INTEGER PRIMARY KEY,
    plate_number VARCHAR(20) NOT NULL,
    type VARCHAR(10) NOT NULL,
    color VARCHAR(20) NOT NULL
);

CREATE TABLE GATES (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE ENTRIES (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL,
    gate_id INTEGER NOT NULL,
    entry_datetime DATETIME NOT NULL,
    FOREIGN KEY(vehicle_id) REFERENCES VEHICLES(id),
    FOREIGN KEY(gate_id) REFERENCES GATES(id)
);

CREATE TABLE EXITS (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL,
    gate_id INTEGER NOT NULL,
    exit_datetime DATETIME NOT NULL,
    FOREIGN KEY(vehicle_id) REFERENCES VEHICLES(id),
    FOREIGN KEY(gate_id) REFERENCES GATES(id)
);


INSERT INTO VEHICLES (id, plate_number, type, color) VALUES 
    (1, 'ABC-123', 'Car', 'Red'),
    (2, 'XYZ-456', 'Bike', 'Blue'),
    (3, 'LMN-789', 'Truck', 'Green');

INSERT INTO GATES (id, name) VALUES
    (1, 'Entrance 1'),
    (2, 'Entrance 2'),
    (3, 'Exit 1'),
    (4, 'Exit 2');

INSERT INTO ENTRIES (id, vehicle_id, gate_id, entry_datetime) VALUES
    (1, 1, 1, '2023-05-05 10:00:00'),
    (2, 2, 2, '2023-05-05 10:15:00'),
    (3, 3, 1, '2023-05-05 10:30:00'),
    (4, 1, 2, '2023-05-05 11:00:00'),
    (5, 2, 1, '2023-05-05 11:30:00');

INSERT INTO EXITS (id, vehicle_id, gate_id, exit_datetime) VALUES
    (1, 1, 3, '2023-05-05 12:00:00'),
    (2, 2, 4, '2023-05-05 12:15:00'),
    (3, 3, 3, '2023-05-05 12:30:00'),
    (4, 1, 4, '2023-05-05 13:00:00'),
    (5, 2, 3, '2023-05-05 13:30:00');



"
VEHICLES
- id (int, primary key)
- plate_number (varchar)
- type (varchar)
- color (varchar)

GATES
- id (int, primary key)
- name (varchar)

ENTRIES
- id (int, primary key)
- vehicle_id (int, foreign key to VEHICLES.id)
- gate_id (int, foreign key to GATES.id)
- entry_datetime (datetime)

EXITS
- id (int, primary key)
- vehicle_id (int, foreign key to VEHICLES.id)
- gate_id (int, foreign key to GATES.id)
- exit_datetime (datetime)
"