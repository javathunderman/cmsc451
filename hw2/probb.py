import math
import random
class Bits:
    nums: list[int]
    BITS_PER_INT = 30
    def __init__(self, size: int) -> None:
        """

        Create a bit array with the designated size

        Usage: bits = Bits(100) # creates a bit array with 100 bits; you will be able to use bits[0] through bits[99]

        """
        self.nums = [0] * (size // self.BITS_PER_INT + 1)



    def __getitem__(self, index: int) -> int:
        """

        Return the bit stored at an index

        Usage: bits[5]

        """
        quotient, remainder = divmod(index, self.BITS_PER_INT)

        return (self.nums[quotient] >> remainder) & 1



    def __setitem__(self, index: int, value: int) -> int:
        """

        Store a 0 or 1 at the designated index

        Usage: bits[5] = 1

        """
        quotient, remainder = divmod(index, self.BITS_PER_INT)

        bit_string = 1 << remainder

        if value == 0:

            self.nums[quotient] &= ~bit_string

        else:

            self.nums[quotient] |= bit_string

def main():
    first_line = input()
    first_line = first_line.split()
    num_ips = int(first_line[0])
    num_reqs = int(first_line[1])
    error_rate = int(first_line[2])
    # basically epsilon
    error_rate /= num_reqs
    # basically our value for m
    bits_for_filter = (-num_ips * math.log(error_rate))/pow((math.log(2)), 2)
    bits_for_filter = math.ceil(bits_for_filter)

    # basically k
    num_hash_functions = (bits_for_filter / num_ips) * math.log(2)
    num_hash_functions = math.ceil(num_hash_functions)
    # print(bits_for_filter, num_hash_functions)
    seeds = []
    for i in range(0, num_hash_functions):
        seeds.append(random.randint(0, pow(2, 32)))
    bloom_filter = Bits(bits_for_filter)
    # check_arr = []
    # For each IP address we should store in the filter
    for i in range(0, num_ips):
        input_str = input()
        input_str = input_str.replace(":", "")
        # Go through each of the k hash functions
        for j in range(0, num_hash_functions):
            hash_index = (hash(input_str) ^ seeds[j]) % bits_for_filter
            # Set the corresponding bit to 1
            bloom_filter[hash_index] = 1
        # check_arr.append(input_str)

    for i in range(0, num_reqs):
        input_str = input()
        input_str = input_str.replace(":", "")
        not_in_filter = False
        for j in range(0, num_hash_functions):
            hash_index = (hash(input_str) ^ seeds[j]) % bits_for_filter
            if (bloom_filter[hash_index] == 0):
                not_in_filter = True
                break
        if (not_in_filter):
            print("reject")
        else:
            print("accept")

if __name__ == "__main__":
    main()