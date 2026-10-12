def common_elements(list1 , list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result
    
if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [2, 3, 5, 6]))


