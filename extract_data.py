

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
