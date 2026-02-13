"""
Command-line interface for the beauti-tex package.

This module defines the CLI using argparse and connects user commands
to the internal project-building functionality.
"""
from pathlib import Path
import argparse
from .proj_builder import make_project


def make_cli(args):
    """Handle the `make-project` CLI command.

    This function serves as a thin adapter between the argparse
    namespace and the internal `make_project` function.

    Args:
        args (argparse.Namespace): Parsed command-line arguments with
            the following attributes:
            - name (str): Name of the LaTeX project.
            - project_path (str | None): Target directory for the project.
            - config_path (str | None): Path to a configuration file.
    """
    make_project(
        args.name,
        proj_path=args.project_path,
        cfg_path=args.config_path,
    )


def main():
    """Entry point for the beauti-tex command-line interface.

    This function sets up argument parsing, registers available
    subcommands, and dispatches execution to the selected handler.
    """
    # Create the top-level argument parser
    parser = argparse.ArgumentParser(
        description="Use beauti-tex from the terminal"
    )

    # Container for subcommands (e.g. make-project)
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands",
    )

    # -------------------------------
    # make-project command definition
    # -------------------------------
    parser_make = subparsers.add_parser(
        "make-project",
        help="Generate a structured project for a LaTeX paper",
    )

    parser_make.add_argument(
        "--name", "-N",
        help="The name of the project",
        required=True,
    )

    parser_make.add_argument(
        "--project-path", "-pp",
        default=None,
        help=(
            "Target directory for the new project. "
            "If omitted, the project is created in the current directory."
        ),
    )

    parser_make.add_argument(
        "--config-path", "-cp",
        default=None,
        help="Path to a configuration file",
    )

    # Assign the handler function for this subcommand
    parser_make.set_defaults(func=make_cli)

    # Parse arguments and execute the selected command
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()