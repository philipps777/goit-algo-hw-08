import heapq
import random


def minimum_network_cables(network_cables):

    if not network_cables:
        raise ValueError("Список кабелів порожній")
    heapq.heapify(network_cables)

    total_cost = 0

    while len(network_cables) > 1:
        cost = heapq.heappop(network_cables) + heapq.heappop(network_cables)
        total_cost += cost
        heapq.heappush(network_cables, cost)

    return total_cost


def main():
    # several_network_cables = [random.randint(1, 20) for _ in range(10)]
    several_network_cables = [7, 7, 19, 17, 18, 9, 13, 19, 10, 5]
    # several_network_cables = []
    print("\nSeveral network cables:", several_network_cables, '\n')
    print("Common costs:", minimum_network_cables(
        several_network_cables), '\n')


if __name__ == "__main__":
    main()
