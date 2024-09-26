import matplotlib.pyplot as plt

# Data
browsers = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Samsung Internet', 'Opera']
market_share = [65.18, 18.55, 5.26, 2.74, 2.56, 2.15]

# colors
colors = ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9', '#92a8d1', '#ffb347']

explode = (0.1, 0, 0, 0, 0, 0)  # explode chrome
plt.figure(figsize=(8, 6))
plt.pie(market_share, labels=browsers, autopct='%1.2f%%', startangle=90, explode=explode, colors=colors)

plt.axis('equal')  # to fix aspect ratio

plt.title('Browser Market - 2024')
plt.show()

# the values are getting adjusted because it automatically normalises the values to sum up to 100
