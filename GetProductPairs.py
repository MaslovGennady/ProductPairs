import psycopg2
import json

with open("PostgreDBconnect.json", "r") as read_file:
    data = json.load(read_file)
    
with psycopg2.connect(dbname=data['dbname'], user=data['user'],
                        password=data['password'], host=data['host']) as conn:
    
    with conn.cursor() as cursor:
        cursor.execute(
            'select plu1, plu2, count(1) cnt '
               'from ( '
                      'select distinct s1.id, '
                             'case when s1.plu >= s2.plu then s1.plu else s2.plu end plu1, '
                             'case when s1.plu >= s2.plu then s2.plu else s1.plu end plu2 '
                        'from sales s1 '
                             'join sales s2 on s1.id = s2.id where s1.plu <> s2.plu '
                    ') t '
              'group by plu1, plu2 '
              'order by count(1) desc '
        )

        print('Query Executed!')
    
        with open("ProductPairs.txt", "w") as write_file:
            for row in cursor:
                write_file.write(' '.join([str(i) for i in list(row)]) + '\n')

conn.close()

print('End!')
