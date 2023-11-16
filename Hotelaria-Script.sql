-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hotelaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotelaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotelaria` DEFAULT CHARACTER SET utf8mb3 ;
USE `hotelaria` ;

-- -----------------------------------------------------
-- Table `hotelaria`.`hospede`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelaria`.`hospede` (
  `idHospede` INT NOT NULL,
  `primeiroNome` VARCHAR(45) NOT NULL,
  `ultimoNome` VARCHAR(45) NOT NULL,
  `numCelular` VARCHAR(20) NOT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idHospede`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotelaria`.`Equipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelaria`.`Equipe` (
  `idEquipe` INT NOT NULL,
  `primeiroNome` VARCHAR(45) NOT NULL,
  `ultimoNome` VARCHAR(45) NOT NULL,
  `numCelular` VARCHAR(20) NOT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `idGerente` INT NOT NULL,
  PRIMARY KEY (`idEquipe`),
  INDEX `fk_Equipe_Equipe1_idx` (`idGerente` ASC) VISIBLE,
  CONSTRAINT `fk_Equipe_Equipe1`
    FOREIGN KEY (`idGerente`)
    REFERENCES `hotelaria`.`Equipe` (`idEquipe`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotelaria`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelaria`.`reserva` (
  `idReserva` INT NOT NULL,
  `idHospede` INT NOT NULL,
  `idRecepcionista` INT NOT NULL,
  `dataCheckIn` DATE NOT NULL,
  `dataCheckOut` DATE NOT NULL,
  `numAdultos` INT NOT NULL,
  `numCriancas` INT NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `fk_Reserva_Hospede1_idx` (`idHospede` ASC) VISIBLE,
  INDEX `fk_Reserva_Recepcionista1_idx` (`idRecepcionista` ASC) VISIBLE,
  CONSTRAINT `fk_Reserva_Hospede1`
    FOREIGN KEY (`idHospede`)
    REFERENCES `hotelaria`.`hospede` (`idHospede`),
  CONSTRAINT `fk_Reserva_Recepcionista1`
    FOREIGN KEY (`idRecepcionista`)
    REFERENCES `hotelaria`.`Equipe` (`idEquipe`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotelaria`.`quarto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelaria`.`quarto` (
  `numero` INT NOT NULL,
  `qtdCamas` INT NOT NULL,
  `valDiariaPes` INT NOT NULL,
  `tipoQuarto` ENUM('executivo', 'luxo', 'superluxo') NOT NULL,
  `idReserva` INT NOT NULL,
  PRIMARY KEY (`numero`),
  INDEX `fk_quarto_reserva1_idx` (`idReserva` ASC) VISIBLE,
  CONSTRAINT `fk_quarto_reserva1`
    FOREIGN KEY (`idReserva`)
    REFERENCES `hotelaria`.`reserva` (`idReserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
