import evaluator

from eval_1 import code as code_1
from eval_2 import code as code_2
from eval_3 import code as code_3
from eval_4 import code as code_4
from eval_5 import code as code_5
from eval_6 import code as code_6
from eval_7 import code as code_7
from eval_8 import code as code_8
from eval_9 import code as code_9
from eval_10 import code as code_10
from eval_11 import code as code_11
from eval_12 import code as code_12
from eval_13 import code as code_13
from eval_14 import code as code_14
from eval_15 import code as code_15
from eval_16 import code as code_16


implementations = {
    "01_is_palindrome": code_1,
    "02_run_length_encode": code_2,
    "03_flatten": code_3,
    "04_most_frequent": code_4,
    "05_is_balanced": code_5,
    "06_caesar_cipher": code_6,
    "07_merge_intervals": code_7,
    "08_roman_to_int": code_8,
    "09_int_to_roman": code_9,
    "10_binary_search": code_10,
    "11_group_anagrams": code_11,
    "12_word_frequencies": code_12,
    "13_fibonacci": code_13,
    "14_parse_csv_line": code_14,
    "15_two_sum": code_15,
    "16_longest_common_prefix": code_16,
}


score, failed = evaluator.score_implementations(
    implementations
)

print(f"Score : {score:.2%}")
print("Tâches échouées :", failed)