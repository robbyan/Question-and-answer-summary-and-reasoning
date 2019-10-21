import numpy as np
import pandas as pd
from jieba import posseg
from seq2seq_tf2 import config
import jieba
from tokenizer import segment
from seq2seq_tf2 import config


def read_stopwords(path):
    lines = set()
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lines.add(line)
    return lines


def parse_data(path):
    pd_data = pd.read_csv(path, encoding='utf-8')
    np_data = np.array(pd_data)
    # data_list = np_data.tolist()[:100]
    data_list = np_data.tolist()

    results_1 = []
    results_2 = []
    for i in data_list:
        if len(i) == 6:
            results_1.append(i[3] + " " + i[4])
            results_2.append(i[5])

        if len(i) == 5:
            results_1.append(i[3] + " " + i[4])

    return results_1, results_2


def save_data(data_1, data_2, data_3, data_path_1, data_path_2, data_path_3, stop_words_path=''):
    stopwords = read_stopwords(stop_words_path)
    with open(data_path_1, 'w', encoding='utf-8') as f1,\
            open(data_path_2, 'w', encoding='utf-8') as f2,\
            open(data_path_3, 'w', encoding='utf-8') as f3:
        count = 0
        for line in data_1:
            # print(line)
            if isinstance(line, str):
                seg_list = segment(line.strip(), cut_type='word')
                # seg_words = []
                # for j in seg_list:
                #     if j in stopwords:
                #         continue
                #     seg_words.append(j)
                seg_line = ' '.join(seg_list)
                f1.write('%s' % seg_line)
            count += 1
            f1.write('\n')

        for line in data_2:
            if isinstance(line, str):
                seg_list = segment(line.strip(), cut_type='word')
                # seg_words = []
                # for j in seg_list:
                #     if j in stopwords:
                #         continue
                #     seg_words.append(j)
                seg_line = ' '.join(seg_list)
                f2.write('%s' % seg_line)
            f2.write('\n')

        for line in data_3:
            if isinstance(line, str):
                seg_list = segment(line.strip(), cut_type='word')
                seg_line = ' '.join(seg_list)
                f3.write('%s' % seg_line)
            f3.write('\n')


if __name__ == '__main__':
    train_list_src, train_list_trg = parse_data(config.train_path)
    test_list_src, _ = parse_data(config.test_path)
    save_data(train_list_src,
              train_list_trg,
              test_list_src,
              config.train_seg_path_x,
              config.train_seg_path_y,
              config.test_seg_path_x,
              stop_words_path=config.stop_words_path)
