if __name__ == '__main__':
    n = int(input())
    sentences = {}
    sentences = set(sentences)
    for i in range(n):
        sentence = input().upper()
        sentences.add(sentence)
    print(len(sentences))