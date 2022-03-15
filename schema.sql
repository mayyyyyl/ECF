CREATE DATABASE IF NOT EXISTS hotel_complex CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hotel_complex;

/* Création des tables*/
CREATE TABLE admin(
    id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
)
ENGINE=InnoDB;

CREATE TABLE hotel(
    id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    description VARCHAR(250) NOT NULL
)
ENGINE=InnoDB;

CREATE TABLE gerant(
    id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    id_hotel INT(100) NOT NULL,
    FOREIGN KEY (id_hotel) REFERENCES hotel(id) ON DELETE CASCADE
)
ENGINE=InnoDB;

CREATE TABLE suite(
    id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    titre VARCHAR(50) NOT NULL,
    img BLOB NOT NULL,
    description VARCHAR(250) NOT NULL,
    price FLOAT(4,2) NOT NULL,
    link VARCHAR(500) NOT NULL,
    id_hotel INT(100) NOT NULL,
    FOREIGN KEY (id_hotel) REFERENCES hotel(id) ON DELETE CASCADE
)
ENGINE=InnoDB;

CREATE TABLE client(
    id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
)
ENGINE=InnoDB;

-- CREATE TABLE reservation(
--     id INT(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
--     id_suite INT(100) NOT NULL,
--     FOREIGN KEY (id_suite) REFERENCES suite(id) ON DELETE CASCADE,
--     id_client INT(100) NOT NULL,
--     FOREIGN KEY (id_client) REFERENCES client(id) ON DELETE CASCADE,
--     date_beginning DATETIME NOT NULL,
--     date_end DATETIME NOT NULL
-- )
-- ENGINE=InnoDB;

CREATE TABLE reservation(
    id INT(100) PRIMARY KEY NOT NULL,
    date_beginning DATETIME NOT NULL,
    date_end DATETIME NOT NULL,
    id_suite INT(100) NOT NULL,
    id_client INT(100) NOT NULL,
    FOREIGN KEY (id_suite) REFERENCES suite(id) ON DELETE CASCADE,
    FOREIGN KEY (id_client) REFERENCES client(id) ON DELETE CASCADE
)

/* Peupler les tables */

insert into admin (id, password, email) values (1, '29HahWo5YVf', 'maylislb@hotmail.fr');

insert into hotel (id, name, address, city, description) values (1, 'Four Seasons', '3751 Waubesa Terrace', 'Rzeszów', 'ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin');
insert into hotel (id, name, address, city, description) values (2, 'Couples Resorts', '65533 Eagan Alley', 'Choroszcz', 'in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque');
insert into hotel (id, name, address, city, description) values (3, 'Ritz-Carlton', '0520 Dahle Alley', 'Changhua', 'amet erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non');
insert into hotel (id, name, address, city, description) values (4, 'Mandarin Oriental', '2 Talisman Junction', 'Louguan', 'venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet');
insert into hotel (id, name, address, city, description) values (5, 'Capital Hotel', '7483 Hanson Street', 'Landim', 'magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in');
insert into hotel (id, name, address, city, description) values (6, 'Best Western', '39847 Dexter Circle', 'Guamal', 'curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi');
insert into hotel (id, name, address, city, description) values (7, 'Hilton', '79079 Morning Way', 'Alegre', 'rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse');

insert into gerant (id, lastname, firstname, email, password, id_hotel) values (1, 'McAvey', 'Östen', 'nmcavey0@free.fr', 'VWZP2kvx', 1);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (2, 'Brindley', 'Clémentine', 'ibrindley1@tripadvisor.com', 'wXFLfu16AsR', 2);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (3, 'Webbe', 'Irène', 'lwebbe2@state.tx.us', '8sQZqY', 3);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (4, 'Cowperthwaite', 'Angèle', 'pcowperthwaite3@independent.co.uk', 'FBPMdrVA', 4);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (5, 'Curtis', 'Zhì', 'ccurtis4@soundcloud.com', 'XOdT50hN', 5);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (6, 'Daye', 'Mélys', 'bdaye5@jimdo.com', '5IXORQq', 6);
insert into gerant (id, lastname, firstname, email, password, id_hotel) values (7, 'Gladdolph', 'Anaëlle', 'bgladdolph6@bing.com', 'b77qT676', 7);

insert into suite (id, titre, img, description, price, link, id_hotel) values (1, 'Toys', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum', 396, 'https://www.booking.com/hotel/fr/holiday-home-bucolique.fr.html?aid=390156;label=duc511jc-1DCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBA-gBAYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgTgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dist=0&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&', 1);
insert into suite (id, titre, img, description, price, link, id_hotel) values (2, 'Dead & Breakfast', 'http://dummyimage.com/334x300.png/dddddd/ffffff', 'leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in felis', 340, 'https://www.booking.com/hotel/fr/villa-orkagna.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dest_id=-1457576;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=2;hpos=2;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647287587;srpvid=5f0d8bd1c5c00009;type=total;ucfs=1&#hotelTmpl', 1);
insert into suite (id, titre, img, description, price, link, id_hotel) values (3, 'Private Eyes', 'http://dummyimage.com/334x300.png/dddddd/ffffff', 'volutpat in congue etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate elementum nullam', 368, 'https://www.booking.com/hotel/fr/roz-de-mer.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 2);
insert into suite (id, titre, img, description, price, link, id_hotel) values (4, 'Don''t Think About It', 'http://dummyimage.com/334x300.png/dddddd/000000', 'condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque', 266, 'https://www.booking.com/hotel/fr/villa-belle-epoque-xixe-vue-mer.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 5);
insert into suite (id, titre, img, description, price, link, id_hotel) values (5, 'Captain Abu Raed', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur at ipsum ac tellus semper interdum', 354, 'https://www.booking.com/hotel/ch/montreux-lake-view-apartments-and-spa.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 2);
insert into suite (id, titre, img, description, price, link, id_hotel) values (6, 'Late Phases', 'http://dummyimage.com/334x300.png/dddddd/000000', 'rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede', 144, 'https://www.booking.com/hotel/fr/gite-les-bravigou-2-4-pers-plage-1km-tregunc-finistere-sud.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 6);
insert into suite (id, titre, img, description, price, link, id_hotel) values (7, 'Jamaica Inn', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel', 254, 'https://www.booking.com/hotel/fr/la-marionnette-du-plateau.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 7);
insert into suite (id, titre, img, description, price, link, id_hotel) values (8, 'J. Gang Meets Dynamite Harry', 'http://dummyimage.com/334x300.png/dddddd/000000', 'sit amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis', 357, 'https://www.booking.com/hotel/fr/maison-au-coeur-de-lyon-avec-jardin-terrasse-patio.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 3);
insert into suite (id, titre, img, description, price, link, id_hotel) values (9, 'Dungeons & Dragons', 'http://dummyimage.com/334x300.png/dddddd/000000', 'hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem', 491, 'https://www.booking.com/hotel/us/5-star-luxury-villa-in-windsor-hills-a-gated-villa-community.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748;dest_id=20023488;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;nflt=sth%3D20;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647334745;srpvid=90313f2c0d0e02a0;type=total;ucfs=1&#hotelTmpl', 4);

-- insert into suite (id, titre, img, description, price, link, id_hotel) values (10, 'Town', 'http://dummyimage.com/388x342.png/5fa2dd/ffffff', 'pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate elementum nullam varius nulla facilisi', 445, 'http://bing.com/amet/lobortis/sapien/sapien/non.html?scelerisque=vel&mauris=dapibus&sit=at&amet=diam&eros=nam&suspendisse=tristique&accumsan=tortor&tortor=eu&quis=pede', 1);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (11, 'Godzilla vs. Mechagodzilla II', 'http://dummyimage.com/103x281.png/dddddd/000000', 'hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat', 376, 'https://miibeian.gov.cn/velit/nec/nisi/vulputate/nonummy/maecenas/tincidunt.jpg?vitae=commodo&ipsum=placerat&aliquam=praesent&non=blandit&mauris=nam&morbi=nulla&non=integer&lectus=pede&aliquam=justo&sit=lacinia&amet=eget&diam=tincidunt&in=eget&magna=tempus&bibendum=vel&imperdiet=pede&nullam=morbi&orci=porttitor&pede=lorem&venenatis=id&non=ligula&sodales=suspendisse&sed=ornare&tincidunt=consequat&eu=lectus&felis=in&fusce=est&posuere=risus&felis=auctor&sed=sed&lacus=tristique&morbi=in&sem=tempus&mauris=sit&laoreet=amet&ut=sem&rhoncus=fusce&aliquet=consequat&pulvinar=nulla&sed=nisl&nisl=nunc&nunc=nisl&rhoncus=duis&dui=bibendum&vel=felis', 5);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (12, 'Nightmares in Red White & Blue', 'http://dummyimage.com/302x216.png/cc0000/ffffff', 'duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor', 301, 'http://hostgator.com/consequat/varius/integer/ac/leo/pellentesque.xml?leo=odio&maecenas=porttitor&pulvinar=id&lobortis=consequat&est=in&phasellus=consequat&sit=ut&amet=nulla&erat=sed&nulla=accumsan&tempus=felis&vivamus=ut&in=at&felis=dolor&eu=quis&sapien=odio&cursus=consequat&vestibulum=varius', 6);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (13, 'Joan of Arc', 'http://dummyimage.com/140x105.png/5fa2dd/ffffff', 'vel est donec odio justo sollicitudin ut suscipit a feugiat et eros vestibulum ac est lacinia', 199, 'http://dmoz.org/nam.xml?platea=pellentesque', 5);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (14, 'Madagascar Skin', 'http://dummyimage.com/158x223.png/ff4444/ffffff', 'in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent', 144, 'https://opensource.org/odio/elementum/eu/interdum/eu/tincidunt/in.jsp?quis=et&justo=ultrices&maecenas=posuere&rhoncus=cubilia&aliquam=curae&lacus=duis&morbi=faucibus&quis=accumsan&tortor=odio&id=curabitur&nulla=convallis&ultrices=duis&aliquet=consequat&maecenas=dui&leo=nec&odio=nisi&condimentum=volutpat&id=eleifend&luctus=donec&nec=ut&molestie=dolor&sed=morbi&justo=vel&pellentesque=lectus&viverra=in&pede=quam&ac=fringilla&diam=rhoncus&cras=mauris&pellentesque=enim&volutpat=leo&dui=rhoncus&maecenas=sed&tristique=vestibulum&est=sit&et=amet&tempus=cursus&semper=id&est=turpis&quam=integer&pharetra=aliquet&magna=massa&ac=id&consequat=lobortis&metus=convallis&sapien=tortor&ut=risus&nunc=dapibus&vestibulum=augue&ante=vel&ipsum=accumsan&primis=tellus&in=nisi', 4);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (15, 'Karate Kid, Part II', 'http://dummyimage.com/198x387.png/ff4444/ffffff', 'morbi a ipsum integer a nibh in quis justo maecenas rhoncus aliquam lacus morbi quis tortor id nulla ultrices aliquet maecenas leo odio condimentum id luctus nec molestie sed', 61, 'https://macromedia.com/eu/sapien.html?dolor=mus&morbi=etiam&vel=vel&lectus=augue&in=vestibulum&quam=rutrum&fringilla=rutrum&rhoncus=neque&mauris=aenean&enim=auctor&leo=gravida&rhoncus=sem&sed=praesent&vestibulum=id&sit=massa&amet=id&cursus=nisl&id=venenatis&turpis=lacinia&integer=aenean&aliquet=sit&massa=amet&id=justo&lobortis=morbi&convallis=ut&tortor=odio&risus=cras&dapibus=mi&augue=pede&vel=malesuada&accumsan=in&tellus=imperdiet&nisi=et', 7);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (16, 'Exploits of a Hollywood Rebel', 'http://dummyimage.com/339x385.png/5fa2dd/ffffff', 'primis in faucibus orci luctus et ultrices posuere cubilia curae', 106, 'https://wisc.edu/massa.png?duis=dignissim&aliquam=vestibulum&convallis=vestibulum&nunc=ante&proin=ipsum&at=primis&turpis=in&a=faucibus&pede=orci&posuere=luctus&nonummy=et&integer=ultrices&non=posuere&velit=cubilia&donec=curae&diam=nulla&neque=dapibus&vestibulum=dolor&eget=vel&vulputate=est&ut=donec&ultrices=odio&vel=justo&augue=sollicitudin&vestibulum=ut&ante=suscipit&ipsum=a&primis=feugiat&in=et&faucibus=eros&orci=vestibulum&luctus=ac&et=est&ultrices=lacinia&posuere=nisi&cubilia=venenatis&curae=tristique&donec=fusce&pharetra=congue&magna=diam&vestibulum=id&aliquet=ornare&ultrices=imperdiet&erat=sapien&tortor=urna&sollicitudin=pretium', 6);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (17, 'Torment', 'http://dummyimage.com/151x275.png/5fa2dd/ffffff', 'euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem', 376, 'http://noaa.gov/volutpat.aspx?pulvinar=in&lobortis=hac&est=habitasse&phasellus=platea&sit=dictumst&amet=etiam&erat=faucibus&nulla=cursus&tempus=urna&vivamus=ut&in=tellus&felis=nulla&eu=ut&sapien=erat&cursus=id&vestibulum=mauris&proin=vulputate&eu=elementum&mi=nullam&nulla=varius&ac=nulla&enim=facilisi&in=cras&tempor=non&turpis=velit&nec=nec&euismod=nisi&scelerisque=vulputate&quam=nonummy&turpis=maecenas&adipiscing=tincidunt&lorem=lacus&vitae=at&mattis=velit&nibh=vivamus&ligula=vel&nec=nulla&sem=eget&duis=eros&aliquam=elementum&convallis=pellentesque&nunc=quisque&proin=porta&at=volutpat&turpis=erat&a=quisque&pede=erat&posuere=eros&nonummy=viverra&integer=eget&non=congue', 7);
-- insert into suite (id, titre, img, description, price, link, id_hotel) values (18, 'Trees Lounge', 'http://dummyimage.com/370x106.png/dddddd/000000', 'neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum', 141, 'https://joomla.org/amet/justo.html?erat=ullamcorper&curabitur=augue&gravida=a&nisi=suscipit&at=nulla&nibh=elit&in=ac&hac=nulla&habitasse=sed&platea=vel&dictumst=enim&aliquam=sit&augue=amet&quam=nunc&sollicitudin=viverra&vitae=dapibus&consectetuer=nulla&eget=suscipit&rutrum=ligula&at=in&lorem=lacus', 7);

insert into client (id, lastname, firstname, email, password) values (1, 'Verring', 'Anaé', 'lverring0@wunderground.com', 'jUc03nI6r');
insert into client (id, lastname, firstname, email, password) values (2, 'Hinkins', 'Naëlle', 'jhinkins1@unicef.org', 'gJvvkGuc5HMY');
insert into client (id, lastname, firstname, email, password) values (3, 'Zute', 'Méthode', 'nzute2@fc2.com', 'PvIQKgCD');
insert into client (id, lastname, firstname, email, password) values (4, 'Nisuis', 'Maïlis', 'lnisuis3@marketwatch.com', 'MUTMI9soP');
insert into client (id, lastname, firstname, email, password) values (5, 'Stiell', 'Aurélie', 'lstiell4@cnet.com', 'w7Wb1Q');

insert into reservation (id, id_client, id_suite, date_beginning, date_end) values (1, 1, 9, '2021-03-30 10:22:16', '2022-02-06 22:29:50');
insert into reservation (id, id_client, id_suite, date_beginning, date_end) values (2, 2, 3, '2021-06-03 13:18:31', '2021-10-23 16:31:10');
insert into reservation (id, id_client, id_suite, date_beginning, date_end) values (3, 3, 8, '2021-08-28 14:19:20', '2022-02-14 00:58:18');
insert into reservation (id, id_client, id_suite, date_beginning, date_end) values (4, 4, 4, '2021-10-30 21:57:51', '2021-09-19 07:45:05');
insert into reservation (id, id_client, id_suite, date_beginning, date_end) values (5, 5, 1, '2021-11-15 11:28:06', '2021-10-10 21:21:01');