def get_value_list(value, nums) -> []:
    checked_nums = []
    for key in value:
        if key in nums:
            checked_nums.append(int(key))
        else:
            pass
    return checked_nums


def calculate(final_list):
    sum = 0
    for nums in final_list:
        sum += nums
    return sum


def main(example, nums):
    final_list = []
    for value in example:
        checked_nums = get_value_list(value, nums)

        if len(checked_nums) == 1:
            final_list.append(checked_nums[0] * 11)
        elif len(checked_nums) > 1:
            final_list.append(int(str(checked_nums[0]) + str(checked_nums[-1])))

    answer = calculate(final_list=final_list)
    print(answer)


if __name__ == "__main__":
    example = [] # paste your input here

    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    main(example, nums)
