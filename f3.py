import logging

logging.basicConfig(
    filename="f3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



from typing import List

def find_second_largest(nums: List[int]) -> int:
    """
    Find the second largest element in a given list.
    
    Parameters:
        nums (list): Input list of integers
        
    Returns:
        int: Second largest element in the list.
    """
    logging.info("Finding second largest element in the list")
    
    if len(nums) < 2:
        logging.error("List must contain at least two elements")

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num


    logging.info(f"Second largest element in {nums} : {second_largest}")
    return second_largest


nums1 = [10, 20, 4, 45, 99]
find_second_largest(nums1)