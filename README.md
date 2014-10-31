nmcssh
======

nmcssh aims to solve [Zooko's triangle][1] for ssh authentication.

- decentralized: all keys are stored in the namecoin block
- secure: the system relies on namecoin's security
- human meaningful: the keys are bound to human chosen strings, like a nickname

[1]: https://en.wikipedia.org/wiki/Zooko%27s_triangle

Usage
=====

    nmcssh kpcyrd >> ~kpcyrd/.ssh/authorized_keys

Register your ssh key
=====================

1. Install the namecoin client and get some namecoins.
2. Register a name in the format `ssh/nickname`.
3. Enter your ssh key as value.
4. Wait until the key is propagated.
5. Done. Your ssh key is now available with `nmcssh nickname`.

License
=======

GPLv3+
