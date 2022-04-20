CREATE DATABASE IF NOT EXISTS hotel CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hotel;

/* Creation des tables */

CREATE TABLE user (
    id        INTEGER NOT NULL PRIMARY KEY,
    lastname  VARCHAR (255) NOT NULL,
    firstname VARCHAR (255) NOT NULL,
    email     VARCHAR (255) NOT NULL,
    password  VARCHAR (255) NOT NULL,
    updated   DATETIME NOT NULL,
    is_admin  INTEGER NOT NULL
)
ENGINE=InnoDB;

CREATE TABLE hotel (
    id          INTEGER NOT NULL PRIMARY KEY,
    name        VARCHAR (255) NOT NULL,
    address     VARCHAR (255) NOT NULL,
    city        VARCHAR (255) NOT NULL,
    description VARCHAR (255) NOT NULL
)
ENGINE=InnoDB;

CREATE TABLE gerant (
    id       INTEGER NOT NULL PRIMARY KEY,
    user_id  INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id) REFERENCES hotel (id) ON DELETE CASCADE
)
ENGINE=InnoDB;

CREATE TABLE suite (
    id          INTEGER NOT NULL PRIMARY KEY,
    titre       VARCHAR (255) NOT NULL,
    img         VARCHAR (255) NOT NULL,
    description VARCHAR (255) NOT NULL,
    price       DECIMAL NOT NULL,
    link        VARCHAR (255) NOT NULL,
    hotel_id    INTEGER NOT NULL,
    updated     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hotel_id) REFERENCES hotel (id) ON DELETE CASCADE
)
ENGINE=InnoDB;

