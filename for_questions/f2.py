import logging

logging.basicConfig(
    filename="f2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def frequency_count(s:str)->dict :
    """
    Count the frequency of characters in a given string.
    Parameters:
        s (str): Input string
    Returns:
        Dict: frequency of each character in a string.
    """
    logging.info("Counting characters in the string")
    
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    logging.info(f"The frequency of each charater in {s} : {freq}")
    return freq

s2 = "aaabbc"
frequency_count(s2)