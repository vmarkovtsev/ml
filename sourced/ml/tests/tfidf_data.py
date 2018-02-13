from pyspark import Row

bags = [{"word1": 1,
         "word2": 2,
         "word3": 3, },
        {"word3": 4,
         "word4": 5,
         "word5": 6, },
        {"word3": 7,
         "word5": 8,
         "word6": 9, },
        {"word7": 10,
         "word8": 11,
         "word9": 12, },
        {"word1": 13,
         "word5": 14,
         "word6": 15, },
        {"word1": 13,
         "word2": 14,
         "word9": 15, },
        ]

datasets = [{"uast": [0, 1, 2],
             "document": [0, 1, 2], },
            {"uast": [0, 1, 2],
             "document": [0, 0, 0], },
            {"uast": [0, 1, 2, 3, 4, 5],
             "document": [0, 1, 2, 3, 4, 5], },
            {"uast": [0, 1, 2, 3, 4, 5],
             "document": [0, 0, 0, 0, 0, 0], },
            {"uast": [0, 1, 2, 3, 4, 5],
             "document": [0, 0, 0, 1, 1, 1], },
            ]

term_freq_result = [{Row(document=1, token='test.word4', value=5),
                     Row(document=2, token='test.word6', value=9),
                     Row(document=0, token='test.word3', value=3),
                     Row(document=1, token='test.word3', value=4),
                     Row(document=2, token='test.word3', value=7),
                     Row(document=2, token='test.word5', value=8),
                     Row(document=1, token='test.word5', value=6),
                     Row(document=0, token='test.word1', value=1),
                     Row(document=0, token='test.word2', value=2)
                     },
                    {Row(document=0, token='test.word4', value=5),
                     Row(document=0, token='test.word5', value=14),
                     Row(document=0, token='test.word6', value=9),
                     Row(document=0, token='test.word3', value=14),
                     Row(document=0, token='test.word1', value=1),
                     Row(document=0, token='test.word2', value=2)
                     },
                    {Row(document=4, token='test.word5', value=14),
                     Row(document=4, token='test.word6', value=15),
                     Row(document=1, token='test.word4', value=5),
                     Row(document=2, token='test.word6', value=9),
                     Row(document=4, token='test.word1', value=13),
                     Row(document=0, token='test.word3', value=3),
                     Row(document=1, token='test.word3', value=4),
                     Row(document=5, token='test.word1', value=13),
                     Row(document=2, token='test.word3', value=7),
                     Row(document=3, token='test.word9', value=12),
                     Row(document=1, token='test.word5', value=6),
                     Row(document=5, token='test.word2', value=14),
                     Row(document=2, token='test.word5', value=8),
                     Row(document=3, token='test.word7', value=10),
                     Row(document=5, token='test.word9', value=15),
                     Row(document=0, token='test.word1', value=1),
                     Row(document=3, token='test.word8', value=11),
                     Row(document=0, token='test.word2', value=2)
                     },
                    {Row(document=0, token='test.word9', value=27),
                     Row(document=0, token='test.word7', value=10),
                     Row(document=0, token='test.word6', value=24),
                     Row(document=0, token='test.word4', value=5),
                     Row(document=0, token='test.word5', value=28),
                     Row(document=0, token='test.word1', value=27),
                     Row(document=0, token='test.word3', value=14),
                     Row(document=0, token='test.word2', value=16),
                     Row(document=0, token='test.word8', value=11)
                     },
                    {Row(document=1, token='test.word1', value=26),
                     Row(document=1, token='test.word7', value=10),
                     Row(document=0, token='test.word6', value=9),
                     Row(document=1, token='test.word2', value=14),
                     Row(document=0, token='test.word2', value=2),
                     Row(document=1, token='test.word8', value=11),
                     Row(document=0, token='test.word5', value=14),
                     Row(document=0, token='test.word1', value=1),
                     Row(document=1, token='test.word6', value=15),
                     Row(document=0, token='test.word4', value=5),
                     Row(document=1, token='test.word5', value=14),
                     Row(document=1, token='test.word9', value=27),
                     Row(document=0, token='test.word3', value=14)
                     },
                    ]

doc_freq_result = results = [{Row(token='test.word4', value=1),
                              Row(token='test.word6', value=1),
                              Row(token='test.word2', value=1),
                              Row(token='test.word5', value=2),
                              Row(token='test.word1', value=1),
                              Row(token='test.word3', value=3),
                              },
                             {Row(token='test.word4', value=1),
                              Row(token='test.word6', value=1),
                              Row(token='test.word2', value=1),
                              Row(token='test.word5', value=1),
                              Row(token='test.word1', value=1),
                              Row(token='test.word3', value=1),
                              },
                             {Row(token='test.word4', value=1),
                              Row(token='test.word9', value=2),
                              Row(token='test.word6', value=2),
                              Row(token='test.word2', value=2),
                              Row(token='test.word5', value=3),
                              Row(token='test.word7', value=1),
                              Row(token='test.word8', value=1),
                              Row(token='test.word1', value=3),
                              Row(token='test.word3', value=3),
                              },
                             {Row(token='test.word4', value=1),
                              Row(token='test.word9', value=1),
                              Row(token='test.word6', value=1),
                              Row(token='test.word2', value=1),
                              Row(token='test.word5', value=1),
                              Row(token='test.word7', value=1),
                              Row(token='test.word8', value=1),
                              Row(token='test.word1', value=1),
                              Row(token='test.word3', value=1),
                              },
                             {Row(token='test.word6', value=2),
                              Row(token='test.word4', value=1),
                              Row(token='test.word7', value=1),
                              Row(token='test.word2', value=2),
                              Row(token='test.word1', value=2),
                              Row(token='test.word9', value=1),
                              Row(token='test.word8', value=1),
                              Row(token='test.word3', value=1),
                              Row(token='test.word5', value=2),
                              },
                             ]