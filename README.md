# Trading with Kalman Filters
This project implements a Kalman Filter for tracking a stock pair price ratio and provides a simple pair trading strategy that utilizes the filter.

### Example Performed on Historical Data from Coca-Cola and Pepsi stocks

Coco-Cola and Pepsi stocks often move in sync as they are in the same industry and produce similar products. Thus, they are good canditates for pair trading. 
Here is the daily closing price data for Coca-Cola and Pepsi stocks from January 1st to September 30th of 2024:

<img width="867" alt="Screenshot 2024-11-06 at 11 29 46 AM" src="https://github.com/user-attachments/assets/7df7a488-7183-43c3-9748-570ad8e4022f">

We can observe that the two companies stocks do appear to have a relationship. Therefore, we will move forward with the Kalman filter.

Below are the Kalman filter results plotted with the observed Coca-Cola and Pepsi stock price ratios: 

<img width="929" alt="Screenshot 2024-11-06 at 11 30 17 AM" src="https://github.com/user-attachments/assets/de165a91-312f-4779-9e68-a2232f6ea968">

**Trading Strategy Results:** After applying a simple pair trading strategy with this filter on the Coca-Cola and Pepsi stocks,the final value of the adjusted holdings were **1.065** the final value of the original holdings.
