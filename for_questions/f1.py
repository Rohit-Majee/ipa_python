import logging

logging.basicConfig(
    filename="f1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def count_vowel(s:str) -> int:
    """
    Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        int: Total number of vowels in the string.
    """
    logging.info("Counting vowels in the string")
    vowel_count = 0
    for ch in s:
        if ch in 'aeiou':
            vowel_count+=1

    logging.info(f"vowel count for {s} : {vowel_count}")
    return vowel_count

s1 = "abcde"
count_vowel(s1)