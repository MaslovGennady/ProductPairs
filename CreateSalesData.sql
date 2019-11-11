/*floor(random()* (high-low + 1) + low)  - рандомное число от low до high*/
DO $$
DECLARE
        i integer := 0;
        J integer := 0;
        J_MAX integer := 0;
	TMP_PLU integer := 0;
BEGIN

  WHILE i <= 100000 LOOP
    J_MAX := floor(random() * (5 - 2 + 1) + 2); /*от двух до пяти товаров в чеке*/
    J := 1;
    WHILE J <= J_MAX LOOP
	TMP_PLU := floor(random() * ((J * 200 - 1) - (J - 1) * 200 + 1) + (J-1) * 200); /*1000 id товаров поделены на 5 частей, из каждой части выбирается случайно id товара, отступ от границы частей на 1*/
	INSERT INTO sales (id, plu) VALUES (i, TMP_PLU);
	J := J + 1;
    END LOOP;	
    i := i + 1;
  END LOOP;
END $$;
