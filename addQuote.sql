DELIMITER //
DROP PROCEDURE IF EXISTS addquote // 

CREATE PROCEDURE addquote(IN quoteString VARCHAR(1024) )
BEGIN
        INSERT INTO quotes (quote) VALUES(quoteString) ;
END //
DELIMITER ;

