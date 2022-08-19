-- db name = personal_site -- 
-- table name = personal => for saving personal data for me.
CREATE TABLE `personal_site`.`personal` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(50) NULL,
    `last_name` VARCHAR(50) NULL,
    `address` TEXT(2000) NULL,
    `phone_number` VARCHAR(11) NULL,
    `email` VARCHAR(100) NULL,
    `github_link` VARCHAR(200) NULL,
    `stackoverflow_link` VARCHAR(200) NULL,
    `linkedin_link` VARCHAR(200) NULL,
    `twitter_link` VARCHAR(200) NULL,
    `facebook_link` VARCHAR(200) NULL,
    `instagram_link` VARCHAR(200) NULL,
    `about_me` TEXT(5000) NULL,
    PRIMARY KEY (`id`)
);
-- table name = experiences => for saving my experiences during my career.
CREATE TABLE `personal_site`.`experiences` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `company_name` VARCHAR(100) NULL,
  `company_site` VARCHAR(200) NULL,
  `start_date` VARCHAR(20) NULL,
  `end_date` VARCHAR(20) NULL,
  `description` TEXT(2000) NULL,
  PRIMARY KEY (`id`)
);
-- table name = educations => for saving my educations such as university and other workshops or courses.
CREATE TABLE `personal_site`.`educations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NULL,
  `grade` VARCHAR(100) NULL,
  `field` VARCHAR(200) NULL,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL,
  `description` TEXT(2000) NULL,
  PRIMARY KEY (`id`)
);
-- table name = skills => for saving my skills such as soft skills or technical skills
CREATE TABLE `personal_site`.`skills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `logo` VARCHAR(400) NULL,
  `point` DOUBLE NULL,
  PRIMARY KEY (`id`)
);
-- table name = workflow
CREATE TABLE `personal_site`.`workflow` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NULL,
  PRIMARY KEY (`id`));
-- table name = interests => for saving my intersets such as technical or habits or entertainments and so on.
CREATE TABLE `personal_site`.`interests` (
  `id` INT NOT NULL,
  `description` VARCHAR(400) NULL,
  PRIMARY KEY (`id`));
-- table name = awards
CREATE TABLE `personal_site`.`awards` (
  `id` INT NOT NULL,
  `titls` VARCHAR(200) NULL,
  PRIMARY KEY (`id`));
-- table name = experience_skills
-- relation between experiences and skills tables (many to many)
CREATE TABLE `personal_site`.`experiense_skills` (
  `id` INT NOT NULL,
  `experience_id` INT NOT NULL,
  `skill_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_idx` (`experience_id` ASC) VISIBLE,
  INDEX `skill_fk_idx` (`skill_id` ASC) VISIBLE,
  CONSTRAINT `experience_fk`
    FOREIGN KEY (`experience_id`)
    REFERENCES `personal_site`.`experiences` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `skill_fk`
    FOREIGN KEY (`skill_id`)
    REFERENCES `personal_site`.`skills` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

