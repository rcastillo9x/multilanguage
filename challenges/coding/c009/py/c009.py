def marsExploration(s):
    count = 0
    
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            count += 1
        if s[i + 1] != 'O':
            count += 1
        if s[i + 2] != 'S':
            count += 1
    
    return count

if __name__ == '__main__':
    s = input("Enter the received signal: ").strip()
    result = marsExploration(s)
    print(result)
