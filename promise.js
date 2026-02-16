/**
 * timeLimit: returns a time-limited wrapper around an async function fn
 * @param {Function} fn
 * @param {number} t - time limit in milliseconds
 * @return {Function} a new function that applies the same arguments to fn with a time limit
 */
var timeLimit = function(fn, t) {
  return async function(...args) {
    // Create a promise that races between fn(...args) and the timeout
    let timeoutHandle;
    const timeoutPromise = new Promise((_, reject) => {
      timeoutHandle = setTimeout(() => reject("Time Limit Exceeded"), t);
    });

    // Run the original function
    const fnPromise = (async () => {
      // If fn itself throws synchronously, this will reject immediately
      return await fn(...args);
    })();

    // Race the two promises
    return Promise.race([fnPromise, timeoutPromise]).then((value) => {
      // If fn resolves first, clear the timeout
      clearTimeout(timeoutHandle);
      return value;
    }).catch((err) => {
      // If timeout wins, ensure the timer is cleared and propagate error
      clearTimeout(timeoutHandle);
      throw err;
    });
  };
};