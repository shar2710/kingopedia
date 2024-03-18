CREATE DATABASE kingopedia;
create table kings(
sno int(2) primary key,
ruler varchar(50),
reign varchar(50),
age int(3),
country varchar(50),
wives int(3)
);



insert into kings values(1, 'Alexander the Great', '336 - 323 BCE', 32, 'Greece', 3);
insert into kings values(2, 'Julius Caesar', '49- 44 BCE', 55, 'Rome', 3);
insert into kings values(3, 'Augustus (Octavian Caesar)', '63 BCE - 14 CE', 75, 'Rome', 3);
insert into kings values(4, 'Constantine the Great(Constantine I)', '306 - 337 BCE', 65, 'Rome', 2);
insert into kings values(5, 'Tiberius', '14 AD - 37 AD', 77, 'Rome', 2);
insert into kings values(6, 'Nero', '54 AD - 68 AD', 30, 'Rome', 4);
insert into kings values(7, 'Philip II of Macedon', '359 - 336 BCE', 46, 'Rome', 4);
insert into kings values(8, 'Ptolemy I Soter', '304 - 282 BCE', 84, 'Greece', 3);
insert into kings values(9, 'Archelaus I', '413 - 399 BCE', 39, 'Greece', 1);
insert into kings values(10, 'Demetrius I', '190 - 167 BCE', 55, 'Greece', 1);
insert into kings values(11, 'Amyntas II', '397 - 393 BCE', 43, 'Greece', 1);