import math
# query = [0.133, 0.032, 0.074]
# # d2 = [0.099, 0.099, 0.048]
# # w_tq, w_td, s = 0, 0, 0
# # for t in query:
# #     for i in d2:
# #         w_tq = t
# #         w_td += i
# #         s+= (w_tq * w_td)/(math.sqrt((math.pow(w_tq,2)) * (math.pow(w_td,2))))
# x=100
# y=90
#
# p=100
# m=400
# e_pl=(x*p)/500
# print(e_pl)
# e_min = (y*m)/500
# print(e_min)
# logp = math.log((x/e_pl),2)
# logm = math.log((y/e_min),2)
# r= 2*((x*logp)+(y*logm))
# print("r",r)

def dcg(rel, p):
    dcg = rel[0]
    for i in range(1, min(p, len(rel))):
        dcg += rel[i] / math.log(i + 1, 2)  # rank position is indexed from 1..
    return dcg
sum_ndcg5 = 0
sum_ndcg10 = 0
rankings = {
    "q1": [10, 7, 9, 8, 2, 1,3, 4, 5, 6],
    "q2": [3, 2, 1, 4, 5, 7, 8, 10, 9, 6]
}
gtruth = {
    "q1": [3, 2, 1, 0, 0, 0, 3, 0, 0, 0],
    "q2": [3, 2, 1, 0, 0, 0, 3, 0, 0, 0]
}
for qid, ranking in sorted(rankings.items()):
    gt = gtruth[qid]
    print("Query", qid)
#     print([_ for _, v in gt.items()])


    gains = [] # holds corresponding relevance levels for the ranked docs
    for doc_id in ranking:
        gain = int(gt.get(doc_id, 0))
        gains.append(gain)

    print("\tGains:", gains)

    # relevance levels of the idealized ranking
    gain_ideal = sorted([int(v) for _, v in gt.items()], reverse=True)
    print("\tIdeal gains:", gain_ideal)

    if sum(gain_ideal) != 0:
        ndcg5 = (dcg(gains, 5)) / (dcg(gain_ideal, 5))
        ndcg10 = (dcg(gains, 10)) / (dcg(gain_ideal, 10))
    else:
        ndcg5 = 0
        ndcg10 = 0
    sum_ndcg5 += ndcg5
    sum_ndcg10 += ndcg10

    print("\tNDCG@5:", round(ndcg5, 3), "\n\tNDCG@10:", round(ndcg10, 3))

print("Average")
print("\tNDCG@5:", round(sum_ndcg5 / len(output), 3), "\n\tNDCG@10:", round(sum_ndcg10 / len(output), 3))
