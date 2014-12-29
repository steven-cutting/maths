## Maths

This is just a module for 'toy problems'. 
I using different mathematical formulas/equations/etc. to practice and
demonstrate various features in python.

[**The Wallis Equation**](http://www.pi314.net/eng/wallis.php)
   Used to approximate pi as closely as you like. i -> ∞ | wallis -> π
+  I have written a version that can take advantage of all of the cores of the
   machine that it is running on.
+  It is also fully capable of running on pypy 2.4 (that is the version I have
   tested it with)
+  For the standard version use wallis. For the multi core version use
   para_wallis.
+  Wallis is able to gracefully handle a keyboard interrupt (ctrl + c), when
   this happens it returns it's current progress and exits.

```python
>>> import maths
>>> i = 100000000
>>> maths.wallis(i)
(3.141592643066262, 100000000)
>>> cores = 4
>>> maths.para_wallis(i, cores)
3.141592643066262
```

   [Some logs that show performance stats.](https://github.com/steven-cutting/maths/tree/master/data/logs)


