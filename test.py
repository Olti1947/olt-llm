import re

from SimpleTokenizerV1 import SimpleTokenizerV1
from SimpleTokenizerV2 import SimpleTokenizerV2
# Tokenizer which uses byte pair encoding (BPE) to encode and decode text. This tokenizer is used for testing purposes.
import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace."
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)