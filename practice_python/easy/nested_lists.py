if __name__ == '__main__':
    scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores[name] = score
    
    min_value = min(scores.values())
    new_dict = {}

    for key, value in scores.items():
        if value != min_value:
            new_dict[key] = value


    min_value = min(new_dict.values())
    all_keys = []

    for key, value in new_dict.items():
        if value == min_value:
            all_keys.append(key)
    
    all_keys = sorted(all_keys)
    for i in all_keys:
        print(i)
