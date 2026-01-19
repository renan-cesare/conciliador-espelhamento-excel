import argparse
from pathlib import Path

import pandas as pd


DEFAULT_COLS_A = (0, 1)  # A:B (base antiga)
DEFAULT_COLS_B = (3, 4)  # D:E (base recriada)
DEFAULT_OUT = "resultado_conciliacao.xlsx"


def _clean_text_series(s: pd.Series) -> pd.Series:
    """Converte para string e aplica strip. Mantém NaN como NaN."""
    s = s.astype("string")
    s = s.str.strip()
    return s


def _normalize_pairs(df: pd.DataFrame, col_viewer: str, col_viewed: str) -> pd.DataFrame:
    """Normaliza pares (viewer, viewed): strip, remove vazios/nulos, remove duplicadas."""
    out = df[[col_viewer, col_viewed]].copy()

    out[col_viewer] = _clean_text_series(out[col_viewer])
    out[col_viewed] = _clean_text_series(out[col_viewed])

    # Remove linhas nulas
    out = out.dropna(subset=[col_viewer, col_viewed])

    # Remove strings vazias e textos típicos de "vazio" após conversões
    invalid = {"", "nan", "none", "null"}
    out = out[~out[col_viewer].str.lower().isin(invalid)]
    out = out[~out[col_viewed].str.lower().isin(invalid)]

    return out.drop_duplicates().reset_index(drop=True)


def _load_base_from_excel(
    path: Path,
    cols: tuple[int, int],
    header: int | None,
    names: tuple[str, str],
    sheet_name: str | int | None,
) -> pd.DataFrame:
    """Carrega duas colunas do Excel como (Visualiza, Visualizado)."""
    return pd.read_excel(
        path,
        usecols=list(cols),
        header=header,
        names=list(names) if header is None else None,
        sheet_name=sheet_name,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Concilia espelhamentos (quem visualiza quem) entre duas bases em Excel."
    )

    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Caminho do Excel com as duas bases (por padrão A:B e D:E).",
    )
    parser.add_argument(
        "--sheet",
        type=str,
        default=None,
        help="Nome da aba (opcional). Se não informar, usa a primeira aba.",
    )

    # Colunas (0-index): 0=A, 1=B, 3=D, 4=E
    parser.add_argument("--a1", type=int, default=DEFAULT_COLS_A[0], help="Coluna (0-index) do 'Visualiza' na Base A.")
    parser.add_argument("--a2", type=int, default=DEFAULT_COLS_A[1], help="Coluna (0-index) do 'Visualizado' na Base A.")
    parser.add_argument("--b1", type=int, default=DEFAULT_COLS_B[0], help="Coluna (0-index) do 'Visualiza' na Base B.")
    parser.add_argument("--b2", type=int, default=DEFAULT_COLS_B[1], help="Coluna (0-index) do 'Visualizado' na Base B.")

    parser.add_argument(
        "--header",
        choices=["none", "0"],
        default="none",
        help="Use '0' se o Excel tiver cabeçalho na primeira linha. Use 'none' se não tiver.",
    )

    parser.add_argument(
        "--out",
        type=Path,
        default=Path(DEFAULT_OUT),
        help=f"Arquivo Excel de saída (padrão: {DEFAULT_OUT}).",
    )

    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {args.input}")

    header = None if args.header == "none" else 0
    sheet_name = args.sheet if args.sheet else 0

    col_viewer = "Visualiza"
    col_viewed = "Visualizado"

    base_a = _load_base_from_excel(
        path=args.input,
        cols=(args.a1, args.a2),
        header=header,
        names=(col_viewer, col_viewed),
        sheet_name=sheet_name,
    )
    base_b = _load_base_from_excel(
        path=args.input,
        cols=(args.b1, args.b2),
        header=header,
        names=(col_viewer, col_viewed),
        sheet_name=sheet_name,
    )

    base_a = _normalize_pairs(base_a, col_viewer, col_viewed)
    base_b = _normalize_pairs(base_b, col_viewer, col_viewed)

    # Diferenças: A-B e B-A
    a_minus_b = (
        pd.merge(base_a, base_b, how="outer", indicator=True)
        .query('_merge == "left_only"')
        .drop(columns=["_merge"])
        .reset_index(drop=True)
    )

    b_minus_a = (
        pd.merge(base_b, base_a, how="outer", indicator=True)
        .query('_merge == "left_only"')
        .drop(columns=["_merge"])
        .reset_index(drop=True)
    )

    with pd.ExcelWriter(args.out, engine="openpyxl") as writer:
        a_minus_b.to_excel(writer, sheet_name="faltando_recriar", index=False)
        b_minus_a.to_excel(writer, sheet_name="novos_na_base_b", index=False)

    print("Conciliação finalizada.")
    print(f"Base A (únicos): {len(base_a)} | Base B (únicos): {len(base_b)}")
    print(f"Faltando recriar (A - B): {len(a_minus_b)}")
    print(f"Novos na Base B (B - A): {len(b_minus_a)}")
    print(f"Saída: {args.out.resolve()}")


if __name__ == "__main__":
    main()
