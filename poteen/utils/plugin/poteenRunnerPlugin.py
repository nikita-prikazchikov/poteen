from optparse import OptionGroup
from nose.plugins import Plugin
from ...contextHolder import ContextHolder
from engine.poteen.poteenLogger import PoteenLogger
from ...error import PoteenError

__author__ = 'nprikazchikov'
logger = ContextHolder.get_logger()


class PoteenRunnerPlugin(Plugin):
    """
    Plugin for processing extra command line arguments and final conversion of
    result log
    """
    def __init__(self):
        super(PoteenRunnerPlugin, self).__init__()

    def options(self, parser, env):
        super(PoteenRunnerPlugin, self).options(parser, env)
        group = OptionGroup(parser, "Extra options of PoteenRunnerPlugin")
        group.add_option(
            "-b", "--browser",
            action="store",
            type="choice",
            choices=["iexplore", "chrome", "firefox"],
            dest="browser",
            default="firefox",
            help="Specify BROWSER for tests"
        )
        group.add_option(
            "--make-screenshot",
            action="store_true",
            dest="make_screenshot",
            default=False,
            help="Flag to say test engine to make screenshots"
        )
        group.add_option(
            "--make-advance-report",
            action="store_true",
            dest="advance_report",
            default=False,
            help="Flag to say test engine to make advanced HTML report"
                 "Most efficient with --make-screenshot"
        )
        group.add_option(
            "-u", "--url",
            action="store",
            dest="url",
            help="basic project URL for testing"
        )
        parser.add_option_group(group)

    def configure(self, options, conf):
        super(PoteenRunnerPlugin, self).configure(options, conf)
        browser = "browser"
        if hasattr(options, browser):
            ContextHolder.set_browser(getattr(options, browser))

        screenshot = "make_screenshot"
        if hasattr(options, screenshot):
            ContextHolder.set_do_screenshot(getattr(options, screenshot))

        report = "advance_report"
        if hasattr(options, report):
            ContextHolder.set_do_report(getattr(options, report))

        url = "url"
        if hasattr(options, url):
            ContextHolder.set_url(getattr(options, url))
        else:
            raise PoteenError("URL is not provided. Don't know what to test")

    def begin(self):
        PoteenLogger.collect_test_result()
        pass

    def finalize(self, result):
        if ContextHolder.get_do_report():
            PoteenLogger.collect_test_result()

    def beforeTest(self, test):
        pass

    def afterTest(self, test):
        if ContextHolder.get_do_report():
            PoteenLogger.save_test_case_to_file()
