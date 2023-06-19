import pandas as pd

days = (
    "Понеділок",
    "Вівторок",
    "Середа",
    "Четвер",
    "П'ятниця",
    "Субота",
    "Неділя",
)
income = (
    "1000",
    "800",
    "1200",
    "900",
    "1400",
    "1500",
    "700",

)
costs = (
    "500",
    "400",
    "600",
    "450",
    "700",
    "750",
    "350",
)

data = pd.DataFrame(
    list(zip(days, income, costs)),
    columns=(
        "День",
        "Дохід",
        "Витрати",
    ),
)

data.to_excel(
    "my_mini_buisness",
    sheet_name="Міні-бізнес",
)
