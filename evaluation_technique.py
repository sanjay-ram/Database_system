import numpy as np

actual = np.array([80, 90, 70, 100, 60])
predicted = np.array([78, 88, 68, 98, 58])

error = actual - predicted

mae = np.mean(np.abs(error))
mse = np.mean(np.square(error))
rmse = np.sqrt(mse)
print(f"Mean Absolute Error(MAE): {mae}")
print(f"Mean Squared Error(MSE): {mse}")
print(f"Root Mean Squared Error(RMSE): {rmse}")