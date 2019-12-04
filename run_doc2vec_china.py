#!/usr/bin/env python
#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import logging
import jieba
from gensim.test.utils import get_tmpfile
import os
import gensim
import smart_open

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
stopkeys = ['nbsp', '$', '&', 'div', 'span', 'br', 'p',
'\r', '\n', ',', '，', '.', '。', ';', '；', '！', ':', '：', '、', '《', '》', '？', '?',
 '"', '“', '”']

__model = None

def __read_corpus(fname, tokens_only=False):
    #with smart_open.open(fname, encoding="iso-8859-1") as f:
    with smart_open.open(fname, encoding="utf-8") as f:
        for i, line in enumerate(f):
            #tokens = gensim.utils.simple_preprocess(line)
            line = line.decode('utf-8')
            words = jieba.cut(line)
            tokens = [w for w in words if w not in stopkeys]
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

def init_model():
    lee_train_file = 'latex'
    fname = get_tmpfile("china_doc2vec_model")
    global __model
    if os.path.exists(fname):
        __model = gensim.models.doc2vec.Doc2Vec.load(fname)
    else:
        __model = gensim.models.doc2vec.Doc2Vec(vector_size=48, min_count=2, epochs=40)
        train_corpus = list(__read_corpus(lee_train_file))
        __model.build_vocab(train_corpus)
        __model.train(train_corpus, total_examples=__model.corpus_count, epochs=__model.epochs)
        __model.save(fname)

def similar(test_corpus, similarity=0.5):
    tokens = list()
    lines = test_corpus.split()
    for line in lines:
        line = line.decode('utf-8')
        words = jieba.cut(line)
        token = [w for w in words if w not in stopkeys]
        tokens.extend(token)
           
    inferred_vector = __model.infer_vector(tokens)
    sims = __model.docvecs.most_similar([inferred_vector], topn=len(__model.docvecs))
    return [{"id":i+1, "similarity":s} for i,s in sims if s >= similarity]

if __name__ == "__main__":
    init_model()
    test_corpus = "设函数$f(x)=\lg \left(x^{2}-x-2\right)$的定义域为集合$A$，函数$g(x)=\sqrt{3-|x|}$的定义域为集合$B$.（1）求$A \cap B$；（2）若${C}，"
    print similar(test_corpus)

