from matplotlib import pyplot as plt
import pandas as pd
import csv

LS_OPT = []
GA_OPT = []
LS_RTIME = []
LS_POP = []
# len(LS_POP) is the generation number
LS_POP_NUM = []
GA_RTIME = []
GA_GEN = []
GA_CHROM = []

# append num of lspop
for i in range(len(LS_POP)):
    LS_POP_NUM.append(i)


def func():
    print("LS_OPT ", LS_OPT)
    print("GA_OPT ", GA_OPT)
    print("LS_RTIME ", LS_RTIME)
    print("LS_POP ", LS_POP)
    print("LS_OPT_len ", len(LS_OPT))
    print("GA_RTIME ", GA_RTIME)
    print("GA_GEN ", GA_GEN)
    print("GA_CHROM ", GA_CHROM)


"""
not finished!!!!
"""

# write to csv with pandas

# cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
# new_column_names = ['City_Name', 'State_Name']
# cities.to_csv('cities.csv', index=False, header=new_column_names)

# data = [GA_OPT, GA_RTIME, LS_OPT, LS_RTIME]
# time_opt = pd.DataFrame([GA_OPT + GA_RTIME, LS_OPT + LS_RTIME], index=['GA', 'LS'], columns=['optimal result', 'runtime'])
# data2 = [LS_POP_NUM[0], LS_POP[0]]
# ls = pd.DataFrame(data2, columns=["ls pop num", "ls pop 3 games"])
# data3 = [GA_GEN[0], GA_CHROM[0]]
# ga = pd.DataFrame(data3, columns=["generation", "ga pop len"])
# with pd.ExcelWriter('data.xlsx') as writer:
#     time_opt.to_excel(writer, sheet_name='sheet1')
#     ls.to_excel(writer, sheet_name='sheet2')
#     ga.to_excel(writer, sheet_name='sheet3')


# time_opt.to_csv('time-opt-data.csv', index=False)

# print runtime and optimal num of steps

# print generation and chromosome length

# for ls population number vs population length

def write_to_csv(write_this):
    # open the file in the write mode
    with open('data.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(write_this)

# plotting data
