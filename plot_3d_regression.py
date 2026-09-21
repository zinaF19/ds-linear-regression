# We adapted this plot from https://www.datarobot.com/blog/multiple-regression-using-statsmodels/#appendix

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


DATA_PATH = Path(__file__).resolve().parent / "data" / "cars_multivariate.csv"


def main() -> None:
    # Load dataset
    cars = pd.read_csv(DATA_PATH)

    # Define features and target
    X2 = cars[["horsepower", "weight"]]
    y2 = cars.mpg

    # Fit linear regression model
    lin_reg2 = LinearRegression()
    lin_reg2.fit(X2, y2)

    # Get intercept and coefficients
    intercept = lin_reg2.intercept_
    coef_horsepower = lin_reg2.coef_[0]
    coef_weight = lin_reg2.coef_[1]

    # Predictions
    y_hat2 = lin_reg2.predict(X2)

    # Create horsepower/weight grid for the 3D plot
    xx1, xx2 = np.meshgrid(
        np.linspace(X2.horsepower.min(), X2.horsepower.max(), 100),
        np.linspace(X2.weight.min(), X2.weight.max(), 100),
    )

    # Regression plane
    Z = intercept + coef_horsepower * xx1 + coef_weight * xx2

    # Create 3D figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="3d", azim=-115, elev=15)

    # Plot the hyperplane
    ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.8, linewidth=0)

    # Calculate residuals
    resid = y2 - y_hat2

    # Plot data points - points over the plane are white, points below are black
    ax.scatter(
        X2[resid >= 0].horsepower,
        X2[resid >= 0].weight,
        y2[resid >= 0],
        color="black",
        alpha=1.0,
        facecolor="white",
    )
    ax.scatter(
        X2[resid < 0].horsepower,
        X2[resid < 0].weight,
        y2[resid < 0],
        color="black",
        alpha=1.0,
    )

    # Set axis labels
    ax.set_xlabel("horsepower")
    ax.set_ylabel("weight")
    ax.set_zlabel("mpg")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
