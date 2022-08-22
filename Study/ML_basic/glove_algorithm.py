from collections import Counter, defaultdict
import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

"""
본 코드 구현은 https://github.com/noaRricky/pytorch-glove/blob/master/glove.py 를 기반으로 복습차원에서 구현하였으며, 단순 공부를 위해서 코드를 구현만 해본 것임을 알립니다.
"""
class GloVeModel(nn.Module):

    def __init__(self, embedding_size, context_size, vocab_size, min_occurrence=1, x_max=100, alpha=3 / 4): 
        super(GloVeModel, self).__init__()

        self.embedding_size = embedding_size
        if isinstance(context_size, tuple): # size 추출 
            self.left_context, self.right_context = context_size
        if isinstance(context_size, int):
            self.left_context = self.right_context = context_size
        else:
            raise ValueError(
                "'context_size' should be an int or a tuple of two ints")
        self.vocab_size = vocab_size
        self.alpha = alpha
        self.min_occurrence = min_occurrence
        self.x_max = x_max

        self._focal_embeddings = nn.Embedding(vocab_size, embedding_size).type(torch.float64) # 모두 embedding layer
        self._context_embeddings = nn.Embedding(vocab_size, embedding_size).type(torch.float64)
        self._focal_biases = nn.Embedding(vocab_size, 1).type(torch.float64)
        self._context_biases = nn.Embedding(vocab_size, 1).type(torch.float64)
        self._glove_dataset = None

        for params in self.parameters(): # 가중치 초기화 
            init.uniform_(params, a=-1, b=1)

    def fit(self, corpus): 
        # 해당 함수를 통해 co-occurence matrix를 구한다.
        left_size, right_size = self.left_context, self.right_context 
        vocab_size, min_occurrence = self.vocab_size, self.min_occurrence # min_occurence is like a constraint

        word_counts = Counter()
        cooccurence_counts = defaultdict(float) # co-occurence matrix의 초기 형태
        for region in corpus: # list내에 접근
            word_counts.update(region) # region의 값을 counter 형태로 변환하는 작업 
            for left_context, word, right_context in _context_windows(region, left_size, right_size):
                for i, context_word in enumerate(left_context[::-1]): # left_context에 거리만큼을 기준으로 1 / (i+1)을 더한다. 
                    # 그래서 [::-1]로 접근한것 (왼쪽은 가까운것이 list에서 제일 오른쪽에 위치한 것이기 때문이다.)
                    cooccurence_counts[(word, context_word)] += 1 / (i + 1)
                for i, context_word in enumerate(right_context):
                    cooccurence_counts[(word, context_word)] += 1 / (i + 1)
        if len(cooccurence_counts) == 0:
            raise Exception("0 found")

        tokens = [word for word, count in word_counts.most_common(vocab_size) if count >= min_occurrence]
        # min occurence보다 높은 token 추출, rare한 단어들을 drop하기 위해 사용된다고 함
        coocurrence_matrix = [(words[0], words[1], count)
                              for words, count in cooccurence_counts.items()
                              if words[0] in tokens and words[1] in tokens] # 둘다 token으로 간주되면 co-occurrnece matrix에 추가
        self._glove_dataset = GloVeDataSet(coocurrence_matrix) # dataset으로 지정 (self)

    def train(self, num_epoch, device, batch_size=512, learning_rate=0.05, loop_step=10):

        if self._glove_dataset is None:
            raise CorpusError("Please fit model with corpus before training")

        # basic training setting
        optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        glove_dataloader = DataLoader(self._glove_dataset, batch_size) # batchsize만큼 load 
        total_loss = 0

        for epoch in range(num_epoch):
            for idx, batch in enumerate(glove_dataloader):
                optimizer.zero_grad()

                i_s, j_s, counts = batch
                i_s = i_s.to(device)
                j_s = j_s.to(device)
                counts = counts.to(device)
                loss = self._loss(i_s, j_s, counts) # loss 구하는 과정

                total_loss += loss.item() # 값 접근 
                if idx % loop_step == 0:
                    avg_loss = total_loss / loop_step
                    print("epoch: {}, current step: {}, average loss: {}".format(epoch, idx, avg_loss))
                    total_loss = 0

                loss.backward() # backward 
                optimizer.step() # update 


    def get_coocurrance_matrix(self):
  
        return self._glove_dataset._coocurrence_matrix

    def embedding_for_tensor(self, tokens):
        if not torch.is_tensor(tokens):
            raise ValueError("the tokens must be pytorch tensor object")

        return self._focal_embeddings(tokens) + self._context_embeddings(tokens)

    def _loss(self, focal_input, context_input, coocurrence_count):
        x_max, alpha = self.x_max, self.alpha

        focal_embed = self._focal_embeddings(focal_input)
        context_embed = self._context_embeddings(context_input)
        focal_bias = self._focal_biases(focal_input)
        context_bias = self._context_biases(context_input)

        # count weight factor
        weight_factor = torch.pow(coocurrence_count / x_max, alpha)
        weight_factor[weight_factor > 1] = 1
        ''' 
        사실 위 코드는 
        weight_factor = min(1, weight_factor) 의 역할을 해준다. 
        '''
        embedding_products = torch.sum(focal_embed * context_embed, dim=1) # 우선 embedding끼리 곱해준다.
        log_cooccurrences = torch.log(coocurrence_count) # logX_{ij} 를 구하는 과정인데, broadcasting으로 여러개를 동시에 구한다.

        distance_expr = (embedding_products + focal_bias + context_bias - log_cooccurrences) ** 2

        single_losses = weight_factor * distance_expr 
        mean_loss = torch.mean(single_losses) 
        return mean_loss # loss 값 반환


class GloVeDataSet(Dataset):

    def __init__(self, coocurrence_matrix):
        self._coocurrence_matrix = coocurrence_matrix

    def __getitem__(self, index):
        return self._coocurrence_matrix[index]

    def __len__(self):
        return len(self._coocurrence_matrix)


class CorpusError(Exception):
    pass


def _context_windows(corpus, lsize, rsize):
    

    for i, word in enumerate(corpus):
        start = i - lsize
        end = i + rsize
        left_context = _window(corpus, start, i - 1)
        right_context = _window(corpus, i + 1, end)
        yield (left_context, word, right_context)


def _window(corpus, start, end):
    # start와 end 인덱스의 corpus를 리스트형태로 반환 - cooccurence matrix의 거리 count시 사용

    last = len(corpus) + 1
    selected_tokens = corpus[max(start, 0): min(end, last) + 1]
    return selected_tokens