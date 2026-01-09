from functools import lru_cache
import pandas as pd


def self_merge(
    df: pd.DataFrame,
    column_id: str = "id",
    column_parent_id: str = "parent_id",
    column_name: str = "name",
) -> pd.DataFrame:
    """
    Given a dataframe with columns 'id', 'name', 'parent_id', return a new dataframe
    with columns:
        'id', 'sub...sub_theme', ..., 'sub_theme', 'theme'

    For each row, these columns contain the chain of names from the *node itself*
    up to the root ancestor, left-to-right in decreasing depth, such that:

        - The rightmost column 'theme' is always the top-level root.
        - The next column to the left is its child in the chain, etc.
        - Unused higher-level columns are filled with pd.NA.

    Example for a chain: 1(one) <- 2(two) <- 3(three) <- 4(four)
      id=4 row will be:
        subsubsub_theme = "four"
        subsub_theme    = "three"
        sub_theme       = "two"
        theme           = "one"
    """
    # Map id -> (name, parent_id)
    node_map = {row[column_id]: (row[column_name], row[column_parent_id]) for _, row in df.iterrows()}

    @lru_cache
    def path_leaf_to_root(node_id):
        """Return list of names from this node up to the root: [leaf, ..., root]."""
        name, parent_id = node_map[node_id]

        if pd.isna(parent_id):
            path = [name]
        else:
            parent_id_int = int(parent_id)
            # NOTE: leaf -> ... -> root
            path = [name] + path_leaf_to_root(parent_id_int)

        return path

    # Build paths and find maximum depth
    paths = []
    max_len = 0
    for node_id in df["id"]:
        p = path_leaf_to_root(node_id)
        paths.append(p)
        max_len = max(max_len, len(p))

    # Column names: for max_len=4 we want
    #   ["subsubsub_theme", "subsub_theme", "sub_theme", "theme"]
    theme_cols = []
    for i in range(max_len):
        prefix = "sub" * (max_len - i - 1)
        if prefix:
            theme_cols.append(f"{prefix}_theme")
        else:
            theme_cols.append("theme")

    # Assemble result with right-aligned paths:
    # path [leaf, ..., root] -> left-to-right: deepest on the left, root at "theme"
    data = {"id": list(df["id"])}
    for col in theme_cols:
        data[col] = []

    for p in paths:
        # pad on the left so len == max_len
        padded = [pd.NA] * (max_len - len(p)) + p
        for col, val in zip(theme_cols, padded):
            data[col].append(val)

    return pd.DataFrame(data)
