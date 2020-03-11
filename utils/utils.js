const Test = {
  runSuite: (suiteName, suite, bonusSuiteName, bonusSuite) => {
    const SEP1 = '------------------------------------------------';
    const SEP2 = '================================================';

    let errorMessage = '';
    let failures = 0;

    console.log(`${SEP2}\n\nRunning test suite ${suiteName}...\n`);
    suite.forEach( (test) => {
      try {
        test();
        console.log(`SUCCESS : ${test.name}`);
      } catch (error) {
        console.log(`ERROR   : ${test.name}`);
        errorMessage += `\nFailure in '${test.name}':\n\n${error.stack}\n\n${SEP1}\n`
        failures++;
      }
    });

    console.log(`\n${SEP2}`);

    if ( failures === 0 ){
      console.log(`\n${suite.length - failures} of ${suite.length} tests passed`);
      console.log(`${SEP1}\n`);

      if (!!bonusSuite) {
        console.log('Minimum conditions met! Checking bonus conditions...\n\n');
        Test.runSuite(bonusSuiteName, bonusSuite);
      } else {
        console.log('OK\n');
      }
    } else {
      console.error(errorMessage);
      console.log(`\n${suite.length - failures} of ${suite.length} tests passed`);
      console.log(`${SEP1}\n`);
      console.log('FAILED (see error log above)');
    }
  },

  assertTruthy: (value) => {
    if (!value)
      throw new Error(`assertTruthy():::Expected ${value} to be truthy`);
  },

  assertFalsey: (value) => {
    if (!!value)
      throw new Error(`assertFalsey():::Expected ${value} to be falsey`);
  },

  assertEqual: (value, expected) => {
    if (value !== expected)
      throw new Error(`assertEqual():::Expected ${value} to equal ${expected}`);
  }
}

const assertEqual  = Test.assertEqual;
const assertTrue   = (value) => { Test.assertEqual(value, true); };
const assertFalse  = (value) => { Test.assertEqual(value, false); };
const assertTruthy = Test.assertTruthy;
const assertFalsey = Test.assertFalsey;
