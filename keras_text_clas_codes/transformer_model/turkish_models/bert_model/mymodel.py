
import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):

    def __init__(self,
                 bert_model,
                 bert_hidden_size,
                 hidden_1_size,
                 hidden_2_size,
                 class_size):
        super(MyModel, self).__init__()
        self.bert_model = bert_model
        self.hidden_1 = nn.Linear(bert_hidden_size, hidden_1_size)
        self.hidden_2 = nn.Linear(hidden_1_size, hidden_2_size)
        self.out = nn.Linear(hidden_2_size, class_size)

    def forward(self, input_ids, token_type_ids, attention_mask):
        x = self.bert_model(input_ids=input_ids,
                            token_type_ids=token_type_ids,
                            attention_mask=attention_mask)
        x = x[1] # # torch.Size([4, 768])
        x = F.relu(self.hidden_1(x))
        x = F.relu(self.hidden_2(x))
        x = F.softmax(self.out(x), dim=1)
        return x

