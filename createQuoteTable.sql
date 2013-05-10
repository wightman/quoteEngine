CREATE TABLE quote
(
  quote_id    INT NOT NULL AUTO_INCREMENT,
	quote       VARCHAR(1024),
	
	CONSTRAINT pk_quoteID PRIMARY KEY (quote_id)
);
