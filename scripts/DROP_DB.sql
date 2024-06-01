-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-04-20 07:08:52.206

-- foreign keys
ALTER TABLE "Favourites"
    DROP CONSTRAINT "Favourites_Products";

ALTER TABLE "Favourites"
    DROP CONSTRAINT "Favourites_Users";

-- tables
DROP TABLE "Favourites";

DROP TABLE "Products";

DROP TABLE "Users";

-- sequences
DROP SEQUENCE IF EXISTS "Products_seq";

DROP SEQUENCE IF EXISTS "Users_seq";

-- End of file.

