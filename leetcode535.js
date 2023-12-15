/*
* auther yeling
* URL加密
*/


/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    return longUrl;
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    return shortUrl;
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */

let origin = 'https://leetcode.com/problems/design-tinyurl'

let enc = encode(origin);
console.log(`${enc}`);

let dec = decode(enc);
console.log(`${dec}`);