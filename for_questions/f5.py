import logging

logging.basicConfig(
    filename="f5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def reverse_string(s: str) -> str:
    """
    Reverse a string using a for loop (no slicing).
    
    Parameters:
        s (str): Input string
        
    Returns:
        str: Reversed string
    """
    logging.info("Reversing the string")

    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str

    logging.info(f"Reversed string of {s} : {reversed_str}")
    return reversed_str


print(reverse_string("hello"))