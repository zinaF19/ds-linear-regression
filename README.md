# Linear Regression

A hands-on introduction to linear regression for data science. You will fit simple and multiple regression models with scikit-learn and statsmodels, see where linear regression breaks down, and learn how to handle categorical predictors. The notebooks alternate between worked lessons and short exercises so you can practice each idea as you go.

## Learning Objectives

By the end of this repository, you should be able to:

- Fit and interpret a simple linear regression model with scikit-learn.
- Extend regression to several predictors and read the resulting coefficients.
- Recognize the assumptions and limitations of linear regression.
- Encode and interpret categorical variables in a regression model.
- Fit an OLS model with statsmodels and read its statistical summary.

## Learning Path

Work through the notebooks in order. The lessons introduce each concept, and the exercise notebooks let you practice before moving on.

| File / Folder | Description |
|---|---|
| [**1 - Simple Linear Regression (scikit-learn)**](1_simple_linear_regression_sklearn.ipynb) | Fit your first linear regression model with scikit-learn. |
| [**2 - Limitations of Linear Regression**](2_limitations_of_linear_regression.ipynb) | Where linear regression breaks down, and the assumptions behind it. |
| [**3 - Exercise: Simple Linear Regression**](3_simple_linear_regression_exercise.ipynb) | Practice simple linear regression on your own. |
| [**4 - Multiple Linear Regression (scikit-learn)**](4_multiple_linear_regression_sklearn.ipynb) | Model a target from several predictors at once. |
| [**5 - Exercise: Multiple Linear Regression**](5_multiple_linear_regression_exercise.ipynb) | Practice multiple linear regression on your own. |
| [**6 - Categorical Variables**](6_categorical_variables.ipynb) | Encode and interpret categorical predictors in a regression. |
| [**7 - Linear Regression with statsmodels**](7_linear_regression_statsmodels.ipynb) | Fit an OLS model and read its statistical summary. |

### Additional Folders and Files

| File / Folder | Description |
|---|---|
| [**Data**](data/) | Datasets used across the notebooks (car prices and car seats). |
| [**Assets**](assets/) | Figures displayed in the notebooks. |
| [**Solutions**](solutions/) | Worked solutions, added later in the course. |
| [**3D Regression Plot**](plot_3d_regression.py) | Standalone script that renders a 3D multiple-regression surface. |
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies. |
| [**uv.lock**](uv.lock) | Dependency lock file. |

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a **placeholder**. Replace it, including the `< >` brackets, with your own value. For example, `cd <repo-name>` becomes `cd ds-linear-regression`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only **one person** should complete this step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings → Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like `git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in `.venv/`.

```bash
cd <repo-name>
uv sync
```

---

### 5. Open the Notebooks

> [!NOTE]
> Make sure you open VS Code from the project root so it automatically detects the environment created by uv sync.

Launch VS Code in the project root folder:

```bash
code .
```

Then open a notebook and select the Python environment created by `uv sync` as the kernel.

## References & Further Reading

- [**Scikit-Learn linear models guide**](https://scikit-learn.org/stable/modules/linear_model.html): The official user guide for linear regression and related models.
- [**Statsmodels regression docs**](https://www.statsmodels.org/stable/regression.html): OLS and other linear models, with full statistical summaries.
- [**Seaborn regression plots**](https://seaborn.pydata.org/tutorial/regression.html): Visualizing linear relationships between variables.
- [**An Introduction to Statistical Learning**](https://www.statlearning.com/): A free textbook whose chapter on linear regression covers the theory in depth (R and Python editions).
- [**Ordinary Least Squares example (scikit-learn)**](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html): A worked example fitting LinearRegression on a real dataset.
