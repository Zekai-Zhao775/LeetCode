// JS version
/**
 * @param { (...args: any[]) => any } fn
 * @returns { (...args: any[]) => any }
 */
// function curry(fn) {
//     // your code here
//     return curried = (...args) => {
//         if (fn.length > args.length) {
//             return curried.bind(null, ...args);
//         }
//         return fn(...args);
//     }
// }

// TS version
type Curry = (fn: (...args: any[]) => any) => (...args: any[]) => any

const curry: Curry = (fn) => {
    // your code here
    const curried: (...args: any[]) => any = (...args: any[]) => {
        if (args.length < fn.length) {
            return curried.bind(null, ...args);
        }
        return fn(...args);
    }
    return curried;
}