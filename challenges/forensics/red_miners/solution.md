# Write-Up for the Challenge: Red Miners

For this challenge looking at the code in detail was actually not required.

When I saw some `base64 -d` statements, I tried to decrypt the base64 encoded strings and directly got some useful hints.

First element found was

```
echo "ZXhwb3J0IHBhcnQ0PSJfdGgzX3IzZF9wbDRuM3R9Ig==" | base64 -d  # That results in -> `export part4="_th3_r3d_pl4n3t`
```

Therefore I knew, that I had to check for the other three missing parts. I searched using the keywords `base64` or `==` (since this is a common ending for base 64). I found the other missing parts:

```sh
echo -n cGFydDE9IkhUQnttMW4xbmciCg==|base64 -d # resulting in -> `part1="HTB{m1n1ng"`
echo "cGFydDI9Il90aDMxcl93NHkiCg==" | base64 -d # resulting in  `part2="_th31r_w4y"`
echo "X3QwX200cnN9Cg=="|base64 -d # resulting in -> `_t0_m4rs}`
```

Stitching everything together I received the following Flag `HTB{m1n1ng_th31r_w4y_t0_m4rs_th3_r3d_pl4n3t}` which was the overall solution.
