import argparse
from contextlib import suppress

import spinedb_api
import sensitivity_scenarios

def main():
    arg_parser = argparse.ArgumentParser(prog="create_scenario", description="Creates scenario for sensitivity analysis.")
    arg_parser.add_argument("db_url", help="Target Spine database URL.")
    arg_parser.add_argument("scenario", help="Name of the base scenario.")
    args = arg_parser.parse_args()
    with spinedb_api.DatabaseMapping(args.db_url) as db_map:
        with spinedb_api.spine_db_client.lock_db(db_map):
            sensitivity_scenarios.make_scenarios(db_map, args.scenario, db_map, db_map)
            with suppress(spinedb_api.exception.NothingToCommit):
                db_map.commit_session("Created scenarios for sensitivity analysis.")


if __name__ == "__main__":
    main()
