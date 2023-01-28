# This is the main settings file for extra utilities that come with the repo
# Package configuration is in pyproject.toml
# Sphinx configuration is in the docsrc folder

# Main package name
PACKAGE_NAME = "finstmt"

# Packages added to Binder environment so that examples can be executed in Binder
BINDER_ENVIRONMENT_REQUIRES = list(set([PACKAGE_NAME]))

# Optional Google Analytics tracking ID for documentation
# Go to https://analytics.google.com/ and set it up for your documentation URL
# Set to None or empty string to not use this
GOOGLE_ANALYTICS_TRACKING_ID = "UA-154145306-1"

# Url of logo
PACKAGE_LOGO_URL = ""

if __name__ == "__main__":
    # Store config as environment variables
    env_vars = dict(locals())
    # Imports after getting locals so that locals are only environment variables
    import shlex

    for name, value in env_vars.items():
        quoted_value = shlex.quote(str(value))
        print(f"export {name}={quoted_value};")

# Does not affect anything about the current package. Simply used for tracking when this repo was created off
# of the quickstart template, so it is easier to bring over new changes to the template.
_TEMPLATE_VERSION_TUPLE = (0, 6, 0)

if __name__ == '__main__':
    # Store config as environment variables
    env_vars = dict(locals())
    # Imports after getting locals so that locals are only environment variables
    import shlex
    for name, value in env_vars.items():
        quoted_value = shlex.quote(str(value))
        print(f'export {name}={quoted_value};')
