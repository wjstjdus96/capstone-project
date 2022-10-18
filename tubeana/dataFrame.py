import pandas as pd

data = [
    ['2022-03-01 08:08:11', '2'],
    ['2022-03-01 08:09:11', '2'],
    ['2022-03-02 08:08:11', '2'],
    ['2022-03-02 08:08:11', '100'],
    ['2022-03-02 08:08:11', '2'],
    ['2022-03-02 08:08:11', '100'],
    ['2022-03-03 08:08:11', '2'],
    ['2022-04-03 08:08:11', '2'],
    ['2022-04-04 08:08:11', '28'],
    ['2022-04-04 08:08:11', '2'],
    ['2022-04-04 08:08:11', '2'],
    ['2022-04-05 08:08:11', '2'],
    ['2022-04-06 08:08:11', '20'],
    ['2022-04-06 08:08:11', '2'],
    ['2022-04-07 08:08:11', '2'],
    ['2022-04-07 08:08:11', '2'],
    ['2022-05-07 08:08:11', '2'],
    ['2022-05-07 08:08:11', '2'],
    ['2022-05-07 08:08:11', '24'],
    ['2022-05-07 08:08:11', '2'],
    ['2022-05-08 08:08:11', '100'],
    ['2022-05-08 08:08:11', '22'],
    ['2022-06-09 08:08:11', '2'],
    ['2022-06-09 08:08:11', '2'],
    ['2022-06-09 08:08:11', '21'],
    ['2022-06-09 08:08:11', '2'],
    ['2022-06-09 08:08:11', '2'],
    ['2022-06-09 08:08:11', '22'],
    ['2022-06-09 08:08:11', '2'],
    ['2022-06-09 08:08:11', '2'],
    ['2023-03-09 08:08:11', '20'],
    ['2023-04-09 08:08:11', '29'],
    ['2023-05-09 08:08:11', '20'],
    ['2023-06-09 08:08:11', '20'],
    ['2023-07-09 08:08:11', '10'],
    ['2023-08-09 08:08:11', '4'],
    ['2023-09-09 08:08:11', '200'],
    ['2023-10-09 08:08:11', '12'],
    ['2023-11-09 08:08:11', '22'],
    ['2023-12-09 08:08:11', '2'],
    ['2023-03-09 08:08:11', '2'],
    ['2023-03-09 08:08:11', '2'],
    ['2023-03-09 08:08:11', '29'],
    ['2023-03-09 08:08:11', '2'],
    ['2023-04-09 08:08:11', '2'],
    ['2023-05-09 08:08:11', '2'],
    ['2023-06-09 08:08:11', '2'],
    ['2023-07-09 08:08:11', '2'],
    ['2023-08-09 08:08:11', '2'],
    ['2023-09-09 08:08:11', '2'],
    ['2023-10-09 08:08:11', '2'],
    ['2023-11-09 08:08:11', '2'],
    ['2023-12-09 08:08:11', '2'],
    ['2023-01-09 08:08:11', '2'],
    ['2023-02-09 08:08:11', '2'],
    ['2023-03-09 08:08:11', '2'],
    ['2023-04-09 08:08:11', '2'],
    ['2023-05-09 08:08:11', '2'],
    ['2023-06-09 08:08:11', '2'],
    ['2023-07-09 08:08:11', '2'],
    ['2023-08-09 08:08:11', '2'],
    ['2023-09-09 08:08:11', '2'],
    ['2023-10-09 08:08:11', '2'],
    # ['2023-01-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],
    # ['2023-03-09 08:08:11', '2'],

]

df = pd.DataFrame(data, columns=['Time','Num'])
df.set_index('Time', inplace=True)