-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema blog
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User` ;

CREATE TABLE IF NOT EXISTS `User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE INDEX `User_username` ON `User` (`username` ASC);


-- -----------------------------------------------------
-- Table `Blog`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Blog` ;

CREATE TABLE IF NOT EXISTS `Blog` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `User_id` INT NOT NULL,
  `deleted` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Blog_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Blog_User1_idx` ON `Blog` (`User_id` ASC);


-- -----------------------------------------------------
-- Table `Post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Post` ;

CREATE TABLE IF NOT EXISTS `Post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post_name` VARCHAR(45) NOT NULL,
  `post_date` DATETIME NOT NULL,
  `User_id` INT NOT NULL,
  `data` MEDIUMTEXT NOT NULL,
  `deleted` TINYINT(1) NOT NULL DEFAULT 0,
  `last_modify` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Post_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Post_User1_idx` ON `Post` (`User_id` ASC);


-- -----------------------------------------------------
-- Table `BlogPost`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `BlogPost` ;

CREATE TABLE IF NOT EXISTS `BlogPost` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Blog_id` INT NOT NULL,
  `Post_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_BlogPost_Blog`
    FOREIGN KEY (`Blog_id`)
    REFERENCES `Blog` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_BlogPost_Post1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `Post` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_BlogPost_Blog_idx` ON `BlogPost` (`Blog_id` ASC);

CREATE INDEX `fk_BlogPost_Post1_idx` ON `BlogPost` (`Post_id` ASC);


-- -----------------------------------------------------
-- Table `Comment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Comment` ;

CREATE TABLE IF NOT EXISTS `Comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` MEDIUMTEXT NOT NULL,
  `Post_id` INT NULL,
  `Comment_id` INT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Comment_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comment_Post1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `Post` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comment_Comment1`
    FOREIGN KEY (`Comment_id`)
    REFERENCES `Comment` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Comment_User1_idx` ON `Comment` (`User_id` ASC);

CREATE INDEX `fk_Comment_Post1_idx` ON `Comment` (`Post_id` ASC);

CREATE INDEX `fk_Comment_Comment1_idx` ON `Comment` (`Comment_id` ASC);


-- -----------------------------------------------------
-- Table `Session`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Session` ;

CREATE TABLE IF NOT EXISTS `Session` (
  `id` VARCHAR(36) NOT NULL,
  `session` VARCHAR(45) NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Session_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Session_User1_idx` ON `Session` (`User_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
