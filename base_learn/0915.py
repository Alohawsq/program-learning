def test(text, location, find_str):
    new_text = list(text)
    # 定义一个字典用于存储每个字的坐标信息,格式为{字符: [(x, y)]}
    location_dict = {}
    # 将location数组展开铺平
    flat_location = []
    for i in range(len(location)):
        flat_location.extend(location[i])
    row = 1
    col = 1
    # 遍历flat_location数组，将每个字符的坐标信息存储在location_dict中
    for index, data in enumerate(flat_location):
        if text:
            # 判断下一行的坐标是否与当前坐标相同，如果不同则该位置为换行符继续处理下一行
            if index + 1 < len(flat_location) and flat_location[index][0] != flat_location[index+1][0]:
                row += 1
                col = 1
            else:
                item = new_text.pop(0)
                if item in location_dict:
                    location_dict[item].append((row, col, data))
                else:
                    location_dict[item] = [(row, col, data)]
                col += 1
    print(location_dict)
    # 在location字典中查找对应字符的位置
    if find_str in location_dict:
        return location_dict[find_str]
    else:
        return []

if __name__ == '__main__':
    text = "中国民生银行"
    location = [
        [(20, 10), (20, 11), (20, 12), (20, 13), (20,14)],
        [(21, 10), (21, 11)]
    ]
    find_str = "行"
    result = test(text, location, find_str)
    print(f"要查找的数据的坐标为: {result}")

