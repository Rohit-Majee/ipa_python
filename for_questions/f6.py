import logging
from typing import List

logging.basicConfig(
    filename = "f6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(nums: List[int]) -> List[int]:
    """
    Remove duplicate elements from a list while preserving order.
    
    Parameters:
        nums (List[int]): Input list
        
    Returns:
        List[int]: List without duplicates
    """
    logging.info("Removing duplicates while preserving order")

    ls = []
    for num in nums:
        if num not in ls:
            ls.append(num)

    logging.info(f"List after removing duplicates: {ls}")
    return ls


print(remove_duplicates([1, 2, 2, 3, 4, 3, 5, 4, 1]))