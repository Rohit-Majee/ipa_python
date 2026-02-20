import logging
from typing import List

logging.basicConfig(
    filename = "f7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing_number(nums: List[int]) -> int:
    """
    Find the missing number in a list containing numbers from 1 to N.
    
    Parameters:
        nums (List[int]): Input list
        
    Returns:
        int: Missing number
    """
    logging.info("Finding missing number")

    n = len(nums) + 1

    missing = 0

    for i in range(1, n + 1):
        missing ^= i

    for num in nums:
        missing ^= num


    logging.info(f"Missing number in {nums} : {missing}")
    return missing



print(find_missing_number([1, 2, 4, 5]))