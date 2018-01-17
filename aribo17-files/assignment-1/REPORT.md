# Assignment 1 Delivery

Please follow the provided structure carefully and complete all of the sections described below. The parts that you need to complete are marked with *TODO*.

## Personal information

**Name**: Ahmed Omar Ali Abdi

List the GitHub usernames of your team here. If you are working alone, then write your GitHub username as the team leader and leave the list of additional team members empty.

**Team leader**: aribo17

**Additional team members**: Bibben,  SCassandraES

If you are working as a part of a team, only the a single person, the *team leader* needs to submit the report. If that is not you, then do not edit anything below this point.

----

## Index statistics

Complete the table with statistics about the index you created using Elasticsearch.

The average field lengths are to be computed across all documents in the collection.

| **Description** | **Value** |
| -- | -- |
| Number of documents | 1033461 |
| Average length of the title field | 6.493642237104255 |
| Average length of the content field | 467.25727144033493 |


## Retrieval evaluation

Report on the retrieval performance of the following methods:

  * **Baseline (BM25)**: baseline retrieval model from Elasticsearch
  * **MLM (default parameters)**: Mixture of Language Models with default parameters: lambda=0.1, field weights: title=0.2, content=0.8
  * **BM25 optimized**: BM25 with optimized k1 and b parameters
  * **MLM optimized**: MLM with optimized field weights, smoothing method, and smoothing parameter

Write the name of the corresponding output file in the table, as well as the name of the file with the source code that was used for producing that output file. These files should be pushed to your repository.


| **Method** | **Output file** | **Code** | **P@10** | **MAP** | **MRR** |
| -- | -- | -- | -- | -- | -- |
| Baseline (BM25) | `data/baseline.txt` | `2_Baseline_retrieval.ipynb` | 0.178 | 0.064 | 0.314 |
| MLM (default parameters) | `data/mlm_default.txt` | `4_MLM_scoring.ipynb` | 0.184 | 0.077 | 0.360 |
| BM25 optimized | `data/bm_optimized.txt` | `5_Param_sweep.ipynb` | 0.193 | 0.081 | 0.444 |
| MLM optimized | `"data/mlm_test.txt"` | `4_MLM_scoring.ipynb` | 0.200| 0.083 | 0.442 |

Best BM25 parameters found:
  - k1= 1.1
  - b= 0.1

Best MLM parameters found:
  - field weights: title=0.6, content=0.4
  - smoothing method: Jelinek-Mercer
  - smoothing parameters: 0.1

## Query-level analysis

Create two plots for comparing the performance of the baseline BM25 model with the best performing MLM model, i.e., the first and last lines of the table above. Use Average Precision (AP) as the metric.

[Plot 1 (delta AP for each query)](delta_ap_query.png)

[Plot 2 (distribution of queries according to delta AP)](dist_query.png)


List the names of Jupyter notebooks or other code files that were used for producing the above plots: 3_Evaluation.ipynb
