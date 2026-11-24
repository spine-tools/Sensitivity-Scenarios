import argparse
from contextlib import suppress

import spinedb_api
import sensitivity_scenarios


def main():
    arg_parser = argparse.ArgumentParser(prog="remove_config", description="Removes structures used by sensitivity analysis.")
    arg_parser.add_argument("db_url", help="Target Spine database URL.")
    args = arg_parser.parse_args()
    with spinedb_api.DatabaseMapping(args.db_url) as db_map:
        sensitivity_scenarios.remove_structure(db_map)
        with suppress(spinedb_api.exception.NothingToCommit):
            db_map.commit_session("Removed sensitivity analysis config.")


if __name__ == "__main__":
    main()
