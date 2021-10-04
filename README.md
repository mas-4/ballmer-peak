# Ballmer Peak Calculator

Finding your Ballmer Peak. Estimated by Randall Munroe to be `0.129 < p < 0.138`
(See frame 2).

![Ballmer Peak](https://imgs.xkcd.com/comics/ballmer_peak.png)

# Use

This is an absurdly simple script. The initial commit took a json object, but I
just inlined the input data in the script. So just open the script and modify
what's present there before running. The datetime is tricky, so just use the
`DATE.replace(hour=h, minute=m)` technique already present, it should take care
of the rest.

# Time

This calculator can take cumulative BAC readings given multiple cocktails. It
just takes the BAC given time for each cocktail and accumulates the results.
