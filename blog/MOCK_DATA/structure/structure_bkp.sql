-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema blog
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `blog` ;

-- -----------------------------------------------------
-- Schema blog
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blog` DEFAULT CHARACTER SET utf8 ;
USE `blog` ;

-- -----------------------------------------------------
-- Table `blog`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`User` ;

CREATE TABLE IF NOT EXISTS `blog`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Blog`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`Blog` ;

CREATE TABLE IF NOT EXISTS `blog`.`Blog` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Blog_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blog`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Blog_User1_idx` ON `blog`.`Blog` (`User_id` ASC);


-- -----------------------------------------------------
-- Table `blog`.`Post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`Post` ;

CREATE TABLE IF NOT EXISTS `blog`.`Post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post_name` VARCHAR(45) NOT NULL,
  `post_date` DATETIME NOT NULL,
  `User_id` INT NOT NULL,
  `data` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Post_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blog`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Post_User1_idx` ON `blog`.`Post` (`User_id` ASC);


-- -----------------------------------------------------
-- Table `blog`.`BlogPost`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`BlogPost` ;

CREATE TABLE IF NOT EXISTS `blog`.`BlogPost` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Blog_id` INT NOT NULL,
  `Post_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_BlogPost_Blog`
    FOREIGN KEY (`Blog_id`)
    REFERENCES `blog`.`Blog` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_BlogPost_Post1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `blog`.`Post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_BlogPost_Blog_idx` ON `blog`.`BlogPost` (`Blog_id` ASC);

CREATE INDEX `fk_BlogPost_Post1_idx` ON `blog`.`BlogPost` (`Post_id` ASC);


-- -----------------------------------------------------
-- Table `blog`.`Comment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`Comment` ;

CREATE TABLE IF NOT EXISTS `blog`.`Comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` MEDIUMTEXT NOT NULL,
  `Post_id` INT NULL,
  `Comment_id` INT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Comment_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blog`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comment_Post1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `blog`.`Post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comment_Comment1`
    FOREIGN KEY (`Comment_id`)
    REFERENCES `blog`.`Comment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Comment_User1_idx` ON `blog`.`Comment` (`User_id` ASC);

CREATE INDEX `fk_Comment_Post1_idx` ON `blog`.`Comment` (`Post_id` ASC);

CREATE INDEX `fk_Comment_Comment1_idx` ON `blog`.`Comment` (`Comment_id` ASC);


-- -----------------------------------------------------
-- Table `blog`.`Session`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blog`.`Session` ;

CREATE TABLE IF NOT EXISTS `blog`.`Session` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `session` VARCHAR(45) NOT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Session_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blog`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Session_User1_idx` ON `blog`.`Session` (`User_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
