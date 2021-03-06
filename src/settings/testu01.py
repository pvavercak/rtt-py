from tools.misc import parse_test_ids


class TestU01Variant:
    """Each TestU01 battery test has its own configuration and multiple configurations
    are supported, too. If a user wants some tests to be executed multiple times
    but with slightly different settings, he just specifies variants.
    The variants are then stored in this object.
    """
    def __init__(self, repetitions: int = 1, bit_nb: int = None, bit_r: int = None, bit_s=None, bit_w=None):
        self.repetitions = repetitions
        self.bit_nb = bit_nb
        self.bit_r = bit_r
        self.bit_s = bit_s
        self.bit_w = bit_w


class TestU01TestIdSettings:
    """Each test with its variants is stored in this object.
    """
    def __init__(self, test_id, variants: 'list[TestU01Variant]'):
        self.test_id = test_id
        self.variants = variants


class TestU01Settings:
    """Wraps all tests and their configurations.
    """
    def __init__(self, test_ids: list, subbattery: str, test_id_settings: 'list[TestU01TestIdSettings]'):
        self.test_ids = test_ids
        self.subbattery = subbattery
        self.per_test_id_settings = test_id_settings


class TestU01SettingsFactory:
    """Helper for making testU01 settings from JSON config.
    """
    def make_settings(test_settings_json: dict, test_subbattery: str) -> TestU01Settings:
        """Take JSON as dictionary and for given subbattery (i.e. rabbit, crust, alphabit, etc)
        produce TestU01Settings object.

        Args:
            test_settings_json (dict): JSON config as dictionary
            test_subbattery (str): Name of a subbattery

        Raises:
            RuntimeError: Throw exeption in case of incomplete/incorrect configuration

        Returns:
            TestU01Settings: JSON config transformed to settings class
        """
        # for example, block_alphabit subbattery has config entry 'tu01-blockalphabit-settings'
        # that's why we are replacing '_'
        config_entry = f"tu01-{test_subbattery}-settings".replace("_", "")
        settings = test_settings_json.get(config_entry)
        if not settings:
            raise Exception(
                f"Configuration '{config_entry}' was not specified")
        try:
            per_tid_settings: list[TestU01TestIdSettings] = []
            defaults = settings["defaults"]
            default_test_ids = parse_test_ids(defaults["test-ids"])
            reps = int(defaults["repetitions"])
            bit_nb = defaults.get("bit-nb")
            bit_nb = int(bit_nb) if bit_nb is not None else None
            bit_r = defaults.get("bit-r")
            bit_r = int(bit_r) if bit_r is not None else None
            bit_s = defaults.get("bit-s")
            bit_s = int(bit_s) if bit_s is not None else None
            bit_w = defaults.get("bit-w")
            bit_w = int(bit_w) if bit_w is not None else None
            for tid in default_test_ids:
                per_tid_settings.append(TestU01TestIdSettings(
                    tid, [TestU01Variant(reps, bit_nb, bit_r, bit_s, bit_w)]))
            specific_settings_raw = settings.get("test-specific-settings")
            if specific_settings_raw:
                for specific_settings in specific_settings_raw:
                    tid = int(specific_settings["test-id"])
                    spec_reps = int(defaults["repetitions"])
                    spec_bit_r = specific_settings.get("bit-r")
                    spec_bit_r = int(
                        spec_bit_r) if spec_bit_r is not None else bit_r
                    spec_bit_s = specific_settings.get("bit-s")
                    spec_bit_s = int(
                        spec_bit_s) if spec_bit_s is not None else bit_s
                    spec_bit_w = specific_settings.get("bit-w")
                    spec_bit_w = int(
                        spec_bit_w) if spec_bit_w is not None else bit_w
                    variants: list[TestU01Variant] = []
                    variants_raw = specific_settings.get("variants")
                    if variants_raw:
                        for variant in variants_raw:
                            var_bit_r = variant.get("bit-r")
                            var_bit_r = int(
                                var_bit_r) if var_bit_r is not None else spec_bit_r
                            var_bit_s = variant.get("bit-s")
                            var_bit_s = int(
                                var_bit_s) if var_bit_s is not None else spec_bit_s
                            var_bit_w = variant.get("bit-w")
                            var_bit_w = int(
                                var_bit_w) if var_bit_w is not None else spec_bit_w
                            variants.append(TestU01Variant(
                                spec_reps, bit_nb, var_bit_r, var_bit_s, var_bit_w))
                    else:
                        variants.append(TestU01Variant(
                            spec_reps, bit_nb, spec_bit_r, spec_bit_s, spec_bit_w))
                    for i in range(len(per_tid_settings)):
                        if per_tid_settings[i].test_id == tid:
                            per_tid_settings[i].variants = variants
                            break
            return TestU01Settings(default_test_ids, test_subbattery, per_tid_settings)
        except:
            raise RuntimeError(
                "TestU01 settings don't contain required fields")
