from tools.misc import parse_test_ids


class DieharderVariant:
    """Each Dieharder test with unique test ID can have multiple configurations.
    A user is allowed to request the same test to be executed with different parameters.
    Actually supported custom parameters are [arguments, psamples].
    Arguments are passed directly as program options to dieharder binary.
    Psamples attribute changes a default psamples value specified in configuration.
    Number of variants represents how much instances of a single test will be performed.
    """
    def __init__(self, arguments: 'list[str]', psamples):
        self.arguments = arguments
        self.psamples = psamples


class DieharderTestIdSetting:
    """DieHarder has a certain number of tests that have unique test IDs.
    This class holds configured variants for one particular test ID.
    """
    def __init__(self, test_id: int, variants: 'list[DieharderVariant]'):
        self.test_id: int = test_id
        self.variants = variants


class DieharderSettings:
    """Data structure used for holding information about all user-defined tests.
    It also holds list of DieharderTestIdSetting elements so for each test_id stored
    in test_ids attribute there is its own configuration. The class is then used
    in execution.
    """
    def __init__(self, test_ids: list, default_psamples, test_configs: 'list[DieharderTestIdSetting]'):
        self.test_ids: list[int] = test_ids
        self.default_psamples = default_psamples
        self.per_test_config = test_configs

    def __str__(self):
        __out = "# " + str(self.__class__.__name__) + " {\n"
        __out += "\tTest IDs: " + ", ".join(str(x) for x in self.test_ids)
        return __out


class DieharderSettingsFactory:
    """Factory object which serves as a helper for easier configuration parsing
    from user-specified test config JSON.
    """
    def make_settings(test_settings_json: dict) -> DieharderSettings:
        """Consumes loaded test settings JSON in dict and gives back parsed
        DieharderSettings.

        Args:
            test_settings_json (dict): Loaded test config JSON

        Raises:
            RuntimeError: Throw if an incomplete/incorrect config was provided

        Returns:
            DieharderSettings: JSON data transformed into settings class
        """
        settings = test_settings_json.get("dieharder-settings")
        if not settings:
            raise RuntimeError("Configuration 'dieharder-settings' was not specified")
        dieharder_settings = None
        try:
            defaults = settings["defaults"]
            default_test_ids = parse_test_ids(defaults["test-ids"])
            default_psamples = defaults["psamples"]
            per_tid_settings = list()
            for tid in default_test_ids:  # fill per_tid_settings array with default settings, override later
                per_tid_settings.append(DieharderTestIdSetting(
                    int(tid), [DieharderVariant([], default_psamples)]))  # defaults for each test id
            specific_settings_raw = settings["test-specific-settings"]
            for specs in specific_settings_raw:
                tid = int(specs["test-id"])
                variants = list()
                variants_raw = specs.get("variants")
                if variants_raw:
                    for variant in variants_raw:
                        variants.append(DieharderVariant(
                            variant["arguments"].split(" "), variant["psamples"]))
                else:
                    psamples = specs["psamples"]
                    variants.append(DieharderVariant("", psamples))
                for i in range(len(per_tid_settings)):
                    if per_tid_settings[i].test_id == tid:
                        per_tid_settings[i].variants = variants
                        break
            dieharder_settings = DieharderSettings(
                default_test_ids, default_psamples, per_tid_settings)
        except:
            raise RuntimeError(
                "Dieharder settings don't contain required fields")
        return dieharder_settings
