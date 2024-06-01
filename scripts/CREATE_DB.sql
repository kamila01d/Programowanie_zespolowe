-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-04-20 07:08:52.206

-- tables
-- Table: Favourites
CREATE TABLE "Favourites" (
    "users_Id" int  NOT NULL,
    "products_Id" int  NOT NULL,
    CONSTRAINT "Favourites_pk" PRIMARY KEY ("Users_Id","Products_Id")
);

-- Table: Products
CREATE TABLE "Products" (
    "id" int  NOT NULL,
    "name" varchar(50)  NULL,
    "url" varchar(70)  NOT NULL,
    "price" decimal(3,2)  NULL,
    "description" text  NULL,
    "json" text  NULL,
    CONSTRAINT "Products_pk" PRIMARY KEY ("id")
);

-- Table: Users
CREATE TABLE "Users" (
    "id" int  NOT NULL,
    "username" varchar(25)  NOT NULL,
    "password" varchar(32)  NOT NULL,
    "email" varchar(32)  NULL,
    CONSTRAINT "Users_pk" PRIMARY KEY ("id")
);

-- foreign keys
-- Reference: Favourites_Products (table: Favourites)
ALTER TABLE "Favourites" ADD CONSTRAINT "Favourites_Products"
    FOREIGN KEY ("Products_Id")
    REFERENCES "Products" ("Id")
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Favourites_Users (table: Favourites)
ALTER TABLE "Favourites" ADD CONSTRAINT "Favourites_Users"
    FOREIGN KEY ("Users_Id")
    REFERENCES "Users" ("Id")
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- sequences
-- Sequence: Products_seq
CREATE SEQUENCE "Products_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: Users_seq
CREATE SEQUENCE "Users_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- End of file.
