"""Smoke tests for module imports and basic functionality."""

import sys
from pathlib import Path

import pytest

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))


def test_run_src_import():
    """Test that the main entry point can be imported without errors."""
    import run_src
    assert hasattr(run_src, "main")
    assert hasattr(run_src, "PAGES")


def test_src_modules_import():
    """Test that all primary src modules can be imported."""
    modules = [
        "src.home.home",
        "src.overview.overview",
        "src.balance_sheet.balance_sheet",
        "src.cash_flow.cash_flow",
        "src.ratios.ratios",
        "src.forecast.forecast",
        "src.outcome_analysis.outcome_analysis",
        "src.data_source.data_source",
    ]
    for mod_path in modules:
        mod = __import__(mod_path, fromlist=[""])
        # Check that the expected function exists (convention: function name matches module name without .py)
        func_name = mod_path.split(".")[-1]
        assert hasattr(mod, func_name), f"Module {mod_path} missing expected function {func_name}"


def test_pandas_and_plotly_available():
    """Verify core dependencies are importable."""
    import pandas as pd
    import plotly.express as px
    import numpy as np
    assert pd.__version__ is not None
    assert px is not None
    assert np is not None
