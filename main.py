from lake import Niedziegiel, Powidzkie


def _run_lake(model, label: str) -> None:
    model.load_data()
    model.train(mode="full")
    future = model.get_future_data()
    pred = model.predict(horizon_months=12, future_features_df=future)
    model.generate_report(
        horizon_months=12,
        future_features_df=future,
        save_png=True,
        save_csv=True,
    )
    metrics = model.evaluate(horizon_months=24)
    print(f"{label} – ewaluacja (24 miesiące po treningu):", metrics)


if __name__ == "__main__":
    _run_lake(Niedziegiel(), "Niedzięgiel")
    _run_lake(Powidzkie(), "Powidzkie")
