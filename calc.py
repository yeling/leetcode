https://atcoder.jp/contests/abc221/submissions/35791225

这是一道基于逆序对的变形题。
不了解逆序对的同学，可以先看看我的讲解 https://www.bilibili.com/video/BV1tW4y1e7rb

用树状数组实现，这里的问题是，如何把 2 的幂次（中间的子序列的个数）也考虑进去。

我们可以把 2^(i-j) 转换成 2^i / 2^j，那么把 2^j 的逆元加到树状数组中即可。

注意需要离散化。

代码中展示了一个巧妙计算逆元的技巧。