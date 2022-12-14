import functions as f
import sys


if __name__ == "__main__":
    is_prod = True if '--prod' in sys.argv else False

    f.build_app(is_prod)
    f.build_app_pro(is_prod)
    f.build_app_auth(is_prod)