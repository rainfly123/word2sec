#coding:utf8
import logging
import os
import gensim
import smart_open
from gensim.test.utils import get_tmpfile
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

__model = None

def __read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding="utf-8") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])


def init_model():
    global __model
    lee_train_file = 'english'
    train_corpus = list(__read_corpus(lee_train_file))
    fname = get_tmpfile("lee_doc2vec_model")
    if os.path.exists(fname):
        __model = gensim.models.doc2vec.Doc2Vec.load(fname)
    else:
        __model = gensim.models.doc2vec.Doc2Vec(vector_size=48, min_count=2, epochs=40)
        __model.build_vocab(train_corpus)
        __model.train(train_corpus, total_examples=__model.corpus_count, epochs=__model.epochs)
        __model.save(fname)

def similar(test_corpus, similarity=0.5):
    tokens = gensim.utils.simple_preprocess(test_corpus)
    inferred_vector = __model.infer_vector(tokens)
    sims = __model.docvecs.most_similar([inferred_vector], topn=len(__model.docvecs))
    #test_data_dir = os.path.join(gensim.__path__[0], 'test', 'test_data')
    #lee_train_file = os.path.join(test_data_dir, 'lee_background.cor')
    #train_corpus = list(__read_corpus(lee_train_file))
    #print " ".join(train_corpus[sims[0][0]].words)
    return [{"id":i, "similarity":round(s,4)} for i,s in sims if s >= similarity]

if __name__ == '__main__':
    init_model()
    test = """Pentagon"""
    result = similar(test)
    for i in result:
        print i
