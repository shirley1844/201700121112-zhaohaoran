#!/usr/bin/env python
# coding: utf-8

# In[9]:


import codecs
import sys


# #### 1. 参数设置。

# In[10]:


MODE = "A"    # 将MODE设置为"PTB_TRAIN", "PTB_VALID", "PTB_TEST", "TRANSLATE_EN", "TRANSLATE_ZH"之一。

# if MODE == "PTB_TRAIN":        # PTB训练数据
#     RAW_DATA = "../../datasets/PTB_data/ptb.train.txt"  # 训练集数据文件
#     VOCAB = "ptb.vocab"                                 # 词汇表文件
#     OUTPUT_DATA = "ptb.train"                           # 将单词替换为单词编号后的输出文件
# elif MODE == "PTB_VALID":      # PTB验证数据
#     RAW_DATA = "../../datasets/PTB_data/ptb.valid.txt"
#     VOCAB = "ptb.vocab"
#     OUTPUT_DATA = "ptb.valid"
# elif MODE == "PTB_TEST":       # PTB测试数据
#     RAW_DATA = "../../datasets/PTB_data/ptb.test.txt"
#     VOCAB = "ptb.vocab"
#     OUTPUT_DATA = "ptb.test"
if MODE == "Q":   # 中文翻译数据
    RAW_DATA = "samples_15w/question2_15w_cut.txt"
    VOCAB = "samples_15w/vocab.txt"
    OUTPUT_DATA = "samples_15w/question2_15w_id.txt"
elif MODE == "A":   # 英文翻译数据
    RAW_DATA = "samples_15w/answer2_15w_cut.txt"
    VOCAB = "samples_15w/vocab.txt"
    OUTPUT_DATA = "samples_15w/answer2_15w_id.txt"


# #### 2.按词汇表对将单词映射到编号。

# In[11]:


# 读取词汇表，并建立词汇到单词编号的映射。
with codecs.open(VOCAB, "r", "utf-8") as f_vocab:
    vocab = [w.strip() for w in f_vocab.readlines()]
word_to_id = {k: v for (k, v) in zip(vocab, range(len(vocab)))}

# 如果出现了不在词汇表内的低频词，则替换为"unk"。
def get_id(word):
    return word_to_id[word] if word in word_to_id else word_to_id["<unk>"]


# #### 3.对数据进行替换并保存结果。

# In[12]:


fin = codecs.open(RAW_DATA, "r", "utf-8")
fout = codecs.open(OUTPUT_DATA, 'w', 'utf-8')
for line in fin:
    words = line.strip().split() + ["<eos>"]  # 读取单词并添加<eos>结束符
    # 将每个单词替换为词汇表中的编号
    out_line = ' '.join([str(get_id(w)) for w in words]) + '\n'
    fout.write(out_line)
fin.close()
fout.close()


# In[ ]:




