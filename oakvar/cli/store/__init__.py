from ...decorators import cli_func
from ...decorators import cli_entry


@cli_entry
def cli_store_publish(args):
    return publish(args)


@cli_func
def publish(args, __name__="store publish"):
    from ...system import get_system_conf
    from ...store.oc import publish_module
    from getpass import getpass

    if args.get("md"):
        from ...system import consts

        consts.custom_modules_dir = args.get("md")
    sys_conf = get_system_conf()
    if args.get("user") is None:
        if "publish_username" in sys_conf:
            args["user"] = sys_conf["publish_username"]
        else:
            args["user"] = input("Username: ")
    if args.get("password") is None:
        if "publish_password" in sys_conf:
            args["password"] = sys_conf["publish_password"]
        else:
            args["password"] = getpass()
    return publish_module(
        args.get("module"),
        args.get("user"),
        args.get("password"),
        overwrite=args.get("overwrite"),
        include_data=args.get("data"),
        quiet=args.get("quiet"),
    )


@cli_entry
def cli_store_fetch(args):
    return fetch(args)


@cli_func
def fetch(args, __name__="store fetch"):
    from ...store.ov import fetch_ov_store_cache

    ret = fetch_ov_store_cache(args=args)
    return ret


@cli_entry
def cli_store_pack(args):
    return pack(args)


@cli_func
def pack(args, __name__="store pack"):
    from ...store.pack import pack_module

    ret = pack_module(args)
    return ret


def get_parser_fn_store():
    from argparse import ArgumentParser, RawDescriptionHelpFormatter
    from ..store.account import get_parser_fn_store_account

    parser_fn_store = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)
    subparsers = parser_fn_store.add_subparsers(title="Commands")
    subparsers.add_parser(
        "account",
        parents=[get_parser_fn_store_account()],
        add_help=False,
        description="Manage OakVar accounts.",
        help="Manage OakVar accounts.",
    )
    get_parser_fn_store_publish(subparsers)
    get_parser_fn_store_fetch(subparsers)
    get_parser_fn_store_pack(subparsers)
    return parser_fn_store


def get_parser_fn_store_publish(subparsers):
    # publish
    parser_cli_store_publish = subparsers.add_parser(
        "publish", help="publishes a module."
    )
    parser_cli_store_publish.add_argument("module", help="module to publish")
    data_group = parser_cli_store_publish.add_mutually_exclusive_group(required=True)
    data_group.add_argument(
        "-d",
        "--data",
        action="store_true",
        default=False,
        help="publishes module with data.",
    )
    data_group.add_argument(
        "-c", "--code", action="store_true", help="publishes module without data."
    )
    parser_cli_store_publish.add_argument(
        "-u", "--user", default=None, help="user to publish as. Typically your email."
    )
    parser_cli_store_publish.add_argument(
        "-p",
        "--password",
        default=None,
        help="password for the user. Enter at prompt if missing.",
    )
    parser_cli_store_publish.add_argument(
        "--force-yes",
        default=False,
        action="store_true",
        help="overrides yes to overwrite question",
    )
    parser_cli_store_publish.add_argument(
        "--overwrite",
        default=False,
        action="store_true",
        help="overwrites a published module/version",
    )
    parser_cli_store_publish.add_argument(
        "--md", default=None, help="Specify the root directory of OakVar modules"
    )
    parser_cli_store_publish.add_argument(
        "--quiet", action="store_true", default=None, help="Run quietly"
    )
    parser_cli_store_publish.set_defaults(func=cli_store_publish)
    parser_cli_store_publish.r_return = "A boolean. A boolean. TRUE if successful, FALSE if not"  # type: ignore
    parser_cli_store_publish.r_examples = [  # type: ignore
        '# Publish "customannot" module to the store',
        '#roakvar::store.publish(module="customannot", user="user1", password="password")',
    ]


def get_parser_fn_store_fetch(subparsers):
    # fetch
    parser_cli_store_fetch = subparsers.add_parser(
        "fetch", help="fetch store information"
    )
    parser_cli_store_fetch.add_argument(
        "--quiet", action="store_true", default=None, help="Run quietly"
    )
    parser_cli_store_fetch.add_argument(
        "--email", default=None, help="email of OakVar store account"
    )
    parser_cli_store_fetch.add_argument(
        "--pw", default=None, help="password of OakVar store account"
    )
    parser_cli_store_fetch.set_defaults(func=cli_store_fetch)
    parser_cli_store_fetch.r_return = "A boolean. A boolean. TRUE if successful, FALSE if not"  # type: ignore
    parser_cli_store_fetch.r_examples = [  # type: ignore
        "# Fetch the store information",
        "#roakvar::store.fetch()",
    ]


def get_parser_fn_store_pack(subparsers):
    # pack
    parser_cli_store_pack = subparsers.add_parser(
        "pack", help="pack a module to register at OakVar store"
    )
    parser_cli_store_pack.add_argument(
        dest="module",
        default=None,
        help="Name of or path to the module to pack",
    )
    parser_cli_store_pack.add_argument(
        "-d",
        "--outdir",
        default=".",
        help="Directory to make code and data zip files in",
    )
    parser_cli_store_pack.add_argument(
        "--quiet", action="store_true", default=None, help="Run quietly"
    )
    parser_cli_store_pack.set_defaults(func=cli_store_pack)
    parser_cli_store_pack.r_return = "A boolean. A boolean. TRUE if successful, FALSE if not"  # type: ignore
    parser_cli_store_pack.r_examples = [  # type: ignore
        '# Pack a module "mymodule" into one zip file for its code and another zip file for its data.',
        '#roakvar::store.pack(module="mymodule")',
    ]
