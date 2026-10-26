def dailyTemperatures(temperatures):
    answer = []

    for i in range(len(temperatures)):
        days = 0

        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                days = j - i
                break

        answer.append(days)

    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))