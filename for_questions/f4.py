import logging

logging.basicConfig(
    filename="f4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from typing import List
def list_isSorted(nums: List[int]) -> bool:
    """
    Find the list is sorted in ascending order or not.
    
    Parameters:
        nums (list): Input list of integers
        
    Returns:
        bool: returns true if list is sorted in ascending order.
    """

    logging.info("Checking if list is sorted")
    
    if len(nums) == 0:
        return True

    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            logging.info(f"the element in {nums} are not sorted in ascending order")
            return False


    logging.info(f"the element in {nums} are sorted in ascending order")
    return True


nums = [1,2,3,4]
print(list_isSorted(nums))