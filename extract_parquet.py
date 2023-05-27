import pyarrow.parquet as pq

index = 0
table = pq.read_table('mnist-test.parquet')
for img in table['image']:
    b = img['bytes'].as_py()
    with open(f'mnist-test/{index}.png', 'wb') as f:
        f.write(b)
        index+=1
