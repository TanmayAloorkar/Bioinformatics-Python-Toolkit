#!/usr/bin/env python3
"""Browse the functions available in the bioinformatics toolkit."""

from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from pathlib import Path


if getattr(sys, "frozen", False):
    MODULES_DIR = Path(sys._MEIPASS) / "modules"
else:
    MODULES_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Tool:
    """A public function discovered in a toolkit source file."""

    category: str
    module: str
    name: str
    signature: str
    summary: str

    @property
    def identifier(self) -> str:
        return f"{self.category}.{self.module}:{self.name}"


def _signature(node: ast.FunctionDef) -> str:
    """Build a readable signature without importing the target module."""
    arguments = []
    positional = [*node.args.posonlyargs, *node.args.args]
    defaults = [None] * (len(positional) - len(node.args.defaults)) + list(
        node.args.defaults
    )
    for argument, default in zip(positional, defaults):
        text = argument.arg
        if default is not None:
            text += f"={ast.unparse(default)}"
        arguments.append(text)
    if node.args.vararg:
        arguments.append(f"*{node.args.vararg.arg}")
    elif node.args.kwonlyargs:
        arguments.append("*")
    for argument, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
        text = argument.arg
        if default is not None:
            text += f"={ast.unparse(default)}"
        arguments.append(text)
    if node.args.kwarg:
        arguments.append(f"**{node.args.kwarg.arg}")
    return f"{node.name}({', '.join(arguments)})"


def discover_tools() -> list[Tool]:
    """Discover public top-level functions in the modules directory."""
    tools = []
    for path in sorted(MODULES_DIR.glob("*/*.py")):
        if path.name == "__init__.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
                continue
            docstring = ast.get_docstring(node) or "No description available."
            tools.append(
                Tool(
                    category=path.parent.name,
                    module=path.stem,
                    name=node.name,
                    signature=_signature(node),
                    summary=docstring.strip().splitlines()[0],
                )
            )
    return tools


def _matching_tools(tools: list[Tool], query: str) -> list[Tool]:
    query = query.casefold()
    return [
        tool
        for tool in tools
        if query
        in " ".join((tool.identifier, tool.signature, tool.summary)).casefold()
    ]


def _print_tools(tools: list[Tool]) -> None:
    if not tools:
        print("No matching tools found.")
        return
    width = max(len(tool.identifier) for tool in tools)
    for tool in tools:
        print(f"{tool.identifier:<{width}}  {tool.summary}")


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for helpdesk commands."""
    parser = argparse.ArgumentParser(
        description="Find functions in the Bioinformatics Python Toolkit."
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("list", help="list every available function")

    search_parser = subparsers.add_parser("search", help="search names and descriptions")
    search_parser.add_argument("query", help="word or phrase to search for")

    show_parser = subparsers.add_parser("show", help="show usage for one function")
    show_parser.add_argument(
        "query", help="function name or category.module:function identifier"
    )
    return parser


def main() -> int:
    """Run the requested helpdesk command and return its exit status."""
    parser = build_parser()
    args = parser.parse_args()
    tools = discover_tools()

    if args.command in (None, "list"):
        print(f"Bioinformatics Toolkit Helpdesk ({len(tools)} functions)\n")
        _print_tools(tools)
        print("\nUse 'python -m modules.helpdesk show FUNCTION' for usage details.")
        return 0

    matches = _matching_tools(tools, args.query)
    if args.command == "search":
        _print_tools(matches)
        return 0 if matches else 1

    exact = [
        tool
        for tool in matches
        if args.query.casefold() in (tool.name.casefold(), tool.identifier.casefold())
    ]
    candidates = exact or matches
    if len(candidates) == 1:
        tool = candidates[0]
        print(tool.identifier)
        print(f"Usage: {tool.signature}")
        print(f"About: {tool.summary}")
        print(f"Import: from modules.{tool.category}.{tool.module} import {tool.name}")
        return 0
    if not candidates:
        print(f"No tool found for {args.query!r}.")
        return 1
    print(f"Multiple tools match {args.query!r}:")
    _print_tools(candidates)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
