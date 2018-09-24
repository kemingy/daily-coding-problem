# Given a array of numbers representing the stock prices of a company in 
# chronological order, write a function that calculates the maximum profit 
# you could have made from buying and selling that stock once. You must buy 
# before you can sell it.


def stock(prices):
    n = len(prices)

    if n <= 1:
        return 0

    buy = float('inf')
    profit = 0
    for i in range(n):
        if prices[i] < buy:
            buy = prices[i]
        elif profit < prices[i] - buy:
            profit = prices[i] - buy

    return profit


if __name__ == '__main__':
    for price in [[9, 11, 8, 5, 7, 10], [5, 4, 3, 2, 1]]:
        print('{} benefit is {}'.format(price, stock(price)))
