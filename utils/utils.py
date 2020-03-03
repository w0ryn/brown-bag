import unittest


class Test():
    MSG_MINIMUM_TESTS = '\nChecking minimum required conditions...\n'
    MSG_MUST_PASS_MIN = '\nMinimum conditions must pass before checking bonus conditions!\n'
    MSG_BONUS_TESTS   = '\nMinimum conditions met! Checking bonus conditions...\n'

    @staticmethod
    def run_suite(test_suite=None, bonus_suite=None):
        if test_suite is None:
            print('No tests to run!')
        else:
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromTestCase(test_suite)
    
            print(Test.MSG_MINIMUM_TESTS)
            results = unittest.TextTestRunner(verbosity=2).run(suite)
    
            if bonus_suite is not None:
                if not Test.passed(results):
                    print(Test.MSG_MUST_PASS_MIN)
                else:
                    suite = loader.loadTestsFromTestCase(bonus_suite)
    
                    print(Test.MSG_BONUS_TESTS)
                    unittest.TextTestRunner(verbosity=2).run(suite)
    
    @staticmethod
    def passed(results):
        failed  = len(results.failures)
        error   = len(results.errors)
        skipped = len(results.skipped)
    
        return failed + error + skipped == 0