CREATE TABLE reservation (
    id            INTEGER  NOT NULL PRIMARY KEY,
    suite_id      INTEGER  NOT NULL,
    customer_id   INTEGER  NOT NULL,
    datebeginning DATETIME NOT NULL,
    dateend       DATETIME NOT NULL,
    updated       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (suite_id) REFERENCES suite (id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES user (id) ON DELETE CASCADE
)
ENGINE=InnoDB;

/* Peupler les tables */

insert into user (id, lastname, firstname, email, is_admin, password, updated) values (1, 'Le Borgne', 'Maylis', 'maylislb@hotmail.fr', true, 'f4516ed3c7295e4f512ea9f8e073fd33db592de4', '2021-10-26 12:20:04');
insert into user (id, lastname, firstname, email, is_admin, password, updated) values (2, 'Durand', 'Jean', 'jean@email.fr', false, 'f4516ed3c7295e4f512ee9f8e073fd33db592de4', '2021-11-09 13:28:37');
insert into user (id, lastname, firstname, email, is_admin, password, updated) values (3, 'Couroy', 'Paul', 'paul@email.fr', false, 'f4516ed3c7295e4f512ee978e073fd33db592de4', '2022-01-03 19:13:25');

insert into hotel (id, name, address, city, description) values (1, 'Four Seasons', '2 Boulevard de la Liberte', 'Paris', 'ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin');
insert into hotel (id, name, address, city, description) values (2, 'Couples Resorts', '65533 Eagan Alley', 'Choroszcz', 'in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque');
insert into hotel (id, name, address, city, description) values (3, 'Ritz-Carlton', '0520 Dahle Alley', 'Changhua', 'amet erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non');
insert into hotel (id, name, address, city, description) values (4, 'Mandarin Oriental', '2 Talisman Junction', 'Louguan', 'venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet');
insert into hotel (id, name, address, city, description) values (5, 'Capital Hotel', '7483 Hanson Street', 'Landim', 'magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in');
insert into hotel (id, name, address, city, description) values (6, 'Best Western', '39847 Dexter Circle', 'Guamal', 'curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi');
insert into hotel (id, name, address, city, description) values (7, 'Hilton', '79079 Morning Way', 'Alegre', 'rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse');

insert into gerant (id, user_id, hotel_id) values(1, 2, 1);

insert into suite (id, titre, img, description, price, link, hotel_id) values (1, 'Toys', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum', 396, 'https://www.booking.com/hotel/fr/holiday-home-bucolique.fr.html?aid=390156;label=duc511jc-1DCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBA-gBAYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgTgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dist=0&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&', 1);
insert into suite (id, titre, img, description, price, link, hotel_id) values (2, 'Dead & Breakfast', 'http://dummyimage.com/334x300.png/dddddd/ffffff', 'leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in felis', 340, 'https://www.booking.com/hotel/fr/villa-orkagna.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dest_id=-1457576;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=2;hpos=2;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647287587;srpvid=5f0d8bd1c5c00009;type=total;ucfs=1&#hotelTmpl', 1);
insert into suite (id, titre, img, description, price, link, hotel_id) values (3, 'Private Eyes', 'http://dummyimage.com/334x300.png/dddddd/ffffff', 'volutpat in congue etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate elementum nullam', 368, 'https://www.booking.com/hotel/fr/roz-de-mer.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 2);
insert into suite (id, titre, img, description, price, link, hotel_id) values (4, 'Don''t Think About It', 'http://dummyimage.com/334x300.png/dddddd/000000', 'condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque', 266, 'https://www.booking.com/hotel/fr/villa-belle-epoque-xixe-vue-mer.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 5);
insert into suite (id, titre, img, description, price, link, hotel_id) values (5, 'Captain Abu Raed', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur at ipsum ac tellus semper interdum', 354, 'https://www.booking.com/hotel/ch/montreux-lake-view-apartments-and-spa.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gC67m-kQbAAgHSAiQ2MTIzZjc4Yi0wZmI3LTQxYTItOTM3Ni0zYTI3NTVhY2MxMDTYAgbgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;srpvid=5f0d8bd1c5c00009&', 2);
insert into suite (id, titre, img, description, price, link, hotel_id) values (6, 'Late Phases', 'http://dummyimage.com/334x300.png/dddddd/000000', 'rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede', 144, 'https://www.booking.com/hotel/fr/gite-les-bravigou-2-4-pers-plage-1km-tregunc-finistere-sud.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 6);
insert into suite (id, titre, img, description, price, link, hotel_id) values (7, 'Jamaica Inn', 'http://dummyimage.com/334x300.png/dddddd/000000', 'pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel', 254, 'https://www.booking.com/hotel/fr/la-marionnette-du-plateau.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 7);
insert into suite (id, titre, img, description, price, link, hotel_id) values (8, 'J. Gang Meets Dynamite Harry', 'http://dummyimage.com/334x300.png/dddddd/000000', 'sit amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis', 357, 'https://www.booking.com/hotel/fr/maison-au-coeur-de-lyon-avec-jardin-terrasse-patio.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748', 3);
insert into suite (id, titre, img, description, price, link, hotel_id) values (9, 'Dungeons & Dragons', 'http://dummyimage.com/334x300.png/dddddd/000000', 'hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem', 491, 'https://www.booking.com/hotel/us/5-star-luxury-villa-in-windsor-hills-a-gated-villa-community.fr.html?aid=390156;label=duc511jc-1FCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBAegBAfgBDYgCAagCA7gCvanBkQbAAgHSAiQ4Njg0MTI2NC0zYTcwLTQzMGMtOGExZS1hNDEzYmZkY2U0M2TYAgbgAgE;sid=25dea7c6ac31ead04633de226085f748;dest_id=20023488;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;nflt=sth%3D20;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647334745;srpvid=90313f2c0d0e02a0;type=total;ucfs=1&#hotelTmpl', 4);

insert into reservation (id, customer_id, suite_id, datebeginning, dateend) values (1, 1, 9, '2021-03-30 10:22:16', '2022-02-06 22:29:50');
insert into reservation (id, customer_id, suite_id, datebeginning, dateend) values (2, 2, 3, '2021-06-03 13:18:31', '2021-10-23 16:31:10');
insert into reservation (id, customer_id, suite_id, datebeginning, dateend) values (3, 3, 8, '2021-08-28 14:19:20', '2022-02-14 00:58:18');
insert into reservation (id, customer_id, suite_id, datebeginning, dateend) values (4, 2, 4, '2021-10-30 21:57:51', '2021-09-19 07:45:05');
insert into reservation (id, customer_id, suite_id, datebeginning, dateend) values (5, 3, 1, '2021-11-15 11:28:06', '2021-10-10 21:21:01');

/* Supprimer des données */

DELETE FROM user where user.id = 1;
DROP TABLE gerant;
DELETE FROM suite where suite.id = 7;

/* Selectionner le nom et le prix des suites de l'hôtel avec l'id numéro 1 */

SELECT suite.titre AS `Nom de la suite`, suite.price AS `Prix`
FROM suite
WHERE suite.hotel_id = 1;


/* Utilisation d'un utilitaire de sauvegarde et restauration de la base de données */
mysqldump -u root -p hotel > hotel.sql