import pandas as pd
from putil import self_merge


def test_self_merge() -> None:
    df_test = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "theme": ["one", "two", "three", "four", "five"],
            "parent_id": [pd.NA, 1, 2, 3, 2],
        }
    )
    df_expected = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "subsubsub_theme": [pd.NA, pd.NA, pd.NA, "four", pd.NA],
            "subsub_theme": [pd.NA, pd.NA, "three", "three", "five"],
            "sub_theme": [pd.NA, "two", "two", "two", "two"],
            "theme": ["one", "one", "one", "one", "one"],
        }
    )
    df_actual = self_merge(
        df_test,
        column_name="theme",
    )
    pd.testing.assert_frame_equal(df_expected, df_actual)
