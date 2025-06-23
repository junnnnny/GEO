import sys
import os
import types

# Ensure src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Provide dummy modules to satisfy imports in utils
search_try = types.ModuleType('search_try')
search_try.search_handler = lambda *args, **kwargs: None
sys.modules['search_try'] = search_try

generative_le = types.ModuleType('generative_le')
generative_le.generate_answer = lambda *args, **kwargs: None
sys.modules['generative_le'] = generative_le

import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from utils import extract_citations_new

def test_extract_citations_new_simple():
    text = "First[1]. Second sentence[2][3]."
    result = extract_citations_new(text)
    assert result[0][0][2] == [1]
    assert result[0][1][2] == [2, 3]
