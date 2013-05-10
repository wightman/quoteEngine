DELIMITER //
DROP PROCEDURE IF EXISTS 'getquote' // 

CREATE PROCEDURE getquote()
begin
  SELECT * FROM quotes
		ORDER BY rand() limit 1;
end//
DELIMITER ;
