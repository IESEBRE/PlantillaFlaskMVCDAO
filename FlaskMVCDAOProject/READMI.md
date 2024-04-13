Per a que ens funcioni el autoincremanl tenim que crear un tigrer


CREATE SEQUENCE llibres_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER llibres_before_insert
BEFORE INSERT ON llibres
FOR EACH ROW
BEGIN
  SELECT llibres_seq.NEXTVAL
  INTO :new.id
  FROM dual;
END;
